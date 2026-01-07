# DISCIPLINE C#
## Delegates ...
### Delegates.
A delegate object encapsulates a reference to a method.

### Multicast Delegate.
The Multicast delegate is a delegate that points to and eventually fires off several methods.

### Create Partial Delegates And Enumerations
No, you cannot create partial delegates and enumerations.

### I Create A Delegate/multicastdelegate
C# requires only a single parameter for delegates: the method address.Unlike other languages, where the programmer must specify an object reference and the method to invoke, C# can infer both pieces of information by just specifying the method's name.For example, let's use System.Threading.ThreadStart: Foo MyFoo = new Foo(); ThreadStart del = new ThreadStart(MyFoo.Baz); This means that delegates can invoke static class methods and instance methods with the exact same syntax!C# 2.0 New FeaturesSupport for all of the new framework features such as generics, anonymous methods, partial classes, iterators and static classes.Delegate inference is a new feature of the C# compiler which makes delegate usage a little simpler.

### It allows you to write this
Thread t = new Thread(ThreadFunc);

### Instead of this
Thread t = new Thread( new ThreadStart(ThreadFunc) );Another minor but welcome addition is the explicit global namespace, which fixes a hole in namespace usage in C# 1.x.You can prefix a type name with global:: to indicate that the type belongs to the global namespace, thus avoiding problems where the compiler infers the namespace and gets it wrong.Finally C# 2.0 includes some syntactic sugar for the new System.Nullable type.You can use T question mark as a synonym for System.Nullable<T>, where T is a value type.As suggested by the name, this allows values of the type to be 'null', or 'undefined'.

## Generics
### Generics.
Generics are the most powerful features introduced in C# 2.0.It is a type-safe data structure that allows us to write codes that works for any data types.

### Generic Class.
A generic class is a special kind of class that can handle any types of data.We specify the data types during the object creations of that class.It is declared with the open, close angle brackets.

### Generics advantages.
Allows creating type-safe classes and methods.Faster. It reduces boxing/un-boxingIncreased code performanceIncreases code reuse and type safety.

## Collections ...
### Collections.
Sometimes we need to work with related objects for data storage and retrieval.There are two ways to work with related objects.One is array and another one is collections.Arrays are most useful for creating and working with a fixed number of strongly-typed objects.Collections are enhancement of array which provides a more flexible way to work with groups of objects.The Microsoft .NET framework provides specialized classes for data storage and retrieval.Collections are one of them.Collection is a data structure that holds data in different ways.Collections are two types.Standard collections, in System.Collections.Generic collections, in System.Collections.Generic.The generic collections are more flexible and preferable to work with data.Common System.Collections collections: ArrayList, SortedList, Hashtable, Stack, Queue and BitArray.

### What The .NET Collection Classes Allow An Element To Be Accessed Using A Unique Key
HashTable, Dictionary, NameValueCollection.

## Assemblies ...
### Ways To Deploy An Assembly.
An MSI Installer.A CAB archive.XCopy command.

### The Dll Hell Problem Solved In .NET
In .NET, Assembly versioning allows the application to specify not only the library it needs to run ,but also the version of the assembly.Satellite Assembly.When you write a multilingual or multi-cultural application in .NET, and want to distribute the core application separately from the localized modules, the localized assemblies that modify the core application are called satellite assemblies.

### How's The Dll Hell Problem Solved In .NET
Assembly versioning allows the application to specify not only the library it needs to run (which was available under Win32), but also the version of the assembly.

### The Ways To Deploy An Assembly
An MSI installer, a CAB archive, and XCOPY command.

### The Smallest Unit Of Execution In .NET
an Assembly.

### It Possible To Inline Assembly Or Il In C# Code
No.

### You Specify A Custom Attribute For The Entire Assembly (rather Than For A Class)
Global attributes must appear after any top-level using clauses and before the first type or namespace declarations.

### An example of this is as follows
using System;[assembly : MyAttributeClass] class X {}Note that in an IDE-created project, by convention, these attributes are placed in AssemblyInfo.cs.

### What Do You Know About .NET Assemblies
Assemblies are the smallest units of versioning and deployment in the .NET application.Assemblies are also the building blocks for programs such as Web services, Windows services, serviced components, and .NET remoting applications.

### The Difference Between Private And Shared Assembly
Private assembly is used inside an application only and does not have to be identified by a strong name.Shared assembly can be used by multiple applications and has to have a strong name.

### You Tell The Application To Look For Assemblies At The Locations Other Than Its Own Install
Use the directive in the XML .config file for a given application.< probing privatePath=c:\mylibs; bin\debug />should do the trick.Or you can add additional search paths in the Properties box of the deployed application.

### You Debug Failed Assembly Binds
Use the Assembly Binding Log Viewer (fuslogvw.exe) to find out the paths searched.

### Shared Assemblies Stored
Global assembly cache.

### You Create A Strong Name For A .NET Assembly
With the help of Strong Name tool (sn.exe).

### Where's Global Assembly Cache Located On The System
Usually C:\winnt\assembly or C:\windows\assembly.

### Have Two Files With The Same File Name In Gac
Yes, remember that GAC is a very special folder, and while normally you would not be able to place two files with the same name into a Windows folder, GAC differentiates by version number as well, so it's possible for MyApp.dll and MyApp.dll to co-exist in GAC if the first one is version 1.0.0.0 and the second one is 1.1.0.0.So Let's Say I Have An Application That Uses Myapp.dll Assembly, Version 1.0.0.0.There Is A Security Bug In That Assembly, And I Publish The Patch, Issuing It Under Name Myapp.dll 1.1.0.0.

### I Tell The Client Applications That Are Already Installed To Start Using This New Myapp.dll
Use publisher policy.To configure a publisher policy, use the publisher policy configuration file, which uses a format similar app .config file.But unlike the app .config file, a publisher policy file needs to be compiled into an assembly and placed in the GAC.

