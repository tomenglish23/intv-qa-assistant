# DISCIPLINE C#
## Basic Knowledge
### Is C# object-oriented? Is C# a purely object-oriented language? Why?
C# is an object-oriented language.  Is C# a purely object-oriented language? No.Purely object-oriented languages do not have primitive data types (int, float, bool, char, etc. that you can use directly without creating objects). In C#, we have primitive data types.

### C# data types: Value Types, Reference Types and Pointer Types.
Value Types: int, float, double, structures, enumerations etc.Reference Types: Classes, Interfaces, Delegates, strings, arrays etc.Pointer Types: Unsafe pointers.

### What is the difference between value types and reference types?
Value types store actual values (e.g., int, float). They are stored on the stack.Reference types store references to their data (e.g., classes, arrays). They are stored on the heap.When you pass a value type, you are passing a copy. When you pass a reference type, you are passing a reference to the data.

### What is boxing and unboxing? What is the performance hit for boxing and unboxing?
Boxing: Converting a value type to a reference type (object).Unboxing: Converting a reference type back to a value type.Performance: Boxing and unboxing are computationally expensive processes because they involve type conversion and memory allocation.

### What is a namespace? Why do we use namespaces?
A namespace is a container for classes, interfaces, structs, enums, and delegates.We use namespaces to organize code and prevent naming conflicts.Example: System.Collections.Generic is a namespace that contains generic collections.

### What is the difference between '==' and Equals() method?
'==' operator: Checks if two object references point to the same memory location.Equals() method: Checks if two objects are equal in value (can be overridden to define custom equality logic).For value types, both do the same thing. For reference types, they behave differently unless Equals() is overridden.

### What is the difference between string and StringBuilder?
string: Immutable. Every modification creates a new string object.StringBuilder: Mutable. Can be modified without creating new objects.Use StringBuilder when you need to perform multiple string manipulations for better performance.

### What is the difference between Array and ArrayList?
Array: Fixed size, type-safe (stores elements of the same type).ArrayList: Dynamic size, not type-safe (stores objects of any type).Arrays are faster and use less memory. ArrayLists are more flexible but require boxing/unboxing for value types.

### What is the difference between ArrayList and List<T>?
ArrayList: Not type-safe, stores objects, requires casting.List<T>: Type-safe, generic collection, no boxing/unboxing needed.List<T> is preferred over ArrayList for better performance and type safety.

### What is the difference between interface and abstract class?
Interface: Can only contain method signatures (no implementation). A class can implement multiple interfaces.Abstract Class: Can contain both abstract and concrete methods. A class can inherit from only one abstract class.Use interfaces for defining contracts. Use abstract classes for sharing common functionality.

### What is the difference between ref and out parameters?
ref: The variable must be initialized before being passed. It can be read and modified.out: The variable does not need to be initialized before being passed. It must be assigned a value before the method returns.Both pass variables by reference.

### What is the difference between const and readonly?
const: Value must be assigned at compile time. Cannot be changed. Implicitly static.readonly: Value can be assigned at runtime (in constructor). Cannot be changed after initialization.

### What is the difference between static and non-static methods?
Static methods: Belong to the class itself, not to instances. Called using the class name.Non-static methods: Belong to instances of the class. Called using object references.

### What is the difference between throw and throw ex?
throw: Re-throws the current exception, preserving the original stack trace.throw ex: Throws the exception as a new exception, resetting the stack trace.Always use 'throw' to preserve the stack trace for better debugging.

### What is the difference between finally and finalize?
finally: A block that executes after try/catch, regardless of whether an exception was thrown. Used for cleanup code.finalize: A method called by the garbage collector before an object is destroyed. Rarely used (use Dispose() instead).

### What is the difference between IEnumerable and IQueryable?
IEnumerable: Used for in-memory collections. Executes queries in-memory (LINQ to Objects).IQueryable: Used for remote data sources (databases). Queries are translated to SQL and executed on the server (LINQ to SQL).

