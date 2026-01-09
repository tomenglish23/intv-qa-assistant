"""
Interview Q&A RAG Assistant - Flask API + CLI

Run web:
  python app.py
Run CLI:
  python app.py cli
"""
from __future__ import annotations

import os
import sys
import tarfile
from typing import TypedDict, List, Optional, Dict, Any

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END


# ============================================================
# CONFIG
# ============================================================

DIR_DATA = "./data"
DIR_PERSIST = "./chroma_db"
CHROMA_TAR = "chroma_db.tar.gz"

OPENAI_CHAT_MODEL = os.environ.get("OPENAI_CHAT_MODEL", "gpt-4o-mini")
OPENAI_EMBED_MODEL = os.environ.get("OPENAI_EMBED_MODEL", "text-embedding-3-small")


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)
CORS(app)


# ============================================================
# GLOBALS
# ============================================================

doc_ingester: "DocIngester | None" = None
vector_store: "VectorStore | None" = None
app_graph = None

_system_initialized = False
_init_error: str | None = None


# ============================================================
# TYPES
# ============================================================

class RAGState(TypedDict):
    """State object for LangGraph workflow"""
    q: str
    discipline: Optional[str]
    area: Optional[str]
    rxd_docs: List[Document]
    ctx: str
    a: str
    confidence: float
    use_fb: bool
    sources: List[str]


# ============================================================
# DOCUMENT INGESTION
# ============================================================

class DocIngester:
    """Loads and parses markdown files with hierarchy awareness"""

    def __init__(self, data_dir: str = DIR_DATA):
        self.data_dir = data_dir
        self.level1: set[str] = set()
        self.level2: Dict[str, set[str]] = {}
        self.level3: Dict[str, Dict[str, set[str]]] = {}

    def load_docs(self) -> List[Document]:
        """Load all .txt/.md files from data directory"""
        docs: List[Document] = []

        if not os.path.exists(self.data_dir):
            print(f"ERROR: data_dir missing: {self.data_dir}")
            return docs

        for filename in os.listdir(self.data_dir):
            if filename.endswith((".txt", ".md")):
                filepath = os.path.join(self.data_dir, filename)
                print(f"📄 Loading: {filename}")

                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                docs.extend(self._parse_hierarchical(content, filename))

        print(f"✅ Chunks: Loaded {len(docs)} chunks total")
        print(f"🔎 Level 1: {len(self.level1)} disciplines")
        print(f"🔎 Level 2: {sum(len(areas) for areas in self.level2.values())} areas")
        return docs

    def get_level1(self) -> List[str]:
        """Get list of all Level 1 disciplines"""
        return sorted(self.level1)

    def get_level2(self) -> dict:
        """Get Level 2 areas organized by Level 1"""
        return {k: sorted(v) for k, v in self.level2.items()}

    def _parse_hierarchical(self, content: str, source: str) -> List[Document]:
        """Parse content tracking discipline/area context"""
        lines = content.split("\n")

        current_discipline = "General"
        current_area = "General"
        current_chunk_lines: List[str] = []
        docs: List[Document] = []

        for line in lines:
            line = line.rstrip("\r")

            if line.startswith("# ") and not line.startswith("## "):
                if current_chunk_lines:
                    self._create_chunk(current_chunk_lines, current_discipline, current_area, source, docs)
                    current_chunk_lines = []

                current_discipline = line[2:].strip()
                self.level1.add(current_discipline)

                if current_discipline not in self.level2:
                    self.level2[current_discipline] = set()
                if current_discipline not in self.level3:
                    self.level3[current_discipline] = {}

                continue

            if line.startswith("## ") and not line.startswith("### "):
                if current_chunk_lines:
                    self._create_chunk(current_chunk_lines, current_discipline, current_area, source, docs)
                    current_chunk_lines = []

                current_area = line[3:].strip()
                self.level2[current_discipline].add(current_area)

                if current_area not in self.level3[current_discipline]:
                    self.level3[current_discipline][current_area] = set()

                continue

            if line.startswith("### ") or line.startswith("Q:"):
                if current_chunk_lines:
                    self._create_chunk(current_chunk_lines, current_discipline, current_area, source, docs)
                    current_chunk_lines = []

                topic = line[4:].strip() if line.startswith("### ") else line[2:].strip()
                if current_area in self.level3.get(current_discipline, {}):
                    self.level3[current_discipline][current_area].add(topic)

                current_chunk_lines.append(line)
            else:
                current_chunk_lines.append(line)

            # chunk flush
            chunk_text = "\n".join(current_chunk_lines)
            if len(chunk_text) >= 2000:
                self._create_chunk(current_chunk_lines, current_discipline, current_area, source, docs)
                current_chunk_lines = []

        if current_chunk_lines:
            self._create_chunk(current_chunk_lines, current_discipline, current_area, source, docs)

        return docs

    def _create_chunk(self, lines: List[str], discipline: str, area: str, source: str, docs: List[Document]) -> None:
        """Create a document chunk with metadata"""
        chunk_text = "\n".join(lines).strip()
        if not chunk_text:
            return

        docs.append(
            Document(
                page_content=chunk_text,
                metadata={"discipline": discipline, "area": area, "source": source},
            )
        )