### I Create A Multi Language, Multi File Assembly
Unfortunately, this is currently not supported in the IDE.To do this from the command line, you must compile your projects into netmodules (/target:module on the C# compiler), and then use the command line tool al.exe (alink) to link these netmodules together.

### The Equivalent To Regsvr32 And Regsvr32 /u A File In .NET Development
Try using RegAsm.exe.The general syntax would be: RegAsm.A good description of RegAsm and its associated switches is located in the .NET SDK docs.Just search on "Assembly Registration Tool".Explain ACID rule of thumb for transactions.Transaction must be Atomic (it is one unit of work and does not dependent on previous and following transactions), Consistent (data is either committed or roll back, no in-between case where something has been updated and something hasnot), Isolated (no transaction sees the intermediate results of the current transaction), Durable (the values persist if the data had been committed even if the system crashes right after).

### I Create A Multilanguage, Single-file Assembly
This is currently not supported by Visual Studio .NET.

### Explain Manifest & Metadata.
Manifest is metadata about assemblies.Metadata is machine-readable information about a resource, or data about data.In .NET, metadata includes type definitions, version information, external assembly references, and other standardized information.Manifest: Manifest describes assembly itself.Assembly Name, version number, culture, strong name, list of all files, Type references, and referenced assemblies.Metadata: Metadata describes contents in an assembly classes, interfaces, enums, structs, etc., and their containing namespaces, the name of each type, its visibility/scope, its base class, the nterfaces it implemented, its methods and their scope, and each method's parameters, type's properties, and so on.

## Serialization ...
### Serialization
When we want to transport an object through network then we need to convert the object into a stream of bytes.Serialization is a process to convert a complex objects into stream of bytes for storage (database, file, cache, etc) or transfer.Its main purpose is to save the state of an object.De-serialization is the reverse process of creating an object from a stream of bytes to their original form.

### The Types Of Serialization


### The types of Serializations are given bellow
1  Binary Serialization            In this process all the public, private, read only members are serialized and convert into stream of bytes.This is used when we want a complete conversion of our objects.2  SOAP Serialization           In this process only public members are converted into SOAP format.This is used in web services.3  XML Serialization            In this process only public members are converted into XML.This is a custom serialization.Required namespaces: System.Xml, System.Xml.Serialization.

### Serialization And Deserialization
For example consider, we have a very complex object and we need XML format to show it on HTML page.Then we can create a XML file in the disk, writes all the necessary data on the XML file, and use it for the HTML page.But this is not good approach for large number of users.Extra space is required; anyone can see the XML file which creates security issue.We can overcome it by using XML serialization.

### To Use Serialization


### Serialization is used in the following purposes
To pass an object from on application to anotherIn SOAP based web servicesTo transfer data through cross platforms, cross devices

### Give Examples Where Serialization Is Used
Serialization is used to save session state in ASP.NET applications, to copy objects to the clipboard in Windows Forms.It is also used to pass objects from one application domain to another.Web services uses serialization.

## Attributes ...
### Attribute In C#
An attributes is a declarative tag that is used to convey information about the behaviors of various elements (classes, methods, assemblies, structures, enumerators, etc). it is access at compile time or run-time. Attributes are declare with a square brackets [] which is places above the elements.[Obsolete(Don't use Old method, please use New method, true)]For example consider the bellow class.If we call the old method it will through error message.public class myClass{    [Obsolete("Don't use Old method, please use New method", true)]    public string Old() { return "Old"; }    public string New() { return "New"; }}myClass omyClass = new myClass();omyClass.Old();

### Attributes Are Used
In a program the attributes are used for adding metadata, like compiler instruction or other information (comments, description, etc).

### The Types Of Attributes
The Microsoft .NET Framework provides two types of attributes: the pre-defined attributes and custom built attributes.

### Pre-define attributes are three types
AttributeUsageConditionalObsoleteThis marks a program that some entity should not be used.

### Custom Attributes
The Microsoft .NET Framework allows creating custom attributes that can be used to store declarative information and can be retrieved at run-time.

## Constructors ...
### Can I Call A Virtual Method From A Constructor/destructor


### I Make My Destructor Virtual
A C# destructor is really just an override of the System.Object Finalize method, and so is virtual by definition.

### A Constructor In C#


### In C#, What Will Happen If You Do Not Explicitly Provide A Constructor For A Class
If you do not provide a constructor explicitly for your class, C# will create one by default that instantiates the object and sets all the member variables to their default values.

### Structs Are Not Reference Types. Can Structs Have Constructors
Yes, even though Structs are not reference types, structs can have constructors.

### Static Class Constructors.
We Cannot Create Instances Of Static Classes.Yet, static classes can have constructors.

### Private Constructors.
A private constructor Prevents A Class From Being Instantiated.

### Can A Class Or A Struct Have Multiple Constructors
Yes, a class or a struct can have multiple constructors. Constructors in csharp can be overloaded.A Child Class Can Call The Constructor Of A Base Class.Yes, a child class can call the constructor of a base class by using the base keyword as shown in the example below.class BaseClass {

### Public BaseClass(string str) containing
Console.WriteLine(str);End BaseClassclass ChildClass : BaseClass {   public ChildClass(string str): base(str) { }

### Public static void Main() containing
ChildClass CC = new ChildClass("Calling base class constructor from child class");End ChildClassThe base constructor is called before the child constructor.When an instance of a child class is created, the base class constructor is called before the child class constructor.Static Constructors.A class can have static constructor.Static constructors are called automatically, immediately before any static fields are accessed, and are generally used to initialize static class members.It is called automatically before the first instance is created or any static members are referenced.Static constructors are called before instance constructors.

### Mark Static Constructor With Access Modifiers
No, we cannot use access modifiers on static constructor.

### Have Parameters For Static Constructors
No, static constructors cannot have parameters.

### What Happens If A Static Constructor Throws An Exception
If a static constructor throws an exception, the runtime will not invoke it a second time, and the type will remain uninitialized for the lifetime of the application domain in which your program is running.

### Give 2 Scenarios Where Static Constructors Can Be Used
1. A typical use of static constructors is when the class is using a log file and the constructor is used to write entries to this file.2. Static constructors are also useful when creating wrapper classes for unmanaged code, when the constructor can call the LoadLibrary method.

### C# Provide Copy Constructor
No, C# does not provide copy constructor.

### Declare A Class Or A Struct As Constant
No, User-defined types including classes, structs, and arrays, cannot be const. Only the C# built-in types excluding System.Object may be declared as const. Use the readonly modifier to create a class, struct, or array that is initialized one time at runtime (for example in a constructor) and thereafter cannot be changed.

### Declare A Field Readonly
Yes, a field can be declared readonly. A read-only field can only be assigned a value during initialization or in a constructor.A Struct cannot Have A Default Constructor (a Constructor Without Parameters) Or A Destructor.

### If A Base Class Has A Number Of Overloaded Constructors, And An Inheriting Class Has A Number Of Overloaded Constructors; Can You Enforce A Call From An Inherited Constructor To A Specific Base Constructor
Yes, just place a colon, and then keyword base (parameter list to invoke the appropriate constructor) in the overloaded constructor definition inside the inherited class.

### If A Base Class Has A Bunch Of Overloaded Constructors, And An Inherited Class Has Another Bunch Of Overloaded Constructors, Can You Enforce A Call From An Inherited Constructor To An Arbitrary Base Constructor
Yes, just place a colon, and then keyword base (parameter list to invoke the appropriate constructor) in the overloaded constructor definition inside the inherited class.C# Provides A Default Constructor For Me. I Write A Constructor That Takes A String As A Parameter, But Want To Keep The No Parameter One.

### How Many Constructors Should I Write
Two. Once you write at least one constructor, C# cancels the freebie constructor, and now you have to write one yourself, even if there is no implementation in.

### The Difference Between Const And Static Read-only
The difference is that static read-only can be modified by the containing class, but const can never be modified and must be initialized to a compile time constant. To expand on the static read-only case a bit, the containing class can only modify it: -- in the variable declaration (through a variable initializer).-- in the static constructor (instance constructors if it's not static).

### Do I Get An Error (cs1006) When Trying To Declare A Method Without Specifying A Return Type
If you leave off the return type on a method declaration, the compiler thinks you are trying to declare a constructor. So if you are trying to declare a method that returns nothing, use void. The following is an example: // This results in a CS1006 error public static staticMethod (mainStatic obj) // This will work as wanted public static void staticMethod (mainStatic obj)

### Explain Constructor.
Constructor is a method in the class which has the same name as the class (in VB .NET its New()). It initializes the member attributes whenever an instance of the class is created.

## Garbage Collection, Finally, Dispose ...
### Describe Ways Of Cleaning Up Objects.
There is a perfect tool provide by .NET frameworks calls Garbage collector, where by mean of GC we can clean up the object and reclaim the memory. The namespace used is System.GCthe run time will maintain a service called as garbage collector. This service will take care of deallocating memory corresponding to objects. it works as a thread with least priority. when application demands for memory the runtime will take care of setting the high priority for the garbage collector, so that it will be called for execution and memory will be released. the programmer can make a call to garbage collector by using GC class in system name space.

### You Clean Up Objects Holding Resources From Within The Code
Call the dispose method from code for clean up of objects.

### There A Way To Force Garbage Collection
Yes. Set all references to null and then call System.GC.Collect(). If you need to have some objects destructed, and System.GC.Collect() doesn't seem to be doing it for you, you can force finalizers to be run by setting all the references to the object to null and then calling System.GC.RunFinalizers().Destructors And Garbage Collection.C# has finalizers (similar to destructors except that the runtime doesn't guarantee they'll be called).Currently, they override object.Finalize(), which is called during the GC process.

### Dispose Method Do With The Connection Object
Deletes it from the memory.

### Destructor.
A Destructor has the same name as the class with a tilde character and is used to destroy an instance of a class.

### Can A Class Have More Than 1 Destructor
Destructors, IDisposable, the Dispose method and the Garbage Collector.The C# destructor syntax (with the familiar ~ character) is just syntactic sugar for an override of the System.Object Finalize method.This Finalize method is called by the garbage collector when it determines that an object is no longer referenced, before it frees the memory associated with the object.The garbage collector makes no guarantees about when this procedure happens.The CLR garbage collector may take a long time after the application has finished with the object.This is called non-deterministic finalization.It means that C# destructors are not suitable for releasing scarce resources such as database connections, file handles, etc.To achieve deterministic destruction, a class must offer a method to be used for the purpose.The standard approach is for the class to implement the IDisposable interface.The user of the object must call the Dispose() method when it has finished with the object.C# offers the using construct to make this easier.No, a class can have only 1 destructor.Structs cannot have Destructors.Structs can have constructors but not destructors, only classes can have destructors.You Cannot Pass Parameters To Destructors.You cannot pass parameters to destructors.

### Can A Class Have More Than 1 Destructor (part 2)
Hence, you cannot overload destructors.You Cannot Explicitly Call A Destructor.You cannot explicitly call a destructor. Destructors are invoked automatically by the garbage collector.Do Not Use Empty Destructors.When a class contains a destructor, an entry is created in the Finalize queue.When the destructor is called, the garbage collector is invoked to process the queue.If the destructor is empty, this just causes a needless loss of performance.You can Force Garbage Collector To Run.It possible to force garbage collector to run by calling the Collect() method, but this is not considered a good practice because this might create a performance over head. Usually the programmer has no control over when the garbage collector runs. The garbage collector checks for objects that are no longer being used by the application. If it considers an object eligible for destruction, it calls the destructor(if there is one) and reclaims the memory used to store the object.

### Usually In .NET, The Clr Takes Care Of Memory Management. Is There Any Need For A Programmer To Explicitly Release Memory And Resources? If Yes, Why And How
If the application is using expensive external resource, it is recommend to explicitly release the resource before the garbage collector runs and frees the object. We can do this by implementing the Dispose method from the IDisposable interface that performs the necessary cleanup for the object. This can considerably improve the performance of the application.

### Do We Generally Use Destructors To Release Resources
If the application uses unmanaged resources such as windows, files, and network connections, we usedestructors to release resources.

### The Dispose Method Do With The Connection Object
Dispose places the connection backing the managed pool. So that other objects/class can use the connection for further use.

### I Get Deterministic Finalization In C#
In a garbage collected environment, it's impossible to get true determinism.However, a design pattern that we recommend is implementing IDisposable on any class that contains a critical resource.Whenever this class is consumed, it may be placed in a using statement, as shown in the following example:When the code leaves the lexical scope of the using, its dispose method will be called.

## Arrays
### We Sort The Elements Of The Array In Descending Order
For This,First we call the Sort () method and then call Reverse() Methods.

### Can We Store Multiple Data Types In System.array
No.

### The Difference Between The System.array.copyto() And System.array.clone()
System.Array.CopyTo()-->It require a destination array to be existed before and it must be capable to hold all the elements in the source array from the index that is specified to copy from the source array.System.Array.Clone()-->It does not require the destination array to be existed as it creates a new one from scratch.Note-These both are used as a shallow copy.

### Store Multiple Data Types In System.array
No.

### The Difference Between The System.array.copyto() And System.array.clone()
The first one performs a deep copy of the array, the second one is shallow.

### You Sort The Elements Of The Array In Descending Order
By calling Sort() and then Reverse() methods.

### C# Do Array Bounds Checking
Yes. An IndexOutOfRange exception is used to signal an error.

### An Array
An array is a data structure that contains several variables of the same type.

### The 3 Different Types Of Arrays
1. Single-Dimensional2. Multidimensional3. Jagged

### Jagged Array
A jagged array is an array of arrays.

### Arrays Value Types Or Reference Types
Arrays are reference types.

### The Base Class For Array Types
System.Array.

### Use Foreach Iteration On Arrays In C#
Yes,Since array type implements IEnumerable, you can use foreach iteration on all arrays in C#.

### C# Support Properties Of Array Types
Yes.

### C# Support Parameterized Properties
No. C# does, however, support the concept of an indexer from language spec. An indexer is a member that enables an object to be indexed in the same way as an array. Whereas properties enable field-like access, indexers enable array-like access. As an example, consider the Stack class presented earlier. The designer of this class may want to expose array-like access so that it is possible to inspect or alter the items on the stack without performing unnecessary Push and Pop operations. That is, Stack is implemented as a linked list, but it also provides the convenience of array access.Indexer declarations are similar to property declarations, with the main differences being that indexers are nameless (the name used in the declaration is this, since this is being indexed) and that indexers include indexing parameters. The indexing parameters are provided between square brackets.

## Safe and Unsafe Code, Managed code ...
### Unsafe Code
In order to maintain security and type safety, C# does not support pointer generally. But by using unsafe keyword we can define an unsafe context in which pointer can be used. The unsafe code or unmanaged code is a code block that uses a pointer variable. In the CLR, unsafe code is referred to as unverifiable code. In C#, the unsafe code is not necessarily dangerous. The CLR does not verify its safety. The CLR will only execute the unsafe code if it is within a fully trusted assembly. If we use unsafe code, it is our own responsibility to ensure that the code does not introduce security risks or pointer errors.

### The Properties Of Unsafe Code


### Some properties of unsafe codes are given bellow
We can define Methods, types, and code blocks as unsafeIn some cases, unsafe code may increase the application's performance by removing array bounds checksUnsafe code is required in order to call native functions that require pointersUsing unsafe code brings security and stability risksIn order to compile unsafe code, the application must be compiled with /unsafe

### Can Unsafe Code Be Executed In Untrusted Environment
Unsafe code cannot be executed in an un-trusted environment. For example, we cannot run unsafe code directly from the Internet.

### Compile Unsafe Code
For compiling unsafe code, we have to specify the /unsafe command-line switch with command-line compiler.For example: to compile a program named myClass.cs containing unsafe code the command line command is:csc /unsafe myClass.csIn Visual Studio IDE at first we need to enable use of unsafe code in the project properties.

### The steps are given bellow
Open project propertiesClick on the Build tabSelect the option Allow unsafe code

### I Use Unsafe Code In C#
In C#, pointer is really used and Microsoft disengaged to use it. But there are some situations that require pointer.

### We can use pointer if required at our own risk. Some sonorous are given bellow
To deal with existing structures on diskSome advanced COM or Platform Invoke scenarios that involve pointerTo performance critical codes

## Strings ...
### The Difference Between String Keyword And System.string Class
string keyword is an alias for Syste.String class.Therefore, System.String and string keyword are the same, and you can use whichever naming convention you prefer.The String class provides many methods for safely creating, manipulating, and comparing strings.

### String Objects Mutable Or Immutable
String objects are immutable.

### What Do You Mean By String Objects Are Immutable
String objects are immutable means, they cannot be changed after they have been created.All of the String methods and C# operators that appear to modify a string actually return the results in a new string object.In the following example, when the contents of s1 and s2 are concatenated to form a single string, the two original strings are unmodified.The += operator creates a new string that contains the combined contents.That new object is assigned to the variable s1, and the original object that was assigned to s1 is released for garbage collection because no other variable holds a reference to it.

### A Verbatim String Literal And Why Do We Use It
The "@" symbol is the verbatim string literal.Use verbatim strings for convenience and better readability when the string text contains backslash characters, for example in file paths.Because verbatim strings preserve new line characters as part of the string text, they can be used to initialize multiline strings.Use double quotation marks to embed a quotation mark inside a verbatim string.

### The Following Code Compile And Run
string str = null;Console.WriteLine(str.Length);The above code will compile, but at runtime System.NullReferenceException will be thrown

### You Create Empty Strings In C#
Using string.empty as shown in the example below.string EmptyString = string.empty;

### The Difference Between System.text.stringbuilder And System.string
1. Objects of type StringBuilder are mutable where as objects of type System.String are immutable.2. As StringBuilder objects are mutable, they offer better performance than string objects of type System.String3. StringBuilder class is present in System.Text namespace where String class is present in System namespace.

### You Determine Whether A String Represents A Numeric Value
To determine whether a String represents a numeric value use TryParse method as shown in the example below.If the string contains nonnumeric characters or the numeric value is too large or too small for the particular type you have specified,TryParse returns false and sets the out parameter to zero.Otherwise, it returns true and sets the out parameter to the numeric value of the string.

### The Difference Between System.string And System.text.stringbuilder Classes
System.String is immutable. System.StringBuilder was designed with the purpose of having a mutable string where a variety of operations can be performed.

### One Compare Strings In C#
In the past, you had to call .ToString() on the strings when using the == or != operators to compare the strings' values. That will still work, but the C# compiler now automatically compares the values instead of the references when the == or != operators are used on string types. If you actually do want to compare references, it can be done as follows: if ((object) str1 == (object) str2) { }

### Console.writeline() Stop Printing When It Reaches A Null Character Within A String
Strings are not null terminated in the runtime, so embedded nulls are allowed. Console.WriteLine() and all similar methods continue until the end of the string.

### The Advantage Of Using System.text.stringbuilder Over System.string
StringBuilder is more efficient in the cases, where a lot of manipulation is done to the text. Strings are im mutable , so each time it is being operated on, a new instance is created.

### I Convert A String To An Int In C#
String s = "105";int x = Convert.ToInt32(s);

### String versus Stringbuilder.
StringBuilder is more efficient than string.String is Immutable and resides within System Namespace.StringBuilder is mutable and resides System.Text Namespace.

### I Do A Case-insensitive String Comparison
Use the String.Compare function. Its third parameter is a boolean which specifies whether case should be ignored or not.

## Interfaces
### An Interface Class
This is an abstract class with public abstract methods , all of which must be implemented in the inherited classes.Interfaces, like classes, define a set of properties, methods, and events. But unlike classes, interfaces do not provide implementation. They are implemented by classes, and defined as separate entities from classes.

### The Difference Between An Interface And Abstract Class
In an interface, all methods must be abstract but in abstract class some methods can be concrete.In interface No accessibility modifiers are alloweded but in abstract class a accessibility modifier are alloweded.

### Can An Interface Contain Fields
No, an Interface cannot contain fields.

### The Difference Between Class Inheritance And Interface Inheritance
Classes and structs can inherit from interfaces just like how classes can inherit a base class or struct. However there are 2 differences.1. A class or a struct can inherit from more than one interface at the same time where as A class or a struct cannot inherit from more than one class at the same time.

### Can An Interface Inherit From Another Interface
Yes, an interface can inherit from another interface. It is possible for a class to inherit an interface multiple times, through base classes or interfaces it inherits. In this case, the class can only implement the interface one time, if it is declared as part of the new class. If the inherited interface is not declared as part of the new class, its implementation is provided by the base class that declared it. It is possible for a base class to implement interface members using virtual members; in that case, the class inheriting the interface can change the interface behavior by overriding the virtual members.

### Create An Instance Of An Interface
No, you cannot create an instance of an interface.

### If A Class Inherits An Interface, What Are The 2 Options Available For That Class
Option 1: Provide Implementation for all the members inheirted from the interface.Option 2: If the class does not wish to provide Implementation for all the members inheirted from the interface, then the class has to be marked as abstract.

### What Do You Mean By "explicitly Implemeting An Interface". Give An Example
If a class is implementing the inherited interface member by prefixing the name of the interface, then the class is "Explicitly Implemeting an Interface member". The disadvantage of Explicitly Implemeting an Interface member is that, the class object has to be type casted to the interface type to invoke the interface member.

### Can't You Specify The Accessibility Modifier For Methods Inside The Interface
They all must be public, and are therefore public by default.

### Inherit Multiple Interfaces
Yes. .NET does support multiple interfaces.

### What Happens If You Inherit Multiple Interfaces And They Have Conflicting Method Names
It's up to you to implement the method inside your own class, so implementation is left entirely up to you. This might cause a problem on a higher-level scale if similarly named methods from different interfaces expect different data, but as far as compiler cares you're okay.To Do: Investigate.

### Cannot You Specify The Accessibility Modifier For Methods Inside The Interface
They all must be public. Therefore, to prevent you from getting the false impression that you have any freedom of choice, you are not allowed to specify any accessibility, it is public by default.

### From A Versioning Perspective, What Are The Drawbacks Of Extending An Interface As Opposed To Extending A Class
With regard to versioning, interfaces are less flexible than classes. With a class, you can ship version 1 and then, in version 2, decide to add another method. As long as the method is not abstract (i.e., as long as you provide a default implementation of the method), any existing derived classes continue to function with no changes. Because interfaces do not support implementation inheritance, this same pattern does not hold for interfaces. Adding a method to an interface is like adding an abstract method to a base class--any class that implements the interface will break, because the class doesn't implement the new interface method.

# C# [Best Qs]
### C# is a Microsoft object oriented language and is derived from C and C++.


### C# borrows concepts from Java, including garbage collection.


### You cannot have Different Access Modifiers On The property Get/set Methods.


### The access modifier on a property applies to both its get and set accessors.
To be different, make the property read-only by only providing a get accessor and create a private/internal set method that is separate from the property.

### The 4 Pillars Of Any Object Oriented Programming Language are: Abstraction, Inheritance, Encapsulation and Polymorphism.


### Again, Abstraction, Inheritance, Encapsulation and Polymorphism.


### The Main Advantage Of Using Inheritance
Code reuse.

### C# Support Multiple-inheritance
No, but you can implement more than one interfaces.

### The Top .NET Class That Everything Is Derived From
System.Object.

### The Syntax To Inherit From A Class In C#
Place a colon and then the name of the base class.Example: class MyNewClass : MyBaseClass.

### If A Class Derives From Another Class, Will The Derived Class Automatically Contain All The Public, Protected, And Internal Members Of The Base Class
Yes, the derived class will automatically contain all the public, protected, and internal members of the base class except its constructors and destructors.Multiple Inheritance is NOT supported.Use interfaces instead.

### The Implicit Name Of The Parameter That Gets Passed Into The Set Method/property Of A Class
Value. The data type of the value parameter is defined by whatever data type the property is declared as.

### Strong Names:
A strong name includes the name of the assembly, version number, culture identity, and a public key token.Again, A strong name includes the name of the assembly, version number, culture identity, and a public key token.

### The is operator:
Example: expr is type.Expression is an instance of this type.

### The Term Immutable Mean
The data value may not be changed.The variable value may be changed, but the original immutable data value was discarded and a new data value was created in memory.

### Indexers: Static Indexers are NOT allowed.


### Method Out Integer Parameters:
Declare the variable as an integer.Mark the parameter as out integer.

### Class Types:
Abstract, Partial, Sealed and Static.

### Abstract Class: Declare using the abstract keyword. Methods are defined as abstract or non-abstract. Cannot create an object of this class.


### Partial Class: A single class can be split into multiple files. During compilation, all the functionalities of the same partial class are merged and compiled.


### Sealed Class: Sealed classes restrict inheritance. A sealed class cannot be inherited. The variable & methods in sealed class can be accessed in main().


### Static Class: Class that cannot be instantiated. Cannot create an object. Class members can be called directly using their class name.


### Constructor:
The Constructor is a method having the same name as its class name and it is invoked when a object is created. It initializes an object of a class.

### Namespace:
The namespace keyword is used to declare a scope.This helps organize code and lets you create globally-unique types.Namespaces are implicitly public and you cannot change this behavior.Declaration does not support modifiers or attributes.

### Interface vs Class:


### Class:
Has both a definition and an implementation.A class generally implements the methods defined in an interface.

### Interface:
only has a definition. Interfaces are implemented via a class.Interfaces define properties, methods, and events, which are the members of the interface.Interfaces contain only the declaration of the members.It is the responsibility of the deriving class to define the members.

### Delegates:
Delegates contain the reference to several methods and call them when needed.So, you create numbers of methods as you need and attach it to delegates.At runtime, an event gets fired and delegates dynamically call the function and show the result.

### Const vs Readonly:


### Const:    Cannot be changed anywhere. They are static by default


### Readonly: This value can only be changed in the constructor. It cannot be changed in normal functions and are evaluated when instance is created.


### Encapsulation: Encapsulation is handled using access modifiers.
Using public, private and protected access specifiers, we can implement how a class will be accessed and from where.

### Public:
class, variable etc can be accessed from anywhere in application, means variables inside class can be accessed by outside of class.

### Private:
class, variable etc can only be accessed by same class members, and variables, functions etc cannot be accessed by any member outside of class

### Protected:
access specifier allows a child class to access the member variables and member functions of its base class

### Interface vs abstract class:
Interfaces have all the methods having only declaration but no definition. Abstract classes can have some concrete methods.In an interface class, all the methods are public. An abstract class may have private methods.

### Generics:
Make code reusable, type safe, and performance optimized.Allow the developer to create generic classes, methods, events, delegates, and interfaces.Allow the developer to create generic collection classes in the System.Collections.Generic namespace.You may get information on the types used in a generic data type at run-time by means of reflection

## Access Modifiers
### The 5 Access Modifiers are: public, protected, internal, protected internal and private.


### Protected:
Protected class-level variables are available to derived-classes.

### Private:
Private class variables are inherited, but not accessible.    Private is the Default Access Modifier.

### Protected Internal:
Protected internal variables are available to classes in the same assembly and derived from the specified base class.

### Accessibility Modifier Protected Internal:
It is available to derived classes and classes within the same Assembly (and naturally from the base class it is declared in).

### You Inherit A Protected Class-level Variable, Who Is It Available To
Classes in the same namespace.

## Structs:
### Do Structs Support Inheritance
No, structs do not support inheritance, but they can implement interfaces.

### C# Support Multiple Class Inheritance
No, C# supports single class inheritance only. However classes can implement multiple interfaces at the same time.

### Static: Structs cannot be declared as static.


### Struct instantiation: Structs can be instantiate without using A New Operator.


### Struct inhertance:
Structs do not support inheritance.    Structs cannot inherit from Another Struct Or Class.    Structs cannot be a base class.    Structs can inherit from an Interface.    Structs inherit directly from System.ValueType, which inherits from System.Object.

### Struct type: Structs are Value Types.
A struct is a value type mean when a struct is created, the variable to which the struct is assigned holds the struct's actual data.    When the struct is assigned to a new variable, it is copied.    The new variable and the original variable therefore contain two separate copies of the same data.    Changes made to one copy do not affect the other copy.

## Structs vs Classes:
### Generally Use A Class Over A Struct
A class is used to model more complex behavior, or data that is intended to be modified after a class object is created.A struct is best suited for small data structures that contain primarily data that is not intended to be modified after the struct is created.

### The Difference Between A Struct And A Class
Structs are value-type variables and are thus saved on the stack, additional overhead but faster retrieval.Another difference is that structs cannot inherit.

### Struct vs Class:
The list of similarities between classes and structs is as follows.Longstructs can implement interfaces and can have the same kinds of members as classes.Structs differ from classes in several important ways; however, structs are value types rather than reference types, and inheritance is not supported for structs.Struct values are stored on the stack or in-line.Careful programmers can sometimes enhance performance through judicious use of structs.For example, the use of a struct rather than a class for a Point can make a large difference in the number of memory allocations performed at runtime.The program below creates and initializes an array of 100 points.With Point implemented as a class, 101 separate objects are instantiated-one for the array and one each for the 100 elements.

## Classes
### What Do You Mean By Saying A "class Is A Reference Type"
A class is a reference type means when an object of the class is created, the variable to which the object is assigned holds only a reference to that memory.When the object reference is assigned to a new variable, the new variable refers to the original object.Changes made through one variable are reflected in the other variable because they both refer to the same data.

## Static Classes and Methods
### Create An Instance Of A Static Class
No, you cannot create an instance of a static class.

### Can A Static Class Contain Non Static Members
No, a static class can contain only static members.You CANNOT Declare The Override Method Static While The Original Method Is Non-static.The signature of the virtual method must remain the same, only the keyword virtual is changed to keyword override.You cannot Declare An Override Method To Be Static If The Original Method Is Not Static:The signature of the virtual method must remain the same.Only the keyword virtual is changed to keyword override.

## Sealed
### A Sealed Class
A sealed class is a class that cannot be inherited from.

### Can A Sealed Class Be Used As A Base Class
No, sealed class cannot be used as a base class. A compile time error will be generated.

### You Prevent A Class From Being Inherited By Another Class
Use the sealed keyword to prevent a class from being inherited by another class.

### Prevent Your Class From Being Inherited By Another Class
Yes. The keyword sealed will prevent the class from being inherited.

### Allow A Class To Be Inherited, But Prevent The Method From Being Over-ridden
Yes. Just leave the class public and make the method sealed.You can Prevent Your Class From Being Inherited And Becoming A Base Class For Some Other Classes:Use the sealed keyword in the class definition.The developer trying to derive from your class will get a message: cannot inherit from Sealed class WhateverBaseClassName.

### Allow Class To Be Inherited, But Prevent The Method From Being Over-ridden
Yes, just leave the class public and make the method sealed.

## Method Overloading
### Method Overloading:


### 3 ways to overload a method:
Different parameter data types,Different number of parameters,Different order of parameters.

### The 5 Access Modifiers are: public, protected, internal, protected internal and private.


### Method Overloading: Different parameter data types, number of parameters or order of parameters.


## Overloading vs Overriding
### Method Overriding vs Method Overloading:
When overriding a method, you change the behavior of the method for the derived class.Overloading a method simply involves having another method with the same name within the class.

### Method Overriding vs Overloading:
When overriding, you change the method behavior for a derived class.Overloading simply involves having a method with the same name within the class.

## Abstract Class
### An Abstract Class
An abstract class is an incomplete class and must be implemented in a derived class.A class that cannot be instantiated.An abstract class is a class that must be inherited and have the methods overridden.An abstract class is essentially a blueprint for a class without any implementation.

### Absolutely Have To Declare A Class As Abstract (as Opposed To Free-willed Educated Choice Or Decision Based On Uml Diagram)
When at least one of the methods in the class is abstract.When the class itself is inherited from an abstract class, but not all base abstract methods have been over-ridden.

### Create An Instance For An Abstract Class
No, you cannot create an instance for an abstract class.

### Absolutely Have To Declare A Class As Abstract
1. When the class itself is inherited from an abstract class, but not all base abstract methods have been overridden.2. When at least one of the methods in the class is abstract.

### Create An Instance Of An Abstract Class
No, abstract classes are incomplete and you cannot create an instance of an abstract class.

### Abstract Methods
Abstract methods are methods that only the declaration of the method and no implementation.

### You Force Derived Classes To Provide New Method Implementations For Virtual Methods
Abstract classes can be used to force derived classes to provide new method implementations for virtual methods.When an abstract class inherits a virtual method from a base class, the abstract class can override the virtual method with an abstract method.If a virtual method is declared abstract, it is still virtual to any class inheriting from the abstract class.A class inheriting an abstract method cannot access the original implementation of the method.In the above example, Method() on class NonAbstractChildClass cannot call Method() on class BaseClass.In this way, an abstract class can force derived classes to provide new method implementations for virtual methods.

## Virtual method vs Abstract method:
### Abstract Method:
Location:   Resides in an abstract class.Body:       Has no body.Overriding: Must be overridden.            Must Override in non-abstract or abstract child class.

### Virtual Method:
Location:   Resides in either an abstract or non-abstract class.Body:       Must have body.Overriding: Not necessary to override.            Can be overridden in a derived class with the override keyword.

### Concreteness:
Abstract Methods: Are not concrete and have no body.Virtual Methods:  Are concrete and must have a body.

### Location:
Abstract Methods: Reside in an abstract class.Virtual Methods:  Reside in either an abstract or non-abstract class.

### Overriding:
Abstract Methods: Must   overriden. Must override in either an abstract or non-abstract derived class.Virtual methods:  May be overriden. May override  in either an abstract or non-abstract derived class.

### Keyword virtual:
Declare methods with the virtual keyword to declare them as virtual.Virtual methods must have a body incase they are not overridden.Abstract Methods do not require a body.

### Keyword abstract:
Declare a class as abstract.Declare a method as abstract or virtual.

### Keyword override:
In a derived class, declare methods as override if they are overriding either an abstract or virtual method in the base class.

### Declaration:


#### public abstract class M   public abstract void AbstractMethod   public virtual  void VirtualMethod open-bracket optional-body close-bracket#### public class D colon M   public override void AbstractMethod   public override void VirtualMethod

## Virtual Methods
### Method Virtual Keyword:
The method can be over-ridden.

### You CANNOT Override Private Virtual Methods.
Moreover, you cannot access private methods in inherited classes, have to be protected in the base class to allow any sort of access.

## Databases
### The Wildcard Character In SQL
The wildcard character is %.

### Between Windows Authentication And SQL Server Authentication, Which One Is Trusted And Which One Is Untrusted
Windows Authentication is trusted because the username and password are checked with the Active Directory, the SQL Server authentication is untrusted, since SQL Server is the only verifier participating in the transaction.

### The Data Provider Name To Connect To Access Database
Microsoft.Access.

### The Datareader Class In ADO.NET Connections:
It returns a read-only, forward-only rowset from the data source.A DataReader provides fast access when a forward-only sequential read is needed.

## Cleanup
### You Call The Garbage Collector In .NET
As a good rule, you should not call the garbage collector. However, you could call the garbage collector when you are done using a large object (or set of objects) to force the garbage collector to dispose of those very large objects from memory. However, this is usually not a good practice.

## Trace vs Debug
### Debug Class vs Trace Class:
Documentation looks the same. Use Debug class for debug builds, use Trace class for both debug and release builds.

### Debug Class vs Trace Class:
Documentation looks the same.Use Debug class for debug builds.Use Trace class for both debug and release builds.

### I Do Implement A Trace And Assert
Use a conditional attribute on the method. Conditional[TRACE].Then, call Debug.Trace().The TRACE preprocessor symbol must be defined at the call site.Define preprocessor symbols on the command line by using the /D switch.The restriction on conditional methods is that they must have void return type.

### Assert() Method:
In debug compilation, assert takes in a Boolean condition as a parameter, and shows the error dialog if the condition is false. The program proceeds without any interruption if the condition is true.

## Threading
### Sample C# Code For Simple Threading:
using System.Threading;Declare method: public void runme().ThreadTest b = new ThreadTest();Thread t = new Thread(new ThreadStart(b.runme));t.Start();

## Value and Reference Types
### Value Types vs Reference Types:
Value type - bool, byte, chat, decimal, double, enum , float, int, long, sbyte, short, strut, uint, ulong, ushortValue types are stored in the StackBY VAL: changes will not be reflected back to the variable.

### Reference type - class, delegate, interface, object, string
Reference types are stored in the HeapBy REF: changes will be reflected back to that variable.( same as & symbol in c, c++)

### Boxing and Unboxing:
Boxing   converts a value-type to a reference-type. The reference object is stored on the heap.Unboxing converts a reference-type to a value-type. The value is stored on the stack.Convert a value-type to a reference-type using Boxing.Convert a reference-type to a value-type using Unboxing.

## Exceptions
### The Finally Block Get Executed If An Exception Has Not Occurred
Yes. Finally block always get executed.

### The C# Syntax To Catch Any Possible Exception
A catch block that catches the exception of type System.Exception. You can also omit the parameter data type in this case and just write catch {}.

### Can Multiple Catch Blocks Be Executed For A Single Try Statement
No. Once the proper catch block processed, control is transferred to the finally block (if there are any).

### I Get Around Scope Problems In A Try/catch
If you try to instantiate the class inside the try, it'll be out of scope when you try to access it from the catch block.Set the variable to null before the try block.

### If I Return Out Of A Try/finally, The Code In The Finally-clause Runs
The code in the finally always runs.If you return out of the try block, or even if you do a goto out of the try, the finally block always runs.Both In Try block and In Finally block will be displayed.Whether the return is in the try block or after the try-finally block, performance is not affected either way.The compiler treats it as if the return were outside the try block anyway.If it's a return without an expression (as it is above), the IL emitted is identical whether the return is inside or outside of the try.If the return has an expression, there's an extra store/load of the value of the expression (since it has to be computed within the try block).

### I Get Around Scope Problems In A Try/catch
If you try to instantiate the class inside the try, it'll be out of scope when you try to access it from the catch block.Set the variable to null before the try block.

## Arrays
### Array:
A collection of elements storing the same type of data.

### Parallel arrays:
Two arrays that store related information in corresponding element positions are parallel arrays.

## Array Declaration
### Size:
You can declare an array without dimensioning its size,but the size must be determined before you can reference it.

### Length:
In C# the length of an array cannot be changed.After it is instantiated with a length, dynamic resizing is not an option.

### Declaration:
Example: Declare memory for 4 values ranging from 0 to 100: int open-close-bracket myArray = new myArray bracket 4 bracketExample: An array to hold 5 Rectangle objects is declared as: Rectangle open-close bracket myRectangle = new Rectangle bracket 5 bracket.

### 2-dimensional array declaration example:
int open-bracket comma close-bracket sales = new int open-bracket 2 comma 3 close-bracket

## Array Elements
### Element data types:
Every element has the same data type.

### Element default values:
In numerical 1 & 2 dimensional arrays, if you don't provide values for elements, all elements default to 0.

## Array Size, Length, Range, Index, Subscript
### Length property:
Returns an integer representing the dimensioned size of the array.

### Index or Subscript:
The index is also referred to as the subscript of an array.

### Indexes:
The smallest array index is 0.

### Range:
If an array is size n, the range of the index is 0 to n - 1.For an array of size 3, the range is 0 to 2.

### Indexes: Element access:
Given int myArray open bracket close bracket = open-curly 2, 3, 5, 8, 9, 11 close-curly.Access the fourth element in myArray as: myArray open bracket 3 close bracket

### Indexes: Index of element:


### The index of the array holding the value of 5 is 2 in this example
for open-parenthesis int i=0 semicolon i < 10; i plus plus close-parenthesismyArray bracket i bracket = 2 times i plus 1.Again, the index of the array holding the value of 5 is 2.

### Indexes: Array Out-of-bounds error
If an array is sized 10, for example, then using 10 as the indexer throws the Array Out-of-bounds error.

## Array: Multi-dimensional arrays
### Multi dimensional array declaration:
Use multiple square brackets.Example: int myArray bracket 20 bracket bracket 20 bracketExample: int open-close-bracket open-close-bracket myArray = new int bracket 3 bracket bracket 3 bracket.

### Multi-dimensional array example:
float myArray open-close-bracket open-close-bracket =open-curly   open-curly 0.0 close-curly comma   open-curly 1.0, 1.1 close-curly comma   open-curly 2.0, 2.1, 2.2 close-curly

### MyArray of 2 1 contains value 2.1 in the following
close-curlyExample: myArray of 2 1 contains value 2.1.  2 1 access the 3rd row and 2nd column.Example: myArray of 3 0 does not exist. 3 0 is out of bounds or out of range.Example: myArray of 1 1 = 7.8 replaces 1.1 with 7.8.

## Array: Jagged Arrays
### Jagged Array:
A jagged array is an array of arrays of difference dimensions and sizes.In a 2-dimensional jagged array, only the outer array is dimensioned. The inner array is dynamic.

### Jagged Array Example:
string open-close-bracket open-close-bracket jaggedArray = new string open-bracket 2 close-bracket open-close-bracketopen-outer-curly-bracket   new string open-close-bracket open-curly-bracket banana comma mango close-curly-bracket   new string open-close-bracket open-curly-bracket orange comma apple comma watermelon close-curly-bracketclose-outer-curly-bracket

## More
### Sortedlist:
Namespace: System.Collections.Generic.Sorts based on ICompare of T.SortedList takes parametes T Key and T Value. T Key is the type of keys in the collection. T Value is the type of values in the collection.Example:    SortedList string string.Inherits:   System.IdentityModel.Metadata.IndexedProtocolEndpointDictionaryImplements: ICollection, IDictionary, IEnumerable, IReadOnlyCollection and IReadOnlyDictionary.Derived from a sorted HashTable.Uses less memory than a SortedDictionary.The SortedList Item property is the indexer. Therefore, don use the property name. Just use the key.The KeyNotFoundException exception may be thrown.

### XML Documentation tags <c> and <code>:
C is for a single line code example.Code is for a multiple-line code example.

### Set Property: What is the implicit name of the parameter
Value. The value datatype is the property's datatype.

### Mark A Method Obsolete:
[Obsolete] public integer Foo()or[Obsolete("with a a message describing why the method is obsolete")] public integer Foo()The O in Obsolete is always capitalized.

### Delay Signing:
Delay signing allows you to place a shared assembly in the GAC by signing the assembly with just the public key.This allows the assembly to be signed with the private key at a later stage, when the development process is complete and the component or assembly is ready to be deployed.This process enables developers to work with shared assemblies as if they were strongly named.It secures the private key of the signature from being accessed at different stages of development.

### Environment.Exit:
Use System.Environment.Exit for quitting an application.Use Application.Exit if it is a Windows Forms app.

### I Make A Dll
You need to use the /target:library compiler option.

### Regular Expression (regex):
The .NET class libraries provide support for regular expressions.Look at the documentation for the System.Text.RegularExpressions namespace.

### Would You Use Untrusted Verification
Web Services might use it, as well as non-Windows applications.

### Regasm:


### I Register My Code For Use By Classic Com Clients
Use the regasm.exe utility to generate a type library (if needed) and the necessary entries in the Windows Registry to make a class available to classic COM clients.Once a class is registered in the Windows Registry with regasm.exe, a COM client can use the class as though it were a COM class.

### It Possible To Restrict The Scope Of A Field/method Of A Class To The Classes In The Same Namespace
There is no way to restrict to a namespace.Namespaces are never units of protection.But if you're using assemblies, you can use the 'internal' access modifier to restrict access to only within the assembly.

### I Create A Process That Is Running A Supplied Native Executable like Cmd.exe
Process p = Process.Start(args[0]);p.WaitForExit();Reference System.Diagnostics.dll.

### XML Documentation tags <c> and <code>:
C is for a single line code example.Code is for a multiple-line code example.

### Set Property: What is the implicit name of the parameter
Value. The value datatype is the property's datatype.Like the pound define statement in C code.

### Templates are NOT supported:
However, there are plans for C# to support a type of template known as a generic.These generic types have similar syntax but are instantiated at run time as opposed to compile time.

### C Type Macros are NOT supported.


### My Windows Application Pop Up A Console Window Every Time I Run It
Make sure that the target type set in the project properties setting is set to Windows Application, and not Console Application.If you're using the command line, compile with /target:winexe & not target:exe.

### I Get The Ascii Code For A Character
Casting the char to an int will give you the ASCII value: char c = 'f';

### System.Console.WriteLine((int)c); or for a character in a string
System.Console.WriteLine((int)s[3]);The base class libraries also offer ways to do this with the Convert class or Encoding classes if you need a particular encoding.

### Registry access:
Access the registry by using Microsoft.Win32.Registry.LocalMachine and Microsoft.Win32.RegistryKey classes.Use the Registry.LocalMachine property, and methods, RegistryKey.OpenSubKey and RegistryKey.GetValue.Set your RegistryKey to Registry.LocalMachine.Call RegistryKey.OpenSubKey with string parameter SystemCentralProcessor.Call RegistryKey.GetValue with parameter VendorIdentifier.GetValue will return the machine's central processor identifier value.

### XML Documentation tags <c> and <code>:
C is for a single line code example.Code is for a multiple-line code example.

### Set Property: What is the implicit name of the parameter
Value. The value datatype is the property's datatype.

### Imperative vs Interrogative Code:
Imperative functions return a value.Interrogative functions do not return a value.

### Which Controls Do Not Have Events
Timer control.The Maximum Size Of The Textbox is 65536.

### Which Property Of The Textbox Cannot Be Changed At Runtime
Locked Property.

### Which Control Cannot Be Placed In Mdi
The controls that do not have events.

# SQL SERVER
## GENERAL
### SQL Server used for
SQL Server is one of the very popular Relational Database Management Systems.This is a product from Microsoft to store and manage the information in the database.

### What function does a database engine serve in the SQL Server
Database Engine is a type of service in the SQL Server which starts as soon as the Operating System starts.This may run by default depending upon the settings in the O/S.

### RDBMS
RDBMS or Relational Database Management Systems are database management systems that maintain data in the form of tables.We can create relationships between the tables.An RDBMS can recombine the data items from different files, providing powerful tools for data usage.

### Which TCP/IP port does SQL Server run on
By default SQL Server runs on port 1433.

### OLTP
OLTP means Online Transaction Processing which follows rules of data normalization to ensure data integrity.Using these rules, complex information is broken down into a most simple structure.

### Collation
Collation refers to a set of rules that determine how data is sorted and compared.Character data is sorted using rules that define the correct character sequence, with options for specifying case-sensitivity, accent marks, kana character types, and character width.Collation is defined to specify the sort order in a table.Sort Order: There are three types of sort order: Case sensitive, Case Insensitive, Binary

### Replication required on the SQL Server
Replication is the mechanism that is used to synchronize the data among the multiple servers with the help of a replica set.This is mainly used to increase the capacity of reading and to provide an option to its users to select among various servers to perform the read/write operations.

### What do mean by XML Datatype
XML data type is used to store XML documents in the SQL Server database.Columns and variables are created and store XML instances in the database.

### CDC
CDC is abbreviated as Change Data Capture which is used to capture the data that has been changed recently.This feature is present in SQL Server 2008.

## VERSIONS
### Which is the latest version of SQL Server and when it is released
SQL Server 2019 is the latest version of SQL Server that is available in the market and Microsoft launched this on November 4th, 2019 with the support of the Linux O/S.

### The various editions of SQL Server 2019 that are available in the market
SQL Server 2019 is available in 5 editions.Enterprise: The Enterprise edition  delivers comprehensive high-end datacenter capabilities with blazing-fast performance, unlimited virtualization, and end-to-end business intelligence for mission-critical workloads and end-user access to data insights.Standard: The Standard edition delivers basic data management and business intelligence database for departments and small organizations to run their applications and supports common development tools for on-premises and cloud-enabling effective database management.Web: The Web edition is a low total-cost-of-ownership option for Web hosters and Web VAPs to provide scalability, affordability, and manageability capabilities for small to large-scale Web properties.Express: The Express edition is the entry-level, free database and is ideal for learning and building desktop and small server data-driven applications.Developer:  The Developer edition lets developers build any kind of application on top of SQL Server.The Developer edition includes all the functionality of Enterprise edition, but is licensed for use as a development and test system, not as a production server.

## PROGRAMMING QUESTIONS
### Delete duplicate rows in SQL Server
Duplicate rows can be deleted using CTE and ROW NUMER feature of SQL Server.

### How data can be copied from one table to another table
INSERT INTO SELECT  is used to insert data into a table which is already created.SELECT INTO         is used to create a new table and its structure and data can be copied from existing table.

### BCP or Bulkcopy
BCP or Bulk Copy is a tool by which we can copy a large amount of data to tables and views.BCP does not copy the structures the same as source to destination.Bulkcopy is a tool used to copy large amount of data from Tables.Bulkcopy is used to load large amount of data in SQL Server.The BULK INSERT command helps to import a data file into a database table or view in a user-specified format.

## SQL INJECTION
### SQL INJECTION - What is SQL injection
SQL injection is an attack by malicious users in which malicious code can be inserted into strings that can be passed to an instance of SQL server for parsing and execution.All statements have to checked for vulnerabilities as it executes all syntactically valid queries that it receives.Even parameters can be manipulated by the skilled and experienced attackers.

### SQL INJECTION ATTACK PREVENTION - What are the methods used to protect against SQL injection attack
Use Parameters for Stored ProceduresFiltering input parametersUse Parameter collection with Dynamic SQLIn like clause, user escape characters

## BACKUP LOGS and BULK COMMANDS
### A Full Backup
A full backup is the most common type of backup in SQL Server.This is the complete backup of the database.It also contains part of the transaction log so that it can be recovered.

### Log Shipping
Log shipping is nothing but the automation of backup and restores the database from one server to another standalone standby server.This is one of the disaster recovery solutions.If one server fails for some reason we will have the same data available on the standby server.

### The advantages of Log shipping
Easy to set up.The secondary database can be used as a read-only purpose.Multiple secondary standby servers are possibleLow maintenance.

### Can we take the full database backup in Log shipping
Yes, we can take the full database backup.It won't affect the log shipping.

### The recovery model? List the types of recovery models available in SQL Server
The recovery model tells SQL Server what data should be kept in the transaction log file and for how long.A database can have only one recovery model.It also tells SQL server which backup is possible in a particular selected recovery model.

### There are three types of recovery models
FullSimpleBulk-Logged

### The different backups available in SQL Server
Full backupDifferential Backup

## USERS, AUTHENTICATION, LOGIN
### The two authentication modes in SQL Server
Windows ModeMixed Mode SQL and WindowsModes can be changed by selecting the tools menu of SQL Server configuration properties and choose security page.

### SQL server usernames and passwords are stored in a SQL server
They get stored in System Catalog Views sys.server_principals and sys.sql_logins.

### You create a login
You can use the following command to create a loginCREATE LOGIN MyLogin WITH PASSWORD = '123';

### SQL Server user names and passwords stored in SQL Server
User Names and Passwords are stored in sys.server_principals and sys.sql_logins.But passwords are not stored in normal text.

## AGENTS, TASKS
### AGENTS, TASKS Overview
The scheduled job allows a user to run the scripts or SQL commands automatically on a scheduled basis.The user can determine the order in which command executes and the best time to run the job to avoid the load on the system.

## LINKED SERVERS
### Can SQL servers linked to other servers
SQL server can be connected to any database which has OLE-DB provider to give a link.Example: Oracle has OLE-DB provider which has link to connect with the SQL server group.

## MIRRORING
### Mirroring
Mirroring is a high availability solution.It is designed to maintain a hot standby server which is consistent with the primary server in terms of a transaction.Transaction Log records are sent directly from the principal server to a secondary server which keeps a secondary server up to date with the principal server.

### The advantages of the Mirroring
It is more robust and efficient than Log shipping.It has an automatic failover mechanism.The secondary server is synced with the primary in near real-time.

## LOCKS
### Can we check locks in database? If so, how can we do this lock check
Yes, we can check locks in the database.It can be achieved by using in-built stored procedure called sp_lock.

## PERFORMANCE
### The common performance issues in SQL Server
DeadlocksBlockingMissing and unused indexes.I/O bottlenecksPoor Query plansFragmentation

### List the various tools available for performance tuning
Windows Performance monitorSQL Server ProfilerQuery PlansQuery OptimizerTuning advisorDynamic Management ViewsServer Side Traces

### A PERFORMANCE MONITOR
The Windows performance monitor captures server metrics and SQL server events.Some useful counters are Disks, Memory, Processors, Network, etc.

### The SQL PROFILER
The SQL Profiler provides a graphical representation of events in an instance of SQL Server for monitoring and investment purpose.The SQL Profiler is a tool which allows system administrator to monitor events in the SQL server.The SQL Profiler captures and saves data about each event of a file or a table for analysis.

### QUERY PLANS and QUERY OPTIMZERS
SQL is a declarative language.A QUERY PLAN is a (list of instructions) that the database follows to execute a (query) on the data.SQL (queries) describe what the user wants.The (query) is transformed into (executable commands) by the QUERY OPTIMIZER.The (executable commands) are known as QUERY PLANS.The QUERY OPTIMIZER generates multiple QUERY PLANS for a single query and determines the most efficient plan to run.

### An EXECUTION PLAN
An execution plan is a graphical or textual way of showing how the SQL server breaks down a query to get the required result.It helps a user to determine why queries are taking more time to execute and based on the investigation user can update their queries for the maximum result.Query Analyzer has an option, called Show Execution Plan (located on the Query drop-down menu).If this option is turned on, it will display a query execution plan in a separate window when the query is run again.

## EXCEPTIONS
### How exceptions can be handled in SQL Server Programming
Exceptions are handled using TRY----CATCH constructs and it is handles by writing scripts inside the TRY block and error handling in the CATCH block.

## NORMALIZATION
### Normalization


### 1st Normal Form
Eliminate repeating groups in individual tables.Create a seperate table for each set of related data.Identify each set of related data with a primary key.Do not use multiple fields in a single table to store similar data.Example: To track an inventory item that may come from 2 possible sources, an inventory record may contain fields for Vendor Code1 and Vendor Code 2.

### 2nd Normal Form
Create seperate tables for sets of values that apply to multiple records.Relate these tables with a foreign key.

### 3rd Normal Form
Eliminate fields that do not depend on the key.

### Normalization
The process of table design to minimize the data redundancy is called normalization.We need to divide a database into two or more tables and define relationships between them.Normalization usually involves dividing a database into two or more tables and defining relationships between the tables.

### List the different normalization forms
1NF (Eliminate Repeating Groups): Make a separate table for each set of related attributes, and give each table a primary key.Each field contains at most one value from its attribute domain.2NF (Eliminate Redundant Data): If an attribute depends on only part of a multi-valued key, remove it to a separate table.3NF (Eliminate Columns Not Dependent On Key): If attributes do not contribute to the description of the key, remove them to a separate table.All attributes must be directly dependent on the primary key.BCNF (Boyce-Codd Normal Form): If there are non-trivial dependencies between candidate key attributes, separate them into distinct tables.4NF (Isolate Independent Multiple Relationships): No table may contain two or more 1:n or n:m relationships that are not directly related.5NF (Isolate Semantically Related Multiple Relationships): There may be practical constraints on information that justifies separating logically related many-to-many relationships.ONF (Optimal Normal Form): A model limited to only simple (elemental) facts, as expressed in Object Role Model notation.DKNF (Domain-Key Normal Form): A model free from all modification is said to be in DKNF.

### De-normalization
De-normalization is the process of adding redundant data to a database to enhance the performance of it.It is a technique to move from higher to lower normal forms of database modeling to speed up database access.SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.

## TYPES
## CLAUSES: HAVING, WHERE and FOR
## COMMANDS: UNION, MINUS, INTERSECT
## COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR
### COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR Overview
SET NOCOUNT OFF - Display the number of records affected when commands are executed.        SET NOCOUNT ON  - Do not display the number of records affected. Default setting.   RAISERROR command.        RAISEERROR is used for user defined error messages.        RAISEERROR generates and initiates error processing for a given session.        Those user defined messages are stored in sys.messages table.

## LOCAL and GLOBAL VARIABLES - SYSTEM DEFINED FUNCTIONS
## FUNCTIONS
### Functions in the SQL Server
Functions are the sequence of the statements which accept inputs, process the inputs to perform some specific task and then provide the outputs.Functions should have some meaningful name but these should not start with a special character such as %, #, @, etc.Functions: SUBSTR and CHARINDEX.SUBSTR    returns a specific portion of string in a given string.CHARINDEX returns the character position in a given string.SUBSTRING('Smiley',1,3)     returns: SmiCHARINDEX('i', 'Smiley',1)  returns: 3 as result as I appears in 3rd position of the string.Function: FLOOR.FLOOR rounds up a non-integer value to the previous least integer.Example: FLOOR(6.7) Returns 6.Function: SIGN.SIGN determines whether the number specified is Positive, Negative or Zero.SIGN returns +1, -1 or 0.Example: SIGN(-35) returns -1Function: ISNULL().ISNULL function checks whether value given is NULL or not NULL.ISNULL provides to replace a value with the NULL.Function: COALESCE.COALESCE returns the first non-null expression within the arguments.COALESCE returns a non-null from more than one column in the arguments.Example: SELECT COALESCE(empno, empname, salary) FROM employee;

## USER-DEFINED FUNCTIONS
### A User-Defined function in the SQL Server and what is its advantage
User-Defined Function is a function that can be written as per the needs of the user by implementing your logic.The biggest advantage of this function is that the user is not limited to pre-defined functions and can simplify the complex code of pre-defined function by writing a simple code as per the requirement.This returns Scalar value or a table.

### User-defined function creation
CREATE FUNCTION FunctionOne(at num int)   returns table   AS   RETURN SELECT * FROM employee WHERE empid = at num;

### User-defined function execution
SELECT * FROM FunctionOne(12);   A function named FunctionOne is created to fetch employee details of an employee having empid=12.

## PRE-DEFINED FUNCTIONS
## SUBQUERIES
### A Subquery
A Subquery is a subset of SELECT statements, whose return values are used in filtering conditions of the main query.It can occur in a SELECT clause, FROM clause and WHERE clause.It is nested inside a SELECT, INSERT, UPDATE, or DELETE statement or inside another subquery.

### Types of Sub-query
Single-row sub-query:      The subquery returns only one row   Multiple-row sub-query:    The subquery returns multiple rows   Multiple column sub-query: The subquery returns multiple columns

### Sub query and its properties
A sub-query is a query which can be nested inside a main query like SELECT, UPDATE, INSERT or DELETE statements.This can be used when expression is allowed.Properties of sub query can be defined asA sub query should not have order by clauseA sub query should be placed in the right hand side of the comparison operator of the main queryA sub query should be enclosed in parenthesis because it needs to be executed first before the main queryMore than one sub query can be included

### The types of sub query
There are three types of sub querySingle row sub query which returns only one rowMultiple row sub query which returns multiple rowsMultiple column sub query which returns multiple columns to the main query.With that sub query result, Main query will be executed.

## TABLES and COLUMNS
### Table records: How can we get count of the number of records in a table
SELECT * from <tablename>SELECT COUNT(*) from <tablename>SELECT rows FROM sysindexes WHERE id=OBJECT_ID(tablename) AND indid<2

### The properties of the Relational tables


### Relational tables have six properties
Values are atomic.

### Identity in SQL
An identity column in the SQL automatically generates numeric values.We can be defined as a start and increment value of the identity column.Identity columns do not need to be indexed.Column values are of the same kind.Each row is unique.The sequence of columns is insignificant.The sequence of rows is insignificant.Each column must have a unique name.

### Can we rename a column in the output of the SQL query
Yes, by using the following syntax we can do this.SELECT column_name AS new_name FROM table_name;SECT returns all distinct rows selected by both queries.

### TABLESAMPLE
TABLESAMPLE is used to extract sample of rows randomly that are all necessary for the application.The sample rows taken are based on the percentage of rows.

## DELETE and TRUNCATE
## LOCAL and GLOBAL TEMPORARY TABLES
## VIEWS
### A View
A view is a virtual table that contains data from one or more tables.Views restrict data access of the table by selecting only required values and make complex queries easy.Rows updated or deleted in the view are updated or deleted in the table the view was created with.It should also be noted that as data in the original table changes, so does data in the view, as views are the way to look at part of the original table.The results of using a view are not permanently stored in the database

### Views required in the SQL Server or any other database


### Views are very beneficial because of the following reasons
Views are required to hide the complexity that is involved in the database schema and also to customize the data for a particular set of users.Views provide a mechanism to control access to particular rows and columns.These help in aggregating the data to improve the performance of the database.

## COLUMNS
### An IDENTITY column in insert statements
IDENTITY column is used in table columns to make that column as Auto incremental number or a surrogate key.

### The PRIMARY KEY
The primary key is a column whose values uniquely identify every row in a table.Primary key values can never be reused.

### The difference between a primary key and a unique key
The primary key is a column whose values uniquely identify every row in a table.Primary key values can never be reused.They create a clustered index on the column and cannot be null.A Unique key is a column whose values also uniquely identify every row in a table but they create a non-clustered index by default and it allows one NULL only.

### A UNIQUE KEY constraint
A UNIQUE constraint enforces the uniqueness of the values in a set of columns, so no duplicate values are entered.The unique key constraints are used to enforce entity integrity as the primary key constraints.

### FOREIGN KEY
When a one table's primary key field is added to related tables to create the common field which relates the two tables, it called a foreign key in other tables.Foreign Key constraints enforce referential integrity.

### A CHECK Constraint
A CHECK constraint is used to limit the values or type of data that can be stored in a column.They are used to enforce domain integrity.

## INDEXES
### The difference between clustered and non-clustered index
A clustered index is an index that rearranges the table in the order of the index itself.Its leaf nodes contain data pages.A table can have only one clustered index.A non-clustered index is an index that does not re-arrange the table in the order of the index itself.Its leaf nodes contain index rows instead of data pages.A table can have many non-clustered indexes.

### List the different index configurations possible for a table


### A table can have one of the following index configurations
No indexesA clustered indexA clustered index and many non-clustered indexesA non-clustered indexMany non-clustered indexes

### The advantages of having an index on the SQL Server
Index supports the mechanism of having faster data retrieval from the database.This forms a data structure in a way that helps in minimizing data comparisons.This improves the performance of the retrieval of the data from the database.

### 3 ways to get a count of the number of records in a table
SELECT * FROM table_Name;SELECT COUNT(*) FROM table_Name;SELECT rows FROM indexes WHERE id = OBJECT_ID(tableName) AND indid&amp;amp;lt; 2;

### A heap
A heap is a table that does not contain any clustered index or non-clustered index.

### The advantages of having an index on the SQL Server
Index supports the mechanism of having faster data retrieval from the database.This forms a data structure in a way that helps in minimizing data comparisons.This improves the performance of the retrieval of the data from the database.

### Filtered Index
Filtered Index is used to filter some portion of rows in a table to improve query performance, index maintenance and reduces index storage costs.When the index is created with WHERE clause, then it is called Filtered Index

### What will be the maximum number of index per table
For SQL Server 2008 100 Index can be used as maximum number per table.1 Clustered Index and 999 Non-clustered indexes per table can be used in SQL Server.1000 Index can be used as maximum number per table.1 Clustered Index and 999 Non-clustered indexes per table can be used in SQL Server.

## CONSTRAINTS
### How is table type constraint applied to a table


### Table Type Constraint is applied in the following way
ALTER TABLE Name of the ConstraintALTER TABLE Constraint_1

### COLUMN Types Constraints
These constraints are applied to the columns of a table in the SQL Server.The definition of these can be given at the time of the creation of a table in the database.TABLE Types Constraints: These constraints are applied on a table and these are defined after the creation of a table is complete.Alter command is used to apply the table type constraint.

### The different types of Columns Types Constraints
SQL Server provides 6 types of COLUMN Constraints.NOT NULL: The NOT NULL constraint puts a constraint that the value of a column cannot be null.CHECK: The CHECK constraint puts a constraint by checking some particular condition before inserting data in the table.CHECK constraints can be applied to a column in a table to limit the values that can be placed in a column.CHECK constraints enforce integrity.DEFAULT: The DEFAULT constraint provides some default value that can be inserted in the column if no value is specified for that column.UNIQUE: The UNIQUE constraint puts a constraint that each row of a particular column must have a unique value. More than one unique constraint can be applied to a single table.PRIMARY KEY: The PRIMARY KEY constraint puts a constraint to have a primary key in the table to identify each row of a table uniquely. This cannot be null or duplicate data.FOREIGN KEY: The FOREIGN KEY constraint puts a constraint that the foreign key should be there.A Primary key in one table is the foreign key of another table.Foreign Key is used to create a relation between 2 or more tables.

## SQL SERVER COMMANDS IN 4 LOGICAL GROUPS
### Which language is supported by SQL Server
SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.

### Name the 4 types of SQL commands.
DML or Data Manipulation Language.DDL or Data Definition Language.DCL or Data Control Language.TCL or Transaction Control Language.

### Using these commands we can
1. Define structure of our database.2. INSERT or UPDATE the data.3. Can control database access and privileges.

### Describe DML, or Data Manipulation Language, commands.
DML commands manipulate table records.

### DML commands are
SELECT records,INSERT new records,UPDATE existing records,DELETE existing records.UPDATE or DELETE without the WHERE clause will UPDATE or DELETE all records in the table.

### Describe DDL, or Data Definition Language, commands.
DDL commands design and define the database structure.DDL commands define and create database objects such as Tables, Procedures, Views, etc.

### DDL commands are
CREATE. Create a new table, database, procedure, view, or trigger.ALTER.  Use alter commands for editing database objects such as table, procedure, view etc, add or delete column from table.DROP.   Delete database objects.RENAME. Rename an database object existing.CREATE TABLE table-name: will create a new table. In the body of this command we enter the table's columns and attributes.Similar syntax is also for creating new Views, Procedures or Triggers.ALTER: Edit an object. For example, add a new column or attribute in a table.DROP: Delete database objects.

### Describe DCL, or Data Control Language, commands.
DCL commands are used for access control and permission management for users in our database.Allow or deny some actions for users on the tables or records.

### DCL commands are


### GRANT
GRANT permissions on the table, and other objects, for certain users of database.GRANT example: Give privileges to a user to SELECT, INSERT, UPDATE and DELETE on a table.

### DENY
DENY permissions from users.

### REVOKE
REVOKE permissions from users.REVOKE takes back privilege to the default permission.REVOKE example: Take back INSERT permissions on a table for a user.

### Describe TCL, or Transaction Control Language, commands.
TCL commands manage and control T-SQL transactions.TCL commands ensure that our transaction is successfully done.TCL commands ensure that the database integrity is not violated.

### TCL commands are
BEGIN TRAN: BEGIN TRAN marks the beginning of a transaction.COMMIT TRAN: COMMIT TRAN commits the completed transaction.COMMIT TRAN permentantly saves the transaction in the database.ROLLBACK: ROLLBACK goes back to beginning if something was not right in transaction.ROLLBACK rolls back changes. For example: (Transactional Log backup, Copy Only backup, File and Filegroup backup)SAVE TRAN: SAVE TRAN saves the transaction to provide the convenience that the transaction can be rolled back to the point wherever required.

### The difference between COMMIT and ROLLBACK
Every statement between BEGIN and COMMIT becomes persistent to database when the COMMIT is executed.Every statement between BEGIN and ROLLBACK are reverted to the state when the ROLLBACK was executed.

### Magic Tables in SQL Server
During DML operations like Insert, Delete, and Update, SQL Server creates magic tables to hold the values during the DML operations.These magic tables are used inside the triggers for data transaction.

## STORED PROCEDURES
### The Stored Procedure
A stored procedure is a set of SQL queries that can take input and send back output.And when the procedure is modified, all clients automatically get the new version.Stored procedures reduce network traffic and improve performance.Stored procedures can be used to help ensure the integrity of the database.

### List the advantages of using Stored Procedures