### What is the difference between early binding and late binding?
Early Binding: Type checking is done at compile time. Faster performance.Late Binding: Type checking is done at runtime using reflection. Slower performance but more flexible.

## OOPS Concepts
### What is encapsulation?
Encapsulation is the bundling of data (fields) and methods that operate on that data into a single unit (class).It hides the internal implementation details and exposes only what is necessary through public methods.Benefits: Data protection, modularity, easier maintenance.

### What is inheritance?
Inheritance allows a class (derived class) to inherit properties and methods from another class (base class).It promotes code reuse and establishes a parent-child relationship between classes.C# supports single inheritance (a class can inherit from only one base class).

### What is polymorphism? What are the types of polymorphism?
Polymorphism means "many forms." It allows objects to be treated as instances of their parent class.Types:1. Compile-time (Static) Polymorphism: Method overloading and operator overloading.2. Runtime (Dynamic) Polymorphism: Method overriding using virtual and override keywords.

### What is abstraction?
Abstraction is the concept of hiding complex implementation details and showing only essential features.It is achieved using abstract classes and interfaces.Benefits: Reduces complexity, improves code readability and maintainability.

### What is method overloading?
Method overloading is defining multiple methods with the same name but different parameters (different number, type, or order of parameters).It is a form of compile-time polymorphism.Example: void Print(int x), void Print(string x), void Print(int x, string y)

### What is method overriding?
Method overriding is redefining a base class method in a derived class using the 'override' keyword.The base class method must be marked as 'virtual' or 'abstract'.It is a form of runtime polymorphism.

### What is the difference between overloading and overriding?
Overloading: Same method name, different parameters. Compile-time polymorphism.Overriding: Same method name and parameters, different implementation. Runtime polymorphism (requires inheritance).

### Can we override private virtual methods?
No. Private methods are not accessible to derived classes, so they cannot be overridden.

### What are access modifiers in C#?
public: Accessible from anywhere.private: Accessible only within the same class.protected: Accessible within the same class and derived classes.internal: Accessible within the same assembly.protected internal: Accessible within the same assembly or derived classes.private protected: Accessible within the same class or derived classes in the same assembly.

### What is a sealed class?
A sealed class cannot be inherited.Use sealed to prevent inheritance and improve performance (compiler optimizations).Example: sealed class MyClass { }

### What is a partial class?
A partial class allows you to split the definition of a class across multiple files.All parts are combined into a single class at compile time.Useful for separating auto-generated code from manually written code.

### What is a static class?
A static class cannot be instantiated. It can only contain static members.Use static classes for utility methods or helper classes.Example: static class MathHelper { public static int Add(int a, int b) { return a + b; } }

## Exception Handling
### What is an exception?
An exception is an error that occurs during the execution of a program.It disrupts the normal flow of the program.C# uses try, catch, finally, and throw keywords to handle exceptions.

### What is the difference between exception and error?
Exception: An issue that occurs during program execution that can be handled (e.g., FileNotFoundException).Error: A serious problem that usually cannot be handled by the program (e.g., OutOfMemoryError).

### What is a try-catch block?
A try-catch block is used to handle exceptions.Code that might throw an exception is placed in the try block.If an exception occurs, it is caught and handled in the catch block.

### What is a finally block?
The finally block executes after try and catch blocks, regardless of whether an exception was thrown.It is used for cleanup code (e.g., closing files, releasing resources).

### What are custom exceptions?
Custom exceptions are user-defined exceptions that inherit from the Exception class.They are used to create application-specific error handling.Example: class MyCustomException : Exception { }

### What is the difference between throw and throw ex?
throw: Re-throws the current exception, preserving the stack trace.throw ex: Re-throws the exception, but resets the stack trace.Always use 'throw' to preserve debugging information.

## Collections
### What is a collection?
A collection is a data structure that stores multiple elements.Examples: Arrays, Lists, Dictionaries, Queues, Stacks.