# ============================================================
# VECTOR STORE
# ============================================================

class VectorStore:
    """Manages ChromaDB vector store"""

    def __init__(self, persist_dir: str = DIR_PERSIST):
        self.persist_dir = persist_dir
        self.embs: OpenAIEmbeddings | None = None
        self.vs: Chroma | None = None

    def _ensure_embeddings(self) -> None:
        if self.embs is None:
            self.embs = OpenAIEmbeddings(model=OPENAI_EMBED_MODEL)

    def create_or_load(self, docs: List[Document] | None = None) -> Chroma:
        """Create new vectorstore or load existing"""
        self._ensure_embeddings()

        if docs:
            self.vs = Chroma.from_documents(
                documents=docs,
                embedding=self.embs,
                persist_directory=self.persist_dir,
            )
            print(f"✅ Vectorstore: Created with {len(docs)} docs")
        else:
            self.vs = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embs,
            )
            print("✅ Vectorstore: Loaded existing")

        return self.vs

    def search(self, query: str, k: int = 4, filter_dict: dict | None = None) -> List[Document]:
        """Search with optional metadata filtering"""
        if self.vs is None:
            raise RuntimeError("Vector store not initialized")
        if filter_dict:
            return self.vs.similarity_search(query, k=k, filter=filter_dict)
        return self.vs.similarity_search(query, k=k)


# ============================================================
# LANGGRAPH WORKFLOW
# ============================================================

def create_rag_graph(vs: VectorStore):
    """Creates the LangGraph workflow.

    Node functions are defined inside to safely capture `llm` & `vs`.
    """
    llm = ChatOpenAI(model=OPENAI_CHAT_MODEL, temperature=0)

    def analyze_query(state: RAGState) -> RAGState:
        """Extract discipline from question"""
        if state.get("discipline"):
            return state

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Extract the technical discipline from this question. "
                    "Options: C#, Angular, SQL, DevOps, General. Return ONLY the discipline name.",
                ),
                ("user", "{q}"),
            ]
        )

        chain = prompt | llm
        response = chain.invoke({"q": state["q"]})
        discipline = response.content.strip()

        if "c sharp" in discipline.lower() or "csharp" in discipline.lower():
            discipline = "C#"

        state["discipline"] = discipline if discipline != "General" else None
        return state

    def retrieve_docs(state: RAGState) -> RAGState:
        """Retrieve relevant docs"""
        filter_dict: Dict[str, Any] = {}
        if state.get("discipline"):
            filter_dict["discipline"] = state["discipline"].upper()
        if state.get("area"):
            filter_dict["area"] = state["area"].upper()

        docs = vs.search(state["q"], k=4, filter_dict=(filter_dict or None))

        state["rxd_docs"] = docs
        state["ctx"] = "\n\n".join([doc.page_content for doc in docs])
        state["sources"] = [doc.metadata.get("source", "unknown") for doc in docs]
        return state

    def grade_relevance(state: RAGState) -> RAGState:
        """Determine if retrieved docs are relevant"""
        if not state["rxd_docs"]:
            state["use_fb"] = True
            state["confidence"] = 0.0
            return state

        q_words = set(state["q"].lower().split())
        ctx_words = set(state["ctx"].lower().split())
        overlap = len(q_words & ctx_words)
        confidence = min(overlap / max(len(q_words), 1), 1.0)

        state["confidence"] = confidence
        state["use_fb"] = confidence < 0.3
        return state

    def gen_a(state: RAGState) -> RAGState:
        """Generate answer from context"""
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert technical interviewer. "
                    "Answer based ONLY on the provided context. Be concise and accurate.",
                ),
                ("user", "Context:\n{ctx}\n\nQuestion: {q}\n\nAnswer:"),
            ]
        )

        chain = prompt | llm
        response = chain.invoke({"ctx": state["ctx"], "q": state["q"]})
        state["a"] = response.content
        return state

    def fallback_a(state: RAGState) -> RAGState:
        """Use OpenAI when docs don't have answer"""
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an expert technical interviewer. Answer this question accurately."),
                ("user", "{q}"),
            ]
        )

        chain = prompt | llm
        response = chain.invoke({"q": state["q"]})
        state["a"] = f"[Using general knowledge] {response.content}"
        return state

    def should_use_fb(state: RAGState) -> str:
        return "fallback" if state["use_fb"] else "generate"

    workflow = StateGraph(RAGState)
    workflow.add_node("analyze", analyze_query)
    workflow.add_node("retrieve", retrieve_docs)
    workflow.add_node("grade", grade_relevance)
    workflow.add_node("generate", gen_a)
    workflow.add_node("fallback", fallback_a)

    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", "retrieve")
    workflow.add_edge("retrieve", "grade")
    workflow.add_conditional_edges("grade", should_use_fb, {"generate": "generate", "fallback": "fallback"})
    workflow.add_edge("generate", END)
    workflow.add_edge("fallback", END)

    return workflow.compile()