### What are generic collections?
Generic collections are type-safe collections that use generics (e.g., List<T>, Dictionary<TKey, TValue>).They provide better performance than non-generic collections (no boxing/unboxing).

### What is the difference between List and Dictionary?
List: Stores elements in a sequential order. Access by index.Dictionary: Stores key-value pairs. Access by key.

### What is the difference between HashSet and List?
HashSet: Stores unique elements, no duplicates. No guaranteed order. Fast lookups.List: Allows duplicates. Maintains insertion order.

### What is the difference between Queue and Stack?
Queue: FIFO (First In, First Out). Elements are added at the rear and removed from the front.Stack: LIFO (Last In, First Out). Elements are added and removed from the top.

## Delegates and Events
### What is a delegate?
A delegate is a type-safe function pointer.It references methods with a specific signature.Delegates are used for callbacks and event handling.Example: delegate void MyDelegate(string message);

### What is a multicast delegate?
A multicast delegate can reference multiple methods.When invoked, all referenced methods are called in sequence.Example: myDelegate += Method1; myDelegate += Method2;

### What is an event?
An event is a notification sent by an object when something happens.Events use delegates to define the signature of event handlers.Example: public event EventHandler MyEvent;

### What is the difference between delegate and event?
Delegate: A type that can hold references to methods.Event: A special kind of delegate that can only be invoked by the class that declares it.Events provide encapsulation and are safer to use.

## LINQ
### What is LINQ?
LINQ (Language Integrated Query) is a feature that allows querying data from different sources using a uniform syntax.Sources: Collections, databases, XML, etc.

### What are the types of LINQ?
LINQ to Objects: Queries in-memory collections (arrays, lists).LINQ to SQL: Queries SQL databases.LINQ to XML: Queries XML documents.LINQ to Entities: Queries using Entity Framework.

### What is the difference between IEnumerable and IQueryable in LINQ?
IEnumerable: Executes queries in-memory. Suitable for LINQ to Objects.IQueryable: Executes queries on the server (e.g., database). Suitable for LINQ to SQL.IQueryable is more efficient for large datasets stored remotely.

### What are the advantages of LINQ?
Type safety: Compile-time checking.Readable syntax: Queries are written in C#.Consistency: Same syntax for different data sources.IntelliSense support: Better developer experience.

### What is deferred execution in LINQ?
Deferred execution means the query is not executed when it is defined.It is executed when the query is iterated (e.g., using foreach).Benefits: Improved performance, ability to modify queries before execution.

### What is immediate execution in LINQ?
Immediate execution means the query is executed as soon as it is defined.Methods like ToList(), ToArray(), Count() trigger immediate execution.

## Async and Await
### What is asynchronous programming?
Asynchronous programming allows a program to perform tasks without blocking the main thread.It improves application responsiveness, especially for I/O-bound operations.

### What are async and await keywords?
async: Marks a method as asynchronous.await: Pauses the execution of an async method until the awaited task completes.Example: async Task<int> GetDataAsync() { await Task.Delay(1000); return 42; }

### What is the difference between Task and Thread?
Task: Higher-level abstraction for asynchronous operations. Managed by the Task Scheduler.Thread: Lower-level construct representing an OS thread. Requires manual management.Tasks are easier to use and more efficient than threads.

### What is Task.Run()?
Task.Run() queues work to run on a thread pool thread.It is used for CPU-bound operations.Example: Task.Run(() => DoWork());

### What is Task.WhenAll()?
Task.WhenAll() waits for multiple tasks to complete.Returns a single task that completes when all input tasks complete.Example: await Task.WhenAll(task1, task2, task3);

### What is Task.WhenAny()?
Task.WhenAny() waits for any one of multiple tasks to complete.Returns a task that completes when the first input task completes.

### What is the difference between Task.Result and await?
Task.Result: Blocks the thread until the task completes. Can cause deadlocks.await: Does not block the thread. Allows asynchronous continuation.Always prefer 'await' over Task.Result.