# ============================================================
# INITIALIZATION
# ============================================================

def _unpack_chroma_if_needed() -> None:
    if os.path.exists(DIR_PERSIST):
        return
    if not os.path.exists(CHROMA_TAR):
        return
    print("📦 Unpacking vector database...")
    with tarfile.open(CHROMA_TAR, "r:gz") as tar:
        tar.extractall(".")


def get_app_graph():
    """Lazy initializer for the RAG system."""
    global doc_ingester, vector_store, app_graph, _system_initialized, _init_error

    if _system_initialized and app_graph is not None:
        return app_graph

    if _init_error:
        print(f"⚠️ Skipping init due to previous error: {_init_error}")
        return None

    try:
        print("=" * 70)
        print("Interview Q&A RAG Assistant - Initializing...")
        print("=" * 70)

        _unpack_chroma_if_needed()

        di = DocIngester(data_dir=DIR_DATA)
        docs = di.load_docs()
        if not docs:
            _init_error = "No documents found!"
            print(f"ERROR: {_init_error}")
            return None

        vs = VectorStore()
        # Load existing if present
        if os.path.exists(DIR_PERSIST):
            vs.create_or_load(docs=None)
        else:
            vs.create_or_load(docs=docs)

        graph = create_rag_graph(vs)

        doc_ingester = di
        vector_store = vs
        app_graph = graph
        _system_initialized = True

        print("✅ System ready!")
        return app_graph

    except Exception as e:
        _init_error = str(e)
        print(f"❌ Initialization error: {e}")
        return None


def initialize_system() -> bool:
    return get_app_graph() is not None


# ============================================================
# API ROUTES
# ============================================================

@app.route("/api/list1", methods=["GET"])
def list1():
    graph = get_app_graph()
    if not graph or not doc_ingester:
        return jsonify({"error": "Not initialized", "detail": _init_error}), 503

    return jsonify({"list1": sorted(doc_ingester.level1)})


@app.route("/api/list2", methods=["GET"])
def list2():
    graph = get_app_graph()
    if not graph or not doc_ingester:
        return jsonify({"error": "Not initialized", "detail": _init_error}), 503

    # discipline= optional query param
    discipline = (request.args.get("discipline") or "").strip()
    if discipline:
        areas = sorted(doc_ingester.level2.get(discipline, set()))
        return jsonify({"discipline": discipline, "list2": areas})

    # all
    all_map = {k: sorted(v) for k, v in doc_ingester.level2.items()}
    return jsonify({"list2": all_map})


@app.route("/api/list3", methods=["GET"])
def list3():
    graph = get_app_graph()
    if not graph or not doc_ingester:
        return jsonify({"error": "Not initialized", "detail": _init_error}), 503

    discipline = (request.args.get("discipline") or "").strip()
    area = (request.args.get("area") or "").strip()

    if discipline and area:
        topics = sorted(doc_ingester.level3.get(discipline, {}).get(area, set()))
        return jsonify({"discipline": discipline, "area": area, "list3": topics})

    if discipline:
        # all areas under 1 discipline
        by_area = {
            a: sorted(s)
            for a, s in doc_ingester.level3.get(discipline, {}).items()
        }
        return jsonify({"discipline": discipline, "list3": by_area})

    # all
    all_map = {
        d: {a: sorted(s) for a, s in areas.items()}
        for d, areas in doc_ingester.level3.items()
    }
    return jsonify({"list3": all_map})

@app.route("/")
def index():
    return jsonify({"status": "ok", "service": "Interview Q&A RAG Assistant"})

@app.route("/health")
def health():
    status = {
        "status": "ok",
        "chroma_db_exists": os.path.exists(DIR_PERSIST),
        "chroma_db_tar_exists": os.path.exists(CHROMA_TAR),
        "data_dir_exists": os.path.exists(DIR_DATA),
        "system_initialized": _system_initialized,
        "init_error": _init_error,
    }

    if os.path.exists(DIR_DATA):
        status["data_files"] = os.listdir(DIR_DATA)

    if os.path.exists(DIR_PERSIST):
        status["chroma_files_sample"] = os.listdir(DIR_PERSIST)[:5]

    if doc_ingester:
        status["disciplines"] = len(doc_ingester.level1)
        status["areas"] = sum(len(a) for a in doc_ingester.level2.values())

    return jsonify(status)


@app.route('/api/query', methods=['POST'])
def query():
    """Handle query requests"""
    try:
        data = request.json
        question = data.get('question', '').strip()
        discipline = data.get('discipline')
        area = data.get('area')
        
        if not question:
            return jsonify({"error": "Question required"}), 400
        
        print(f"?? Querying: {question}")
        print(f"   Discipline: {discipline}")
        print(f"   Area: {area}")
        
        graph = get_app_graph()
        if not graph:
            return jsonify({"error": "System not initialized"}), 503
        
        result = graph.invoke({
            "q": question,
            "discipline": discipline,
            "area": area,
            "rxd_docs": [],
            "ctx": "",
            "a": "",
            "confidence": 0.0,
            "use_fb": False,
            "sources": []
        })
        
        return jsonify({
            "answer": result["a"],
            "confidence": result["confidence"],
            "sources": result["sources"],
            "use_fallback": result["use_fb"]
        })
        
    except Exception as e:
        print(f"? ERROR in /api/query: {e}")  # ? ADD THIS
        import traceback
        traceback.print_exc()  # ? AND THIS
        return jsonify({"error": str(e)}), 500

@app.route("/api/disciplines", methods=["GET"])
def get_disciplines():
    graph = get_app_graph()
    if not graph or not doc_ingester:
        return jsonify({"error": "Not initialized", "detail": _init_error}), 503
    return jsonify({"disciplines": doc_ingester.get_level1()})


@app.route("/api/stats", methods=["GET"])
def stats():
    graph = get_app_graph()
    if not graph or not doc_ingester:
        return jsonify({"error": "Not initialized", "detail": _init_error}), 503

    return jsonify(
        {
            "disciplines": len(doc_ingester.level1),
            "areas": sum(len(areas) for areas in doc_ingester.level2.values()),
            "status": "ready",
        }
    )


# ============================================================
# CLI
# ============================================================

def run_cli() -> None:
    graph = get_app_graph()
    if not graph:
        print("Failed to initialize!")
        return

    print("❓ Ask questions (type 'quit' to exit)")
    print("   Commands: /set <discipline>, /seta <area>, /clear")
    print("-" * 70)

    active_discipline: str | None = None
    active_area: str | None = None

    while True:
        q = input("➜ Your question: ").strip()

        if q.lower() in {"quit", "exit", "q"}:
            print("\n👋 Goodbye!")
            break

        if q.lower().startswith("/set "):
            active_discipline = q[5:].strip() or None
            print(f"✅ Discipline set to: {active_discipline}")
            continue

        if q.lower().startswith("/seta "):
            active_area = q[6:].strip() or None
            print(f"✅ Area set to: {active_area}")
            continue

        if q.lower() == "/clear":
            active_discipline = None
            active_area = None
            print("✅ Filters cleared")
            continue

        if not q:
            continue

        result = graph.invoke(
            {
                "q": q,
                "discipline": active_discipline,
                "area": active_area,
                "rxd_docs": [],
                "ctx": "",
                "a": "",
                "confidence": 0.0,
                "use_fb": False,
                "sources": [],
            }
        )

        print(f"\n🧠 Answer: {result.get('a','')}")
        print(f"📊 Confidence: {float(result.get('confidence',0.0)):.1%}")
        print("-" * 70 + "\n")


# ============================================================
# ENTRYPOINT
# ============================================================

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].lower() == "cli":
        run_cli()
        return

    if initialize_system():
        port = int(os.environ.get("PORT", 5000))
        # use_reloader=False avoids double-init issues locally
        app.run(host="0.0.0.0", port=port, use_reloader=False)
    else:
        print("Failed to initialize!")
        if _init_error:
            print(_init_error)


if __name__ == "__main__":
    main()