## Garbage Collection
### What is garbage collection?
Garbage collection (GC) is the automatic memory management process in .NET.The GC reclaims memory used by objects that are no longer referenced.It helps prevent memory leaks.

### What are the generations in garbage collection?
Generation 0: Short-lived objects. Collected most frequently.Generation 1: Objects that survived one GC cycle.Generation 2: Long-lived objects. Collected least frequently.The GC uses a generational approach to improve performance.

### What is the difference between Dispose and Finalize?
Dispose(): Explicitly releases unmanaged resources. Implements IDisposable interface. Called by the developer.Finalize(): Called by the garbage collector before an object is destroyed. Used as a backup for cleanup.Always prefer Dispose() over Finalize().

### What is the using statement?
The using statement ensures that Dispose() is called automatically.It is used for managing resources (files, database connections, etc.).Example: using (var file = new FileStream("file.txt", FileMode.Open)) { ... }

### What is the IDisposable interface?
IDisposable interface provides a mechanism to release unmanaged resources.It contains a single method: Dispose().Classes that use unmanaged resources should implement IDisposable.

## Miscellaneous
### What is the difference between String and string?
String: .NET Framework class (System.String).string: C# keyword (alias for System.String).They are the same. 'string' is preferred for readability.

### What is a nullable type?
A nullable type can represent the normal range of values for its underlying type, plus null.Syntax: int? x = null;Useful for database fields that can be null.

### What is the ?? operator (null-coalescing operator)?
The ?? operator returns the left operand if it is not null; otherwise, it returns the right operand.Example: int x = nullableInt ?? 0;

### What is the ?. operator (null-conditional operator)?
The ?. operator safely accesses members of an object that might be null.If the object is null, it returns null instead of throwing an exception.Example: string name = person?.Name;

### What is reflection?
Reflection is the ability to inspect and manipulate metadata about types, methods, properties, etc., at runtime.It is used for dynamic type creation, late binding, and accessing private members.Example: Type type = typeof(MyClass);

### What is serialization?
Serialization is the process of converting an object into a format that can be stored or transmitted (e.g., JSON, XML, binary).Deserialization is the reverse process.Used for saving object state, transmitting data over networks, etc.

### What is dependency injection?
Dependency injection (DI) is a design pattern where dependencies are provided to a class rather than the class creating them.Benefits: Loose coupling, easier testing, better maintainability.Example: Constructor injection, property injection, method injection.

### What is the difference between var and dynamic?
var: Type is determined at compile time (statically typed).dynamic: Type is determined at runtime (dynamically typed).var is preferred for better performance and type safety.

### What is the difference between is and as operators?
is: Checks if an object is of a specific type. Returns true or false.as: Attempts to cast an object to a specific type. Returns null if the cast fails.

### What is pattern matching?
Pattern matching allows you to test expressions for specific patterns and extract data.Introduced in C# 7.0.Example: if (obj is int number) { Console.WriteLine(number); }

### What is a tuple?
A tuple is a data structure that can hold multiple values of different types.Introduced in C# 7.0.Example: (int, string) tuple = (1, "Hello");

### What is deconstruction?
Deconstruction allows you to unpack values from tuples or objects into separate variables.Example: var (id, name) = GetPerson();

### What is a record?
A record is a reference type that provides value-based equality.Introduced in C# 9.0.Records are immutable by default and are useful for data transfer objects (DTOs).Example: record Person(string Name, int Age);

### What is the init accessor?
The init accessor allows a property to be set during object initialization but not afterward.Introduced in C# 9.0.Example: public string Name { get; init; }

### What is a local function?
A local function is a function defined inside another function.It is only accessible within the containing function.Example: void OuterFunction() { void InnerFunction() { } }

### What is expression-bodied member?
Expression-bodied members provide a concise syntax for simple methods, properties, and other members.Example: public int Square(int x) => x * x;
