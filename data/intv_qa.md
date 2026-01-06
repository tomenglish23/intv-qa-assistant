# Angular
## Node.js
## Angular Features and Benefits
### Feature categories: Cross Platform, Speed & Performance, Productivity and Full Development
Cross Platform:      Progressive Web Apps, Native and DesktopSpeed & Performance: Code Generation, Universal and Code SplittingProductivity:        Templates, Angular CLI and IDEsFull Development:    Testing, Animation and Accessibility#### CROSS PLATFORM:      Progressive Web Apps, Native & DesktopPWAs:                Modern web capabilities. High performance, offline & zero-step installs.Native:              Build native mobile apps with strategies from Cordova, Ionic or NativeScript.Desktop:             Install Mac, Windows & Linux desktop apps using web Angular methods. Access native OS APIs.#### SPEED & PERFORMANCE: Code Generation, Universal and Code SplittingCode Generation:     Turn templates into optimized codeUniversal:           Serve the app view on servers like Node.js & .NET. Quick HTML & CSS rendering. Good for SEO.Code Splitting:      New Component Router for quick loads.

### Feature categories: Cross Platform, Speed & Performance, Productivity and Full Development (continued)
Only load code required to render the requested view.#### PRODUCTIVITY:        Templates, Angular CLI and IDEsTemplates:           Create UI views with template syntax.Angular CLI:         Command line tools: Build fast, add components & tests, then deploy.IDEs:                Get intelligent code completion, instant errors and more editors & IDEs.#### FULL DEVELOPMENT:    Testing, Animation and Accessibility

### Testing with Karma:  for unit tests on save
Animation:           Create choreographies and animation timelines.Accessibility:       Create accessible apps with ARIA-enabled components, developer guides, and a11y test infrastructure.

## Angular Create, Generate & Components
### Modules:
Feature Modules: NgModules for the purpose of organizing code.Shared Modules:  Common directives/pipes/components.

### @NgModule:
@NgModule takes a metadata object that describes how to compile a component's template and how to create an injector at runtime.It identifies the module's own components, directives, and pipes, making some of them public, through the exports property, so that external components can use them.

### Webpack:
Webpack is a popular module bundler, a tool for bundling application source code in convenient chunks and for loading that code from a server into a browser.This guide offers a taste of Webpack and explains how to use it with Angular applications.

### Ng build:
ng build is the command you use when you're ready to build your application and deploy it.The CLI will analyze the application and build the files, all while optimizing the application as best as it can.

## Lazy Loading
### Lazy loading
Lazy loading is a technique in Angular that allows you to load JavaScript components asynchronously when a specific route is activated.It improves the speed of the application load time by splitting the application into several bundles.When the user navigates through the app, the bundles are loaded as required.Lazy loading is a routing technique in which the JavaScript components load in the browser only when their corresponding route is activated.The main aim of lazy loading is to improve the performance of the Angular app by restricting the unnecessary loading of components.To lazy load Angular modules, use loadChildren (instead of component) in your AppRoutingModule routes configuration as follows.content_copy const routes: Routes = [ { path: 'items', loadChildren: () => import('./items/items. module'). then(m => m.

## @Input and @Output
## Async
### Zone:
A zone is an execution context that persists across async tasks.You can think of it as thread-local storage for JavaScript VMs.This guide describes how to use Angular's NgZone to automatically detect changes in the component to update HTML.

### RxJS:


#### RxJS Observable Pipe, Subscribe, Map and Filter Examples with Angular 9/8.pipe() is a function/method that is used to chain multiple RxJS operators while map() and filter() are operators that operate and transform the values of an Observable (sequence of values).#### An RxJS Subject is a special type of Observable that allows values to be multicasted to many Observers.While plain Observables are unicast (each subscribed Observer owns an independent execution of the Observable), Subjects are multicast.A Subject is like an Observable, but can multicast to many Observers.#### flatMap function: RxJs does have a flatMap function.The principle is similar.A flatMap is used to flatten an observable of observables into a single observable.So if you used map, you would end up with an observable containing an observable.So in this use-case, flatMap is really just used to unwrap the dealer.

### Observables and Promises:
Both observables and promises help us work with asynchronous functionality in JavaScript.Promises deal with one asynchronous event at a time, while observables handle a sequence of asynchronous events over a period of time.Emit multiple values over a period of time.Emit a single value at a time.Promises in the built-in $q service.They provide a way to execute asynchronous functions in series by registering them with a promise object.Practically speaking AJAX calls using the $http service are some of the most common scenarios where promises are used.Promises deal with one asynchronous event at a time, while observables handle a sequence of asynchronous events over a period of time.Emit multiple values over a period of time.Emit a single value at a time.A promise is a placeholder for a future value.It serves the same function as callbacks but has a nicer syntax and makes it easier to handle errors.

### Pipe
The pipe method is for chaining observable operators, and the subscribe is for activating the observable and listening for emitted values.The purpose of the pipe() function is to lump together all the functions that take, and return observable.It takes an observable initially, then that observable is used throughout the pipe() function by each function used inside of it.Pipes are a useful feature in Angular.They are a simple way to transform values in an Angular template.There are some built in pipes, but you can also build your own pipes.A pipe takes in a value or values and then returns a value.

### NgFor:
NgFor has a not-so-obvious feature that lets us will help us deal with asynchronous operations - the async pipe.The async pipe takes care of subscribing/unsubscribing to Observable streams for us.Let's explore how we can handle NgFor alongside the async pipe to subscribe to an Observable!

### TakeUntil:
The takeUntil operator is used to automatically unsubscribe from an observable.It also monitors a second Observable, notifier that you provide.If the notifier emits a value, the output Observable stops mirroring the source Observable and completes.

### Services:
Services are a unit of functionality that are run independently.Services are designed to maximize reuse as opposed to being designed to fit a particular system or application.A service is a stateless object and provides some very useful functions.These functions can be invoked from any component of Angular, like Controllers, Directives, etc.This helps in dividing the web application into small, different logical units which can be reused.Each service contains one or more service components.Each service component can support one or more actual services.The service component and the actual service represent the business service logic of the organization in the Service Asset and Configuration Management data model.A service component configures a service implementation.A service component is presented in a standard block diagram.Services are singleton objects that get instantiated only once during the lifetime of an application.Services organize and share business logic, models, or data and functions with different components.Angular injectors do not know automatically how to create service instances, so we need to specify providers for every service otherwise service instance will not be injected.Injector creates singleton object of a service and hence same object is injected in components and services.

### Promises and Observables


### #### Promise
$q service: AngularJS Promises are in the built-in $q service.Register promise objects.Promises provide a way to execute asynchronous functions in series by registering them with a promise object.$http service AJAX calls are common scenarios where promises are used.#### RxJS Observables: Implemented HTTP requests to source API values.RxJS (Reactive Extensions for JavaScript)RxJS is a library for reactive programming using observables that makes it easier to compose asynchronous or callback-based code.RxJS provides an implementation of the Observable type, which is needed until the type becomes part of the language and until browsers support it.#### Observable: Items to observe and action on.Observer pattern: Register, Subscribe, Act.                  Register:  Register observable objects.                  Subscribe: Use the subscribe method to observe the observable objects.                  Act:       Take action when the observable object is acted on.

## Components and Directives
### Components:
A component is a single unit that encapsulates both view and logic.Components define views, which are sets of screen elements that Angular can choose among and modify according to your program logic and data.Components use services, which provide specific functionality not directly related to views.Components are parts of a system or application that are designed to work together.A component consists of an implementation and one or more interfaces, which defines its inputs, outputs, and faults, and also its references, if applicable.

### Directives: Build HTML+CSS modular components.


#### Directive Types: Component, Structural & AttributeComponents--directives: With a template. @Component: Forms the main class and is declared by @Component.Structural directives: Directives that change the DOM layout by adding and removing DOM elements.Attribute directives:  Directives that change the appearance or behavior of an element, component, or another directive.#### Creation: ng generate directive#### Directives enhance the behavior of components or DOM elements.Directives are classes that add additional behavior to elements.Built-in Directives:  Manage forms, lists, styles, and what users see.

### Attribute Directives: Directives that change the appearance or behavior of
an element, component, or another directive.

### #### Directive: ngModel
ngModel is a directive which binds input, select and textarea, and stores the required user value in a variable and we can use that variable whenever we require that value. It also is used during validations in a form.

## Decorators
### Decorators Overview
A set of arguments to pass to the handler method when the event occurs.

## Dependency Injection and Providers
### Providers:
Providers are classes that create and manage service objects the first time that Angular needs to resolve a dependency.Providers is used to register the classes to an angular module as a service.And then, this service classes can be used by other components during the itself creation phase in the module.A provider is an instruction to the Dependency Injection system on how to obtain a value for a dependency.Most of the time, these dependencies are services that you create and provide.For the final sample application using the provider that this page describes, see the live example / download example .

### ProvidedIn root
Providing a servicelinkThe service itself is a class that the CLI generated and that's decorated with @Injectable() .By default, this decorator has a providedIn property, which creates a provider for the service.In this case, providedIn: 'root' specifies that Angular should provide the service in the root injector.

### Dependency Injection or D I:
A design pattern. A class requests dependencies from external sources rather than creating them.Angular's DI framework provides dependencies to a class upon instantiation.Angular DI to increase flexibility and modularity in your applications.Dependency injection, or DI, is a design pattern in which a class requests dependencies from external sources rather than creating them.Angular's DI framework provides dependencies to a class upon instantiation.You can use Angular DI to increase flexibility and modularity in your applications.Dependency Injection type: constructor injection, method injection, and property injection

## Compilation
### Angular Ivy
Ivy is the code name for Angular's next-generation compilation and rendering pipeline.With the version 9 release of Angular, the new compiler and runtime instructions are used by default instead of the older compiler and runtime, known as View Engine.

### What was before Ivy
Ivy is a complete rewrite of Angular's rendering engine.In fact, it is the fourth rewrite of the engine and the third since Angular 2.But unlike rewrites two and three, which you might not have even noticed, Ivy promises huge improvements to your application.

### Angular material compatible with Ivy
The Angular team has worked hard to ensure Ivy is as backwards-compatible with the previous rendering engine ("View Engine") as possible.

### I enable Ivy in Angular 10
To update an existing project to use Ivy, set the enableIvy option in the angularCompilerOptions in your project's tsconfig.app. json . AOT compilation with Ivy is faster and should be used by default.

### Not compatible with Angular Ivy
The typical full message looks like this: This likely means that the library (@***) which declares *** has not been processed correctly by ngcc, or is not compatible with Angular Ivy.Check if a newer version of the library is available, and update if so.

### Ngcc do Angular
ngcc is the Angular compatibility compiler.ngcc is designed to process code coming from NPM and produce the equivalent Ivy version, as if the code was compiled with ngtsc .ngcc is a separate script entry point to @angular/compiler-cli .

### AOT
The Angular ahead-of-time (AOT) compiler converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.Compiling your application during the build process provides a faster rendering in the browser.

### AOT and JIT
The main differences between JIT and AOT in Angular are: Just-in-Time (JIT), compiles your app in the browser at runtime.Ahead-of-Time (AOT), compiles your app at build time on the server.JIT compilation is the default when you run the ng build (build only) or ng serve (build and serve locally) CLI commands.

### Angular 9 backward compatible
Angular 9 brings Ivy in a backwards compatible version and, as a result, smaller bundles.This provides new possibilities not only for the developer but also for future versions of Angular.With the release of Angular 9, it's ready: Ivy will finally become the standard.

### A View engine
View Engine is Angular's legacy compilation and rendering pipeline.The goal of Ivy is to make Angular simpler, faster, and easier to maintain.When it first enabled Ivy in Angular 9, the team developed a compatibility compiler called ngcc that ensures backward compatibility with libraries that use View Engine.

### Which is better AOT or JIT
Loading in JIT is slower than the AOT because it needs to compile your application at runtime.Loading in AOT is much quicker than the JIT because it already has compiled your code at build time.JIT is more suitable for development mode.AOT is much suitable in the case of Production mode.

### Which transpiler is used
TypeScriptThe compiler takes the TypeScript code and converts it into JavaScript.This process is commonly referred to as transpiling, and since the TypeScript compiler does it, it's called a transpiler.

### Flutter AOT:
1) The Dart code is ahead-of-time (AOT) compiled into a native, ARM library.2) When launched, the app loads the Flutter library.Any rendering, input or event handling, and so on, are delegated to the compiled Flutter and app code.

### DART AOT:
1. 10. A compiler creates the binary code from Dart source code.For mobile applications the source code is compiled for multiple processors ARM, ARM64, x64 and for both platforms - Android and iOS.This means there are multiple resulting binary files for each supported processor and platform combination.

### I enable AOT in Angular 8
Steps necessary to enable AOT1. Run npm install @ngtools/webpack.2. Configure Webpack: Configure AngularCompilerPlugin which comes with @ngtools.Using configuration parameters you will set up locations of tsconfig and entry files.

### Which is better kotlin or Flutter
Flutter and Kotlin are the two leading technologies used to build mobile applications.Flutter is a framework, while Kotlin is a programing language.

## General
### Angular Generic Features:
Cross-Platform. With Angular, you can develop progressive web applications (PWA).High Speed & Optimum Performance.Angular Applications for Everyone.MVC Architecture.Efficient Two-Way Data Binding.Less Code Framework.Angular CLI (Command Line Interface)CDK and Angular Material.

### Use Angular
Automatic synchronization with two-way data binding.Bug fixes.Code consistency and reusability.Default Ivy renderer.Declarative UI.Supported by Google.

### Vendor Ts:
About 1.5 years ago, Angular was officially released the so-called Angular 2 after years in beta version.polyfills: the polyfills needed to run Angular applications in most modern browsers.vendor: the third-party dependencies such as Angular, lodash, and bootstrap. css.

### Angular advantages:
Combines: dependency injection, declarative templates, end-to-end tooling.

### Use Angular instead of MVC
Angular does away with the problem of mixing client and server code within the same file.Razor syntax allows the developer to embed client and server code within the same file and to use server-side logic to control the client-side presentation.Angular decouples the client-side processing completely from the server.

### Angular disadvantages:
Limited SEO options and poor accessibility for search engine crawlers.

### Angular run in the browser
Running the Development Web ServerWhile AngularJS applications are purely client-side code, and it is possible to open them in a web browser directly from the file system, it is better to serve them from an HTTP web server.

### Which apps use Angular
Many companies use AngularJS as the frontend of their MEAN stack, consisting of the:MongoDB database.Angular. js for front-side development.Express. js web app server, and.Node. js server runtime environment.

### Angular is a front-end framwork:
That's why Angular is considered a frontend framework.Its capabilities do not include any of the features that you will find in a backend language.Angular 4 is front-end framework Powered by Google, it helps a lot in making fastest single page application and works 100% perfect.

### Angular full stack
Angular 6 is out! You'll learn Angular by example by building a full-stack CRUD -- Create, Read, Update and Delete -- web application.We will use the latest version of the most popular framework and platform for building mobile and desktop client-side applications.

### Angular 8 Advantages:
IvyEnhanced payload size.Smaller builds.Shipment of pre-compiled code.Improved backwards compatibility.Quick re-build time.No requirement of metadata.json.Advent of meta programming in Angular.

## Angular vs React vs Vue
## Companies
## TypeScript
### TypeScript mandatory for Angular
Write Angular apps in either TypeScript, ES6 or even ES5 JavaScript.Angular is written in TypeScript.

### Install script type:
$ npm install typescript with options: --save-dev, -g, @latest

### TypeScript vs JavaScript:
Language type: TypeScript: An object oriented programming language.               JavaScript: A scripting language.Modules:   TypeScript: Supports modules           JavaScript: Does not support modules.Interface: TypeScript has Interface.           JavaScript does not have Interface.

### Typescript: A superset of JavaScript.
Typescript: An interpreted language inside a web browser. No compiler needed.

## Material
## Browsers
### Polyfills: the polyfills needed to run Angular applications in most modern browsers.


### Polyfills TS
Polyfills in angular are few lines of code which make your application compatible for different browsers.The code we write is mostly in ES6(New Features: Overview and Comparison) and is not compatible with IE or firefox and needs some environment setups before being able to be viewed or used in these browsers.

### IE
Supporting Internet Explorer in an Angular CLI applicationBut, when you try to view it in Internet Explorer (IE), you see nothing.Angular CLI applications require a few more steps in order to support Internet Explorer.The good news: It's really simple: un-comment a few imports and install a couple of npm packages.

### Mobile browser JavaScript
Using only javascript (support by all modern browsers), a media query match can easily infer whether the device is mobile.There's no perfect solution for detecting whether JS code is executed on a mobile browser, but the following two options should work in most cases.

## Testing
### Karma in angular
Karma is a task runner.It uses a configuration file (karma. js) in order to set the startup file, the reporters, the testing framework and the browser among other things.Karma basically supports the execution of test cases which we will be writing in angular framework.

### TestBed angular
The TestBed is the first and largest of the Angular testing utilities.It creates an Angular testing module -- a @NgModule class-- that you configure with the configureTestingModule method to produce the module environment for the class you want to test.

### The difference between mocha and Jasmine
Mocha is younger than Jasmine, created around 2011.Mocha is not a "complete" test framework, and doesn't attempt to be.Instead, Mocha covers the basics and allows developers to extend it with other frameworks.

### Spec TS in angular
spec. ts file. This file contains unit tests for the main AppComponent.When running tests using the Angular CLI, all unit tests in files with the *.

## Bundling
### Bundle
Bundling is the process of joining multiple files into a single file.In our case, we'll be bundling all of our application's code into app.bundle.js .Third party libraries like Angular and other dependencies will be bundled into vendor.bundle.js.

### Webpack
Webpack is a popular module bundler, a tool for bundling application source code in convenient chunks and for loading that code from a server into a browser.This guide offers a taste of Webpack and explains how to use it with Angular applications.

### Which is better Webpack or Gulp
Webpack is a bundler whereas Gulp is a task runner, so you'd expect to see these two tools commonly used together.Simply put, Webpack is such a powerful tool that it can already perform the vast majority of the tasks you'd otherwise do through a task runner.

### I use Webpack with Angular
1 Answer. No. It means it uses standard TypeScript / EcmaScript imports.The Angular CLI does use Webpack, though.

## Mobile
### Angular good for mobile
Angular is an excellent tool for building any kind of mobile app.Naturally, you can use this framework to build a web application that runs on any device.Combine Angular with NativeScript, another open-source framework that allows building iOS and Android.

### Which cross-platform is best for mobile development
React Native is a star in itselfWhen we are talking about the leading cross-platform app frameworks, it is hard to not include React Native in that list.React Native is extensively used for iOS and Android as it is a well-known entity cross-platform development.

## Other
### Latest version: 12.1.3


### Tree shaking
Tree shake -- Popular term used to refer to a step during the build process where unused code is not included in the bundle, making the overall bundle smaller.

### NgbModule installation:
Manual installation: Add bootstrap and @ng-bootstrap/ng-bootstrap dependencies from npm.Install the @angular/localize polyfill.Add bootstrap CSS/SCSS to your project (no javascript is required)Import NgbModule or any other component module like NgbPaginationModule in your application.

### Clear cache:
Use the $scope. remove function

### Ng --version:
Angular version and version of all Angular packages.

### Encapsulation:
Component CSS styles are encapsulated into the component's view and don't affect the rest of the application.Emulated view encapsulation (the default) emulates the behavior of shadow DOM.It does so by preprocessing (and renaming) the CSS code to effectively scope the CSS to the component's view.

### Browserslist
ie-test\browserslist.

### The default file created by Angular CLI looks something like this
# This file is used by the build system to adjust CSS and JS output to support the specified browsers below.

### Angular app is not working in IE
Sometimes, your application may throw errors in IE11, even when it is working fine in other browsers.There can be numerous reasons why your Angular application is not working, including: Missing polyfills in polyfills.Importing third-party dependencies using a TypeScript target version which IE11 does not support.

### I use angular universal
Key Benefits for SEOA primary benefit for using Angular Universal is that it improves web crawler support for enhanced Search Engine Optimization (SEO).With traditional client-side rendered SPAs, anything that is not in that shell of an . html is all rendered by the JavaScript.

### $scope:
The $scope in an AngularJS is a built-in object, which contains application data and methods.You can create properties to a $scope object inside a controller function and assign a value or function to it.The $scope is glue between a controller and view (HTML).

### Three dots mean
The spread operator from Typescript (also from ES7).The spread operator returns all elements of an array.

### Prerender:
Angular Universal allows you to prerender the pages of your application.Prerendering is the process where a dynamic page is processed at build time generating static HTML.

### Deploy URL in angular
--deploy-urlA second parameter that is important is '--deploy-url'.This parameter will update the generated url's for our assets(scripts, css) inside the index.To make your assets available at /angularapp/, the deploy url should be set to /angularapp/.

### Python or JavaScript better
Hands down, JavaScript is undeniably better than Python for website development for one simple reason:   JS runs in the browser while Python is a backend server-side language.While Python can be used in part to create a website, it can't be used alone.JavaScript is the better choice for desktop and mobile websites.

### Lodash:
A JavaScript library that works on the top of underscore.js.Lodash helps in working with arrays, collection, strings, objects, numbers etc.

# Angular 7
### Architecture Overview Of Angular


### Angular Architecture Overview
Angular is a most popular web development framework for developing mobile apps as well as desktop applications.Angular framework is also utilized in the cross platform mobile development called IONIC and so it is not limited to web apps only.Angular is an open source framework written and maintained by angular team at Google and the Father of Angular is Misko Hevery.The bootstrapping process creates the components listed in the bootstrap array and inserts each one into the browser (DOM)

### The 7 building blocks of an Angular Application are: Component, Templates, Metadata, Data, Binding, Directives, Services and Dependency Injection.
Again, The 7 building blocks of an Angular Application are: Component, Templates, Metadata, Data, Binding, Directives, Services and Dependency Injection.

### The basic building blocks of an Angular application are NG Modules, which provide a compilation context for components.
Angular app is defined by a set of NG Modules and it always has at least a root module that enables bootstrapping, and many more feature modules.

### Components
Components define Template viewsComponents use services

### The Angular Module (NG Modules) helps us to organize an application into connected blocks of functionality.
The NG Module properties for the minimum AppModule generated by the CLI which are: Declarations, Imports, Providers and Bootstrap.Declarations: Use to declare the application components.Imports:      Every application must import BrowserModule to run the app in a browser.Providers:    There are none to start.Bootstrap:    This is a root AppComponent that Angular creates and inserts into the index.html host web page.How To Update Angular 6 To Angular 7NG update @angular/cli @angular/coreUrlsegment Interface In Angular 7

### UrlSegment Interface
UrlSegment interface represents a single URL segment and the constructor, properties, and methods look like below UrlSegment class i.e.class UrlSegment {constructor(path: string, parameters: {...})path: stringparameters: {...}toString(): string}The UrlSegment is a part of a URL between the two slashes and it contains a path and matrix parameters associated with the segment.

### Angular Compatibility Compiler (NGCC) In Angular 7


### The NGCC Angular node_module compatibility compiler
The NGCC is a tool which "upgrades" node_module compiled with non-ivy ngc into ivy compliant format.This compiler will convert node_modules compiled with Angular Compatibility Compiler (NGCC),into node_modules which appear to have been compiled with TSC compiler transformer (NGTSC) and this compiler conversions will allow such legacy packages to be used by the Ivy rendering engine.TSC transformer which removes and converts @Pipe, @Component, @Directive and@NG Module to the corresponding definePipe, defineComponent, defineDirective and defineInjector.Do Bootstrap (NG Do Bootstrap ) In Angular 7

### Do Bootstrap Interface
Angular 7 added a new life-cycle hook that is called ng Do Bootstrap and an interface that is called Do Bootstrap.Example://NG Do Bootstrap - Life-Cycle Hook InterfaceclassApp Module implements Do Bootstrap { NG Do Bootstrap(appRef: ApplicationRef) {appRef.bootstrap(AppComponent);  }}

### XMB
The XMB is key value pairs with no deeper structure.It has a mechanism for named placeholders with descriptions and examples.The  messages for any given other language must be correspond 1:1.XMB Placeholders have one example tag and a text node.The example will represent a dummy value.The text node is used as the original value from the placeholder.

### New In Angular 7: Core framework, Angular Material, CLI.


### The Ivy Rendering Engine is a new backwards-compatible Angular renderer focused on:
Speed Improvements, Size Reduction and Increased Flexibility.The template functions for creating dynamically views are no longer nested functions inside each other.Now we use for loops that are nested inside other loops.Example:functionAppComponent(rf: RenderFlags, ctx: AppComponent) {  functionulTemplateFunction(rf1: RenderFlags, ctx0: any) {    functionliTemplateFunction(rf1: RenderFlags, ctx1: any) { }  }}

### Key Value Pipe
Change your object into an array of key value pairs that output array will be ordered by keys.By default it will be by Unicode point value.Syntax: {{your input expression | key value [:compareFn] }}

### Core Dependencies
There are two types of core dependencies: RxJS 6.3 and TypeScript 3.1.RxJS 6.3 has no changes in the version from Angular 6.TypeScript 3.1 is the upgrade from the version 2.9 of Angular 6.

### Bazel
Bazel is a test tool just like the Make, Maven and Gradle and it is an open-source build.Bazel utilizes the readable and high-level build language.It handles the project in a great number of languages and builds the product for a large number of platforms.Moreover, it supports multiple users and large codebases over several repositories.

### Generate A Class Using Cli
ng generate class [options]ngg class [options]Whose name refers the name of a class.Options refer to the project name, spec value in Boolean or type of a file.

### Create A Decorator
There are two ways to register decorators in Angular.$ provide DOT decorator and module DOT decorator.

### Event Handling
There are various methods to handle events in Angular 7.1. Binding to user input events: You are able to use the Angular event binding to answer to DOM event.User input triggers so many DOM events.It is a very effective method to get the input from the user.

### For example
<button (click)="onClickMe()">Click me!</button>2. Get user input from the event object: DOM carries a cargo of the information that possibly is valuable for the components.Here is an example to show you the keyup event of an input box to obtain the user's input after every strokesrc/app/keyup.components.ts (template v.1)content_copytemplate: `<input (keyup)="onKey($event)"><p>{{values}} </p>3. Key event filtering: Every keystroke is heard by the (keyup) event handler.The enter keys matter the most as it provides the sign of the user that he has done with the typing.The most efficient method of eliminating the noise is to look after every $event.keyCode and the action is taken only when the enter key is pressed.

### Directives: The Difference Between Structural And Attribute Directives
Structural directives alter the DOM layout by removing and adding DOM elements. It is far better in changing the structure of the view.Examples of Structural directives are NG For and NG if.Attribute Directives are used as characteristics of elements.For example, a directive such as built-in NG Style in the template Syntax guide is an attribute directive.

## Angular General
### Angular Framework:
Angular is a TypeScript-based open-source front-end platform that makes it easy to build applications with in web/mobile/desktop.The major features of this framework such as declarative templates, dependency injection, end to end tooling, and many more other features are used to ease the development.

### AngularJS vs Angular:
Angular is a completely revived component-based framework in which an application is a tree of individual components.AngularJS is based on MVC architecture.This is based on Service/ControllerIt uses JavaScript to build the application.Introduced the TypeScript to write the applicationBased on controllers concept.This is a component based UI approachNot a mobile friendly framework.Developed considering mobile platformDifficulty in SEO friendly application development.Ease to create SEO friendly applications

### Angular library:
An Angular library is an Angular project that differs from an app in that it cannot run on its own.It must be imported and used in an app.For example, you can import or add service worker library to an Angular application which turns an application into a Progressive Web App (PWA).Note: You can create own third party library and publish it as npm package to be used in an Application.

### TypeScript:
TypeScript is a typed superset of JavaScript created by Microsoft that adds optional types, classes, async/await, and many other features, and compiles to plain JavaScript.Angular built entirely in TypeScript and used as a primary language.You can install it globally as: npm install -g typescript

### Angular key components:
Angular key components are: Component, Modules, Templates, Services and Metadata.Component: are the basic building blocks of angular application to control HTML views.Modules: An angular module is set of angular basic building blocks like component, directives, services etc.An application is divided into logical pieces and each piece of code is called as "module" which perform a single task.Templates: represent the views of an Angular application.Services: is used to create components which can be shared across the entire application.Metadata: can be used to add more data to an Angular class.

### Interpolation:
Interpolation is a special syntax that Angular converts into property binding.It's a convenient alternative to property binding.It is represented by double curly braces({{}}).The text between the braces is often the name of a component property.Angular replaces that name with the string value of the corresponding component property.

### Interpolated content vs innerHTML:
The main difference between interpolated and innerHTML code is the behavior of code interpreted.Interpolated content is always escaped i.e, HTML isn't interpreted and the browser displays angle brackets in the element's text content.Where as in innerHTML binding, the content is interpreted i.e, the browser will convert < and > characters as HTMLEntities.Even though innerHTML binding create a chance of XSS attack, Angular recognizes the value as unsafe and automatically sanitizes it.

### InnerHTML:
The innerHtml is a property of HTML-Elements, which allows you to set it's HTML-content programmatically.Let's display the below HTML code snippet in a <div> tag as below using innerHTML binding,<div [innerHTML]="HTMLSnippet"></div>and define the HTMLSnippet property from any componentexport class myComponent { HTMLSnippet: string = '<b>Hello World</b>, Angular'; }Unfortunately this property could cause Cross Site Scripting (XSS) security bugs when improperly handled.

### Bootstrapping module:
Every application has at least one Angular module, the root module that you bootstrap to launch the application is called as bootstrapping module.It is commonly known as AppModule.

### Manually bootstrap an application:
Use ngDoBootstrap hook for a manual bootstrapping of the application instead of using bootstrap array in @NgModule annotation.This hook is part of DoBootstap interface.

### Use polyfills in Angular application
The Angular CLI provides support for polyfills officially.When you create a new project with the ng new command, a src/polyfills.ts configuration file is created as part of your project folder.This file includes the mandatory and many of the optional polyfills as JavaScript import statements.Polyfills call into 2 categories: Mandatory and Optional.Mandatory polyfills: These are installed automatically when you create your project with ng new command and the respective import statements enabled in 'src/polyfills.ts' file.Optional polyfills: You need to install its npm package and then create import statement in 'src/polyfills.ts' file. For example, first you need to install below npm package for adding web animations (optional) polyfill. bash npm install --save web-animations-js and create import statement in polyfill file. javascript import 'web-animations-js';

## Data Binding
### Data binding:
Data binding is a core concept in Angular and allows to define communication between a component and the DOM, making it very easy to define interactive applications without worrying about pushing and pulling data. There are four forms of data binding(divided as 3 categories) which differ in the way the data is flowing.

### From the Component to the DOM
Interpolation: {{ value }}: Adds the value of a property from the componentProperty binding: [property]=value: The value is passed from the component to the specified property or simple HTML attributeFrom the DOM to the Component: Event binding: (event)=function: When a specific DOM event happens (eg.: click, change, keyup), call the specified method in the componentTwo-way binding: Two-way data binding: [(ngModel)]=value: Two-way data binding allows to have the data flow both ways.

### Data binding type categories:
Binding types can be grouped into three categories distinguished by the direction of data flow.From the source-to-view is One-way. Types used are: Interpolation, Property, Attribute, Class and Style. 1. {{expression}} 2. [target]="expression" 3. bind-target="expression":From view-to-source is One-way. This is an Event type. 1. (target)="statement" 2. on-target="statement":View-to-source-to-view is Two-way. 1. [(target)]="expression" 2. bindon-target="expression":

## LifeCycle
### What lifecycle hooks are available
Angular application goes through an entire set of processes or has a lifecycle right from its initiation to the end of the application.The representation of lifecycle in pictorial representation as follows,

### The description of each lifecycle method is:
ngOnChanges, ngOnInit, ngDoCheck, ngAfterContentInit, ngAfterContentChecked, ngAfterViewInit, ngAfterViewChecked and ngOnDestroy.ngOnChanges: is called when the value of a data bound property changes.ngOnInit: is called whenever the initialization of the directive/component after Angular first displays the data-bound properties happens.ngDoCheck: is for the detection and to act on changes that Angular can't or won't detect on its own.ngAfterContentInit: is called in response after Angular projects external content into the component's view.ngAfterContentChecked: is called in response after Angular checks the content projected into the component.ngAfterViewInit: is called in response after Angular initializes the component's views and child views.ngAfterViewChecked: is called in response after Angular checks the component's views and child views.ngOnDestroy: is the cleanup phase just before Angular destroys the directive/component.

## CLI
### The different types of commands would be,
ng generate class my-new-class: add a class to your applicationng generate component my-new-component: add a component to your applicationng generate directive my-new-directive: add a directive to your applicationng generate enum my-new-enum: add an enum to your applicationng generate module my-new-module: add a module to your applicationng generate pipe my-new-pipe: add a pipe to your applicationng generate service my-new-service: add a service to your applicationRunning the Project: ng serve

### Differential loading:
From Angular8 release onwards, the applications are built using differential loading strategy from CLI to build two separate bundles as part of your deployed application.The first build contains ES2015 syntax which takes the advantage of built-in support in modern browsers, ships less polyfills, and results in a smaller bundle size.The second build contains old ES5 syntax to support older browsers with all necessary polyfills.But this results in a larger bundle size.This strategy is used to support multiple browsers but it only load the code that the browser needs.

## Versions
### You upgrade angular version
The Angular upgrade is quite easier using Angular CLI ng update command as mentioned below.For example, if you upgrade from Angular 7 to 8 then your lazy loaded route imports will be migrated to the new import syntax automatically.$ ng update @angular/cli @angular/core

### Angular 1:
Angular 1 (AngularJS) is the first angular framework released in the year 2010.AngularJS is not built for mobile devices.It is based on controllers with MVC architecture.

### Angular 2:
Angular 2 was released in the year 2016. Angular 2 is a complete rewrite of Angular1 version.The performance issues that Angular 1 version had has been addressed in Angular 2 version.Angular 2 is built from scratch for mobile devices unlike Angular 1 version.Angular 2 is components based.

### Angular 3:


### The following are the different package versions in Angular 2
@angular/core v2.3.0@angular/compiler v2.3.0@angular/http v2.3.0@angular/router v3.3.0The router package is already versioned 3 so to avoid confusion switched to Angular 4 version and skipped 3 version.

### Angular 4:
The compiler generated code file size in AOT mode is very much reduced.With Angular 4 the production bundles size is reduced by hundreds of KB's.Animation features are removed from angular/core and formed as a separate package.Supports Typescript 2.1 and 2.2.Angular UniversalNew HttpClient

### Angular 5:
Angular 5 makes angular faster.It improved the loading time and execution time.Shipped with new build optimizer.Supports Typescript 2.5.Service Worker

### Angular 6:
It is released in May 2018.Includes Angular Command Line Interface (CLI), Component Development KIT (CDK), Angular Material Package, Angular Elements.Service Worker bug fixes.i18nExperimental mode for Ivy.RxJS 6.0Tree Shaking

### Angular 7:
It is released in October 2018.TypeScript 3.1RxJS 6.3New Angular CLICLI Prompts capability provide an ability to ask questions to the user before they run.It is like interactive dialog between the user and the CLIWith the improved CLI Prompts capability, it helps developers to make the decision.New ng commands ask users for routing and CSS styles types(SCSS) and ng add @angular/material asks for themes and gestures or animations.

### Angular 8:
It is released in May 2019.TypeScript 3.4

### Angular 9:
It is released in February 2020.TypeScript 3.7Ivy enabled by default

### Angular 10:
It is released in June 2020.TypeScript 3.9TSlib 2.0

## Compilation
### Compilation Overview
Angular compiler:The Angular compiler is used to convert the application code into JavaScript code.It reads the template markup, combines it with the corresponding component class code, and emits component factories which creates JavaScript representation of the component along with elements of @Component metadata.

### Build configuration for multiple locales
You can provide build configuration such as translation file path, name, format and application url in configuration settings of Angular.json file.

### Angular CLI Builder
In Angular8, the CLI Builder API is stable and available to developers who want to customize the Angular CLI by adding or modifying commands.For example, you could supply a builder to perform an entirely new task, or to change which third-party tool is used by an existing command.A builder function ia a function that uses the Architect API to perform a complex process such as "build" or "test".The builder code is defined in an npm package.For example, BrowserBuilder runs a webpack build for a browser target and KarmaBuilder starts the Karma server and runs a webpack build for unit tests.

### Invoke a builder
The Angular CLI command ng run is used to invoke a builder with a specific target configuration.The workspace configuration file, angular.json, contains default configurations for built-in builders.

### Create an app shell in Angular
An App shell is a way to render a portion of your application via a route at build time.This is useful to first paint of your application that appears quickly because the browser can render static HTML and CSS without the need to initialize JavaScript.You can achieve this using Angular CLI which generates an app shell for running server-side of your app.ng generate appShell [options] or ng g appShell [options]

### JIT
Just-in-Time (JIT) is a type of compilation that compiles your app in the browser at runtime.JIT compilation is the default when you run the ng build (build only) or ng serve (build and serve locally) CLI commands.Commands used for JIT compilation are: ng build and ng serve.

### AOT
Ahead-of-Time (AOT) is a type of compilation that compiles your app at build time.For AOT compilation, include the --aot option with the ng build or ng serve command as: ng build --aot and ng serve --aot.Note: The ng build command with the --prod meta-flag (ng build --prod) compiles with AOT by default.

### AOT compiler
The AOT compiler is part of a build process that produces a small, fast, ready-to-run application package, typically for production.It converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.

### AOT Advantages
Faster rendering, Fewer asynchronous requests, Smaller Angular framework download size, Detect template errors earlier, and Better security.Faster rendering: The browser downloads a pre-compiled version of the application. So it can render the application immediately without compiling the app.Fewer asynchronous requests: It inlines external HTML templates and CSS style sheets within the application javascript which eliminates separate ajax requests.Smaller Angular framework download size: Doesn't require downloading the Angular compiler. Hence it dramatically reduces the application payload.Detect template errors earlier: Detects and reports template binding errors during the build step itselfBetter security: It compiles HTML templates and components into JavaScript. So there won't be any injection attacks.

### AOT compilation control
You can control your app compilation in two ways,By providing template compiler options in the tsconfig.json fileBy configuring Angular metadata with decorators

### AOT Phases
The AOT compiler works in three phases,Code Analysis: The compiler records a representation of the sourceCode generation: It handles the interpretation as well as places restrictions on what it interprets.Validation: In this phase, the Angular template compiler uses the TypeScript compiler to validate the binding expressions in templates.

### Can I use arrow functions in AOT
No, Arrow functions or lambda functions can't be used to assign values to the decorator properties.If you still use arrow function, it generates an error node in place of the function.When the compiler later interprets this node, it reports an error to turn the arrow function into an exported function.Note: From Angular5 onwards, the compiler automatically performs this rewriting while emitting the .js file.

### Can I use any javascript feature for expression syntax in AOT
No, the AOT collector understands a subset of (or limited) JavaScript features.If an expression uses unsupported syntax, the collector writes an error node to the .metadata.json file.Later point of time, the compiler reports an error if it needs that piece of metadata to generate the application code.

### Angular Ivy
Angular Ivy is a new rendering engine for Angular.You can choose to opt in a preview version of Ivy from Angular version 8.You can enable ivy in a new project by using the --enable-ivy flag with the ng new commandng new ivy-demo-app --enable-ivy

### Ivy preview features
You can expect below features with Ivy preview,Generated code that is easier to read and debug at runtimeFaster re-build timeImproved payload sizeImproved template type checking

### AOT compilation with Ivy
It is a recommended configuration.AOT compilation with Ivy is faster.Set the default build options(with in angular.json) for your project to always use AOT compilation.

## Dependency and Injection
### Dependency and Injection Overview
For example, If you don't register a logger provider anywhere, the injector sets the value of logger(or logger service) to null in the below class.import { Optional } from '@angular/core';

### Constructor(@Optional() private logger?: Logger) {
if (this.logger) {    this.logger.log('This is an optional dependency message');  } else {    console.log('The logger is not registered');  }}

### Dependency injection
Dependency injection (DI), is an important application design pattern in which a class asks for dependencies from external sources rather than creating them itself.Angular comes with its own dependency injection framework for resolving dependencies( services or objects that a class needs to perform its function).So you can have your services depend on other services throughout your application.

### AngularJS vs Angular with respect to dependency injection
Dependency injection is a common component in both AngularJS and Angular, but there are some key differences between the two frameworks in how it actually works.AngularJS AngularDependency injection tokens are always strings	Tokens can have different types.They are often classes and sometimes can be strings.There is exactly one injector even though it is a multi-module applications.There is a tree hierarchy of injectors, with a root injector and an additional injector for each component.

### Configure injectors with providers at different levels
You can configure injectors with providers at different levels of your application by setting a metadata value.The configuration can happen in one of three places,In the @Injectable() decorator for the service itselfIn the @NgModule() decorator for an NgModuleIn the @Component() decorator for a component

### It is not mandatory to use injectable on every service class
The @Injectable() decorator is not strictly required if the class has other Angular decorators on it or does not have any dependencies.But the important thing here is any class that is going to be injected with Angular is decorated.i.e, If we add the decorator, the metadata design:paramtypes is added, and the dependency injection can do it's job.That is the exact reason to add the @Injectable() decorator on a service if this service has some dependencies itself.For example, Let's see the different variations of AppService in a root component,The below AppService can be injected in AppComponent without any problems.This is because there are no dependency services inside AppService.export class AppService {  constructor() { } }The below AppService with dummy decorator and httpService can be injected in AppComponent without any problems.This is because meta information is generated with dummy decorator.function SomeDummyDecorator() {  return (constructor: Function) => console.log(constructor);}@SomeDummyDecorator()export class AppService {  constructor(http: HttpService) {    console.log(http);  }}

### Injector hierarchy types
There are two types of injector hierarchies in AngularModuleInjector hierarchy: It configure on a module level using an @NgModule() or @Injectable() annotation.ElementInjector hierarchy: It created implicitly at each DOM element.Also it is empty by default unless you configure it in the providers property on @Directive() or @Component().

## Validators
### Validators Overview
The main use cases are complex validations like hitting a server to check the availability of a username or email.

### Built-in validators example
In reactive forms, you can use built-in validator like required and minlength on your input form controls.Whereas in template-driven forms, both required and minlength validators available as attributes.

### Optimize the performance of async validators
Since all validators run after every form value change, it creates a major impact on performance with async validators by hitting the external API on each keystroke.This situation can be avoided by delaying the form validity by changing the updateOn property from change (default) to submit or blur.The usage would be different based on form types,Template-driven forms: Set the property on ngModelOptions directive<input [(ngModel)]="name" [ngModelOptions]="{updateOn: 'blur'}">Reactive-forms: Set the property on FormControl instancename = new FormControl('', {updateOn: 'blur'});

## Key Components
### Key Components Overview
Use inline template with template syntax or use separate template file such as app.component.HTML.

### Modules
Modules are logical boundaries in your application and the application is divided into separate modules to separate the functionality of your application.The NgModule decorator has five important options: imports, declarations, bootstrap, providers and entryComponents.The imports option is used to import other dependent modules. The BrowserModule is required by default for any web based angular applicationThe declarations option is used to define components in the respective moduleThe bootstrap option tells Angular which Component to bootstrap in the applicationThe providers option is used to configure set of injectable objects that are available in the injector of this module.The entryComponents option is a set of components dynamically loaded into the view.

### Metadata
Metadata is used to decorate a class so that it can configure the expected behavior of the class.The metadata is represented by decoratorsClass decorators, like @Component and @NgModule: import { NgModule, Component } from '@angular/core';Property decorators Used for properties inside classes, like @Input and @Output: import { Component, Input } from '@angular/core';Method decorators Used for methods inside classes like @HostListener: import { Component, HostListener } from '@angular/core';Parameter decorators Used for parameters inside class constructors, e.g. @Inject, Optionalimport { Component, Inject } from '@angular/core';import { MyService } from './my-service';

### Components vs Directives
In a short note, A component(@component) is a directive-with-a-template.To register a component: use @Component meta-data annotation.To register directives: use @Directive meta-data annotationComponents are typically used to create UI widgets.Directive is used to add behavior to an existing DOM elementComponent is used to break up the application into smaller components.Directive is use to design re-usable componentsOnly one component can be present per DOM element.Many directives can be used per DOM element@View decorator or templateurl/template are mandatory.Directive doesn't use View

### Angular find components, directives and pipes
The Angular compiler finds a component or directive in a template when it can match the selector of that component or directive in that template.Whereas it finds a pipe if the pipe's name appears within the pipe syntax of the template HTML.

## Elements
### Elements Overview
Edge: Currently it is in progress

### Custom elements
Custom elements (or Web Components) are a Web Platform feature which extends HTML by allowing you to define a tag whose content is created and controlled by JavaScript code.The browser maintains a CustomElementRegistry of defined custom elements, which maps an instantiable JavaScript class to an HTML tag.Currently this feature is supported by Chrome, Firefox, Opera, and Safari, and available in other browsers through polyfills.

### Do I need to bootstrap custom elements
No, custom elements bootstrap (or start) automatically when they are added to the DOM, and are automatically destroyed when removed from the DOM.Once a custom element is added to the DOM for any page, it looks and behaves like any other HTML element, and does not require any special knowledge of Angular.

### Custom elements internal workings
Below are the steps in an order about custom elements functionality,App registers custom element with browser: Use the createCustomElement() function to convert a component into a class that can be registered with the browser as a custom element.App adds custom element to DOM: Add custom element just like a built-in HTML element directly into the DOM.Browser instantiate component based class: Browser creates an instance of the registered class and adds it to the DOM.Instance provides content with data binding and change detection: The content with in template is rendered using the component and DOM data.

### Transfer components to custom elements
Transforming components to custom elements involves two major steps,Build custom element class: Angular provides the createCustomElement() function for converting an Angular component (along with its dependencies) to a custom element.The conversion process implements NgElementConstructor interface, and creates a constructor class which is used to produce a self-bootstrapping instance of Angular component.Register element class with browser: Uses customElements.define() JS function, to register the configured constructor and its associated custom-element tag with the browser's CustomElementRegistry.When the browser encounters the tag for the registered element, it uses the constructor to create a custom-element instance.The detailed structure would be as follows, CreateElement

### Mapping rules between Angular component and custom element
The Component properties and logic maps directly into HTML attributes and the browser's event system.Let us describe them in two steps,The createCustomElement() API parses the component input properties with corresponding attributes for the custom element.For example, component @Input('myInputProp') converted as custom element attribute my-input-prop.The Component outputs are dispatched as HTML Custom Events, with the name of the custom event matching the output name.For example, component @Output() valueChanged = new EventEmitter() converted as custom element with dispatch event as "valueChanged".

### Define typings for custom elements
You can use the NgElement and WithProperties types exported from @angular/elements.

## Components
### Dynamic components:
Are the components in which components location in the application is not defined at build time.I.E.: they are not used in any angular template.But:  the component is instantiated and placed in the application at runtime.

### Create displayBlock components:
By default, Angular CLI creates components in an inline displayed mode(i.e, display:inline).But it is possible to create components with display: block style using displayBlock option,ng generate component my-component --displayBlock(OR) the option can be turned on by default in Angular.json with schematics.@schematics/angular:component.displayBlock key value as true.

### Component Test Harnesses:
A component harness is a testing API around an Angular directive or component to make tests simpler by hiding implementation details from test suites.This can be shared between unit tests, integration tests, and end-to-end tests.The idea for component harnesses comes from the PageObject pattern commonly used for integration testing.

### Bootstrapped component:
A bootstrapped component is an entry component that Angular loads into the DOM during the bootstrap process or application launch time.Generally, this bootstrapped or root component is named as AppComponent in your root module using bootstrap property as below.@NgModule({ bootstrap: [AppComponent] // bootstrapped entry component need to be declared here })

### It necessary for bootstrapped component to be entry component
Yes, the bootstrapped component needs to be an entry component.This is because the bootstrapping process is an imperative process.

### Entry component:
An entry component is any component that Angular loads imperatively(i.e, not referencing it in the template) by type.Due to this behavior, they can't be found by the Angular compiler during compilation.These components created dynamically with ComponentFactoryResolver.Basically, there are two main kinds of entry components which are following -The bootstrapped root componentA component you specify in a route

### Routed entry component:
The components referenced in router configuration are called as routed entry components.

### This routed entry component defined in a route definition as
const routes: Routes = [ { path: '', component: TodoListComponent // router entry component } ];Since router definition requires you to add the component in two places (router and entryComponents), these components are always entry components.The compilers are smart enough to recognize a router definition and automatically add the router component into entryComponents.

### Not necessary to use entryComponents array every time
A: Most of the time, you don't need to explicity to set entry components in entryComponents array of ngModule decorator.   Because angular adds components from both @NgModule.bootstrap and route definitions to entry components automatically.

### Do I still need to use entryComponents array in Angular9/hat are angular elements
A: No. In previous angular releases, the entryComponents array of ngModule decorator is used to tell the compiler   which components would be created and inserted dynamically in the view.   In Angular9, this is not required anymore with Ivy.

## Templates
### Select an element with in a component template
A: You can use @ViewChild directive to access elements in the view directly.EX: Let's take input element with a reference,    <input #uname>    and define view child directive and access it in ngAfterViewInit lifecycle hook    @ViewChild('uname') input;    ngAfterViewInit() {      console.log(this.input.nativeElement.value);    }

### Select an element in component template:
You can control any DOM element via ElementRef by injecting it into your component's constructor.The component should have constructor with ElementRef parameter,constructor(myElement: ElementRef) { el.nativeElement.style.backgroundColor = 'yellow'; }

### The option to choose between inline and external template file:
You can store your component's template in one of two places.You can define it inline using the template property, or you can define the template in a separate HTML file and link to it in the component metadata using the @Component decorator's templateUrl property.The choice between inline and separate HTML is a matter of taste, circumstances, and organization policy.But normally we use inline template for small portion of code and external template file for bigger views.By default, the Angular CLI generates components with a template file.But you can override that with the below command,ng generate component hero -it

### What happens if you use script tag inside template
A: Angular recognizes the value as unsafe and automatically sanitizes it, which removes the script tag but keeps safe content such as the text content of the script tag.   This way it eliminates the risk of script injection attacks.   If you still use it then it will be ignored and a warning appears in the browser console.   Let's take an example of innerHtml property binding which causes XSS vulnerability,   export class InnerHtmlBindingComponent {     // For example, a user/attacker-controlled value from a URL.     HTMLSnippet = 'Template <script>alert("0wned")</script> <b>Syntax</b>'; }

### Template expressions:
A template expression produces a value similar to any Javascript expression.Angular executes the expression and assigns it to a property of a binding target; the target might be an HTML element, a component, or a directive.In the property binding, a template expression appears in quotes to the right of the = symbol as in [property]="expression".In interpolation syntax, the template expression is surrounded by double curly braces.For example, in the below interpolation, the template expression is {{username}},<h3>{{username}}, welcome to Angular</h3>The below javascript expressions are prohibited in template expressionassignments (=, +=, -=, ...)newchaining expressions with ; or ,increment and decrement operators (++ and --)

### Template statements:
A template statement responds to an event raised by a binding target such as an element, component, or directive.The template statements appear in quotes to the right of the = symbol like (event)="statement".Let's take an example of button click event's statement<button (click)="editProfile()">Edit Profile</button>In the above expression, editProfile is a template statement.The below JavaScript syntax expressions are not allowed.newincrement and decrement operators, ++ and --operator assignment, such as += and -=the bitwise operators | and &the template expression operators

### Specify angular template compiler options:
The angular template compiler options are specified as members of the angularCompilerOptions object in the tsconfig.json file.These options will be specified adjecent to typescript compiler options.

### Template translation phases:


### The i18n template translation process has four phases
1. Mark static text messages in your component templates for translation: You can place i18n on every element tag whose fixed text is to be translated.For example, you need i18n attribue for heading as: <h1 i18n>Hello i18n!</h1>2. Create a translation file: Use the Angular CLI xi18n command to extract the marked text into an industry-standard translation source file.Open terminal window at the root of the app project and run the CLI command xi18n. ng xi18nThis command creates a file named messages.xlf in your project's root directory.You can supply command options to change the format, the name, the location, and the source locale of the extracted file.3.

### The i18n template translation process has four phases (continued)
Edit the generated translation file: Translate the extracted text into the target language.In this step, create a localization folder (such as locale)under root directory(src) and then create target language translation file by copying and renaming the default messages.xlf file.You need to copy source text node and provide the translation under target tag.4. Merge the completed translation file into the app: You need to use Angular CLI build command to compile the app, choosing a locale-specific configuration, or specifying the following command options.--i18nFile=path to the translation file--i18nFormat=format of the translation file--i18nLocale= locale id

### The list of 3 template expression operators:
The Angular template expression language supports three special template expression operators.- Pipe operator- Safe navigation operator- Non-null assertion operator

## Forms
### Reactive forms: is a model-driven approach for creating forms in a reactive style(form inputs changes over time).
These are built around observable streams, where form inputs and values are provided as streams of input values.Follow the below steps to create reactive forms and register the reactive forms module which declares reactive-form directives in your app.

### Template driven forms: Model-driven forms where you write the logic, validations, controls etc, in the template part of the code using directives.
They are suitable for simple scenarios and uses two-way binding with [(ngModel)] syntax.

### For example, you can create register form easily by following these steps
1. Import the FormsModule into the Application module's imports array2. Bind the form from template to the component using ngModel syntax3. Attach NgForm directive to the tag in order to create FormControl instances and register them4. Let's submit the form with ngSubmit directive and add type="submit" button at the bottom of the form to trigger form submit.5. Finally, the completed template-driven registration form will be appeared as follow.

### Reactive forms vs template driven forms:
The differences are in: Form model setup, Data updates, Form custom validation, Testing, Mutability and Scalability.

### Here are the features with Reactive vs Template-Driven
Form model setup: Created(FormControl instance) in component explicitly vs Created by directivesData updates: Synchronous vs AsynchronousForm custom validation: Defined as Functions vs Defined as DirectivesTesting: No interaction with change detection cycle vs Need knowledge of the change detection processMutability: Immutable(by always returning new value for FormControl instance) vs Mutable(Property always modified to new value)Scalability: More scalable using low-level APIs vs Less scalable using due to abstraction on APIs

### The different ways to group form controls:
Reactive forms provide two ways of grouping multiple related controls, FormGroup and FormArray.FormGroup: defines a form with a fixed set of controls those can be managed together in an one object.It has same properties and methods similar to a FormControl instance.This FormGroup can be nested to create complex forms.FormArray: defines a dynamic form in an array format, where you can add and remove controls at run time.This is useful for dynamic forms when you don't know how many controls will be present within the group.

### Update specific properties of a form model:
Use patchValue() method to update specific properties defined in the form model.Use setValue method to update properties.Remember to update the properties against the exact model structure.

### FormBuilder: is used as syntactic sugar for easily creating instances of a FormControl, FormGroup, or FormArray.
This is helpful to reduce the amount of boilerplate needed to build complex reactive forms.It is available as an injectable helper class of the @angular/forms package.

### You verify the model changes in forms
A: You can add a getter property(let's say, diagnostic) inside component to return a JSON representation of the model during the development.This is useful to verify whether the values are really flowing from the input box to the model and vice versa or not.And add diagnostic binding near the top of the form.{{diagnostic}} <div class="form-group">

### The state CSS classes provided by ngModel
A: The ngModel directive updates the form control with special Angular CSS classes to reflect it's state.Form control state: If true or If falseVisited: ng-touched or ng-untouchedValue has changed: ng-dirty or ng-pristineValue is valid: ng-valid or ng-invalid

### Reset the form
In a model-driven form, you can reset the form just by calling the function reset() on our form model.The form model resets the form back to its original pristine state.

## Directives
### Directive types:
Components, Structural directives and Attribute direectives.Components: These are directives with a template.Structural directives: These directives change the DOM layout by adding and removing DOM elements.Attribute directives: These directives change the appearance or behavior of an element, component, or another directive.

### You create directives using CLI
A: You can use CLI command ng generate directive to create the directive class file.It creates the source file(src/app/components/directivename.directive.ts), the respective test file(.spec.ts) and declare the directive class file in root module.

## Metadata
### Metadata Restrictions:
In Angular, You must write metadata with the following general constraints,Write expression syntax with in the supported range of javascript featuresThe compiler can only reference symbols which are exportedOnly call the functions supported by the compilerDecorated and data-bound class members must be public.

### Metadata json files:
The metadata.json file can be treated as a diagram of the overall structure of a decorator's metadata, represented as an abstract syntax tree(AST).During the analysis phase, the AOT collector scan the metadata recorded in the Angular decorators and outputs metadata information in .metadata.json files, one per .d.ts file.

### Metadata error examples:
Below are some of the errors encountered in metadata,Expression form not supported: Some of the language features outside of the compiler's restricted expression syntax used in angular metadata can produce this error.

### Some examples are
1. export class User   const prop = typeof User; // typeof is not valid in metadata2. { provide: 'token', useValue: { [prop]: 'value' } }; // bracket notation is not valid in metadataReference to a local (non-exported) symbol: The compiler encountered a referenced to a locally defined symbol that either wasn't exported or wasn't initialized.Function calls are not supported: The compiler does not currently support function expressions or lambda functions.You cannot set a provider's useFactory to an anonymous function or arrow function.Fix this with exported function.Destructured variable or constant not supported: The compiler does not support references to variables assigned by destructuring.

### Metadata rewriting:
Metadata rewriting is the process in which the compiler converts the expression initializing the fields such as useClass, useValue, useFactory, and data into an exported variable, which replaces the expression.Remember that the compiler does this rewriting during the emit of the .js file but not in definition files( .d.ts file).

## Decorators
### Class decorators:
A class decorator is a decorator that appears immediately before a class definition, which declares the class to be of the given type, and provides metadata suitable to the typeThese decorators are class decorators: @Component(), @Directive(), @Pipe(), @Injectable() and @NgModule().

### Class field decorators:
The class field decorators are the statements declared immediately before a field in a class definition that defines the type of that field.Some of the examples are: @input and @output,

## Animation
### Angular animation:
Angular's animation system is built on CSS functionality in order to animate any property that the browser considers animatable.These properties includes positions, sizes, transforms, colors, borders etc.The Angular modules for animations are @angular/animations and @angular/platform-browser and these dependencies are automatically added to your project when you create a project using Angular CLI.

### Animate function:
Angular Animations are a powerful way to implement sophisticated and compelling animations for your Angular single page web application.

### Trigger an animation:
Angular provides a trigger() function for animation in order to collect the states and transitions with a specific animation name,so that you can attach it to the triggering element in the HTML template.This function watch for

### Find the angular CLI version
Angular CLI provides it's installed version using below different ways using ng command,ng v gives: Angular CLI: 1.6.3ng version gives: Node: 8.11.3ng -v gives: OS: darwin x64

### Ng --version gives: Angular
changes and trigger initiates the actions when a change occurs.

## NG
### The role of ngModule metadata in compilation process:
The @NgModule metadata is used to tell the Angular compiler what components to be compiled for this module and how to link this module with other modules.

### NgModules examples:
The Angular core libraries and third-party libraries are available as NgModules.

### Constructor vs ngOnInit:
TypeScript classes has a default method called constructor which is normally used for the initialization purpose.Whereas ngOnInit method is specific to Angular, especially used to define Angular bindings.Even though constructor getting called first, it is preferred to move all of your Angular bindings to ngOnInit method.In order to use ngOnInit, you need to implement OnInit interface.

### NgFor directive:
We use Angular ngFor directive in the template to display each item in the list.For example, here we iterate over list of users, <li *ngFor="let user of users"> {{ user }} </li>The user variable in the ngFor double-quoted instruction is a template input variable

### NgIf directive:
Sometimes an app needs to display a view or a portion of a view only under specific circumstances.The Angular ngIf directive inserts or removes an element based on a truthy/falsy condition.

### Here is an example to display a message if the user age is more than 18
<p *ngIf="user.age > 18">You are not eligible for student pass!</p>Note: Angular isn't showing and hiding the message.It is adding and removing the paragraph element from the DOM.That improves performance, especially in the larger projects with many data bindings.

### NgUpgrade:
NgUpgrade is a library put together by the Angular team, which you can use in your applications to mix and match AngularJS and Angular components and bridge the AngularJS and Angular dependency injection systems.

### NgIf vs hidden property:
The main difference is that *ngIf will remove the element from the DOM, while [hidden] actually plays with the CSS style by setting display:none. Generally it is expensive to add and remove stuff from the DOM for frequent actions.

### NgFor directive index property:
The index property of the NgFor directive is used to return the zero-based index of the item in each iteration.You can capture the index in a template input variable and use it in the template.For example, you can capture the index in a variable named indexVar and displays it with the todo's name using ngFor directive as below.<div *ngFor="let todo of todos; let i=index">{{i + 1}} - {{todo.name}}</div>

### NgFor trackBy:
The main purpose of using *ngFor with trackBy option is performance optimization.Normally if you use NgFor with large data sets, a small change to one item by removing or adding an item, can trigger a cascade of DOM manipulations.In this case, Angular sees only a fresh list of new object references and to replace the old DOM elements with all new DOM elements.You can help Angular to track which items added or removed by providing a trackBy function which takes the index and the current item as arguments and needs to return the unique identifier for this item.

### NgSwitch directive:
NgSwitch directive is similar to JavaScript switch statement which displays one element from among several possible elements, based on a switch condition.In this case only the selected element placed into the DOM.It has been used along with NgSwitch, NgSwitchCase and NgSwitchDefault directives.Example, display the browser details based on selected browser using ngSwitch directive.<div [ngSwitch]="currentBrowser.name"> <chrome-browser *ngSwitchCase="'chrome'" [item]="currentBrowser"></chrome-browser>, etc.

### Set ngFor and ngIf on the same element:
Sometimes you may need to both ngFor and ngIf on the same element but unfortunately you are going to encounter below template error.Template parse errors: Can't have multiple template bindings on one element.In this case, You need to use either ng-container or ng-template.

## RxJS Observables
### RxJS:
RxJS is a library for composing asynchronous and callback-based code in a functional, reactive style using Observables.Many APIs such as HttpClient produce and consume RxJS Observables and also uses operators for processing observables.

### For example, you can import observables and operators for using HttpClient as
import { Observable, throwError } from 'rxjs';import { catchError, retry } from 'rxjs/operators';

### RxJS subject:
An RxJS Subject is a special type of Observable that allows values to be multicasted to many Observers.While plain Observables are unicast (each subscribed Observer owns an independent execution of the Observable), Subjects are multicast.A Subject is like an Observable, but can multicast to many Observers.Subjects are like EventEmitters: they maintain a registry of many listeners.

### RxJS Utility Functions:
The RxJS library also provides below utility functions for creating and working with observables.Converting existing code for async operations into observablesIterating through the values in a streamMapping values to different typesFiltering streamsComposing multiple streams

### Multicasting:
Multi-casting is the practice of broadcasting to a list of multiple subscribers in a single execution.

### Subscribing:
An Observable instance begins publishing values only when someone subscribes to it.So you need to subscribe by calling the subscribe() method of the instance, passing an observer object to receive the notifications.

### Subscribe method short hand notation:
The subscribe() method can accept callback function definitions in line, for next, error, and complete handlers is known as short hand notation or Subscribe method with positional arguments.

### Observable:
An Observable is a unique Object similar to a Promise that can help manage async code.Observables are not part of the JavaScript language so we need to rely on a popular Observable library called RxJS.The observables are created using new keyword.

### Observer:
Observer is an interface for a consumer of push-based notifications delivered by an Observable.A handler that implements the Observer interface for receiving observable notifications will be passed as a parameter for observable as:myObservable.subscribe(myObserver);Note: If you don't supply a handler for a notification type, the observer ignores notifications of that type.

### Observables:
Observables are declarative which provide support for passing messages between publishers and subscribers in your application.They are mainly used for event handling, asynchronous programming, and handling multiple values.In this case, you define a function for publishing values, but it is not executed until a consumer subscribes to it.The subscribed consumer then receives notifications until the function completes, or until they unsubscribe.

### Observable creation functions:
RxJS provides creation functions for the process of creating observables from things such as promises, events, timers and Ajax requests.Create an observable from a promise.Create an observable that creates an AJAX request.Create an observable from a counter.Create an observable from an event.

### Promise vs observable:


### I need to clean this up
Declarative: Computation does not start until subscription so that they can be run whenever you need the result.Execute immediately on creation.Provide multiple values over time: Provide only oneSubscribe method is used for error handling which makes centralized and predictable error handling.Push errors to the child promisesProvides chaining and subscription to handle complex applications.Uses only .then() clause.

### Observable Error handling:
You can handle errors by specifying an error callback on the observer instead of relying on try/catch which are ineffective in asynchronous environment.

### What will happen if you do not supply handler for observer
A: Normally an observer object can define any combination of next, error and complete notification type handlers.If you don't supply a handler for a notification type, the observer just ignores notifications of that type.

## Routes and Router
### Routes and Router Overview
The RouterOutlet is a directive from the router library and it acts as a placeholder that marks the spot in the template where the router should display the components for that outlet.Router outlet is used like a component,<router-outlet></router-outlet><!-- Routed components go here -->

### Router links
The RouterLink is a directive on the anchor tags give the router control over those elements.Since the navigation paths are fixed, you can assign string values to router-link directive as below,<h1>Angular Router</h1><nav>  <a routerLink="/todosList" >List of todos</a>  <a routerLink="/completed" >Completed todos</a></nav><router-outlet></router-outlet>

### Active router links
RouterLinkActive is a directive that toggles css classes for active RouterLink bindings based on the current RouterState.The Router will add CSS classes when this link is active and and remove when the link is inactive.

### Router state
RouterState is a tree of activated routes.Every node in this tree knows about the "consumed" URL segments, the extracted parameters, and the resolved data.You can access the current RouterState from anywhere in the application using the Router service and the routerState property.

### Router events
During each navigation, the Router emits navigation events through the Router.events property allowing you to track the lifecycle of the route.

### The sequence of router events is
NavigationStart, RouteConfigLoadStart, RouteConfigLoadEnd, RoutesRecognized, GuardsCheckStart, ChildActivationStart, ActivationStart,GuardsCheckEnd, ResolveStart, ResolveEnd, ActivationEnd ChildActivationEnd NavigationEnd, NavigationCancel, NavigationError

### Activated route
ActivatedRoute contains the information about a route associated with a component loaded in an outlet.It can also be used to traverse the router state tree.The ActivatedRoute will be injected as a router service to access the information.

### Define routes
A router must be configured with a list of route definitions.You configures the router with routes via the RouterModule.forRoot() method, and adds the result to the AppModule's imports array.

### Wildcard route
If the URL doesn't match any predefined routes then it causes the router to throw an error and crash the app.In this case, you can use wildcard route.A wildcard route has a path consisting of two asterisks to match every URL.

### Do I need a Routing Module always
No, the Routing Module is a design choice.You can skip routing Module (for example, AppRoutingModule) when the configuration is simple and merge the routing configuration directly into the companion module (for example, AppModule).But it is recommended when the configuration is complex and includes specialized guard and resolver services.

### Detect route change
In Angular7, you can subscribe to router to detect the changes.The subscription for router events would be as below,this.router.events.subscribe((event: Event) => {})

### Use if-statements to check for states
this.router.events.subscribe((event: Event)if (event instanceof NavigationStart), if (event instanceof NavigationEnd) and if (event instanceof NavigationError).

### ForRoot method helpful to avoid duplicate router instances
If the RouterModule module didn't have forRoot() static method then each feature module would instantiate a new Router instance,which leads to broken application due to duplicate instances.After using forRoot() method,the root application module imports RouterModule.forRoot() and gets a Router,and all feature modules import RouterModule.forChild() which does not instantiate another Router.

### You get the current route
In Angular, there is an url property of router package to get the current route.

### You need to follow these steps
Import Router from @angular/router: import {Router} from @angular/routerInject router inside constructor: constructor private router: RouterAccess url parameter: this.router.url

## Modules
### Feature modules
Feature modules are NgModules, which are used for the purpose of organizing code.The feature module can be created with Angular CLI using the below command in the root directory,ng generate module MyCustomFeatureAngular CLI creates a folder called my-custom-feature with a file inside called my-custom-feature.module.ts with the following contentsimport { NgModule } from '@angular/core';import { CommonModule } from '@angular/common';@NgModule({ imports: [ CommonModule ], declarations: [] })export class MyCustomFeature { }The Module suffix shouldn't present in the name because the CLI appends it.

### The imported modules in CLI generated feature modules
In the CLI generated feature module, there are two JavaScript import statements at the top of the fileNgModule: InOrder to use the @NgModule decoratorCommonModule: It provides many common directives such as ngIf and ngFor.

### The differences between ngmodule and javascript module


### NgModule vs JavaScript module
NgModule bounds declarable classes only vs There is no restriction classesList the module's classes in declarations array only vs Can define all member classes in one giant fileIt only export the declarable classes it owns or imports from other modules vs It can export any classesExtend the entire application with services by adding providers to provides array vs Can't extend the application with services

### The possible errors with declarations
There are two common possible errors with declarations array,If you use a component without declaring it, Angular returns an error message.If you try to declare the same class in more than one module then compiler emits an error.

### The steps to use declaration elements
Below are the steps to be followed to use declaration elements.Create the element(component, directive and pipes) and export it from the file where you wrote itImport it into the appropriate module.Declare it in the @NgModule declarations array.

### What happens if browserModule used in feature module
If you do import BrowserModule into a lazy loaded feature module, Angular returns an error telling you to use CommonModule instead. Because BrowserModule's providers are for the entire app so it should only be in the root module, not in feature module. Whereas Feature modules only need the common directives in CommonModule.

### Feature module types
There are 5 categories of feature modules: Domain, Routed, Routing, Service and Widget.Domain: Deliver a user experience dedicated to a particular application domain(For example, place an order, registration etc)Routed: These are domain feature modules whose top components are the targets of router navigation routes.Routing: It provides routing configuration for another module.Service: It provides utility services such as data access and messaging(For example, HttpClientModule)Widget: It makes components, directives, and pipes available to external modules(For example, third-party libraries such as Material UI)

### Provider
A provider is an instruction to the Dependency Injection system on how to obtain a value for a dependency(aka services created).The service can be provided using Angular CLI as below,ng generate service my-service

### The created service by CLI would be as
import { Injectable } from '@angular/core';@Injectable({ providedIn: 'root', //Angular provide the service in root injector })export class MyService { }

### The recommendation for provider scope
You should always provide your service in the root injector unless there is a case where you want the service to be available only if you import a particular @NgModule.

### You restrict provider scope to a module
It is possible to restrict service provider scope to a specific module instead making available to entire application.There are two ways to do it: Using providedIn in service and Declare provider for the service in module.

### Using providedIn in service
import { Injectable } from '@angular/core';import { SomeModule } from './some.module';@Injectable({ providedIn: SomeModule, })export class SomeService { }

### Declare provider for the service in module
import { NgModule } from '@angular/core';import { SomeService } from './some.service';@NgModule({ providers: [SomeService], })export class SomeModule { }

### A shared module
The Shared Module is the module in which you put commonly used directives, pipes, and components into one module that is shared(import it) throughout the application.

### Common module
The commonly-needed services, pipes, and directives provided by @angular/common module.Apart from these HttpClientModule is available under @angular/common/http.

### What happens if I import the same module twice
If multiple modules imports the same module then angular evaluates it only once (When it encounters the module first time).It follows this condition even the module appears at any level in a hierarchy of imported NgModules.

## Services
### You upgrade location service of angularjs
If you are using $location service in your old AngularJS application, now you can use LocationUpgradeModule(unified location service) which puts the responsibilities of $location service to Location service in Angular.

### A service worker and its role in Angular
A service worker is a script that runs in the web browser and manages caching for an application.Starting from 0 version 5, Angular ships with a service worker implementation.Angular service worker is designed to optimize the end user experience of using an application over a slow or unreliable network connection, while also minimizing the risks of serving outdated content.

### The design goals of service workers


### The design goals of Angular's service workers are
It caches an application just like installing a native applicationA running application continues to run with the same version of all fileswithout any incompatible files.When you refresh the application, it loads the latest fully cached version.When changes are published then it immediately updates in the background.Service workers saves the bandwidth by downloading the resources only when they changed.

### Add web workers in your application
You can add web worker anywhere in your application.For example, If the file that contains your expensive computation is src/app/app.component.ts, you can add a Web Worker using ng generate web-worker app command which will create src/app/app.worker.ts web worker file.

### This command will perform these actions
Configure your project to use Web Workers.Adds app.worker.ts to receive messages.The component app.component.ts file updated with web worker file.Note: You may need to refactor your initial scaffolding web worker code for sending messages to and from.

### Web workers limitations
You need to remember two important things when using Web Workers in Angular projects,Some environments or platforms(like @angular/platform-server) used in Server-side Rendering, don't support Web Workers.In this case you need to provide a fallback mechanism to perform the computations to work in this environments.Running Angular in web worker using @angular/platform-webworker is not yet supported in Angular CLI.

### The reason to deprecate web worker packages
Both @angular/platform-webworker and @angular/platform-webworker-dynamic are officially deprecated, the Angular team realized it's not good practice to run the Angular application on Web worker

### You provide a singleton service
There are two ways to provide a singleton service.1. Set the providedIn property of the @Injectable() to "root".This is the preferred way(starting from Angular 6.0) of creating a singleton service since it makes your services tree-shakable.import { Injectable } from '@angular/core';@Injectable({ providedIn: 'root', })export class MyService { }1. Include the service in root module or in a module that is only imported by root module.It has been used to register services before Angular 6.0.@NgModule({ providers: [MyService] })

### Ways to remove duplicate service registration
If a module defines provides and declarations then loading the module in multiple feature modules will duplicate the registration of the service.

### These are the ways to prevent this duplicate behavior
1. Use the providedIn syntax instead of registering the service in the module.2. Separate your services into their own module.3. Define forRoot() and forChild() methods in the module.

### Can I share services using modules
No, it is not recommended to share services by importing module.Import modules when you want to use directives, pipes, and components only.The best approach to get a hold of shared services is through 'Angular dependency injection' because importing a module will result in a new service instance.

## Pipes
### Pipes Overview
@Pipe({name: 'myCustomPipe'})The pipe class implements the PipeTransform interface's transform method that accepts an input value followed by optional parameters and returns the transformed value.The structure of pipeTransform would be as below,interface PipeTransform {  transform(value: any, ...args: any[]): any}The @Pipe decorator allows you to define the pipe name that you'll use within template expressions.It must be a valid JavaScript identifier.template: `{{someInputValue | myCustomPipe: someOtherValue}}`

### Custom pipe example
You can create custom reusable pipes for the transformation of existing value.

### Pure vs impure pipe
A pure pipe is only called when Angular detects a change in the value or the parameters passed to a pipe.For example, any changes to a primitive input value (String, Number, Boolean, Symbol) or a changed object reference (Date, Array, Function, Object).An impure pipe is called for every change detection cycle no matter whether the value or parameters changes.i.e, An impure pipe is called often, as often as every keystroke or mouse-move.

### Async pipe
The AsyncPipe subscribes to an observable or promise and returns the latest value it has emitted.When a new value is emitted, the pipe marks the component to be checked for changes.

### Slice pipe
The slice pipe is used to create a new Array or String containing a subset (slice) of the elements.The syntax looks like: {{ value_expression | slice : start [ : end ] }}For example, you can provide 'hello' list based on a greeting array,

### The precedence between pipe and ternary operators
The pipe operator has a higher precedence than the ternary operator (?:).For example, the expression first ? second : third | fourth is parsed as first ? second : (third | fourth).Angular libraries such as FormsModule, HttpClientModule, and RouterModule are NgModules.Many third-party libraries such as Material Design, Ionic, and AngularFire2 are NgModules.

## Location Service
### You install angular language service in the project
You can install Angular Language Service in your project with the following npm command,npm install --save-dev @angular/language-serviceAfter that add the following to the "compilerOptions" section of your project's tsconfig.json"plugins": [ {"name": "@angular/language-service"} ]Note: The completion and diagnostic services works for .ts files only.You need to use custom plugins for supporting HTML files.

### There any editor support for Angular Language Service
Yes, Angular Language Service is currently available for Visual Studio Code and WebStorm IDEs.You need to install angular language service using an extension and devDependency respectively.In sublime editor, you need to install typescript which has has a language service plugin model.

### Explain the features provided by Angular Language Service
The main features provided by Angular Language Service are: Autocompletion, Error checking and Navigation.Autocompletion: Autocompletion can speed up your development time by providing you with contextual possibilities and hints as you type with in an interpolation and elements.Error checking: It can also warn you of mistakes in your code.Navigation: Navigation allows you to hover a component, directive, module and then click and press F12 to go directly to its definition.

## Zones and Locales
### Zone
A Zone is an execution context that persists across async tasks.Angular relies on zone.js to run Angular's change detection processes when native JavaScript operations raise events

### You get current direction for locales
In Angular 9.1, the API method getLocaleDirection can be used to get the current direction in your app.This method is useful to support Right to Left locales for your Internationalization based applications.

### Ngcc
The ngcc(Angular Compatibility Compiler) is a tool which upgrades node_module compiled with non-ivy ngc into ivy compliant format.The postinstall script from package.json will make sure your node_modules will be compatible with the Ivy renderer."scripts": { "postinstall": "ngcc" }Whereas, Ivy compiler (ngtsc), which compiles Ivy-compatible code.

### What classes should not be added to declarations


### These class types shouldn't be added to declarations
A class which is already declared in any another module, Directives imported from another module, Module classes and Service classes.Non-Angular classes and objects, such as strings, numbers, functions, entity models, configurations, business logic, and helper classes.

### NgZone
Angular provides a service called NgZone which creates a zone named angular to automatically trigger change detection when the following conditions are satisfied.   When a sync or async function is executed.   When there is no microTask scheduled.

### NoopZone
Zone is loaded/required by default in Angular applications and it helps Angular to know when to trigger the change detection.This way, it make sures developers focus on application development rather core part of Angular.You can also use Angular without Zone but the change detection need to be implemented on your own and noop zone need to be configured in bootstrap process.Let's follow the below two steps to remove zone.js,Remove the zone.js import from polyfills.ts.

### The possible data update scenarios for change detection
The change detection works in the following scenarios where the data changes needs to update the application HTML.

### Component initialization: While bootstrapping the Angular application, Angular triggers the ApplicationRef.tick() to call change detection and View Rendering.


### Event listener: The DOM event listener can update the data in an Angular component and trigger the change detection too.


### HTTP Data Request: You can get data from a server through an HTTP request


### Macro tasks setTimeout() or setInterval(): You can update the data in the callback function of setTimeout or setInterval


### Micro tasks Promises: You can update the data in the callback function of promise


### Async operations like Web sockets and Canvas: The data can be updated asynchronously using WebSocket.onmessage() and Canvas.toBlob().


### A zone context
Execution Context is an abstract concept that holds information about the environment within the current code being executed.A zone provides an execution context that persists across asynchronous operations is called as zone context. For example, the zone context will be same in both outside and inside setTimeout callback function,zone.run(() => {  // outside zone  expect(zoneThis).toBe(zone);  setTimeout(function() {    // the same outside zone exist here    expect(zoneThis).toBe(zone);  });});The current zone is retrieved through Zone.current.

### The lifecycle hooks of a zone
There are four lifecycle hooks for asynchronous operations from zone.js: onScheduleTask, onInvokeTask, onHasTask and onInvoke.onScheduleTask: This hook triggers when a new asynchronous task is scheduled.  For example, when you call setTimeout()onScheduleTask: function(delegate, curr, target, task) { return delegate.scheduleTask(target, task); }onInvokeTask: This hook triggers when an asynchronous task is about to execute. For example, when the callback of setTimeout() is about to execute.onInvokeTask: function(delegate, curr, target, task, applyThis, applyArgs) { return delegate.invokeTask(target, task, applyThis, applyArgs); }onHasTask: This hook triggers when the status of one kind of task inside a zone changes from stable(no tasks in the zone) to unstable(a new task is scheduled in the zone) or from unstable to stable.onHasTask: function(delegate, curr, target, hasTaskState) { return delegate.hasTask(target, hasTaskState); }onInvoke: This hook triggers when a synchronous function is going to execute in the zone.onInvoke: function(delegate, curr, target, callback, applyThis, applyArgs) { return delegate.invoke(target, callback, applyThis, applyArgs); }

### The methods of NgZone used to control change detection
NgZone service provides a run() method that allows you to execute a function inside the angular zone.This function is used to execute third party APIs which are not handled by Zone and trigger change detection automatically at the correct time.ngOnInit() { // use ngZone.run() to make the asynchronous operation in the angular zonethis.ngZone.run(() => { someNewAsyncAPI(() => { // update the data of the component }); }); } }Whereas runOutsideAngular() method is used when you don't want to trigger change detection.ngOnInit() { // Use this method when you know no data will be updatedthis.ngZone.runOutsideAngular(() => { setTimeout(() => { // update component data and don't trigger change detection }); }); } }

### You change the settings of zonejs
You can change the settings of zone by configuring them in a separate file and import it just after zonejs import.For example, you can disable the requestAnimationFrame() monkey patch to prevent change detection for no data update as one settingand prevent DOM events(a mousemove or scroll event) to trigger change detection.

### Angular simplifies Internationalization
Angular simplifies these areas of internationalization: Displaying dates, number, percentages, and currencies in a local format,Preparing text in component templates for translation, Handling plural forms of words and Handling alternative text.

### You manually register locale data
By default, Angular only contains locale data for en-US which is English as spoken in the United States of America.But if you want to set to another locale, you must import locale data for that new locale.After that you can register using the registerLocaleData method.

## Security
### The security principles in angular
Avoid direct use of the DOM APIs.Enable Content Security Policy (CSP) and configure your web server to return appropriate CSP HTTP headers.Use the offline template compiler.Use Server Side XSS protection.Use DOM Sanitizer.Preventing CSRF or XSRF attacks.

### The best practices for security in angular
Below are the best practices of security in angular,Use the latest Angular library releases.Don't modify your copy of Angular.Avoid Angular APIs marked in the documentation as Security Risk.

### Angular security model for preventing XSS attacks
Angular treats all values as untrusted by default.Angular sanitizes and escapes untrusted values when a value is inserted into the DOM from a template, via property, attribute, style, class binding, or interpolation.

### The role of template compiler for prevention of XSS attacks
The offline template compiler prevents vulnerabilities caused by template injection, and greatly improves application performance.So it is recommended to use offline template compiler in production deployments without dynamically generating any template.

### You support server side XSS protection in Angular application
The server-side XSS protection is supported in an angular application by using a templating language that automatically escapes values to prevent XSS vulnerabilities on the server.But don't use a templating language to generate Angular templates on the server side which creates a high risk of introducing template-injection vulnerabilities.

### The various security contexts in Angular
Angular defines the following security contexts for sanitization,HTML: It is used when interpreting a value as HTML such as binding to innerHtml.Style: It is used when binding CSS into the style property.URL: It is used for URL properties such as <a href>.Resource URL: It is a URL that will be loaded and executed as code such as <script src>.

### Safe to use direct DOM API methods in terms of security
No,the built-in browser DOM APIs or methods don't automatically protect you from security vulnerabilities.In this case it is recommended to use Angular templates instead of directly interacting with DOM.If it is unavoidable then use the built-in Angular sanitization functions.

### Sanitization? Does angular supports it
Sanitization is the inspection of an untrusted value, turning it into a value that's safe to insert into the DOM.Yes, Angular suppports sanitization. It sanitizes untrusted values for HTML, styles, and URLs but sanitizing resource URLs isn't possible because they contain arbitrary code.

### You prevent automatic sanitization
Sometimes the applications genuinely need to include executable code such as displaying <iframe> from an URL.In this case, you need to prevent automatic sanitization in Angular by saying that you inspected a value, checked how it was generated, and made sure it will always be secure.

### It involves 2 steps
Inject DomSanitizer: You can inject DomSanitizer in component as parameter in constructor.Mark the trusted value by calling some of the below methods.bypassSecurityTrustHtmlbypassSecurityTrustScriptbypassSecurityTrustStylebypassSecurityTrustUrlbypassSecurityTrustResourceUrl

### DOM sanitizer
DomSanitizer is used to help preventing Cross Site Scripting Security bugs (XSS) by sanitizing values to be safe to use in the different DOM contexts.

### Angular prevent HTTP level vulnerabilities
Angular has built-in support for preventing http level vulnerabilities such as as cross-site request forgery (CSRF or XSRF) and cross-site script inclusion (XSSI).Even though these vulnerabilities need to be mitigated on server-side, Angular provides helpers to make the integration easier on the client side.HttpClient supports a token mechanism used to prevent XSRF attacksHttpClient library recognizes the convention of prefixed JSON responses(which non-executable js code with ")]}',\n" characters) and automatically strips the string ")]}',\n" from all responses before further parsing

### HTTP Interceptors
Http Interceptors are part of @angular/common/http, which inspect and transform HTTP requests from your application to the server and vice-versa on HTTP responses.These interceptors can perform a variety of implicit tasks, from authentication to logging.

### The syntax of HttpInterceptor interface looks like
interface HttpInterceptor { intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> }You can use interceptors by declaring a service class that implements the intercept() method of the HttpInterceptor interface.

### The applications of HTTP interceptors


### The HTTP Interceptors can be used for different variety of tasks
Authentication, Logging, Caching, Fake backend, URL transformation and Modifying headers.

### Multiple interceptors supported in Angular
Yes, Angular supports multiple interceptors at a time.

### You could define multiple interceptors in providers property
providers: [  { provide: HTTP_INTERCEPTORS, useClass: MyFirstInterceptor, multi: true },  { provide: HTTP_INTERCEPTORS, useClass: MySecondInterceptor, multi: true } ],The interceptors will be called in the order in which they were provided., MyFirstInterceptor will be called first in the above interceptors configuration.

### I use interceptor for an entire application
You can use same instance of HttpInterceptors for the entire app by importing the HttpClientModule only in your AppModule, and add the interceptors to the root application injector.

## HTTP Client
### HTTP Client Overview
The response body doesn't may not return full response data because sometimes servers also return special headers or status code which which are important for the application workflow.Inorder to get full response, you should use observe option from HttpClient,getUserResponse(): Observable<HttpResponse<User>> {  return this.http.get<User>(    this.userUrl, { observe: 'response' });}Now HttpClient.get() method returns an Observable of typed HttpResponse rather than just the JSON data.

### Perform Error handling
If the request fails on the server or failed to reach the server due to network issues then HttpClient will return an error object instead of a successful reponse.In this case, you need to handle in the component by passing error object as a second callback to subscribe() method.Let's see how it can be handled in the component with an example,fetchUser() {  this.userService.getProfile()    .subscribe(      (data: User) => this.userProfile = { ...data }, // success path      error => this.error = error // error path    );}It is always a good idea to give the user some meaningful feedback instead of displaying the raw error object returned from HttpClient.

### Pass headers for HTTP client
You can directly pass object map for http client or create HttpHeaders class to supply the headers.constructor(private _http: HttpClient) {}this._http.get('someUrl',{ headers: {'header1':'value1','header2':'value2'} });return this._http.get<any[]>('someUrl', { headers: headers, params: params })

## Types
### Types Overview
The expression used in an ngIf directive is used to narrow type unions in the Angular template compiler similar to if expression in typescript.So *ngIf allows the typeScript compiler to infer that the data used in the binding expression will never be undefined.

### Case types
Angular uses capitalization conventions to distinguish the names of various types.Angular follows the list of the below case types: camelCase, UpperCamelCase (or PascalCase), dash-case (or kebab-case) and UPPER_UNDERSCORE_CASE.camelCase : Symbols, properties, methods, pipe names, non-component directive selectors, constants uses lowercase on the first letter of the item. For example, "selectedUser"UpperCamelCase (or PascalCase): Class names, including classes that define components, interfaces, NgModules, directives, and pipes uses uppercase on the first letter of the item.dash-case (or kebab-case): The descriptive part of file names, component selectors uses dashes between the words. For example, "app-user-list".UPPER_UNDERSCORE_CASE: All constants uses capital letters connected with underscores. For example, "NUMBER_OF_USERS".

## Schematics
### Schematics Overview
You can install Schematic CLI globally as: npm install -g @angular-devkit/schematics-cli

### Create schematics for libraries
You can create your own schematic collections to integrate your library with the Angular CLI.These collections are classified as 3 main schematics,Add schematics: These schematics are used to install library in an Angular workspace using ng add command.For example, @angular/material schematic tells the add command to install and set up Angular Material and theming.Generate schematics: These schematics are used to modify projects, add configurations and scripts, and scaffold artifacts in library using ng generate command. For example, @angular/material generation schematic supplies generation schematics for the UI components. Let's say the table component is generated using ng generate @angular/material:table .Update schematics: These schematics are used to update library's dependencies and adjust for breaking changes in a new library release using ng update command. For example, @angular/material update schematic updates material and cdk dependencies using ng update @angular/material command.

## CSS and Fonts
## Bazel Tool
### Bazel Tool Overview
Use in a new application: Install the package and create the application with collection optionnpm install -g @angular/bazelng new --collection=@angular/bazelWhen you use ng build and ng serve commands, Bazel is used behind the scenes and outputs the results in dist/bin folder.

### Run Bazel directly
Sometimes you may want to bypass the Angular CLI builder and run Bazel directly using Bazel CLI.You can install it globally using @bazel/bazel npm package., Bazel CLI is available under @bazel/bazel package.After you can apply the common commands: bazel build, bazel test and bazel run.bazel build [targets] // Compile the default output artifacts of the given targets.bazel test [targets] // Run the tests with *_test targets found in the pattern.bazel run [target]: Compile the program represented by target and then run it.

## Test
### You test Angular application using CLI
Angular CLI downloads and install everything needed with the Jasmine Test framework.You just need to run ng test to see the test results.By default this command builds the app in watch mode, and launches the Karma test runner.The output of test results would be as below,10% building modules 1/1 modules 0 active...INFO [karma]: Karma v1.7.1 server started at http://0.0.0.0:9876/...INFO [launcher]: Launching browser Chrome ......INFO [launcher]: Starting browser Chrome...INFO [Chrome ...]: Connected on socket ...Chrome ...: Executed 3 of 3 SUCCESS (0.135 secs / 0.205 secs)Note: A chrome browser also opens and displays the test output in the "Jasmine HTML Reporter".

### TestBed
TestBed is an api for writing unit tests for Angular applications and it's libraries.Even though We still write our tests in Jasmine and run using Karma, this API provides an easier way to create components, handle injection, test asynchronous behaviour and interact with our application.

### Type safe TestBed API changes in Angular9
Angular 9 provides type safe changes in TestBed API changes by replacing the old get function with the new inject method.Because TestBed.get method is not type-safe.

### The usage would be as
TestBed.get(ChangeDetectorRef) // returns any. It is deprecated now.TestBed.inject(ChangeDetectorRef) // returns ChangeDetectorRef

### Mandatory to pass static flag for ViewChild
In Angular 8, the static flag is required for ViewChild.Whereas in Angular9, you no longer need to pass this property.Once you updated to Angular9 using ng update, the migration will remove { static: false } script everywhere.Angular 9: @ViewChild(ChildDirective) child: ChildDirective;Angular 8: @ViewChild(ChildDirective, { static: false }) child: ChildDirective;

## More Angular
### Angular Universal
Angular Universal is a server-side rendering module for Angular applications in various scenarios.This is a community driven project and available under @angular/platform-server package.Recently Angular Universal is integrated with Angular CLI.

### Folding
The compiler can only resolve references to exported symbols in the metadata.Where as some of the non-exported members are folded while generating the code.i.e Folding is a process in which the collector evaluate an expression during collection and record the result in the .metadata.json instead of the original expression.The compiler couldn't refer selector reference because it is not exported.Will be folded into inline selectorRemember that the compiler can't fold everything.For example, spread operator on arrays, objects created using new keywords and function calls.

### Macros
The AOT compiler supports macros in the form of functions or static methods that return an expression in a single return expression.Define a macro function and use it inside metadata as an expression.The compiler treats the macro expression as it is written directly.

### You provide configuration inheritance
Angular Compiler supports configuration inheritance through extends in the tsconfig.json on angularCompilerOptions.The configuration from the base file(for example, tsconfig.base.json) are loaded first, then overridden by those in the inheriting config file.

### You enable binding expression validation
You can enable binding expression validation explicitly by adding the compiler option fullTemplateTypeCheck in the "angularCompilerOptions" of the project's tsconfig.json.It produces error messages when a type error is detected in a template binding expression.

### AOT compiler
The AOT compiler is part of a build process that produces a small, fast, ready-to-run application package, typically for production.It converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.

### You describe various dependencies in angular application
The dependencies section of package.json with in an angular application can be divided as follow,Angular packages: Angular core and optional modules; their package names begin @angular/.Support packages: Third-party libraries that must be present for Angular apps to run.Polyfill packages: Polyfills plug gaps

### AOT compiler
The AOT compiler is part of a build process that produces a small, fast, ready-to-run application package, typically for production.It converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.in a browser's JavaScript implementation.

### Codelyzer
Codelyzer provides set of tslint rules for static code analysis of Angular TypeScript projects.You can run the static code analyzer over web apps, NativeScript, Ionic etc.Angular CLI has support for this and it can be use as: ng new codelyzer, ng lint.

### State function
Angular's state() function is used to define different states to call at the end of each transition.This function takes two arguments: a unique name like open or closed and a style() function.Write an open state function as: state open style etc.

### Style function
The style function is used to define a set of styles to associate with a given state name.You need to use it along with state() function to set CSS style attributes.For example, in the close state, the button has a height of 100 pixels, an opacity of 0.8, and a background color of green.state close style etc.The style attributes must be in camelCase.

### Transition function
The animation transition function is used to specify the changes that occur between one state and another over a period of time.It accepts two arguments: the first argument accepts an expression that defines the direction between two transition states, and the second argument accepts an animate() function.

### Declarable in Angular
Declarable is a class type that you can add to the declarations list of an NgModule.The class types such as components, directives, and pipes comes can be declared in the module.The structure of declarations would be: declarations: [ YourComponent, YourPipe, YourDirective ],

### The restrictions on declarable classes
Below classes shouldn't be declared: A class that's already declared in another NgModule, Ngmodule classes, Service classes and Helper classes.

### Angular DSL
A domain-specific language (DSL) is a computer language specialized to a particular application domain.Angular has its own Domain Specific Language (DSL) which allows us to write Angular specific HTML-like syntax on top of normal HTML.It has its own compiler that compiles this syntax to HTML that the browser can understand.This DSL is defined in NgModules such as animations, forms, and routing and navigation.Basically there are 3 main syntax in Angular DSL: Open-close paranthesis, Open-close bracket and astrisk.(): Used for Output and DOM events.[]: Used for Input and specific DOM element attributes.*: Structural directives(*ngFor or *ngIf) will affect/change the DOM structure.

### Platform in Angular
A platform is the context in which an Angular application runs.The most common platform for Angular applications is a web browser, but it can also be an operating system for a mobile device, or a web server.The runtime-platform is provided by the @angular/platform-* packages and these packages allow apps that make use of @angular/core and @angular/common to execute in different environments., Angular can be used as platform-independent framework in different environments, For example,While running in the browser, it uses platform-browser package.When SSR(server-side rendering ) is used, it uses platform-server package for providing web server implementation.

### Angular supports dynamic imports
Yes, Angular 8 supports dynamic imports in router configuration.You can use the import statement for lazy loading the module using loadChildren method and it will be understood by the IDEs(VSCode and WebStorm), webpack, etc.Previously, you have been written as below to lazily load the feature module.By mistake, if you have typo in the module name it still accepts the string and throws an error during build time.{path: 'user', loadChildren: './users/user.module#UserModulee'},This problem is resolved by using dynamic imports and IDEs are able to find it during compile time itself.{path: 'user', loadChildren: () => import('./users/user.module').then(m => m.UserModule)};

### Lazy loading
Lazy loading is one of the most useful concepts of Angular Routing.It helps us to download the web pages in chunks instead of downloading everything in a big bundle.It is used for lazy loading by asynchronously loading the feature module for routing whenever required using the property loadChildren.Let's load both Customer and Order feature modules lazily as below,const routes: Routes = [  {    path: 'customers',    loadChildren: () => import('./customers/customers.module').then(module => module.CustomersModule)  },  {    path: 'orders',    loadChildren: () => import('./orders/orders.module').then(module => module.OrdersModule)  },  {    path: '',    redirectTo: '',    pathMatch: 'full'  }];

### Workspace APIs
Angular 8.0 release introduces Workspace APIs to make it easier for developers to read and modify the angular.json file instead of manually modifying it.Currently, the only supported storage3 format is the JSON-based format used by the Angular CLI.Example: buildTarget.options.optimization = true;

### Angular Material
Angular Material is a collection of Material Design components for Angular framework following the Material Design spec.You can apply Material Design very easily using Angular Material.The installation can be done through npm or yarn,npm install --save @angular/material @angular/cdk @angular/animationsoryarn add @angular/material @angular/cdk @angular/animationsIt supports the most recent two versions of all major browsers.The latest version of Angular material is 8.1.1.

### The ways to trigger change detection in Angular
You can inject either ApplicationRef or NgZone, or ChangeDetectorRef into your component and apply below specific methods to trigger change detection in Angular.There are 3 possible ways,ApplicationRef.tick(): Invoke this method to explicitly process change detection and its side-effects. It check the full component tree.NgZone.run(callback): It evaluate the callback function inside the Angular zone.ChangeDetectorRef.detectChanges(): It detects only the components and it's children.

### The reason to deprecate Web Tracing Framework
Angular has supported the integration with the Web Tracing Framework (WTF) for the purpose of performance testing.Since it is not well maintained and failed in majority of the applications, the support is deprecated in latest releases.

### The browser support for Angular
Angular supports most recent browsers which includes both desktop and mobile browsers.Chrome: latest versionFirefox: latest versionEdge: 2 most recent major versionsIE: 11, 10, 9 (Compatibility mode is not supported)Safari: 2 most recent major versionsIE Mobile: 11iOS: 2 most recent major versionsAndroid: Versions 7.0, 6.0, 5.0, 5.1, 4.4

### The purpose of i18n attribute
The Angular i18n attribute marks translatable content.It is a custom attribute, recognized by Angular tools and compilers.The compiler removes it after translation.Note: Remember that i18n is not an Angular directive.

### The purpose of custom id
When you change the translatable text, the Angular extractor tool generates a new id for that translation unit.Because of this behavior, you must then update the translation file with the new id every time.For example, the translation file messages.de.xlf.HTML has generated trans-unit for some text message as:<trans-unit id=some number datatype="HTML">You can avoid this manual update of id attribute by specifying a custom id in the i18n attribute by using the prefix @@.<h1 i18n="@@welcomeHeader">Hello i18n!</h1>

### What happens if the custom id is not unique
You need to define custom ids as unique.If you use the same id for two different text messages then only the first one is extracted.But its translation is used in place of both original text messages.For example, let's define same custom id myCustomId for two messages,<h2 i18n="@@myCustomId">Good morning</h3><h2 i18n="@@myCustomId">Good night</p>and the translation unit generated for first text in for German language as<trans-unit id="myId" datatype="HTML">  <source>Good morning</source>  <target state="new">Guten Morgen</target></trans-unit>Since custom id is the same, both of the elements in the translation contain the same text as below<h2>Guten Morgen</h2><h2>Guten Morgen</h2>

### Can I translate text without creating an element
Yes, you can achieve using <ng-container> attribute.Normally you need to wrap a text content with i18n attribute for the translation.But if you don't want to create a new DOM element just for the sake of translation, you can wrap the text in an element.<ng-container i18n>I'm not using any DOM element for translation</ng-container>Remember that <ng-container> is transformed into an HTML comment

### I translate attribute
You can translate attributes by attaching i18n-x attribute where x is the name of the attribute to translate.

### For example, you can translate image title attribute as
<img [src]="example" i18n-title title="Internationlization" />By the way, you can also assign meaning, description and id with the i18n-x="|@@" syntax.

### List down the pluralization categories
Pluralization has these categories depending on the language: =0 (or any other number), zero, one, two, few, many or other.

### Select ICU expression
ICU expression is is similar to the plural expressions except that you choose among alternative translations based on a string value instead of a number.Here you define those string values.Let's take component binding with residence property which has "citizen", "permanent resident" and "foreigner" possible values and the message maps those values to the appropriate translations.<span i18n>The person is {residence, select, citizen {citizen} permanent resident {permanentResident} foreigner {foreigner}}</span>

### You report missing translations
By default, When translation is missing, it generates a warning message such as "Missing translation for message 'somekey'".But you can configure with a different level of message in Angular compiler

### As
Error: It throws an error.If you are using AOT compilation, the build will fail.But if you are using JIT compilation, the app will fail to load.Warning (default): It shows a 'Missing translation' warning in the console or shell.Ignore: It doesn't do anything.If you use AOT compiler then you need to perform changes in configurations section of your Angular CLI configuration file, angular.json.If you use the JIT compiler, specify the warning level in the compiler config at bootstrap by adding the 'MissingTranslationStrategy' property.

### Protractor
Protractor is an end-to-end test framework for Angular and AngularJS applications.It runs tests against your application running in a real browser, interacting with it as a user would.npm install -g protractor

### Collection
Collection is a set of related schematics collected in an npm package.For example, @schematics/angular collection is used in Angular CLI to apply transforms to a web-app project.You can create your own schematic collection for customizing angular projects.

### You use J Query in Angular
You can use J Query in Angular using 3 simple steps,1. Install the dependency: At first, install the J Query dependency using npm   npm install --save J Query2. Add the J Query script: In Angular-CLI project, add the relative path to J Query in the angular.json file."scripts": [ "node_modules/J Query/dist/J Query.min.js" ]3. Start using J Query: Define the element in template. Whereas declare the J Query variable and apply CSS classes on the element.

### The reason for No provider for HTTP exception
This exception is due to missing HttpClientModule in your module.

### Import in module as
import { HttpClientModule } from '@angular/common/http';@NgModule({ imports: [ BrowserModule, HttpClientModule, ], etc.

### Router state
The RouteState is an interface which represents the state of the router as a tree of activated routes.interface RouterState extends Tree { snapshot: RouterStateSnapshot toString(): string }You can access the current RouterState from anywhere in the Angular app using the Router service and the routerState property.

### I use SASS in angular project
When you are creating your project with angular cli, you can use ng newcommand.It generates all your components with predefined sass files.ng new My_New_Project --style=sassBut if you are changing your existing style in your project then use ng set command,ng set defaults.styleExt scss

### The purpose of hidden property
The hidden property is used to show or hide the associated DOM element, based on an expression.It can be compared close to ng-show directive in AngularJS.Let's say you want to show user name based on the availability of user using hidden property.<div [hidden]="!user.name"> My name is: {{user.name}} </div>

### It possible to do aliasing for inputs and outputs
Yes, it is possible to do aliasing for inputs and outputs in two ways.1. Aliasing in metadata: The inputs and outputs in the metadata aliased using a colon-delimited (:) string with the directive property name on the left and the public alias on the right.It will be in the format of propertyName:alias.inputs: ['input1: buyItem'],outputs: ['outputEvent1: completedEvent']2. Aliasing with @Input()/@Output() decorator: The alias can be specified for the property name by passing the alias name to the @Input()/@Output() decorator.It will be in the form of @Input(alias) or @Output(alias).@Input('buyItem') input1: string;@Output('completedEvent') outputEvent1 = new EventEmitter<string>();

### Safe navigation operator
The safe navigation operator(?)(or known as Elvis Operator) is used to guard against null and undefined values in property paths when you are not aware whether a path exists or not.It returns value of the object path if it exists, else it returns the null value.For example, you can access nested properties of a user profile easily without null reference errors as below,

### <p>The user firstName is: {{user?.fullName.firstName}}</p>
Using this safe navigation operator, Angular framework stops evaluating the expression when it hits the first null value and renders the view without any errors.

### Any special configuration required for Angular9
You don't need any special configuration.In Angular9, the Ivy renderer is the default Angular compiler.Even though Ivy is available Angular8 itself, you had to configure it in tsconfig.json file as below,"angularCompilerOptions": {    "enableIvy": true  }

### A shared module
The Shared Module is the module in which you put commonly used directives, pipes, and components into one module that is shared(import it) throughout the application.

# C# [Advanced]
## C# [Basic Knowledge]
### SOLID Principles
Single-responsibility: 1 jobOpen-closed: Open for extension. Closed for modification.Liskov substitution: Substitutable: Every derived class should be substitutable for their base class.Interface segregation: No forced implementation: Do not force to implement an intf. Do not force to depend on methods.Dependency Inversion: Entities depend on abstractions, not concretions.

### Mediator Pattern
A Mediator has hooks for each Colleague.When creating each Colleague, set the Mediator.Add each Colleague to the Mediator.Colleagues communicate through the Mediator API.

### Attribute In C#
An attributes is a declarative tag that is used to convey information about the behaviors of various elements (classes, methods, assemblies, structures, enumerators, etc).it is access at compile time or run-time.Attributes are declare with a square brackets [] which is places above the elements.[Obsolete(Don't use Old method, please use New method, true)]For example consider the bellow class.If we call the old method it will through error message.public class myClass{  [Obsolete("Don't use Old method, please use New method", true)]  public string Old() { return "Old"; }  public string New() { return "New"; }}myClass omyClass = new myClass();omyClass.Old();

### Attributes Are Used
In a program the attributes are used for adding metadata, like compiler instruction or other information (comments, description, etc).

### The Types Of Attributes
The Microsoft .NET Framework provides two types of attributes: the pre-defined attributes and custom built attributes.Pre-define attributes are three types: AttributeUsage, Conditional, and Obsolete.This marks a program that some entity should not be used.

### Custom Attributes
The Microsoft .NET Framework allows creating custom attributes that can be used to store declarative information and can be retrieved at run-time.

### Reflection
Reflection is a process by which a computer program can monitor and modify its own structure and behavior.It is a way to explore the structure of assemblies at run time (classes, resources, methods).Reflection is the capability to find out the information about objects, metadata, and application details (assemblies) at run-time.We need to include System.Reflection namespace to perform reflections in C#.For example consider the following C# codes, which will returns some meta information's.public class MyClass{  public virtual int Add(int numb1, int numb2)  {    return numb1 + numb2;  }  public virtual int Subtract(int numb1, int numb2)  {    return numb1 - numb2;  }}static void Main(string[] args){  MyClass oMyClass = new MyClass();  //Type information.  Type oMyType = oMyClass.GetType();  //Method information.  MethodInfo oMyMethodInfo = oMyType.GetMethod("Subtract");  Console.WriteLine("nType information:" + oMyType.FullName);  Console.WriteLine("nMethod info:" + oMyMethodInfo.Name);  Console.Read();}

### We Need Reflection In C#
Reflections needed when we want to determine / inspect contents of an assembly.For example: at Visual Studio editor intelligence, when we type dot before any object, it gives us all the members of the object.This is possible for Reflection.

### Beside this we need reflection for the following purposes
To view attribute information at run timeTo view the structure of assemblies at run time (classes, resources, methods)It allows dynamic/late binding to methods and propertiesIn serialization, it is used to serialize and de-serialize objectsIn web service, it is used to create and consume SOAP messages and also to generate WSDLDebugging tools can use reflection to examine the state of an object.

### Dynamic Keyword
The dynamic is a keyword which was introduced in .NET 4.0.Computer programming languages are two types: strongly typed and dynamically typed.In strongly types all types checks are happened at compile time, in dynamic types all types of checks are happened at run time.For example consider the following codedynamic x = "C#";x++;It will not provide error at compile time but will provide error at run time.

### To Use Dynamic
The biggest practical use of the dynamic keyword is when we operate on MS Office.

### The Difference Between Reflection And Dynamic
Both Reflection and dynamic are used to operate on an object during run time.

### But they have some differences
Dynamic uses reflection internallyReflection can invoke both public and private members of an object.But dynamic can only invoke public members of an object

### Serialization
When we want to transport an object through network then we need to convert the object into a stream of bytes.Serialization is a process to convert a complex objects into stream of bytes for storage (database, file, cache, etc) or transfer.Its main purpose is to save the state of an object.De-serialization is the reverse process of creating an object from a stream of bytes to their original form.

### The Types Of Serialization


### The types of Serializations are given bellow
1. Binary Serialization: In this process all the public, private, read only members are serialized and convert into stream of bytes. This is used when we want a complete conversion of our objects.2. SOAP Serialization: In this process only public members are converted into SOAP format. This is used in web services.3. XML Serialization: In this process only public members are converted into XML. This is a custom serialization. Required namespaces: System.Xml, System.Xml.Serialization.

### Serialization And Deserialization
For example consider, we have a very complex object and we need XML format to show it on HTML page.Then we can create a XML file in the disk, writes all the necessary data on the XML file, and use it for the HTML page.But this is not good approach for large number of users.Extra space is required; anyone can see the XML file which creates security issue.We can overcome it by using XML serialization.

### To Use Serialization


### Serialization is used in the following purposes
To pass an object from on application to another.In SOAP based web services.To transfer data through cross platforms, cross devices.

### Give Examples Where Serialization Is Used
Serialization is used to save session state in ASP .NET applications, to copy objects to the clipboard in Windows Forms.It is also used to pass objects from one application domain to another.Web services uses serialization.

### Generics
Generics are the most powerful features introduced in C# 2.0.It is a type-safe data structure that allows us to write codes that works for any data types.

### A Generic Class
A generic class is a special kind of class that can handle any types of data.We specify the data types during the object creations of that class.It is declared with the bracket <>.For example consider the following Comparer class, which has a method that compare two value and returns as Boolean output.public class Comparer{  public bool Compare(Unknown t1, Unknown t2)  {    if (t1.Equals(t2))    {      return true;    }    else    {      return false;    }  }}Comparer oComparerInt = new Comparer();Console.WriteLine(oComparerInt.Compare(10, 10));Comparer oComparerStr = new Comparer();Console.WriteLine(oComparerStr.Compare("jdhsjhds", "10"));

### We Should Use Generics
Generic provides lot of advantages during programming.

### We should use generics for the following reasons
It allows creating class, methods which are type-safeIt is faster. Because it reduce boxing/un-boxingIt increase the code performanceIt helps to maximize code reuse, and type safety

### Collections In C#
Sometimes we need to work with related objects for data storage and retrieval.There are two ways to work with related objects.One is array and another one is collections.Arrays are most useful for creating and working with a fixed number of strongly-typed objects.Collections are enhancement of array which provides a more flexible way to work with groups of objects.The Microsoft .NET framework provides specialized classes for data storage and retrieval.Collections are one of them.Collection is a data structure that holds data in different ways.Collections are two types.One is standard collections, which is found under System.Collections namespace and another one is generic collections, which is found under System.Collections.Generic namespace.The generic collections are more flexible and preferable to work with data.

### Collections: Commonly used collections under System.Collections
ArrayList, SortedList, Hashtable, Stack, Queue, BitArray

### Unsafe Code
In order to maintain security and type safety, C# does not support pointer generally.But by using unsafe keyword we can define an unsafe context in which pointer can be used.The unsafe code or unmanaged code is a code block that uses a pointer variable.In the CLR, unsafe code is referred to as unverifiable code.In C#, the unsafe code is not necessarily dangerous.The CLR does not verify its safety.The CLR will only execute the unsafe code if it is within a fully trusted assembly.If we use unsafe code, it is our own responsibility to ensure that the code does not introduce security risks or pointer errors.

### The Properties Of Unsafe Code


### Some properties of unsafe codes are given bellow
We can define Methods, types, and code blocks as unsafeIn some cases, unsafe code may increase the application's performance by removing array bounds checksUnsafe code is required in order to call native functions that require pointersUsing unsafe code brings security and stability risksIn order to compile unsafe code, the application must be compiled with /unsafe

### Can Unsafe Code Be Executed In Untrusted Environment
Unsafe code cannot be executed in an un-trusted environment.For example, we cannot run unsafe code directly from the Internet.

### Compile Unsafe Code
For compiling unsafe code, we have to specify the /unsafe command-line switch with command-line compiler.For example: to compile a program named myClass.cs containing unsafe code the command line command is:csc /unsafe myClass.csIn Visual Studio IDE at first we need to enable use of unsafe code in the project properties.

### The steps are given bellow
Open project propertiesClick on the Build tabSelect the option, Allow unsafe code

### Pointer
Pointer is a variable that stores the memory address of another variable.Pointers in C# have the same capabilities as in C or C++.

### Some examples of pointers are
int *i // pointer of an integerfloat *f // pointer to a floatdouble *d // pointer to a doublechar *ch // pointer to a character

### I Use Unsafe Code In C#
In C#, pointer is really used and Microsoft disengaged to use it.But there are some situations that require pointer.We can use pointer if required at our own risk.

### Some sonorous are given bellow
To deal with existing structures on diskSome advanced COM or Platform Invoke scenarios that involve pointerTo performance critical codes

### We Sort The Elements Of The Array In Descending Order
For This,First we call the Sort () method and then call Reverse() Methods.

### Can We Store Multiple Data Types In System.array
No.

### The Difference Between The System.array.copyto() And System.array.clone()
System.Array.CopyTo(): It requires a destination array to be existed before and   it must be capable to hold all the elements in the source array from the index that is specified to copy from the source array.System.Array.Clone():  It does not require the destination array to be existed as it creates a new one from scratch.Note-These both are used as a shallow copy.

### Difference Between String And Stringbuilder
StringBuilder is more efficient than string.String: It is Immutable and resides within System Namespace.StringBuilder: It is mutable and resides System.Text Namespace.

### Class Sortedlist Underneath
It is a Hash Table.

### The .NET Data Type That Allow The Retrieval Of Data By A Unique Key
Hash Table

### Finally Block Get Executed If The Exception Is Not Occured
Yes.

### Can Multiple Catch () Block Get Executed If The Exception Is Not Occured
No,Once the proper catch code fires off ,the control is transferred to the finally block(if any),and the whatever follows the finally block.

### Multicast Delegate
The Multicast delegate is a delegate that points to and eventually fires off several methods.

### The Ways To Deploy An Assembly
An MSI InstallerA CAB archiveX Copy command

### The Dll Hell Problem Solved In .NET
In .NET, Assembly versioning allows the application to specify not only the library it needs to run ,but also the version of the assembly.

### A Satellite Assembly
When we write the code, a multicultural or multilingual application in .NETand want to distribute the core application separately from the localized modules,the localized assemblies that modify the core application,that is known as Satellite assembly.

### We Inherit From A Class In C#
In C#, we use a colon (:) and then the name of the base class.

### C# Support Multiple Inheritance
No, we use interface for this purpose.

### Private Class -label Variables Inherited
Yes, but it is not accessible.we generally know that they are inherited but not accessible.

### The Implicit Name Of The Parameter That Gets Passed Into Class "set" Method
Value and it's datatype(it depends whatever variable we are changing).

### The Top .NET Class
System.Object

### Method Overloading Different From Overriding
A method overloading simply involves having a method with the same name within the class.Whereas in method overriding we can change method behaviour for a derived class.

### Can We Override Private Virtual Method
No.

### Can We Declare The Override Method Static While The Original Method Is Non Static
No.

### Can We Prevent My Class From Being Inherited And Becoming A Base Class From The Other Classes
Yes.

### An Interface Class
This is an abstract class with public abstract methods , all of which must be implemented in the inherited classes.

### Can We Inherit Multiple Interfaces
Yes.

### Can We Allow Class To Be Inherited ,but Prevent The Method From Being Overridden
Yes, first create class as public and make it's method sealed.

### Signature Used For Overloaded A Method
Use different data typesUse different number of parametersUse different order of parameters

### The Difference Between An Interface And Abstract Class
In an interface, all methods must be abstract but in abstract class some methods can be concrete.In interface No accessibility modifiers are alloweded but in abstract class a accessibility modifier are alloweded.

# C# LANGUAGE, APPLICATIONS and MANAGED CODE Q&As
### C# LANGUAGE:
C# is an object-oriented, type-safe, and managed language.It is compiled by the .NET framework to generate Microsoft Intermediate Language.

### C# code is managed or unmanaged code
C# is managed code because Common language runtime can compile C# code to Intermediate language.

### A Console application
A console application is an application that can be run in the command prompt in Windows.For any beginner on .NET, building a console application is ideally the first step, to begin with.

### An object pool
An object pool is a container having objects ready to be used.It tracks the object that is currently in use, total number of objects in the pool.This reduces the overhead of creating and re-creating objects.

## COMMENTS
### TYPES OF COMMENTS
There are 3 types of comments in csharp, single line, multiple line and XML.Single line comments: start with double forward slashes.Multiple line comments: are encased in forward slash asterix and asterix forard slash.XML comments: start with 3 forward slashes.

## DECLARATION TYPES
### Use nullable types
Value types can take either their normal values or a null value.Such types are called nullable types.Nullable Int someID = null;If someID.HasVAlue

## OPERATIONS - COMPARISON
### And As operators:
"is" operator is used to check the compatibility of an object with a given type, and it returns the result as Boolean."as" operator is used for casting of an object to a type or a class.

## ATTRIBUTES
### C# attributes and its significance
C# provides developers a way to define declarative tags on certain entities, eg.Class, method, etc. are called attributes.The attribute's information can be retrieved at runtime using Reflection.

## CASTING
### Directcast vs ctype:
DirectCast is used to convert the type of object that requires the run-time type to be the same as the specified type in DirectCast.Ctype is used for conversion where the conversion is defined between the expression and the type.

## GENERICS
### Generics
Generics are used to make reusable code classes to decrease the code redundancy, increase type safety, and performance.Using generics, we can create collection classes.To create generic collection, System.Collections.Generic namespace should be used instead of classes such as ArrayList in the System.Collections namespace.Generics promotes the usage of parameterized types.

## CLASSES and INTERFACES
### Define Constructors
A constructor is a member function in a class that has the same name as its class.The constructor is automatically invoked whenever an object class is created.It constructs the values of data members while initializing the class.

### You inherit a class into other class
Colon is used as inheritance operator.Just place a colon and then the class name.public class DerivedClass : BaseClass

### The base class in .net from which all the classes are derived from
System.Object

### An interface class
An Interface is an abstract class which has only public abstract methods, and the methods only have the declaration and not the definition.These abstract methods must be implemented in the inherited classes.

### Interface vs abstract class
Interfaces have all the methods having only declaration but no definition.In an abstract class, we can have some concrete methods.In an interface class, all the methods are public.An abstract class may have private methods.

### Sealed classes
We create sealed classes when we want to restrict the class to be inherited.Sealed modifier used to prevent derivation from a class.

### We set the class to be inherited, but prevent the method from being over-ridden
Declare the class as public and make the method sealed to prevent it from being overridden.

### Struct vs Class
Structs are value-type variables, and classes are reference types.Structs stored on the Stack causes additional overhead but faster retrieval.Structs cannot be inherited.

### Implement a singleton design pattern
In a singleton pattern, a class can only have one instance and provides an access point to it globally.Example: Public sealed class Singleton { Private static readonly Singleton _instance = new Singleton(); }

### An object
An object is an instance of a class through which we access the methods of that class."New" keyword is used to create an object.A class that creates an object in memory will contain the information about the methods, variables, and behavior of that class.

## METHODS
### Can we use "this" command within a static method
We can't use 'This' in a static method because we can only use static variables/methods in a static method.

### Finalize() vs Dispose()
Dispose() is called when we want for an object to release any unmanaged resources with them.On the other hand, Finalize() is used for the same purpose, but it doesn't assure the garbage collection of an object.

### What happens if the inherited interfaces have conflicting method names
Implement is up to you as the method is inside your own class.There might be a problem when the methods from different interfaces expect different data, but as far as compiler cares you're okay.

## METHOD OVERLOADING AND OVERRIDING
### Can a private virtual method can be overridden
No, because they are not accessible outside the class.

### Method overloading
Method overloading is creating multiple methods with the same name with unique signatures in the same class.When we compile, the compiler uses overload resolution to determine the specific method to be invoke.

### Method overriding vs method overloading:
In method overriding, we change the method definition in the derived class that changes the method behavior.Method overloading is creating a method with the same name within the same class having different signatures.

### The different ways a method can be overloaded
Methods can be overloaded using different data types for a parameter, different order of parameters, and different number of parameters.

### Method overloading
Method overloading is creating multiple methods with the same name with unique signatures in the same class.When we compile, the compiler uses overload resolution to determine the specific method to be invoke.

### Can't you specify the accessibility modifier for methods inside the interface
In an interface, we have virtual methods that do not have method definition.All the methods are there to be overridden in the derived class.That's why they all are public.

## DATA: PARAMETERS, REFERENCES and VALUES
### Ref vs out parameters:
An argument passed as ref must be initialized before passing to the method whereas out parameter needs not to be initialized before passing to a method.

### The use of the using block
The 'using' block is used to obtain a resource and process it and then automatically dispose of when the execution of the block completed.

### Serialization
When we want to transport an object through a network, then we have to convert the object into a stream of bytes.The process of converting an object into a stream of bytes is called Serialization.For an object to be serializable, it should implement ISerialize Interface.De-serialization is the reverse process of creating an object from a stream of bytes.

### Constants vs readonly
Constant variables are declared and initialized at compile time.The value can't be changed afterward.Read-only is used only when we want to assign the value at run time.

### Custom Control and User Control
Custom Controls are controls generated as compiled code (Dlls), those are easier to use and can be added to toolbox.Developers can drag and drop controls to their web forms.Attributes can, at design time.We can easily add custom controls to Multiple Applications (If Shared Dlls).So, If they are private, then we can copy to dll to bin directory of web application and then add reference and can use them.User Controls are very much similar to ASP include files, and are easy to create.User controls can't be placed in the toolbox and dragged - dropped from it.They have their design and code-behind.The file extension for user controls is ascx.

### Circular references
Circular reference is situation in which two or more resources are interdependent on each other causes the lock condition and make the resources unusable.

## DATA: ARRAYS, QUEUES, STACKS
### Jagged Arrays
The Array which has elements of type array is called jagged Array.The elements can be of different dimensions and sizes.We can also call jagged Array as an Array of arrays.

### Array vs Arraylist:
In an array, we can have items of the same type only.The size of the array is fixed when compared.To an arraylist is similar to an array, but it doesn't have a fixed size.

### System.Array.CopyTo() vs System.Array.Clone():
Using Clone() method, we creates a new array object containing all the elements in the original Array and using CopyTo() method.All the elements of existing array copies into another existing array.Both methods perform a shallow copy.

### We sort the elements of the Array in descending order
Using Sort() methods followed by Reverse() method.

### How we can create an array with non-default values
We can create an array with non-default values using Enumerable.Repeat.

### Indexers
Indexers are known as smart arrays.It allows the instances of a class to be indexed in the same way as an array.Example: public int this[int index]    // This is an Indexer declaration

### Give an example of removing an element from the queue
The dequeue method is used to remove an element from the queue.The engueue method is used to add an element to the queue.

## DATA: STRINGS
### System.String vs System.Text.StringBuilder:


### System.String is immutable.
When we modify the value of a string variable, then a new memory is allocated to the new value and the previous memory allocation released.System.StringBuilder was designed to have a concept of a mutable string where a variety of operations can be performed without allocation separate memory location for the modified string.

## FLOW: EXCEPTIONS
### Can multiple catch blocks be executed
No, Multiple catch blocks of similar type can't be executed.Once the proper catch code executed, the control is transferred to the finally block, and then the code that follows the finally block gets executed.

### Write down the C# syntax to catch an exception
To catch an exception, we use try-catch blocks.Catch block can have a parameter of system.Exception type.

### Throw vs Throw ex
"Throw" statement preserves original error stack whereas "throw ex" have the stack trace from their throw point.It is always advised to use "throw" because it provides more accurate error information.

### List down the commonly used types of exceptions in .net
ArgumentException, ArgumentNullException , ArgumentOutOfRangeException, ArithmeticException, DivideByZeroException ,OverflowException , IndexOutOfRangeException ,InvalidCastException ,InvalidOperationException , IOEndOfStreamException , NullReferenceException , OutOfMemoryException , StackOverflowException etc.

### Custom Exceptions
Sometimes there are some errors that need to be handled as per user requirements.Custom exceptions are used for them and are used defined exceptions.

## FLOW TOPIC: EVENTS and DELEGATES
### A multicast delegate
A delegate having multiple handlers assigned to it is called multicast delegate.Each handler is assigned to a method.

### Delegates
Delegates are same are function pointers in C++, but the only difference is that they are type safe, unlike function pointers.Delegates are required because they can be used to write much more generic type-safe functions.

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

# C# - Best Qs
## SOLID
## C#
### C# Overview
Namespace:The namespace keyword is used to declare a scope.This helps organize code and lets you create globally-unique types.Namespaces are implicitly public and you cannot change this behavior.Declaration does not support modifiers or attributes.

### Constant vs Readonly
Constant:  No changes, anywhere. Static by defaultRead-only: Changed in the constructor. No post-instantiation changes.

### Value Types vs Reference Types
Value type - bool, byte, chat, decimal, double, enum , float, int, long, sbyte, short, strut, uint, ulong, ushortValue types are stored in the StackBY VAL: changes will not be reflected back to the variable.Reference type - class, delegate, interface, object, stringReference types are stored in the HeapBy REF: changes will be reflected back to that variable.( same as & symbol in c, c++)

### Boxing and Unboxing
Boxing   converts a value-type to a reference-type. The reference object is stored on the heap.Unboxing converts a reference-type to a value-type. The value is stored on the stack.Convert a value-type to a reference-type using Boxing.Convert a reference-type to a value-type using Unboxing.

## Object Oriented Programming. OO is based on AIEP.
### Object Oriented Programming. OO is based on AIEP. Overview
public:    class, variable, etc., can be accessed from anywhere in application. Public variables inside class can be accessed by outside of class.private:   class, variable, etc., can only be accessed by same class members. They cannot be accessed outside the class.protected: access specifier allows a child class to access the member variables and member functions of its base class

### Polymorphism
Polymorphism is changing the operation of a class or its components in OO programming.

## Class Types:
### Class Types: Overview
Class that cannot be instantiated.Cannot create an object of a Static Class.Static Class members can be called directly using their class name.Class Types: A P S S, are: Abstract, Partial, Sealed and Static.

## Access Modifiers
### Access Modifiers Overview
You can make a property read-only by only providing a get accessor. Create a private/internal set method separate from the property.

## Method Overloading and Overriding
## Interfaces
## Generics:
## Structs vs Classes:
### Structs: no modification, value-type variables, stack, no inheritance, faster.
Structs are used for:  data that will not be modified.Structs are:           value-type variables, saved on the stack or inline.Structs cannot:        inherit.Structs are used when: multiple accesses are required.Struct access is:      faster. Additional overhead. Faster retrieval.A new struct variable: is a completely new struct in memory.Struct changes thru one variable: are not reflected in another variable.Structs: no modification, value-type variables, stack, no inheritance, faster.Structs do not support inheritance, but they can implement interfaces.Structs cannot be declared as static.Structs can be instantiate without using A New Operator.Structs do not support inheritance.Structs cannot inherit from Another Struct Or Class.Structs cannot be a base class.Structs can inherit from an Interface.Structs derive from System.ValueType.Structs are Value Types.A struct is a value type mean when a struct is created, the variable to which the struct is assigned holds the struct's actual data.When the struct is assigned to a new variable, it is copied.

### Classes: Modification, reference-type variables, heap, inheritance, slower.
Classes are used for:  data that will be modified.Classes are:           reference-type variables, saved on the heap.Classes can:           inherit.Classes are used when: complex operations are required.Class  access is:      slower. because it is an indirect access. The class variable is a reference to the class data location.A new class  variable: is assigned and refers to the original object.Class  changes thru one variable: are reflected in another variable of the same instance.Classes: Modification, reference-type variables, heap, inheritance, slower.The new variable and the original variable therefore contain two separate copies of the same data.Changes made to one copy do not affect the other copy.

## Static Classes and Methods
## Abstract Class
### An Abstract Class
A class that cannot be instantiated.An abstract class is a class that must be inherited and have the methods overridden.An abstract class is essentially a blueprint for a class without any implementation.

### Create An Instance Of An Abstract Class
No, abstract classes are incomplete and you cannot create an instance of an abstract class.

### Abstract Methods
Abstract methods are methods that only the declaration of the method and no implementation.

### Abstract Classes


### Absolutely Have To Declare A Class As Abstract (as Opposed To Free-willed Educated Choice Or Decision Based On Uml Diagram)
When at least one of the methods in the class is abstract.When the class itself is inherited from an abstract class, but not all base abstract methods have been over-ridden.

### Create An Instance For An Abstract Class
No, you cannot create an instance for an abstract class.

### Absolutely Have To Declare A Class As Abstract
1. When the class itself is inherited from an abstract class, but not all base abstract methods have been overridden.2. When at least one of the methods in the class is abstract.

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

### The Datareader Class In ADO .NET Connections:
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

### Indexes: Array Out-of-bounds error:
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

## Design a DDD-oriented microservice
### Design a DDD-oriented microservice Overview
Sometimes these DDD technical rules and patterns are perceived as obstacles that have a steep learning curve for implementing DDD approaches. But the important part is not the patterns themselves, but organizing the code so it is aligned to the business problems, and using the same business terms (ubiquitous language). In addition, DDD approaches should be applied only if you are implementing complex microservices with significant business rules. Simpler responsibilities, like a CRUD service, can be managed with simpler approaches.Where to draw the boundaries is the key task when designing and defining a microservice. DDD patterns help you understand the complexity in the domain. For the domain model for each Bounded Context, you identify and define the entities, value objects, and aggregates that model your domain. You build and refine a domain model that is contained within a boundary that defines your context. And that is explicit in the form of a microservice. The components within those boundaries end up being your microservices, although in some cases a BC or business microservices can be composed of several physical services.

### Design a DDD-oriented microservice Overview (part 2)
DDD is about boundaries and so are microservices.Keep the microservice context boundaries relatively smallDetermining where to place boundaries between Bounded Contexts balances two competing goals. First, you want to initially create the smallest possible microservices, although that should not be the main driver; you should create a boundary around things that need cohesion. Second, you want to avoid chatty communications between microservices. These goals can contradict one another. You should balance them by decomposing the system into as many small microservices as you can until you see communication boundaries growing quickly with each additional attempt to separate a new Bounded Context. Cohesion is key within a single bounded context.It is similar to the Inappropriate Intimacy code smell when implementing classes. If two microservices need to collaborate a lot with each other, they should probably be the same microservice.Another way to look at this aspect is autonomy. If a microservice must rely on another service to directly service a request, it is not truly autonomous.

### Layers in DDD microservices
Most enterprise applications with significant business and technical complexity are defined by multiple layers. The layers are a logical artifact, and are not related to the deployment of the service. They exist to help developers manage the complexity in the code. Different layers (like the domain model layer versus the presentation layer, etc.) might have different types, which mandate translations between those types.For example, an entity could be loaded from the database. Then part of that information, or an aggregation of information including additional data from other entities, can be sent to the client UI through a REST Web API. The point here is that the domain entity is contained within the domain model layer and should not be propagated to other areas that it does not belong to, like to the presentation layer.Additionally, you need to have always-valid entities (see the Designing validations in the domain model layer section) controlled by aggregate roots (root entities).

### Layers in DDD microservices (continued)
Therefore, entities should not be bound to client views, because at the UI level some data might still not be validated. This reason is what the ViewModel is for. The ViewModel is a data model exclusively for presentation layer needs. The domain entities do not belong directly to the ViewModel.

### Layers in DDD microservices (part 2)
Instead, you need to translate between ViewModels and domain entities and vice versa.When tackling complexity, it is important to have a domain model controlled by aggregate roots that make sure that all the invariants and rules related to that group of entities (aggregate) are performed through a single entry-point or gate, the aggregate root.Figure 7-5 shows how a layered design is implemented in the eShopOnContainers application.Diagram showing the layers in a domain-driven design microservice.Figure 7-5: DDD layers in the ordering microservice in eShopOnContainersThe three layers in a DDD microservice like Ordering. Each layer is a VS project: Application layer is Ordering.API, Domain layer is Ordering.Domain and the Infrastructure layer is Ordering.Infrastructure. You want to design the system so that each layer communicates only with certain other layers.

### Layers in DDD microservices (part 2) (continued)
That approach may be easier to enforce if layers are implemented as different class libraries, because you can clearly identify what dependencies are set between libraries. For instance, the domain model layer should not take a dependency on any other layer (the domain model classes should be Plain Old CLR Objects, or POCO, classes).

### Layers in DDD microservices (part 3)
As shown in Figure 7-6, the Ordering.Domain layer library has dependencies only on the .NET libraries or NuGet packages, but not on any other custom library, such as data library or persistence library.Screenshot of Ordering.Domain dependencies.Figure 7-6: Layers implemented as libraries allow better control of dependencies between layers

### The domain model layer
Eric Evans's excellent book Domain Driven Design says the following about the domain model layer and the application layer.Domain Model Layer: Responsible for representing concepts of the business, information about the business situation, and business rules. State that reflects the business situation is controlled and used here, even though the technical details of storing it are delegated to the infrastructure. This layer is the heart of business software.The domain model layer is where the business is expressed. When you implement a microservice domain model layer in .NET, that layer is coded as a class library with the domain entities that capture data plus behavior (methods with logic).Following the Persistence Ignorance and the Infrastructure Ignorance principles, this layer must completely ignore data persistence details. These persistence tasks should be performed by the infrastructure layer.

### The domain model layer (continued)
Therefore, this layer should not take direct dependencies on the infrastructure, which means that an important rule is that your domain model entity classes should be POCOs.Domain entities should not have any direct dependency (like deriving from a base class) on any data access infrastructure framework like Entity Framework or NHibernate.

### The domain model layer (part 2)
Ideally, your domain entities should not derive from or implement any type defined in any infrastructure framework.Most modern ORM frameworks like Entity Framework Core allow this approach, so that your domain model classes are not coupled to the infrastructure. However, having POCO entities is not always possible when using certain NoSQL databases and frameworks, like Actors and Reliable Collections in Azure Service Fabric.Even when it is important to follow the Persistence Ignorance principle for your Domain model, you should not ignore persistence concerns. It is still important to understand the physical data model and how it maps to your entity object model. Otherwise you can create impossible designs.Also, this aspect does not mean you can take a model designed for a relational database and directly move it to a NoSQL or document-oriented database. In some entity models, the model might fit, but usually it does not. There are still constraints that your entity model must adhere to, based both on the storage technology and ORM technology.

### The application layer
Moving on to the application layer, we can again cite Eric Evans's book Domain Driven Design:Application Layer: Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems. The tasks this layer is responsible for are meaningful to the business or necessary for interaction with the application layers of other systems. This layer is kept thin. It does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down. It does not have state reflecting the business situation, but it can have state that reflects the progress of a task for the user or the program.A microservice's application layer in .NET is commonly coded as an ASP.NET Core Web API project. The project implements the microservice's interaction, remote network access, and the external Web APIs used from the UI or client apps. It includes queries if using a CQRS approach, commands accepted by the microservice, and even the event-driven communication between microservices (integration events).

### The application layer (part 2)
The ASP.NET Core Web API that represents the application layer must not contain business rules or domain knowledge (especially domain rules for transactions or updates); these should be owned by the domain model class library. The application layer must only coordinate tasks and must not hold or define any domain state (domain model). It delegates the execution of business rules to the domain model classes themselves (aggregate roots and domain entities), which will ultimately update the data within those domain entities.Basically, the application logic is where you implement all use cases that depend on a given front end. For example, the implementation related to a Web API service.The goal is that the domain logic in the domain model layer, its invariants, the data model, and related business rules must be completely independent from the presentation and application layers. Most of all, the domain model layer must not directly depend on any infrastructure framework.

### The infrastructure layer
The infrastructure layer is how the data that is initially held in domain entities (in memory) is persisted in databases or another persistent store. An example is using Entity Framework Core code to implement the Repository pattern classes that use a DBContext to persist data in a relational database.In accordance with the previously mentioned Persistence Ignorance and Infrastructure Ignorance principles, the infrastructure layer must not "contaminate" the domain model layer. You must keep the domain model entity classes agnostic from the infrastructure that you use to persist data (EF or any other framework) by not taking hard dependencies on frameworks.

### The infrastructure layer (part 2)
Your domain model layer class library should have only your domain code, just POCO entity classes implementing the heart of your software and completely decoupled from infrastructure technologies.Thus, your layers or class libraries and projects should ultimately depend on your domain model layer (library), not vice versa, as shown in Figure 7-7.Diagram showing dependencies that exist between DDD service layers.Figure 7-7: Dependencies between layers in DDDDependencies in a DDD Service, the Application layer depends on Domain and Infrastructure, and Infrastructure depends on Domain, but Domain doesn't depend on any layer. This layer design should be independent for each microservice. As noted earlier, you can implement the most complex microservices following DDD patterns, while implementing simpler data-driven microservices (simple CRUD in a single layer) in a simpler way.

## Design a microservice domain model
### The Domain Entity pattern
Entities represent domain objects and are primarily defined by their identity, continuity, and persistence over time, and not only by the attributes that comprise them. As Eric Evans says, "an object primarily defined by its identity is called an Entity." Entities are very important in the domain model, since they are the base for a model. Therefore, you should identify and design them carefully.An entity's identity can cross multiple microservices or Bounded Contexts.The same identity (that is, the same Id value, although perhaps not the same domain entity) can be modeled across multiple Bounded Contexts or microservices. However, that does not imply that the same entity, with the same attributes and logic would be implemented in multiple Bounded Contexts.

### The Domain Entity pattern (continued)
Instead, entities in each Bounded Context limit their attributes and behaviors to those required in that Bounded Context's domain.For instance, the buyer entity might have most of a person's attributes that are defined in the user entity in the profile or identity microservice, including the identity. But the buyer entity in the ordering microservice might have fewer attributes, because only certain buyer data is related to the order process.

### The Domain Entity pattern (part 2)
The context of each microservice or Bounded Context impacts its domain model.Domain entities must implement behavior in addition to implementing data attributes.A domain entity in DDD must implement the domain logic or behavior related to the entity data (the object accessed in memory). For example, as part of an order entity class you must have business logic and operations implemented as methods for tasks such as adding an order item, data validation, and total calculation. The entity's methods take care of the invariants and rules of the entity instead of having those rules spread across the application layer.Figure 7-8 shows a domain entity that implements not only data attributes but operations or methods with related domain logic.Diagram showing a Domain Entity's pattern.Figure 7-8: Example of a domain entity design implementing data plus behaviorA domain model entity implements behaviors through methods, that is, it's not an "anemic" model.

### The Domain Entity pattern (part 2) (continued)
Of course, sometimes you can have entities that do not implement any logic as part of the entity class. This can happen in child entities within an aggregate if the child entity does not have any special logic because most of the logic is defined in the aggregate root.

### The Domain Entity pattern (part 3)
If you have a complex microservice that has logic implemented in the service classes instead of in the domain entities, you could be falling into the anemic domain model, explained in the following section.

### Rich domain model versus anemic domain model
In his post AnemicDomainModel, Martin Fowler describes an anemic domain model this way:The basic symptom of an Anemic Domain Model is that at first blush it looks like the real thing. There are objects, many named after the nouns in the domain space, and these objects are connected with the rich relationships and structure that true domain models have. The catch comes when you look at the behavior, and you realize that there is hardly any behavior on these objects, making them little more than bags of getters and setters.Of course, when you use an anemic domain model, those data models will be used from a set of service objects (traditionally named the business layer) which capture all the domain or business logic. The business layer sits on top of the data model and uses the data model just as data.The anemic domain model is just a procedural style design. Anemic entity objects are not real objects because they lack behavior (methods). They only hold data properties and thus it is not object-oriented design.

### Rich domain model versus anemic domain model (part 2)
By putting all the behavior out into service objects (the business layer), you essentially end up with spaghetti code or transaction scripts, and therefore you lose the advantages that a domain model provides.Regardless, if your microservice or Bounded Context is very simple (a CRUD service), the anemic domain model in the form of entity objects with just data properties might be good enough, and it might not be worth implementing more complex DDD patterns. In that case, it will be simply a persistence model, because you have intentionally created an entity with only data for CRUD purposes.That is why microservices architectures are perfect for a multi-architectural approach depending on each Bounded Context. For instance, in eShopOnContainers, the ordering microservice implements DDD patterns, but the catalog microservice, which is a simple CRUD service, does not.Some people say that the anemic domain model is an anti-pattern. It really depends on what you are implementing. If the microservice you are creating is simple enough (for example, a CRUD service), following the anemic domain model it is not an anti-pattern.

### Rich domain model versus anemic domain model (part 3)
However, if you need to tackle the complexity of a microservice's domain that has a lot of ever-changing business rules, the anemic domain model might be an anti-pattern for that microservice or Bounded Context. In that case, designing it as a rich model with entities containing data plus behavior as well as implementing additional DDD patterns (aggregates, value objects, etc.) might have huge benefits for the long-term success of such a microservice.

### The Value Object pattern
As Eric Evans has noted, "Many objects do not have conceptual identity. These objects describe certain characteristics of a thing."An entity requires an identity, but there are many objects in a system that do not, like the Value Object pattern. A value object is an object with no conceptual identity that describes a domain aspect. These are objects that you instantiate to represent design elements that only concern you temporarily. You care about what they are, not who they are. Examples include numbers and strings, but can also be higher-level concepts like groups of attributes.Something that is an entity in a microservice might not be an entity in another microservice, because in the second case, the Bounded Context might have a different meaning. For example, an address in an e-commerce application might not have an identity at all, since it might only represent a group of attributes of the customer's profile for a person or company.

### The Value Object pattern (continued)
In this case, the address should be classified as a value object. However, in an application for an electric power utility company, the customer address could be important for the business domain. Therefore, the address must have an identity so the billing system can be directly linked to the address.

### The Value Object pattern (part 2)
In that case, an address should be classified as a domain entity.A person with a name and surname is usually an entity because a person has identity, even if the name and surname coincide with another set of values, such as if those names also refer to a different person.Value objects are hard to manage in relational databases and ORMs like Entity Framework (EF), whereas in document-oriented databases they are easier to implement and use.EF Core 2.0 and later versions include the Owned Entities feature that makes it easier to handle value objects, as we'll see in detail later on.

### The Aggregate pattern
A domain model contains clusters of different data entities and processes that can control a significant area of functionality, such as order fulfillment or inventory. A more fine-grained DDD unit is the aggregate, which describes a cluster or group of entities and behaviors that can be treated as a cohesive unit.You usually define an aggregate based on the transactions that you need. A classic example is an order that also contains a list of order items. An order item will usually be an entity. But it will be a child entity within the order aggregate, which will also contain the order entity as its root entity, typically called an aggregate root.Identifying aggregates can be hard. An aggregate is a group of objects that must be consistent together, but you cannot just pick a group of objects and label them an aggregate. You must start with a domain concept and think about the entities that are used in the most common transactions related to that concept. Those entities that need to be transactionally consistent are what forms an aggregate. Thinking about transaction operations is probably the best way to identify aggregates.

### The Aggregate Root or Root Entity pattern
An aggregate is composed of at least one entity: the aggregate root, also called root entity or primary entity. Additionally, it can have multiple child entities and value objects, with all entities and objects working together to implement required behavior and transactions.The purpose of an aggregate root is to ensure the consistency of the aggregate; it should be the only entry point for updates to the aggregate through methods or operations in the aggregate root class. You should make changes to entities within the aggregate only via the aggregate root. It is the aggregate's consistency guardian, considering all the invariants and consistency rules you might need to comply with in your aggregate. If you change a child entity or value object independently, the aggregate root cannot ensure that the aggregate is in a valid state. It would be like a table with a loose leg. Maintaining consistency is the main purpose of the aggregate root.In Figure 7-9, you can see sample aggregates like the buyer aggregate, which contains a single entity (the aggregate root Buyer).

### The Aggregate Root or Root Entity pattern (part 2)
The order aggregate contains multiple entities and a value object.Diagram comparing a buyer aggregate and an order aggregate.Figure 7-9: Example of aggregates with multiple or single entitiesA DDD domain model is composed from aggregates, an aggregate can have just one entity or more, and can include value objects as well. Note that the Buyer aggregate could have additional child entities, depending on your domain, as it does in the ordering microservice in the eShopOnContainers reference application. Figure 7-9 just illustrates a case in which the buyer has a single entity, as an example of an aggregate that contains only an aggregate root.In order to maintain separation of aggregates and keep clear boundaries between them, it is a good practice in a DDD domain model to disallow direct navigation between aggregates and only having the foreign key (FK) field, as implemented in the Ordering microservice domain model in eShopOnContainers. The Order entity only has a foreign key field for the buyer, but not an EF Core navigation property.

## Implement a microservice domain model with .NET
### Domain model structure in a custom .NET Standard Library
The folder organization used for the eShopOnContainers reference application demonstrates the DDD model for the application.You might find that a different folder organization more clearly communicates the design choices made for your application.As you can see in Figure 7-10, in the ordering domain model there are two aggregates, the order aggregate and the buyer aggregate.Each aggregate is a group of domain entities and value objects, although you could have an aggregate composed of a single domain entity (the aggregate root or root entity) as well.Screenshot of the Ordering.Domain project in Solution Explorer.The Solution Explorer view for the Ordering.Domain project, showing the AggregatesModel folder containing the BuyerAggregate and OrderAggregate folders, each one containing its entity classes, value object files and so on.Figure 7-10: Domain model structure for the ordering microservice in eShopOnContainersAdditionally, the domain model layer includes the repository contracts (interfaces) that are the infrastructure requirements of your domain model.In other words, these interfaces express what repositories and the methods the infrastructure layer must implement.It is critical that the implementation of the repositories be placed outside of the domain model layer, in the infrastructure layer library, so the domain model layer is not "contaminated" by API or classes from infrastructure technologies, like Entity Framework.You can also see a SeedWork folder that contains custom base classes that you can use as a base for your domain entities and value objects, so you do not have redundant code in each domain's object class.

### Domain model structure in a custom .NET Standard Library (part 2)


### Structure aggregates in a custom .NET Standard library
An aggregate refers to a cluster of domain objects grouped together to match transactional consistency.Those objects could be instances of entities (one of which is the aggregate root or root entity) plus any additional value objects.Transactional consistency means that an aggregate is guaranteed to be consistent and up to date at the end of a business action.For example, the order aggregate from the eShopOnContainers ordering microservice domain model is composed as shown in Figure 7-11.Screenshot of the OrderAggregate folder and its classes.A detailed view of the OrderAggregate folder: Address.cs is a value object, IOrderRepository is a repo interface, Order.cs is an aggregate root, OrderItem.cs is a child entity, and OrderStatus.cs is an enumeration class.Figure 7-11: The order aggregate in Visual Studio solutionIf you open any of the files in an aggregate folder, you can see how it is marked as either a custom base class or interface, like entity or value object, as implemented in the SeedWork folder.

### Implement domain entities as POCO classes
You implement a domain model in .NET by creating POCO classes that implement your domain entities.In the following example, the Order class is defined as an entity and also as an aggregate root.Because the Order class derives from the Entity base class, it can reuse common code related to entities.Bear in mind that these base classes and interfaces are defined by you in the domain model project, so it is your code, not infrastructure code from an ORM like EF.It is important to note that this is a domain entity implemented as a POCO class.It does not have any direct dependency on Entity Framework Core or any other infrastructure framework.This implementation is as it should be in DDD, just C# code implementing a domain model.In addition, the class is decorated with an interface named IAggregateRoot.That interface is an empty interface, sometimes called a marker interface, that is used just to indicate that this entity class is also an aggregate root.A marker interface is sometimes considered as an anti-pattern; however, it is also a clean way to mark a class, especially when that interface might be evolving.An attribute could be the other choice for the marker, but it is quicker to see the base class (Entity) next to the IAggregate interface instead of putting an Aggregate attribute marker above the class.It is a matter of preferences, in any case.Having an aggregate root means that most of the code related to consistency and business rules of the aggregate's entities should be implemented as methods in the Order aggregate root class (for example, AddOrderItem when adding an OrderItem object to the aggregate).You should not create or update OrderItems objects independently or directly; the AggregateRoot class must keep control and consistency of any update operation against its child entities.

### Implement domain entities as POCO classes (part 2)


### Encapsulate Data in Domain Entities (Part 1)
A common problem in entity models is that they expose collection navigation properties as publicly accessible list types.This allows any collaborator developer to manipulate the contents of these collection types, which may bypass important business rules related to the collection, possibly leaving the object in an invalid state.The solution to this is to expose read-only access to related collections and explicitly provide methods that define ways in which clients can manipulate them.In the previous code, note that many attributes are read-only or private and are only updatable by the class methods, so any update considers business domain invariants and logic specified within the class methods.For example, following DDD patterns, you should not do the following from any command handler method or application layer class (actually, it should be impossible for you to do so):WRONG ACCORDING TO DDD PATTERNS -- CODE AT THE APPLICATION LAYER OR COMMAND HANDLERSCode in command handler methods or Web API controllersWRONG: Some code with business logic out of the domain classes ...OrderItem myNewOrderItem = new OrderItem(orderId, productId, productName, pictureUrl, unitPrice, discount, units);WRONG: Accessing the OrderItems collection directly from the application layer // or command handlersmyOrder.OrderItems.Add(myNewOrderItem);In this case, the Add method is purely an operation to ad

### Encapsulate Data in Domain Entities (Part 2)
d data, with direct access to the OrderItems collection.Therefore, most of the domain logic, rules, or validations related to that operation with the child entities will be spread across the application layer (command handlers and Web API controllers).If you go around the aggregate root, the aggregate root cannot guarantee its invariants, its validity, or its consistency.Eventually you will have spaghetti code or transactional script code.To follow DDD patterns, entities must not have public setters in any entity property.Changes in an entity should be driven by explicit methods with explicit ubiquitous language about the change they are performing in the entity.Furthermore, collections within the entity (like the order items) should be read-only properties (the AsReadOnly method explained later).You should be able to update it only from within the aggregate root class methods or the child entity methods.As you can see in the code for the Order aggregate root, all setters should be private or at least read-only externally, so that any operation against the entity's data or its child entities has to be performed through methods in the entity class.This maintains consistency in a controlled and object-oriented way instead of implementing transactional script code.The following code snippet shows the proper way to code the task of adding an OrderItem object to the Order aggregate.RIGHT ACCORDING TO DDD - CODE AT THE APPLICATION LAYER OR COMMAND HANDLERSThe code in command handlers or WebAPI controllers, related only to application stuff.There is NO code here related to OrderItem object's business logic.myOrder.AddOrderItem(productId, productName, pictureUrl, unitPrice, discount, units);The code related to OrderItem params validations or domain rules should be WITHIN the AddOrderItem method.In this snippet, most of the validations or logic related to the creation of an OrderItem object will be under the control of the Order aggregate root, in the AddOrderItem method, especially validations and logic related to other elements in the aggregate.For instance, you might get the same product item as the result of multiple calls to AddOrderItem.In that method, you could examine the product items and consolidate the same product items into a single OrderItem object with several units.Additionally, if there are different discount amounts but the product ID is the same, you would likely apply the higher discount.This principle applies to any other domain logic for the OrderItem object.In addition, the new OrderItem(params) operation will also be controlled and performed by the AddOrderItem method from the Order aggregate root.Therefore, most of the logic or validations related to that operation (especially anything that impacts the consistency between other child entities) will be in a single place within the aggregate root.That is the ultimate purpose of the aggregate root pattern.When you use Entity Framework Core 1.1 or later, a DDD entity can be better expressed because it allows mapping to fields in addition to properties.This is useful when protecting collections of child entities or value objects.With this enhancement, you can use simple private fields instead of properties and you can implement any update to the field collection in public methods and provide read-only access through the AsReadOnly method.In DDD, you want to update the entity only through methods in the entity (or the constructor) in order to control any invariant and the consistency of the data, so properties are defined only with a get accessor.The properties are backed by private fields.Private members can only be accessed from within the class.However, there is one exception: EF Core needs to set these fields as well (so it can return the object with the proper values).


### Encapsulate data in the Domain Entities (part 2)


### Map properties with only get accessors to the fields in the database table
Mapping properties to database table columns is not a domain responsibility but part of the infrastructure and persistence layer.We mention this here just so you are aware of the new capabilities in EF Core 1.1 or later related to how you can model entities.Additional details on this topic are explained in the infrastructure and persistence section.When you use EF Core 1.0 or later, within the DbContext you need to map the properties that are defined only with getters to the actual fields in the database table.This is done with the HasField method of the PropertyBuilder class.

### Map fields without properties
With the feature in EF Core 1.1 or later to map columns to fields, it is also possible to not use properties.Instead, you can just map columns from a table to fields.A common use case for this is private fields for an internal state that does not need to be accessed from outside the entity.For example, in the preceding OrderAggregate code example, there are several private fields, like the _paymentMethodId field, that have no related property for either a setter or getter.That field could also be calculated within the order's business logic and used from the order's methods, but it needs to be persisted in the database as well.So in EF Core (since v1.1) there is a way to map a field without a related property to a column in the database.This is also explained in the Infrastructure layer section of this guide.

## AnemicDomainModel
### AnemicDomainModel Overview
The basic symptom of an Anemic Domain Model is that at first blush it looks like the real thing. There are objects, many named after the nouns in the domain space, and these objects are connected with the rich relationships and structure that true domain models have. The catch comes when you look at the behavior, and you realize that there is hardly any behavior on these objects, making them little more than bags of getters and setters. Indeed often these models come with design rules that say that you are not to put any domain logic in the the domain objects. Instead there are a set of service objects which capture all the domain logic, carrying out all the computation and updating the model objects with the results. These services live on top of the domain model and use the domain model for data.The fundamental horror of this anti-pattern is that it's so contrary to the basic idea of object-oriented design; which is to combine data and process together. The anemic domain model is really just a procedural style design, exactly the kind of thing that object bigots like me (and Eric) have been fighting since our early days in Smalltalk.

### AnemicDomainModel Overview (part 2)
What's worse, many people think that anemic objects are real objects, and thus completely miss the point of what object-oriented design is all about.Now object-oriented purism is all very well, but I realize that I need more fundamental arguments against this anemia. In essence the problem with anemic domain models is that they incur all of the costs of a domain model, without yielding any of the benefits. The primary cost is the awkwardness of mapping to a database, which typically results in a whole layer of O/R mapping. This is worthwhile iff you use the powerful OO techniques to organize complex logic. By pulling all the behavior out into services, however, you essentially end up with Transaction Scripts, and thus lose the advantages that the domain model can bring.

### AnemicDomainModel Overview (part 2) (continued)
As I discussed in P of EAA, Domain Models aren't always the best tool.It's also worth emphasizing that putting behavior into the domain objects should not contradict the solid approach of using layering to separate domain logic from such things as persistence and presentation responsibilities. The logic that should be in a domain object is domain logic - validations, calculations, business rules - whatever you like to call it.

### AnemicDomainModel Overview (part 3)
(There are cases when you make an argument for putting data source or presentation logic in a domain object, but that's orthogonal to my view of anemia.)One source of confusion in all this is that many OO experts do recommend putting a layer of procedural services on top of a domain model, to form a Service Layer. But this isn't an argument to make the domain model void of behavior, indeed service layer advocates use a service layer in conjunction with a behaviorally rich domain model.Eric Evans's excellent book Domain Driven Design has the following to say about these layers.Application Layer [his name for Service Layer]: Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems. The tasks this layer is responsible for are meaningful to the business or necessary for interaction with the application layers of other systems. This layer is kept thin. It does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down.

### AnemicDomainModel Overview (part 4)
It does not have state reflecting the business situation, but it can have state that reflects the progress of a task for the user or the program.Domain Layer (or Model Layer): Responsible for representing concepts of the business, information about the business situation, and business rules. State that reflects the business situation is controlled and used here, even though the technical details of storing it are delegated to the infrastructure. This layer is the heart of business software.The key point here is that the Service Layer is thin - all the key logic lies in the domain layer. He reiterates this point in his service pattern:Now, the more common mistake is to give up too easily on fitting the behavior into an appropriate object, gradually slipping toward procedural programming.I don't know why this anti-pattern is so common. I suspect it's due to many people who haven't really worked with a proper domain model, particularly if they come from a data background.

### AnemicDomainModel Overview (part 4) (continued)
Some technologies encourage it; such as J2EE's Entity Beans which is one of the reasons I prefer POJO domain models, Plain Old Java Object.In general, the more behavior you find in the services, the more likely you are to be robbing yourself of the benefits of a domain model.

### AnemicDomainModel Overview (part 5)
If all your logic is in services, you've robbed yourself blind.

## Domain events: design and implementation
### ### What is a domain event
An event is something that has happened in the past. A domain event is, something that happened in the domain that you want other parts of the same domain (in-process) to be aware of. The notified parts usually react somehow to the events.An important benefit of domain events is that side effects can be expressed explicitly.For example, if you're just using Entity Framework and there has to be a reaction to some event, you would probably code whatever you need close to what triggers the event. So the rule gets coupled, implicitly, to the code, and you have to look into the code to, hopefully, realize the rule is implemented there.On the other hand, using domain events makes the concept explicit, because there is a DomainEvent and at least one DomainEventHandler involved.For example, in the eShopOnContainers application, when an order is created, the user becomes a buyer, so an OrderStartedDomainEvent is raised and handled in the ValidateOrAddBuyerAggregateWhenOrderStartedDomainEventHandler, so the underlying concept is evident.In short, domain events help you to express, explicitly, the domain rules, based in the ubiquitous language provided by the domain experts.

### What is a domain event (part 2)
Domain events also enable a better separation of concerns among classes within the same domain.It's important to ensure that, just like a database transaction, either all the operations related to a domain event finish successfully or none of them do.Domain events are similar to messaging-style events, with one important difference. With real messaging, message queuing, message brokers, or a service bus using AMQP, a message is always sent asynchronously and communicated across processes and machines. This is useful for integrating multiple Bounded Contexts, microservices, or even different applications. However, with domain events, you want to raise an event from the domain operation you are currently running, but you want any side effects to occur within the same domain.The domain events and their side effects (the actions triggered afterwards that are managed by event handlers) should occur almost immediately, usually in-process, and within the same domain. Thus, domain events could be synchronous or asynchronous. Integration events, however, should always be asynchronous.

### Domain events versus integration events
Semantically, domain and integration events are the same thing: notifications about something that just happened. However, their implementation must be different. Domain events are just messages pushed to a domain event dispatcher, which could be implemented as an in-memory mediator based on an IoC container or any other method.On the other hand, the purpose of integration events is to propagate committed transactions and updates to additional subsystems, whether they are other microservices, Bounded Contexts or even external applications. Hence, they should occur only if the entity is successfully persisted, otherwise it's as if the entire operation never happened.As mentioned before, integration events must be based on asynchronous communication between multiple microservices (other Bounded Contexts) or even external systems/applications.Thus, the event bus interface needs some infrastructure that allows inter-process and distributed communication between potentially remote services. It can be based on a commercial service bus, queues, a shared database used as a mailbox, or any other distributed and ideally push based messaging system.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain
If executing a command related to one aggregate instance requires additional domain rules to be run on one or more additional aggregates, you should design and implement those side effects to be triggered by domain events. As shown in Figure 7-14, and as one of the most important use cases, a domain event should be used to propagate state changes across multiple aggregates within the same domain model.Diagram showing a domain event controlling data to a Buyer aggregate.Figure 7-14. Domain events to enforce consistency between multiple aggregates within the same domainFigure 7-14 shows how consistency between aggregates is achieved by domain events. When the user initiates an order, the Order Aggregate sends an OrderStarted domain event.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (continued)
The OrderStarted domain event is handled by the Buyer Aggregate to create a Buyer object in the ordering microservice, based on the original user info from the identity microservice (with information provided in the CreateOrder command).Alternately, you can have the aggregate root subscribed for events raised by members of its aggregates (child entities). For instance, each OrderItem child entity can raise an event when the item price is higher than a specific amount, or when the product item amount is too high.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (part 2)
The aggregate root can then receive those events and perform a global calculation or aggregation.It is important to understand that this event-based communication is not implemented directly within the aggregates; you need to implement domain event handlers.Handling the domain events is an application concern. The domain model layer should only focus on the domain logic--things that a domain expert would understand, not application infrastructure like handlers and side-effect persistence actions using repositories. Therefore, the application layer level is where you should have domain event handlers triggering actions when a domain event is raised.Domain events can also be used to trigger any number of application actions, and what is more important, must be open to increase that number in the future in a decoupled way. For instance, when the order is started, you might want to publish a domain event to propagate that info to other aggregates or even to raise application actions like notifications.The key point is the open number of actions to be executed when a domain event occurs. Eventually, the actions and rules in the domain and application will grow.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (part 3)
The complexity or number of side-effect actions when something happens will grow, but if your code were coupled with "glue" (that is, creating specific objects with new), then every time you needed to add a new action you would also need to change working and tested code.This change could result in new bugs and this approach also goes against the Open/Closed principle from SOLID. Not only that, the original class that was orchestrating the operations would grow and grow, which goes against the Single Responsibility Principle (SRP).On the other hand, if you use domain events, you can create a fine-grained and decoupled implementation by segregating responsibilities using this approach:Send a command (for example, CreateOrder).Receive the command in a command handler.Execute a single aggregate's transaction.(Optional) Raise domain events for side effects (for example, OrderStartedDomainEvent).Handle domain events (within the current process) that will execute an open number of side effects in multiple aggregates or application actions.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (part 4)
For example:Verify or create buyer and payment method.Create and send a related integration event to the event bus to propagate states across microservices or trigger external actions like sending an email to the buyer.Handle other side effects.As shown in Figure 7-15, starting from the same domain event, you can handle multiple actions related to other aggregates in the domain or additional application actions you need to perform across microservices connecting with integration events and the event bus.Diagram showing a domain event passing data to several event handlers.Figure 7-15. Handling multiple actions per domainThere can be several handlers for the same domain event in the Application Layer, one handler can solve consistency between aggregates and another handler can publish an integration event, so other microservices can do something with it.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (part 4) (continued)
The event handlers are typically in the application layer, because you will use infrastructure objects like repositories or an application API for the microservice's behavior. In that sense, event handlers are similar to command handlers, so both are part of the application layer. The important difference is that a command should be processed only once.

### Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain (part 5)
A domain event could be processed zero or n times, because it can be received by multiple receivers or event handlers with a different purpose for each handler.Having an open number of handlers per domain event allows you to add as many domain rules as needed, without affecting current code. For instance, implementing the following business rule might be as easy as adding a few event handlers (or even just one):When the total amount purchased by a customer in the store, across any number of orders, exceeds $6,000, apply a 10% off discount to every new order and notify the customer with an email about that discount for future orders.

### Implement domain events
In C#, a domain event is simply a data-holding structure or class, like a DTO, with all the information related to what just happened in the domain, as shown in the following example:This is essentially a class that holds all the data related to the OrderStarted event.In terms of the ubiquitous language of the domain, since an event is something that happened in the past, the class name of the event should be represented as a past-tense verb, like OrderStartedDomainEvent or OrderShippedDomainEvent. That's how the domain event is implemented in the ordering microservice in eShopOnContainers.As noted earlier, an important characteristic of events is that since an event is something that happened in the past, it should not change. Therefore, it must be an immutable class. You can see in the previous code that the properties are read-only.

### Implement domain events (continued)
There's no way to update the object, you can only set values when you create it.It's important to highlight here that if domain events were to be handled asynchronously, using a queue that required serializing and deserializing the event objects, the properties would have to be "private set" instead of read-only, so the deserializer would be able to assign the values upon dequeuing. This is not an issue in the Ordering microservice, as the domain event pub/sub is implemented synchronously using MediatR.

### Raise domain events
The next question is how to raise a domain event so it reaches its related event handlers. You can use multiple approaches.Udi Dahan originally proposed (for example, in several related posts, such as Domain Events - Take 2) using a static class for managing and raising the events. This might include a static class named DomainEvents that would raise domain events immediately when it is called, using syntax like DomainEvents.Raise(Event myEvent). Jimmy Bogard wrote a blog post (Strengthening your domain: Domain Events) that recommends a similar approach.However, when the domain events class is static, it also dispatches to handlers immediately. This makes testing and debugging more difficult, because the event handlers with side-effects logic are executed immediately after the event is raised. When you are testing and debugging, you just want to focus on what is happening in the current aggregate classes; you do not want to suddenly be redirected to other event handlers for side effects related to other aggregates or application logic. This is why other approaches have evolved, as explained in the next section.

### The deferred approach to raise and dispatch events
Instead of dispatching to a domain event handler immediately, a better approach is to add the domain events to a collection and then to dispatch those domain events right before or right after committing the transaction (as with SaveChanges in EF). (This approach was described by Jimmy Bogard in this post A better domain events pattern.)Deciding if you send the domain events right before or right after committing the transaction is important, since it determines whether you will include the side effects as part of the same transaction or in different transactions. In the latter case, you need to deal with eventual consistency across multiple aggregates. This topic is discussed in the next section.The deferred approach is what eShopOnContainers uses. First, you add the events happening in your entities into a collection or list of events per entity.

### The deferred approach to raise and dispatch events (part 2)
That list should be part of the entity object, or even better, part of your base entity class, as shown in the following example of the Entity base class:When you want to raise an event, you just add it to the event collection from code at any method of the aggregate-root entity.The following code, part of the Order aggregate-root at eShopOnContainers, shows an example:Notice that the only thing that the AddDomainEvent method is doing is adding an event to the list. No event is dispatched yet, and no event handler is invoked yet.You actually want to dispatch the events later on, when you commit the transaction to the database. If you are using Entity Framework Core, that means in the SaveChanges method of your EF DbContext, as in the following code:With this code, you dispatch the entity events to their respective event handlers.The overall result is that you have decoupled the raising of a domain event (a simple add into a list in memory) from dispatching it to an event handler. In addition, depending on what kind of dispatcher you are using, you could dispatch the events synchronously or asynchronously.Be aware that transactional boundaries come into significant play here.

### The deferred approach to raise and dispatch events (part 3)
If your unit of work and transaction can span more than one aggregate (as when using EF Core and a relational database), this can work well. But if the transaction cannot span aggregates, such as when you are using a NoSQL database like Azure CosmosDB, you have to implement additional steps to achieve consistency. This is another reason why persistence ignorance is not universal; it depends on the storage system you use.

### Single transaction across aggregates versus eventual consistency across aggregates
The question of whether to perform a single transaction across aggregates versus relying on eventual consistency across those aggregates is a controversial one. Many DDD authors like Eric Evans and Vaughn Vernon advocate the rule that one transaction = one aggregate and therefore argue for eventual consistency across aggregates. For example, in his book Domain-Driven Design, Eric Evans says this:Any rule that spans Aggregates will not be expected to be up-to-date at all times. Through event processing, batch processing, or other update mechanisms, other dependencies can be resolved within some specific time. (page 128)Vaughn Vernon says the following in Effective Aggregate Design. Part II: Making Aggregates Work Together:Thus, if executing a command on one aggregate instance requires that additional business rules execute on one or more aggregates, use eventual consistency [...] There is a practical way to support eventual consistency in a DDD model. An aggregate method publishes a domain event that is in time delivered to one or more asynchronous subscribers.This rationale is based on embracing fine-grained transactions instead of transactions spanning many aggregates or entities.

### Single transaction across aggregates versus eventual consistency across aggregates (part 2)
The idea is that in the second case, the number of database locks will be substantial in large-scale applications with high scalability needs. Embracing the fact that highly scalable applications need not have instant transactional consistency between multiple aggregates helps with accepting the concept of eventual consistency. Atomic changes are often not needed by the business, and it is in any case the responsibility of the domain experts to say whether particular operations need atomic transactions or not. If an operation always needs an atomic transaction between multiple aggregates, you might ask whether your aggregate should be larger or was not correctly designed.However, other developers and architects like Jimmy Bogard are okay with spanning a single transaction across several aggregates--but only when those additional aggregates are related to side effects for the same original command.

### Single transaction across aggregates versus eventual consistency across aggregates (part 3)
For instance, in A better domain events pattern, Bogard says this:Typically, I want the side effects of a domain event to occur within the same logical transaction, but not necessarily in the same scope of raising the domain event [...] Just before we commit our transaction, we dispatch our events to their respective handlers.If you dispatch the domain events right before committing the original transaction, it is because you want the side effects of those events to be included in the same transaction. For example, if the EF DbContext SaveChanges method fails, the transaction will roll back all changes, including the result of any side effect operations implemented by the related domain event handlers. This is because the DbContext life scope is by default defined as "scoped." Therefore, the DbContext object is shared across multiple repository objects being instantiated within the same scope or object graph. This coincides with the HttpRequest scope when developing Web API or MVC apps.Actually, both approaches (single atomic transaction and eventual consistency) can be right. It really depends on your domain or business requirements and what the domain experts tell you.

### Single transaction across aggregates versus eventual consistency across aggregates (part 4)
It also depends on how scalable you need the service to be (more granular transactions have less impact with regard to database locks). And it depends on how much investment you are willing to make in your code, since eventual consistency requires more complex code in order to detect possible inconsistencies across aggregates and the need to implement compensatory actions. Consider that if you commit changes to the original aggregate and afterwards, when the events are being dispatched, if there is an issue and the event handlers cannot commit their side effects, you will have inconsistencies between aggregates.A way to allow compensatory actions would be to store the domain events in additional database tables so they can be part of the original transaction. Afterwards, you could have a batch process that detects inconsistencies and runs compensatory actions by comparing the list of events with the current state of the aggregates. The compensatory actions are part of a complex topic that will require deep analysis from your side, which includes discussing it with the business user and domain experts.In any case, you can choose the approach you need.

### Single transaction across aggregates versus eventual consistency across aggregates (part 5)
But the initial deferred approach--raising the events before committing, so you use a single transaction--is the simplest approach when using EF Core and a relational database. It is easier to implement and valid in many business cases. It is also the approach used in the ordering microservice in eShopOnContainers.But how do you actually dispatch those events to their respective event handlers? What's the _mediator object you see in the previous example? It has to do with the techniques and artifacts you use to map between events and their event handlers.

### The domain event dispatcher: mapping from events to event handlers
Once you're able to dispatch or publish the events, you need some kind of artifact that will publish the event, so that every related handler can get it and process side effects based on that event.One approach is a real messaging system or even an event bus, possibly based on a service bus as opposed to in-memory events. However, for the first case, real messaging would be overkill for processing domain events, since you just need to process those events within the same process (that is, within the same domain and application layer).Another way to map events to multiple event handlers is by using types registration in an IoC container so you can dynamically infer where to dispatch the events. In other words, you need to know what event handlers need to get a specific event. Figure 7-16 shows a simplified approach for this approach.Diagram showing a domain event dispatcher sending events to the appropriate handlers.Figure 7-16. Domain event dispatcher using IoCYou can build all the plumbing and artifacts to implement that approach by yourself. However, you can also use available libraries like MediatR that uses your IoC container under the covers.

### The domain event dispatcher: mapping from events to event handlers (part 2)
You can therefore directly use the predefined interfaces and the mediator object's publish/dispatch methods.In code, you first need to register the event handler types in your IoC container, as shown in the following example at eShopOnContainers Ordering microservice:The code first identifies the assembly that contains the domain event handlers by locating the assembly that holds any of the handlers (using typeof(ValidateOrAddBuyerAggregateWhenXxxx), but you could have chosen any other event handler to locate the assembly). Since all the event handlers implement the IAsyncNotificationHandler interface, the code then just searches for those types and registers all the event handlers.

### Subscribe to domain events
When you use MediatR, each event handler must use an event type that is provided on the generic parameter of the INotificationHandler interface, as you can see in the following code:Based on the relationship between event and event handler, which can be considered the subscription, the MediatR artifact can discover all the event handlers for each event and trigger each one of those event handlers.

### Handle domain events
Finally, the event handler usually implements application layer code that uses infrastructure repositories to obtain the required additional aggregates and to execute side-effect domain logic. The following domain event handler code at eShopOnContainers, shows an implementation example.The previous domain event handler code is considered application layer code because it uses infrastructure repositories, as explained in the next section on the infrastructure-persistence layer. Event handlers could also use other infrastructure components.Domain events can generate integration events to be published outside of the microservice boundariesFinally, it's important to mention that you might sometimes want to propagate events across multiple microservices. That propagation is an integration event, and it could be published through an event bus from any specific domain event handler.

### Conclusions on domain events
As stated, use domain events to explicitly implement side effects of changes within your domain. To use DDD terminology, use domain events to explicitly implement side effects across one or multiple aggregates. Additionally, and for better scalability and less impact on database locks, use eventual consistency between aggregates within the same domain.The reference app uses MediatR to propagate domain events synchronously across aggregates, within a single transaction. However, you could also use some AMQP implementation like RabbitMQ or Azure Service Bus to propagate domain events asynchronously, using eventual consistency but, as mentioned above, you have to consider the need for compensatory actions in case of failures.

## The Repository Pattern
### Context
In many applications, the business logic accesses data from data stores such as databases, SharePoint lists, or Web services. Directly accessing the data can result in the following:Duplicated codeA higher potential for programming errorsWeak typing of the business dataDifficulty in centralizing data-related policies such as cachingAn inability to easily test the business logic in isolation from external dependencies

### Objectives


### Use the Repository pattern to achieve one or more of the following objectives
You want to maximize the amount of code that can be tested with automation and to isolate the data layer to support unit testing.You access the data source from many locations and want to apply centrally managed, consistent access rules and logic.You want to implement and centralize a caching strategy for the data source.You want to improve the code's maintainability and readability by separating business logic from data or service access logic.You want to use business entities that are strongly typed so that you can identify problems at compile time instead of at run time.You want to associate a behavior with the related data. For example, you want to calculate fields or enforce complex relationships or business rules between the data elements within an entity.You want to apply a domain model to simplify complex business logic.

### Solution
Use a repository to separate the logic that retrieves the data and maps it to the entity model from the business logic that acts on the model. The business logic should be agnostic to the type of data that comprises the data source layer. For example, the data source layer can be a database, a SharePoint list, or a Web service.The repository mediates between the data source layer and the business layers of the application. It queries the data source for the data, maps the data from the data source to a business entity, and persists changes in the business entity to the data source. A repository separates the business logic from the interactions with the underlying data source or Web service.

### Solution (continued)
The separation between the data and business tiers has three benefits:It centralizes the data logic or Web service access logic.It provides a substitution point for the unit tests.It provides a flexible architecture that can be adapted as the overall design of the application evolves.There are two ways that the repository can query business entities. It can submit a query object to the client's business logic or it can use methods that specify the business criteria. In the latter case, the repository forms the query on the client's behalf.

### Solution (part 2)
The repository returns a matching set of entities that satisfy the query. The following diagram shows the interactions of the repository with the client and the data source.Interactions of the repositoryFf649690.4058e458-bd54-4597-845e-6f8b1a21cfc3(en-us,PandP.10).pngThe client submits new or changed entities to the repository for persistence. In more complex situations, the client business logic can use the Unit of Work pattern. This pattern demonstrates how to encapsulate several related operations that should be consistent with each other or that have related dependencies. The encapsulated items are sent to the repository for update or delete actions. This guidance does not include an example of the Unit of Work pattern. For more information, see Unit of Work on Martin Fowler's Web site.Repositories are bridges between data and operations that are in different domains.

### Solution (part 2) (continued)
A common case is mapping from a domain where data is weakly typed, such as a database or SharePoint list, into a domain where objects are strongly typed, such as a domain entity model. One example is a database that uses IDbCommand objects to execute queries and returns IDataReader objects. Another example is SharePoint, which uses SPQuery objects to return SPListItem collections.

### Solution (part 3)
A repository issues the appropriate queries to the data source, and then it maps the result sets to the externally exposed business entities. Repositories often use the Data Mapper pattern to translate between representations. Repositories remove dependencies that the calling clients have on specific technologies. For example, if a client calls a catalog repository to retrieve some product data, it only needs to use the catalog repository interface. For example, the client does not need to know if the product information is retrieved with SQL queries to a database or Collaborative Application Markup Language (CAML) queries to a SharePoint list. Isolating these types of dependences provides flexibility to evolve implementations.

### Implementation Details
This section discusses the implementation strategies for SharePoint list repositories and Web service repositories.

### SharePoint List Repositories
The following diagram illustrates the interactions of a SharePoint list repository with SharePoint lists and the business logic.Interactions of a SharePoint list repositoryFf649690.a3b014d3-7677-4e99-886e-fd3432a8f914(en-us,PandP.10).pngUsing the Repository pattern in a SharePoint application addresses several concerns.SharePoint applications often store business information in SharePoint lists. To retrieve data from SharePoint lists requires careful use of the SharePoint API, knowledge of the GUIDs that are related to the lists and their fields, and a working knowledge of CAML. Repositories centralize this logic.The amount of code that is required to query or update a SharePoint list item is enough to warrant its encapsulation into helper methods. When Web Forms, event receivers, and workflow business logic all require access to the same lists, the code that accesses the SharePoint lists can be duplicated throughout the application. This can make the application prone to bugs and difficult to maintain. Repositories eliminate this duplication.Without a repository, the application is difficult to unit test because the business logic has direct dependencies on the SharePoint lists.

### SharePoint List Repositories (part 2)
Repositories centralize the access logic and provide a substitution point for the unit tests.Externally, the repository exposes strongly-typed business entities. Internally, it works with SharePoint-specific objects, such as the SPQuery and the SPListItem objects. The SharePoint Guidance Library, which is a part of this guidance, provides classes for mapping and querying that make it easier to build repositories for SharePoint lists. The ListItemFieldMapper class converts strongly-typed business entities to and from SPListItem objects based on a set of mapping definitions. The CAMLQueryBuilder class builds SPQuery objects based on common query operations. The SPQuery object is used to query a SharePoint list.The following sections show how the repository pattern is implemented in the SharePoint Guidance Library. For more information, see List-Based Repositories.

### SharePoint Guidance Library Helper Classes
The following diagram shows the major components of a SharePoint list repository.

### Components of a SharePoint list repository
Client Business Logic, Business Entity, persist, query, Your List Repository with List Item Field Mapper and CAML Query Builder, SharePoint List Item, SharePoint query and SharePoint List.The list repository contains a query object and a data mapper object that are specific to SharePoint. These are the ListItemFieldMapper and CAMLQueryBuilder classes. The data mapper translates between an SPListItem and the business entity that is defined by the application. The query object internally constructs an SPQuery object and uses CAML to query the list. NoteWhen you design a SharePoint list repository, keep in mind that a list can contain fields from multiple content types. The logic that is implemented in the ListItemFieldMapper and CAMLQueryBuilder objects does not prevent fields from multiple content types from being retrieved.

### Components of a SharePoint list repository (continued)
In some cases, if the content types have the same parent content type, you can use a single repository to project a common view across these content types.However, it is generally inadvisable to create repositories that deal with dissimilar content types and return different business entities from the same repository. In this situation, create a repository for each content type because the content types logically represent different entities.

### Implementation Variations
When you create a SharePoint list repository, you should consider how the repository locates the list that it is going to access. A list typically resides in a site, and it can be accessed either through its Uniform Resource Identifier (URI) or its GUID. The repository needs one of these, but passing this information to a repository can be challenging if you use the repository in conjunction with a service location. For more information, see The Service Locator Pattern.

### There are three ways in which a repository can access a list
A list can be centrally located. In this case, a repository is associated with a list that is at a fixed location. All sites retrieve the data from this central location. The PartnerPromotionsRepository class in the Partner Portal application is an example of a repository that uses such as list.A list can be accessed relative to the current site context. In this case, a repository is associated with a list whose location is relative to the current site. The IncidentManagementRepository class in the Partner Portal application is an example of such a repository.A list can be accessed according to a context that is supplied by a consumer. In this case, only the consumer of the repository knows which list the repository should access. There is no example of this in the Partner Portal application. However, you can extend the Training Management application to support this use case.

### There are three ways in which a repository can access a list (continued)
You can implement a repository that accesses the list of training courses for your department on your local installation and also accesses related training courses that are located on another departmental site. In this case, the consumer instructs the repository to target a particular list.The following sections describe more details about how to associate repositories with lists.

### Lists That Are Centrally Accessed from a Fixed Location
In this case, a list is at a fixed location, and all sites access it from this central point. Its location cannot be determined based on the current context. Although it is possible to hard code the location of the list, this is not recommended, because the topology of the site can change. It is often better to make the location of the list a configuration setting. In that case, defining the list's location is an administrative task. The location is established when the site topology is set up.For example, the Partner Portal application centrally manages the published promotions for all partners by locating them on one site collection. Partners see their particular promotions on their collaboration home pages. Each partner collaboration site is hosted in its own site collection. This establishes security boundaries and isolates the data intended for one partner from the data intended for another partner. Because the relationship between the list and consumers of the list is based on the operational topology, the list location is defined with configuration data.

### The following are characteristics of a list with a fixed location
There is typically only one instance of that list within the Web application scope.The location of the list is determined when the site topology is designed or when the site is installed.The list location should be retrieved from configuration data that is shared by all consumers. This data is typically at the Web application level or Web farm level.The following diagram shows the flow of information among components that access a list at a central location.

### Associating a repository with a list at a central location
Consumer, get repository instance, service locator, construct repository, repository, read list location, Configuration manager, access list, SharePoint List.The service locator constructs a repository object, which then reads the configuration information. The repository accesses the list based on this data. Because the repository relies on the configuration data, it can be constructed independently of the application context. It does not need any additional information from the list consumers.This approach is susceptible to run-time exceptions because it depends on configuration data, which can be erroneous, lost, or corrupted. Make sure that you provide adequate diagnostics that inform IT administrators of any configuration errors. Problems that are caused by configuration errors are difficult to resolve without adequate logging information.

### Lists with a Location That Is Fixed, Relative to the Current Context
In this case, the repository is associated with a list whose location is fixed, relative to the current context. For example, in the Training Management application, registration and course lists are located at the same relative location within a site. However, there can be several Training Management sites within a SharePoint farm. In this situation, the list repository is loaded from the current context.The following are characteristics of a list with a location that is relative to the context:The list has a fixed location that is relative to a site (an SPWeb object).The location is independent of the site topology.The list location is based on the current SharePoint context.The following diagram shows the components and flow of information that access a list with a location that is relative to the context.

### Associating a repository with a list whose location is relative to the context
Consomer, Get Repository Factory, Service Locator, Construct Repository Factory, Repository Factory, Get Repository with provided context, Construct Repository with provided contect, Repository, Access List, SharePoint List.SharePoint often has a number of instances of the same Web application. In this situation, the repository gets the current site from the SharePoint context (the SPContext.Current.Web object) and loads the list information from this context. Because this relationship is fixed relative to the current site, the repository needs no additional information. The repository instance can be directly constructed by the service locator.

### Lists Whose Context Is Supplied by a Consumer
In this case, the repository is associated with a particular content type and can access any list that has SPListItems of this content type. The consumer must provide context to the repository. For example, the consumer might provide the SPWeb object that holds the list or the GUID of the list. Although it is generally a good practice to keep technology-specific dependencies (such as a reliance on SQL Server) out of the repository interface, providing context when the repository is constructed is an accepted, widely used practice.This scenario occurs with sites that have a dynamic topology, or where relationships are established by a user who supplies configuration information. If you add or remove sites at run time that contain lists that the repository accesses, you often have to provide the context.

### Lists Whose Context Is Supplied by a Consumer (continued)
An example is if you use the Finance training site to view courses but you also want to see the courses on the Human Resources training site.To provide this capability, you can build a general purpose Web Part to view the courses from other departmental training sites. You can add this Web Part to the Finance training site and configure it to view the related Human Resources department courses.

### Lists Whose Context Is Supplied by a Consumer (part 2)
The repository that the Web Part on the Finance site uses receives the location of the Human Resources course list as context information when the Web Part constructs it.One challenge with this type of repository is using it in combination with the SharePoint Guidance Library service locator. The ActivatingServiceLocator class can only use parameterless constructors for the repositories. It is not possible to pass the contextual information (in this case, the location of the list) into the repository through the constructor. One way to solve this is to pass the location of the list with each method call, but this inserts a dependency on the list's URL into the interface definition. The Training Management application uses this approach.A better, but more complicated way to pass the location of the list to the repository is to use a factory. The factory includes a method that creates the repository. The consumer passes the location of the list to the method.

### Lists Whose Context Is Supplied by a Consumer (part 2) (continued)
The consumer then uses the ActivatingServiceLocator to access the factory and uses it to create the repository. With this approach, the consumer provides the location of the list to the factory, which in turn creates the repository. The factory passes the context through the repository constructor.

### Lists Whose Context Is Supplied by a Consumer (part 3)
This technique is known as constructor injection.The following are characteristics of a list whose context is supplied by a consumer:The consumer can determine which list the repository should access.The location of the list is often determined at run time.This list location is derived from the current business context.The following diagram shows the components and flow of information that are involved in accessing a list whose context is supplied by the consumer.

### Associating a repository with a list whose context is supplied by the consumer
Consomer, Get Repository Factory, Service Locator, Construct Repository Factory, Repository Factory, Get Repository with provided context, Construct Repository with provided contect, Repository, Access List, SharePoint List.The consumer constructs the context for the repository. The consumer retrieves an instance of a repository factory from the service locator. The consumer then uses the repository factory to construct the repository. The consumer provides the context for the list. The repository uses this information to locate the list. Because the repository is decoupled from both the configuration data and the context, it is suitable for many scenarios. However, because the consumer provides the context, it increases the coupling between the consuming code and the repository.

### Web Service Repositories
A common backing store for data is a business service that is exposed by a line-of-business (LOB) application. Generally, these business services are at a higher level of abstraction than the standard Create/Read/Update/Delete (CRUD) semantics of a database or SharePoint list. However, from the perspective of the client, they often are equivalent to a data source. Like with SharePoint lists, accessing Web services can be complex and prone to error. A repository centralizes the access logic for a service and provides a substitution point for unit tests. Note that services are often expensive to invoke and benefit from caching strategies that are implemented within the repository.The following diagram shows a service back-end repository that uses caching.

### Using a repository with a Web service
Client Business Logic, Business Entiry, persist, Query, Your Service Repository with cache and Web Service Proxy, Line of Business Service.In this case, the query logic in the repository first checks to see whether the queried items are in the cache. If they are not, the repository accesses the Web service to retrieve the information. Although it is possible to access services directly, it is also possible to access them through the SharePoint Business Data Catalog (BDC). The BDC can aggregate several data sources, including Web services, and expose them through a uniform, generic interface. The BDC allows you to use standard Web Parts to display and modify data. For more information, see Consuming Web Services with the Business Data Catalog (BDC).You may need more complex security options than the BDC supports. In this situation, you can use the Windows Communication Foundation (WCF). This requires that your own code and configuration data manage the service information and security context. For more information, see Integrating Line-of-Business Systems.

### Repository Examples
For an example of the list repository pattern, see Development How-to Topics. Also, the Partner Portal application includes the following list repositories that can be used as starting points:The Partner Promotion Repository is in the PartnerPromotionRepository.cs file of the PartnerPortal\Contoso.PartnerPortal.Promotions directory. There is also a mock implementation for unit testing in the PartnerPromotionsPresenterFixture.cs file of the PartnerPortal\Contoso.PartnerPortal.Promotions.Tests directory.The Business Event Type Configuration Repository is in the BusinessEventTypeConfigurationRepository.cs file of the Microsoft.Practices.SPG2\Microsoft.Practices.SPG.SubSiteCreation\BusinessEventTypeConfiguration directory.

### Repository Examples (part 2)
There is also a mock implementation for unit testing in the ResolveSiteTemplateFixture.cs file of the Microsoft.Practices.SPG2\Microsoft.Practices.SPG.SubSiteCreation.Tests directory.The Subsite Creation Requests Repository is in the SubSiteCreationRequestsRepository.cs file of the directory Microsoft.Practices.SPG2\Microsoft.Practices.SPG.SubSiteCreation\SubSiteCreationRequests.For an example of the data repository pattern using Web services, see the following areas of the reference implementation:The Incident Management Repository is in the IncidentManagementRepository.cs file of the directory PartnerPortal\Contoso.LOB.Services.Client\Repositories.The Pricing Repository is in the PricingRepository.cs file of the directory PartnerPortal\Contoso.LOB.Services.Client\Repositories.The Cached BDC Product Catalog Repository is in the CachedBdcProductCatalogRepository.cs file of the directory PartnerPortal\Contoso.LOB.Services.Client\Repositories. There is also a mock implementation for unit testing in the ProductDetailsPresenterFixture.cs file of the directory PartnerPortal\Contoso.PartnerPortal.ProductCatalog.Tests.

### The Partner Portal application also contains two other repositories
The Full Text Search IncidentTask Repository uses SharePoint Search as its data source. This repository is found in the FullTextSearchIncidentTaskRepository.cs file of the directory PartnerPortal\Contoso.PartnerPortal.Collaboration.Incident\Repositories.The Partner Site Directory uses the site directory list to provide the Partner site collection URL and the user profile to provide the PartnerID. The repository is implemented in the PartnerSiteDirectory.cs file of the directory PartnerPortal\Contoso.PartnerPortal.PartnerDirectory.For more information about the Repository pattern, Unit of Work pattern, and Data Mapper pattern, see Repository on Martin Fowler's Web site.

### Considerations
The Repository pattern increases the level of abstraction in your code. This may make the code more difficult to understand for developers who are unfamiliar with the pattern. Although implementing the pattern reduces the amount of redundant code, it generally increases the number of classes that must be maintained.The Repository pattern helps to isolate both the service and the list access code. Isolation makes it easier to treat them as independent services and to replace them with mock objects in unit tests. Typically, it is difficult to unit test the repositories themselves, so it is often better to write integration tests for them.When caching data in a multithreaded environment, consider synchronizing access to the cache in addition to the cached objects.

### Considerations (continued)
Often, common caches, such as the ASP.NET cache, are already thread safe, but you must also ensure that the objects themselves can operate in a multithreaded environment.If you are caching data in heavily loaded systems, performance can be an issue. Consider synchronizing access to the data source. This ensures that only a single request for the data is issued to the list or back-end service. All other clients rely on the retrieved data. For more information, see Techniques for Aggregating List and Site Information.

### Related Patterns
The following two patterns are often used in conjunction with the Repository pattern:Data Mapper. This pattern describes how to map data to different schemas. It is often used to map between a data store and a domain model.Unit of Work. This pattern keeps track of everything that happens during a business transaction that affects the database. At the conclusion of the transaction, it determines how to update the database to conform to the changes.

# DevOps
## General DevOps
### The fundamental differences between DevOps & Agile
The differences between the two are listed down in the table below.Features	DevOps	AgileAgility	Agility in both Development & Operations	Agility in only DevelopmentProcesses/ Practices	Involves processes such as CI, CD, CT, etc.	Involves practices such as Agile Scrum, Agile Kanban, etc.Key Focus Area	Timeliness & quality have equal priority	Timeliness is the main priorityRelease Cycles/ Development Sprints	Smaller release cycles with immediate feedback	Smaller release cyclesSource of Feedback	Feedback is from self (Monitoring tools)	Feedback is from customersScope of Work	Agility & need for Automation	Agility onlyDevOps vs Agile

### The need for DevOps
According to me, this answer should start by explaining the general market trend.Instead of releasing big sets of features, companies are trying to see if small features can be transported to their customers through a series of release trains.This has many advantages like quick feedback from customers, better quality of software etc.which in turn leads to high customer satisfaction.

### To achieve this, companies are required to
Increase deployment frequencyLower failure rate of new releasesShortened lead time between fixesFaster mean time to recovery in the event of new release crashingDevOps fulfills all these requirements and helps in achieving seamless software delivery.You can give examples of companies like Etsy, Google and Amazon which have adopted DevOps to achieve levels of performance that were unthinkable even five years ago.They are doing tens, hundreds or even thousands of code deployments per day while delivering world class stability, reliability and security.

### How is DevOps different from Agile / SDLC


### I would advise you to go with the below explanation
Agile is a set of values and principles about how to produce i.e.develop software.Example: if you have some ideas and you want to turn those ideas into working software, you can use the Agile values and principles as a way to do that.But, that software might only be working on a developer's laptop or in a test environment.You want a way to quickly, easily and repeatably move that software into production infrastructure, in a safe and simple way.To do that you need DevOps tools and techniques.You can summarize by saying Agile software development methodology focuses on the development of software but DevOps on the other hand is responsible for development as well as deployment of the software in the safest and most reliable way possible.Here's a blog that will give you more information on the evolution of DevOps.

### Which are the top DevOps tools? Which tools have you worked on


### The most popular DevOps tools are mentioned below
Git : Version Control System toolJenkins : Continuous Integration toolSelenium : Continuous Testing toolPuppet, Chef, Ansible : Configuration Management and Deployment toolsNagios : Continuous Monitoring toolDocker : Containerization tool

### The second part of the answer has two possibilities
If you have experience with all the above tools then you can say that I have worked on all these tools for developing good quality software and deploying those softwares easily, frequently, and reliably.If you have experience only with some of the above tools then mention those tools and say that I have specialization in these tools and have an overview about the rest of the tools.Our DevOps certification course includes hands-on training on the most popular DevOps tools.Find out when the next batch starts.

### All these tools work together
Given below is a generic logical flow where everything gets automated for seamless delivery.However, this flow may vary from organization to organization as per the requirement.Developers develop the code and this source code is managed by Version Control System tools like Git etc.Developers send this code to the Git repository and any changes made in the code is committed to this Repository.Jenkins pulls this code from the repository using the Git plugin and build it using tools like Ant or Maven.Configuration management tools like puppet deploys & provisions testing environment and then Jenkins releases this code on the test environment on which testing is done using tools like selenium.Once the code is tested, Jenkins send it for deployment on the production server (even production server is provisioned & maintained by tools like puppet).After deployment It is continuously monitored by tools like Nagios.Docker containers provides testing environment to test the build features.

### The advantages of DevOps
For this answer, you can use your past experience and explain how DevOps helped you in your previous job.If you don't have any such experience, then you can mention the below advantages.

### Technical benefits
Continuous software deliveryLess complex problems to fixFaster resolution of problems

### Business benefits
Faster delivery of featuresMore stable operating environmentsMore time available to add value (rather than fix/maintain)

### The most important thing DevOps helps us achieve
According to me, the most important thing that DevOps helps us achieve is to get the changes into production as quickly as possible while minimizing risks in software quality assurance and compliance.This is the primary objective of DevOps.Learn more in this DevOps tutorial blog.However, you can add many other positive effects of DevOps.For example, clearer communication and better working relationships between teams i.e.both the Ops team and Dev team collaborate together to deliver good quality software which in turn leads to higher customer satisfaction.Explain with a use case where DevOps can be used in industry/ real-life.There are many industries that are using DevOps so you can mention any of those use cases, you can also refer the below example:Etsy is a peer-to-peer e-commerce website focused on handmade or vintage items and supplies, as well as unique factory-manufactured items.Etsy struggled with slow, painful site updates that frequently caused the site to go down.It affected sales for millions of Etsy's users who sold goods through online market place and risked driving them to the competitor.With the help of a new technical management team, Etsy transitioned from its waterfall model, which produced four-hour full-site deployments twice weekly, to a more agile approach.Today, it has a fully automated deployment pipeline, and its continuous delivery practices have reportedly resulted in more than 50 deployments a day with fewer disruptions.Explain your understanding and expertise on both the software development side and the technical operations side of an organization you have worked with in the past.For this answer, share your past experience and try to explain how flexible you were in your previous job.

### The most important thing DevOps helps us achieve (part 2)


### You can refer the below example
DevOps engineers almost always work in a 24/7 business-critical online environment.I was adaptable to on-call duties and was available to take up real-time, live-system responsibility.I successfully automated processes to support continuous software deployments.I have experience with public/private clouds, tools like Chef or Puppet, scripting and automation with tools like Python and PHP, and a background in Agile.

### The anti-patterns of DevOps
A pattern is common usage usually followed.If a pattern commonly adopted by others does not work for your organization and you continue to blindly follow it, you are essentially adopting an anti-pattern.There are myths about DevOps.

### Some of them include
- DevOps is a process.

### Agile equals DevOps
We need a separate DevOps groupDevops will solve all our problemsDevOps means Developers Managing ProductionDevOps is Development-driven release managementDevOps is not development driven.DevOps is not IT Operations driven.We can't do DevOps - We're UniqueWe can't do DevOps - We've got the wrong people

## Version Control System (VCS)
### Version control
This is probably the easiest question you will face in the interview.My suggestion is to first give a definition of Version control.It is a system that records changes to a file or set of files over time so that you can recall specific versions later.Version control systems consist of a central shared repository where teammates can commit changes to a file or set of file.Then you can mention the uses of version control.

### Version control allows you to
Revert files back to a previous state.Revert the entire project back to a previous state.Compare changes over time.See who last modified something that might be causing a problem.Who introduced an issue and when.

### The benefits of using version control


### I will suggest you to include the following advantages of version control
With Version Control System (VCS), all the team members are allowed to work freely on any file at any time.VCS will later allow you to merge all the changes into a common version.All the past versions and variants are neatly packed up inside the VCS.When you need it, you can request any version at any time and you'll have a snapshot of the complete project right at hand.Every time you save a new version of your project, your VCS requires you to provide a short description of what was changed.Additionally, you can see what exactly was changed in the file's content.This allows you to know who has made what change in the project.A distributed VCS like Git allows all the team members to have complete history of the project so if there is a breakdown in the central server you can use any of your teammate's local Git repository.Describe branching strategies you have used.This question is asked to test your branching experience so tell them about how you have used branching in your previous job and what purpose does it serves, you can refer the below points:Feature branchingA feature branch model keeps all of the changes for a particular feature inside of a branch.When the feature is fully tested and validated by automated tests, the branch is then merged into master.Task branchingIn this model each task is implemented on its own branch with the task key included in the branch name.It is easy to see which code implements which task, just look for the task key in the branch name.Release branchingOnce the develop branch has acquired enough features for a release, you can clone that branch to form a Release branch.Creating this branch starts the next release cycle, so no new features can be added after this point, only bug fixes, documentation generation, and other release-oriented tasks should go in this branch.Once it is ready to ship, the release gets merged into master and tagged with a version number.In addition, it should be merged back into develop branch, which may have progressed since the release was initiated.In the end tell them that branching strategies varies from one organization to another, so I know basic branching operations like delete, merge, checking out a branch etc.

### I will suggest you to include the following advantages of version control (part 2)


### Which VCS tool you are comfortable with
You can just mention the VCS tool that you have worked on like this: "I have worked on Git and one major advantage it has over other VCS tools like SVN is that it is a distributed version control system."Distributed VCS tools do not necessarily rely on a central server to store all the versions of a project's files.Instead, every developer "clones" a copy of a repository and has the full history of the project on their own hard drive.

### Git
I will suggest that you attempt this question by first explaining about the architecture of git as shown in the below diagram.

### You can refer to the explanation given below
Git is a Distributed Version Control system (DVCS).It can track changes to a file and allows you to revert back to any particular change.Its distributed architecture provides many advantages over other Version Control Systems (VCS) like SVN one major advantage is that it does not rely on a central server to store all the versions of a project's files.Instead, every developer "clones" a copy of a repository I have shown in the diagram below with "Local repository" and has the full history of the project on his hard drive so that when there is a server outage, all you need for recovery is one of your teammate's local Git repository.There is a central cloud repository as well where developers can commit changes and share it with other teammates as you can see in the diagram where all collaborators are commiting changes "Remote repository".

### Explain some basic Git commands


### Below are some basic Git commands


### In Git how do you revert a commit that has already been pushed and made public
There can be two answers to this question so make sure that you include both because any of the below options can be used depending on the situation:Remove or fix the bad file in a new commit and push it to the remote repository.This is the most natural way to fix an error.Once you have made necessary changes to the file, commit it to the remote repository for that I will usegit commit -m "commit message"Create a new commit that undoes all changes that were made in the bad commit.to do this I will use a commandgit revert <name of bad commit>

### You squash last N commits into a single commit
There are two options to squash last N commits into a single commit.

### Include both of the below mentioned options in your answer
If you want to write the new commit message from scratch use the following commandgit reset -soft HEAD~N &&git commitIf you want to start editing the new commit message with a concatenation of the existing commit messages then you need to extract those messages and pass them to Git commit for that I will usegit reset -soft HEAD~N &&git commit -edit -m"$(git log -format=%B -reverse .HEAD@{N})"

### Git bisect? How can you use it to determine the source of a (regression) bug
I will suggest you to first give a small definition of Git bisect, Git bisect is used to find the commit that introduced a bug by using binary search.Command for Git bisect isgit bisect <subcommand> <options>Now since you have mentioned the command above, explain what this command will do, This command uses a binary search algorithm to find which commit in your project's history introduced a bug.You use it by first telling it a "bad" commit that is known to contain the bug, and a "good" commit that is known to be before the bug was introduced.Then Git bisect picks a commit between those two endpoints and asks you whether the selected commit is "good" or "bad".It continues narrowing down the range until it finds the exact commit that introduced the change.

### Git rebase and how can it be used to resolve conflicts in a feature branch before merge
According to me, you should start by saying git rebase is a command which will merge another branch into the branch where you are currently working, and move all of the local commits that are ahead of the rebased branch to the top of the history on that branch.Now once you have defined Git rebase time for an example to show how it can be used to resolve conflicts in a feature branch before merge, if a feature branch was created from master, and since then the master branch has received new commits, Git rebase can be used to move the feature branch to the tip of master.The command effectively will replay the changes made in the feature branch at the tip of master, allowing conflicts to be resolved in the process.When done with care, this will allow the feature branch to be merged into master with relative ease and sometimes as a simple fast-forward operation.

### You configure a Git repository to run code sanity checking tools right before making commits, and preventing them if the test fails
I will suggest you to first give a small introduction to sanity checking, A sanity or smoke test determines whether it is possible and reasonable to continue testing.Now explain how to achieve this, this can be done with a simple script related to the pre-commit hook of the repository.The pre-commit hook is triggered right before a commit is made, even before you are required to enter a commit message.In this script one can run other tools, such as linters and perform sanity checks on the changes being committed into the repository.

### Finally give an example, you can refer the below script


#!/bin/shfiles=$(git diff -cached -name-only -diff-filter=ACM | grep '.go$')if [ -z files ]; thenexit 0fiunfmtd=$(gofmt -l $files)if [ -z unfmtd ]; thenexit 0fiecho "Some .go files are not fmt'd"exit 1This script checks to see if any .go file that is about to be committed needs to be passed through the standard Go source code formatting tool gofmt.By exiting with a non-zero status, the script effectively prevents the commit from being applied to the repository.

### You find a list of files that has changed in a particular commit
For this answer instead of just telling the command, explain what exactly this command will do so you can say that, To get a list files that has changed in a particular commit use commandgit diff-tree -r {hash}Given the commit hash, this will list all the files that were changed or added in that commit.The -r flag makes the command list individual files, rather than collapsing them into root directory names only.You can also include the below mention point although it is totally optional but will help in impressing the interviewer.The output will also include some extra information, which can be easily suppressed by including two flags:git diff-tree -no-commit-id -name-only -r {hash}Here -no-commit-id will suppress the commit hashes from appearing in the output, and -name-only will only print the file names, instead of their paths.

### You setup a script to run every time a repository receives new commits through push
There are three ways to configure a script to run every time a repository receives new commits through push, one needs to define either a pre-receive, update, or a post-receive hook depending on when exactly the script needs to be triggered.Pre-receive hook in the destination repository is invoked when commits are pushed to it.Any script bound to this hook will be executed before any references are updated.This is a useful hook to run scripts that help enforce development policies.Update hook works in a similar manner to pre-receive hook, and is also triggered before any updates are actually made.However, the update hook is called once for every commit that has been pushed to the destination repository.Finally, post-receive hook in the repository is invoked after the updates have been accepted into the destination repository.This is an ideal place to configure simple deployment scripts, invoke some continuous integration systems, dispatch notification emails to repository maintainers, etc.Hooks are local to every Git repository and are not versioned.Scripts can either be created within the hooks directory inside the ".git" directory, or they can be created elsewhere and links to those scripts can be placed within the directory.

### How will you know in Git if a branch has already been merged into master


### I will suggest you to include both the below mentioned commands
git branch -merged lists the branches that have been merged into the current branch.git branch -no-merged lists the branches that have not been merged.

## Continuous Integration
### Meant by Continuous Integration
I will advise you to begin this answer by giving a small definition of Continuous Integration (CI).It is a development practice that requires developers to integrate code into a shared repository several times a day.Each check-in is then verified by an automated build, allowing teams to detect problems early.I suggest that you explain how you have implemented it in your previous job.

### You can refer the below given example
Developers check out code into their private workspaces.When they are done with it they commit the changes to the shared repository (Version Control Repository).The CI server monitors the repository and checks out changes when they occur.The CI server then pulls these changes and builds the system and also runs unit and integration tests.The CI server will now inform the team of the successful build.If the build or tests fails, the CI server will alert the team.The team will try to fix the issue at the earliest opportunity.This process keeps on repeating.

### Need a Continuous Integration of Dev & Testing
For this answer, you should focus on the need of Continuous Integration.

### My suggestion would be to mention the below explanation in your answer
Continuous Integration of Dev and Testing improves the quality of software, and reduces the time taken to deliver it, by replacing the traditional practice of testing after completing all development.It allows Dev team to easily detect and locate problems early because developers need to integrate code into a shared repository several times a day (more frequently).Each check-in is then automatically tested.

### The success factors for Continuous Integration
Here you have to mention the requirements for Continuous Integration.

### You could include the following points in your answer
Maintain a code repositoryAutomate the buildMake the build self-testingEveryone commits to the baseline every dayEvery commit (to baseline) should be builtKeep the build fastTest in a clone of the production environmentMake it easy to get the latest deliverablesEveryone can see the results of the latest buildAutomate deployment

### Explain how you can move or copy Jenkins from one server to another
I will approach this task by copying the jobs directory from the old server to the new one.

### There are multiple ways to do that; I have mentioned them below


### You can
Move a job from one installation of Jenkins to another by simply copying the corresponding job directory.Make a copy of an existing job by making a clone of a job directory by a different name.Rename an existing job by renaming a directory.Note that if you change a job name you will need to change any other job that tries to call the renamed job.

### Explain how can create a backup and copy files in Jenkins
Answer to this question is really direct.To create a backup, all you need to do is to periodically back up your JENKINS_HOME directory.This contains all of your build jobs configurations, your slave node configurations, and your build history.To create a back-up of your Jenkins setup, just copy this directory.You can also copy a job directory to clone or replicate a job or rename the directory.

### Explain how you can setup Jenkins job
My approach to this answer will be to first mention how to create Jenkins job.Go to Jenkins top page, select "New Job", then choose "Build a free-style software project".

### Then you can tell the elements of this freestyle job
Optional SCM, such as CVS or Subversion where your source code resides.Optional triggers to control when Jenkins will perform builds.Some sort of build script that performs the build (ant, maven, shell script, batch file, etc.) where the real work happens.Optional steps to collect information out of the build, such as archiving the artifacts and/or recording javadoc and test results.Optional steps to notify other people/systems with the build result, such as sending e-mails, IMs, updating issue tracker, etc..Mention some of the useful plugins in Jenkins.

### Below, I have mentioned some important Plugins
Maven 2 projectAmazon EC2HTML publisherCopy artifactJoinGreen BallsThese Plugins, I feel are the most useful plugins.If you want to include any other Plugin that is not mentioned above, you can add them as well.But, make sure you first mention the above stated plugins and then add your own.

### How will you secure Jenkins
The way I secure Jenkins is mentioned below.If you have any other way of doing it, please mention it in the comments section below:Ensure global security is on.Ensure that Jenkins is integrated with my company's user directory with appropriate plugin.Ensure that matrix/Project matrix is enabled to fine tune access.Automate the process of setting rights/privileges in Jenkins with custom version controlled script.Limit physical access to Jenkins data/folders.Periodically run security audits on same.Jenkins is one of the many popular tools that are used extensively in DevOps.

## Continuous Testing
### Continuous Testing


### I will advise you to follow the below mentioned explanation
Continuous Testing is the process of executing automated tests as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with in the latest build.In this way, each build is tested continuously, allowing Development teams to get fast feedback so that they can prevent those problems from progressing to the next stage of Software delivery life-cycle.This dramatically speeds up a developer's workflow as there's no need to manually rebuild the project and re-run all tests after making changes.

### Automation Testing
Automation testing or Test Automation is a process of automating the manual process to test the application/system under test.Automation testing involves use of separate testing tools which lets you create test scripts which can be executed repeatedly and doesn't require any manual intervention.

### The benefits of Automation Testing
I have listed down some advantages of automation testing.Include these in your answer and you can add your own experience of how Continuous Testing helped your previous company:Supports execution of repeated test casesAids in testing a large test matrixEnables parallel executionEncourages unattended executionImproves accuracy thereby reducing human generated errorsSaves time and money

### Automate Testing in DevOps lifecycle


### I have mentioned a generic flow below which you can refer to
In DevOps, developers are required to commit all the changes made in the source code to a shared repository.Continuous Integration tools like Jenkins will pull the code from this shared repository every time a change is made in the code and deploy it for Continuous Testing that is done by tools like Selenium as shown in the below diagram.In this way, any change in the code is continuously tested unlike the traditional approach.

### Continuous Testing important for DevOps
You can answer this question by saying, "Continuous Testing allows any change made in the code to be tested immediately.This avoids the problems created by having "big-bang" testing left to the end of the cycle such as release delays and quality issues.In this way, Continuous Testing facilitates more frequent and good quality releases."

### The key elements of Continuous Testing tools


### Key elements of Continuous Testing are
Risk Assessment: It Covers risk mitigation tasks, technical debt, quality assessment and test coverage optimization to ensure the build is ready to progress toward next stage.Policy Analysis: It ensures all processes align with the organization's evolving business and compliance demands are met.Requirements Traceability: It ensures true requirements are met and rework is not required.An object assessment is used to identify which requirements are at risk, working as expected or require further validation.Advanced Analysis: It uses automation in areas such as static code analysis, change impact analysis and scope assessment/prioritization to prevent defects in the first place and accomplishing more within each iteration.Test Optimization: It ensures tests yield accurate outcomes and provide actionable findings.Aspects include Test Data Management, Test Optimization Management and Test MaintenanceService Virtualization: It ensures access to real-world testing environments.Service visualization enables access to the virtual form of the required testing stages, cutting the waste time to test environment setup and availability.

### Which Testing tool are you comfortable with and what are the benefits of that tool
Here mention the testing tool that you have worked with and accordingly frame your answer.

### I have mentioned an example below
I have worked on Selenium to ensure high quality and more frequent releases.

### Some advantages of Selenium are:
It is free and open sourceIt has a large user base and helping communitiesIt has cross Browser compatibility (Firefox, chrome, Internet Explorer, Safari etc.)It has great platform compatibility (Windows, Mac OS, Linux etc.)It supports multiple programming languages (Java, C#, Ruby, Python, Pearl etc.)It has fresh and regular repository developmentsIt supports distributed testing

### The Testing types supported by Selenium


### Selenium supports two types of testing
Regression Testing: It is the act of retesting a product around an area where a bug was fixed.Functional Testing: It refers to the testing of software features (functional points) individually.

### Selenium IDE
My suggestion is to start this answer by defining Selenium IDE.It is an integrated development environment for Selenium scripts.It is implemented as a Firefox extension, and allows you to record, edit, and debug tests.Selenium IDE includes the entire Selenium Core, allowing you to easily and quickly record and play back tests in the actual environment that they will run in.Now include some advantages in your answer.With autocomplete support and the ability to move commands around quickly, Selenium IDE is the ideal environment for creating Selenium tests no matter what style of tests you prefer.

### The difference between Assert and Verify commands in Selenium


### I have mentioned differences between Assert and Verify commands below
Assert command checks whether the given condition is true or false.Let's say we assert whether the given element is present on the web page or not.If the condition is true, then the program control will execute the next test step.But, if the condition is false, the execution would stop and no further test would be executed.Verify command also checks whether the given condition is true or false.Irrespective of the condition being true or false, the program execution doesn't halts i.e.any failure during verification would not stop the execution and all the test steps would be executed.

### Launch Browser using WebDriver


### The following syntax can be used to launch Browser
WebDriver driver = new FirefoxDriver();WebDriver driver = new ChromeDriver();WebDriver driver = new InternetExplorerDriver();

### I use Selenium Grid
For this answer, my suggestion would be to give a small definition of Selenium Grid.It can be used to execute same or different test scripts on multiple platforms and browsers concurrently to achieve distributed test execution.This allows testing under different environments and saving execution time remarkably.

## Configuration Management
### The goals of Configuration management processes
The purpose of Configuration Management (CM) is to ensure the integrity of a product or system throughout its life-cycle by making the development or deployment process controllable and repeatable, therefore creating a higher quality product or system.The CM process allows orderly management of system information and system changes for purposes such as to:Revise capability,Improve performance,Reliability or maintainability,Extend life,Reduce cost,Reduce risk andLiability, or correct defects.

### The difference between Asset management and Configuration Management
Given below are few differences between Asset Management and Configuration Management:

### The difference between an Asset and a Configuration Item
According to me, you should first explain Asset.It has a financial value along with a depreciation rate attached to it.IT assets are just a sub-set of it.Anything and everything that has a cost and the organization uses it for its asset value calculation and related benefits in tax calculation falls under Asset Management, and such item is called an asset.Configuration Item on the other hand may or may not have financial values assigned to it.It will not have any depreciation linked to it.Thus, its life would not be dependent on its financial value but will depend on the time till that item becomes obsolete for the organization.Now you can give an example that can showcase the similarity and differences between both:

### 1) Similarity
Server - It is both an asset as well as a CI.

### 2) Difference
Building - It is an asset but not a CI.Document - It is a CI but not an asset

### What do you understand by "Infrastructure as code"? How does it fit into the DevOps methodology? What purpose does it achieve
Infrastructure as Code (IAC) is a type of IT infrastructure that operations teams can use to automatically manage and provision through code, rather than using a manual process.Companies for faster deployments treat infrastructure like software: as code that can be managed with the DevOps tools and processes.These tools let you make infrastructure changes more easily, rapidly, safely and reliably.

### Which among Puppet, Chef, SaltStack and Ansible is the best Configuration Management (CM) tool? Why
This depends on the organization's need so mention few points on all those tools:Puppet is the oldest and most mature CM tool.Puppet is a Ruby-based Configuration Management tool, but while it has some free features, much of what makes Puppet great is only available in the paid version.Organizations that don't need a lot of extras will find Puppet useful, but those needing more customization will probably need to upgrade to the paid version.Chef is written in Ruby, so it can be customized by those who know the language.It also includes free features, plus it can be upgraded from open source to enterprise-level if necessary.On top of that, it's a very flexible product.Ansible is a very secure option since it uses Secure Shell.It's a simple tool to use, but it does offer a number of other services in addition to configuration management.It's very easy to learn, so it's perfect for those who don't have a dedicated IT staff but still need a configuration management tool.SaltStack is python based open source CM tool made for larger businesses, but its learning curve is fairly low.

### Puppet
I will advise you to first give a small definition of Puppet.It is a Configuration Management tool which is used to automate administration tasks.Now you should describe its architecture and how Puppet manages its Agents.Puppet has a Master-Slave architecture in which the Slave has to first send a Certificate signing request to Master and Master has to sign that Certificate in order to establish a secure connection between Puppet Master and Puppet Slave as shown on the diagram below.Puppet Slave sends request to Puppet Master and Puppet Master then pushes configuration on Slave.Refer the diagram below that explains the above description.Before a client can authenticate with the Puppet Master, its certs need to be signed and accepted.

### How will you automate this task
The easiest way is to enable auto-signing in puppet.conf.Do mention that this is a security risk.

### If you still want to do this
Firewall your puppet master - restrict port tcp/8140 to only networks that you trust.Create puppet masters for each 'trust zone', and only include the trusted nodes in that Puppet masters manifest.Never use a full wildcard such as *.Describe the most significant gain you made from automating a process through Puppet.For this answer, I will suggest you to explain you past experience with Puppet.

### You can refer the below example
I automated the configuration and deployment of Linux and Windows machines using Puppet.In addition to shortening the processing time from one week to 10 minutes, I used the roles and profiles pattern and documented the purpose of each module in README to ensure that others could update the module using Git.The modules I wrote are still being used, but they've been improved by my teammates and members of the community

### Which open source or community tools do you use to make Puppet more powerful
Over here, you need to mention the tools and how you have used those tools to make Puppet more powerful.

### Below is one example for your reference
Changes and requests are ticketed through Jira and we manage requests through an internal process.Then, we use Git and Puppet's Code Manager app to manage Puppet code in accordance with best practices.Additionally, we run all of our Puppet changes through our continuous integration pipeline in Jenkins using the beaker testing framework.

### Puppet Manifests
It is a very important question so make sure you go in a correct flow.According to me, you should first define Manifests.Every node (or Puppet Agent) has got its configuration details in Puppet Master, written in the native Puppet language.These details are written in the language which Puppet can understand and are termed as Manifests.They are composed of Puppet code and their filenames use the .pp extension.Now give an exampl.You can write a manifest in Puppet Master that creates a file and installs apache on all Puppet Agents (Slaves) connected to the Puppet Master.

### Puppet Module and How it is different from Puppet Manifest


### For this answer, you can go with the below mentioned explanation
A Puppet Module is a collection of Manifests and data (such as facts, files, and templates), and they have a specific directory structure.Modules are useful for organizing your Puppet code, because they allow you to split your code into multiple Manifests.It is considered best practice to use Modules to organize almost all of your Puppet Manifests.Puppet programs are called Manifests which are composed of Puppet code and their file names use the .pp extension.

### Facter in Puppet
You are expected to answer what exactly Facter does in Puppet so according to me, you should say, "Facter gathers basic information (facts) about Puppet Agent such as hardware details, network settings, OS type and version, IP addresses, MAC addresses, SSH keys, and more.These facts are then made available in Puppet Master's Manifests as variables."

### Chef
Begin this answer by defining Chef.It is a powerful automation platform that transforms infrastructure into code.Chef is a tool for which you write scripts that are used to automate processes.

### What processes? Pretty much anything related to IT.


### Now you can explain the architecture of Chef, it consists of
Chef Server: The Chef Server is the central store of your infrastructure's configuration data.The Chef Server stores the data necessary to configure your nodes and provides search, a powerful tool that allows you to dynamically drive node configuration based on data.Chef Node: A Node is any host that is configured using Chef-client.Chef-client runs on your nodes, contacting the Chef Server for the information necessary to configure the node.Since a Node is a machine that runs the Chef-client software, nodes are sometimes referred to as "clients".Chef Workstation: A Chef Workstation is the host you use to modify your cookbooks and other configuration data.

### A resource in Chef
My suggestion is to first define Resource.A Resource represents a piece of infrastructure and its desired state, such as a package that should be installed, a service that should be running, or a file that should be generated.You should explain about the functions of Resource for that include the following points:Describes the desired state for a configuration item.Declares the steps needed to bring that item to the desired state.Specifies a resource type such as package, template, or service.Lists additional details (also known as resource properties), as necessary.Are grouped into recipes, which describe working configurations.

### What do you mean by recipe in Chef
For this answer, I will suggest you to use the above mentioned flow: first define Recipe.A Recipe is a collection of Resources that describes a particular configuration or policy.A Recipe describes everything that is required to configure part of a system.After the definition, explain the functions of Recipes by including the following points:DevOps TrainingInstall and configure software components.Manage files.Deploy applications.Execute other recipes.

### A Cookbook differ from a Recipe in Chef
The answer to this is pretty direct.You can simply say, "a Recipe is a collection of Resources, and primarily configures a software package or some piece of infrastructure.A Cookbook groups together Recipes and other information in a way that is more manageable than having just Recipes alone."

### What happens when you don't specify a Resource's action in Chef
My suggestion is to first give a direct answer: when you don't specify a resource's action, Chef applies the default action.

### Now explain this with an example, the below resource
file 'C:UsersAdministratorchef-reposettings.ini' docontent 'greeting=hello world'end

### Same as the below resource
file 'C:UsersAdministratorchef-reposettings.ini' doaction :createcontent 'greeting=hello world'endbecause: create is the file Resource's default action.

### Ansible module
Modules are considered to be the units of work in Ansible.Each module is mostly standalone and can be written in a standard scripting language such as Python, Perl, Ruby, bash, etc..One of the guiding properties of modules is idempotency, which means that even if an operation is repeated multiple times e.g.upon recovery from an outage, it will always place the system into the same state.

### Playbooks in Ansible
Playbooks are Ansible's configuration, deployment, and orchestration language.They can describe a policy you want your remote systems to enforce, or a set of steps in a general IT process.Playbooks are designed to be human-readable and are developed in a basic text language.At a basic level, playbooks can be used to manage configurations of and deployments to remote machines.

### I see a list of all of the ansible_ variables
Ansible by default gathers "facts" about the machines under management, and these facts can be accessed in Playbooks and in templates.To see a list of all of the facts that are available about a machine, you can run the "setup" module as an ad-hoc action:Ansible -m setup hostnameThis will print out a dictionary of all of the facts that are available for that particular host.

### I set deployment order for applications
WebLogic Server 8.1 allows you to select the load order for applications.See the Application MBean Load Order attribute in Application.WebLogic Server deploys server-level resources (first JDBC and then JMS) before deploying applications.Applications are deployed in this order: connectors, then EJBs, then Web Applications.If the application is an EAR, the individual components are loaded in the order in which they are declared in the application.xml deployment descriptor.

### Can I refresh static components of a deployed application without having to redeploy the entire application
Yes, you can use weblogic.Deployer to specify a component and target a server, using the following syntax:java weblogic.Deployer -adminurl http://admin:7001 -name appname -targets server1,server2 -deploy jsps/*.jsp

### I turn the auto-deployment feature off
The auto-deployment feature checks the applications folder every three seconds to determine whether there are any new applications or any changes to existing applications and then dynamically deploys these changes.The auto-deployment feature is enabled for servers that run in development mode.To disable auto-deployment feature, use one of the following methods to place servers in production mode:In the Administration Console, click the name of the domain in the left pane, then select the Production Mode checkbox in the right pane.At the command line, include the following argument when starting the domain's Administration Server:-Dweblogic.ProductionModeEnabled=trueProduction mode is set for all WebLogic Server instances in a given domain.

### I use the external_stage option
Set -external_stage using weblogic.Deployer if you want to stage the application yourself, and prefer to copy it to its target by your own means.Ansible and Puppet are two of the most popular configuration management tools among DevOps engineers.Learn them and more in our DevOps Masters Program designed by industry experts to certify you as a DevOps Engineer!

# DevOps
## Continuous Monitoring
### Continuous monitoring necessary


### I will suggest you to go with the below mentioned flow
Continuous Monitoring allows timely identification of problems or weaknesses and quick corrective action that helps reduce expenses of an organization.Continuous monitoring provides solution that addresses three operational disciplines known as:continuous auditcontinuous controls monitoringcontinuous transaction inspection

### Nagios
You can answer this question by first mentioning that Nagios is one of the monitoring tools.It is used for Continuous monitoring of systems, applications, services, and business processes etc in a DevOps culture.In the event of a failure, Nagios can alert technical staff of the problem, allowing them to begin remediation processes before outages affect business processes, end-users, or customers.With Nagios, you don't have to explain why an unseen infrastructure outage affect your organization's bottom line.Now once you have defined what is Nagios, you can mention the various things that you can achieve using Nagios.

### By using Nagios you can
Plan for infrastructure upgrades before outdated systems cause failures.Respond to issues at the first sign of a problem.Automatically fix problems when they are detected.Coordinate technical team responses.Ensure your organization's SLAs are being met.Ensure IT infrastructure outages have a minimal effect on your organization's bottom line.Monitor your entire infrastructure and business processes.This completes the answer to this question.Further details like advantages etc.can be added as per the direction where the discussion is headed.

### Nagios works


### I will advise you to follow the below explanation for this answer
Nagios runs on a server, usually as a daemon or service.Nagios periodically runs plugins residing on the same server, they contact hosts or servers on your network or on the internet.One can view the status information using the web interface.You can also receive email or SMS notifications if something happens.The Nagios daemon behaves like a scheduler that runs certain scripts at certain moments.It stores the results of those scripts and will run other scripts if these results change.

### Plugins in Nagios
Begin this answer by defining Plugins.They are scripts (Perl scripts, Shell scripts, etc.) that can run from a command line to check the status of a host or service.Nagios uses the results from Plugins to determine the current status of hosts and services on your network.Once you have defined Plugins, explain why we need Plugins.Nagios will execute a Plugin whenever there is a need to check the status of a host or service.Plugin will perform the check and then simply returns the result to Nagios.Nagios will process the results that it receives from the Plugin and take the necessary actions.

### NRPE (Nagios Remote Plugin Executor) in Nagios
For this answer, give a brief definition of Plugins.The NRPE addon is designed to allow you to execute Nagios plugins on remote Linux/Unix machines.The main reason for doing this is to allow Nagios to monitor "local" resources (like CPU load, memory usage, etc.) on remote machines.Since these public resources are not usually exposed to external machines, an agent like NRPE must be installed on the remote Linux/Unix machines.I will advise you to explain the NRPE architecture on the basis of diagram shown below.

### The NRPE addon consists of two pieces
The check_nrpe plugin, which resides on the local monitoring machine.The NRPE daemon, which runs on the remote Linux/Unix machine.There is a SSL (Secure Socket Layer) connection between monitoring host and remote host as shown in the diagram below.

### What do you mean by passive check in Nagios
According to me, the answer should start by explaining Passive checks.They are initiated and performed by external applications/processes and the Passive check results are submitted to Nagios for processing.Then explain the need for passive checks.They are useful for monitoring services that are Asynchronous in nature and cannot be monitored effectively by polling their status on a regularly scheduled basis.They can also be used for monitoring services that are Located behind a firewall and cannot be checked actively from the monitoring host.

### Nagios Check for external commands
Make sure that you stick to the question during your explanation so I will advise you to follow the below mentioned flow.

### Nagios check for external commands under the following conditions
At regular intervals specified by the command_check_interval option in the main configuration file or,Immediately after event handlers are executed.This is in addition to the regular cycle of external command checks and is done to provide immediate action if an event handler submits commands to Nagios.

### The difference between Active and Passive check in Nagios
For this answer, first point out the basic difference Active and Passive checks.The major difference between Active and Passive checks is that Active checks are initiated and performed by Nagios, while passive checks are performed by external applications.If your interviewer is looking unconvinced with the above explanation then you can also mention some key features of both Active and Passive checks:

### Passive checks are useful for monitoring services that are
Asynchronous in nature and cannot be monitored effectively by polling their status on a regularly scheduled basis.Located behind a firewall and cannot be checked actively from the monitoring host.

### The main features of Actives checks are as follows
Active checks are initiated by the Nagios process.Active checks are run on a regularly scheduled basis.

### Nagios help with Distributed Monitoring
The interviewer will be expecting an answer related to the distributed architecture of Nagios.

### So, I suggest that you answer it in the below mentioned format
With Nagios you can monitor your whole enterprise by using a distributed monitoring scheme in which local slave instances of Nagios perform monitoring tasks and report the results back to a single master.You manage all configuration, notification, and reporting from the master, while the slaves do all the work.This design takes advantage of Nagios's ability to utilize passive checks i.e.external applications or processes that send results back to Nagios.In a distributed configuration, these external applications are other instances of Nagios.

### Explain Main Configuration file of Nagios and its location
First mention what this main configuration file contains and its function.The main configuration file contains a number of directives that affect how the Nagios daemon operates.This config file is read by both the Nagios daemon and the CGIs (It specifies the location of your main configuration file).Now you can tell where it is present and how it is created.A sample main configuration file is created in the base directory of the Nagios distribution when you run the configure script.The default name of the main configuration file is nagios.cfg.It is usually placed in the etc/ subdirectory of you Nagios installation (i.e./usr/local/nagios/etc/).

### Explain how Flap Detection works in Nagios
I will advise you to first explain Flapping first.Flapping occurs when a service or host changes state too frequently, this causes lot of problem and recovery notifications.Once you have defined Flapping, explain how Nagios detects Flapping.Whenever Nagios checks the status of a host or service, it will check to see if it has started or stopped flapping.

### Nagios follows the below given procedure to do that
Storing the results of the last 21 checks of the host or service analyzing the historical check results and determine where state changes/transitions occurUsing the state transitions to determine a percent state change value (a measure of change) for the host or serviceComparing the percent state change value against low and high flapping thresholdsA host or service is determined to have started flapping when its percent state change first exceeds a high flapping threshold.A host or service is determined to have stopped flapping when its percent state goes below a low flapping threshold.

### The three main variables that affect recursion and inheritance in Nagios


### According to me the proper format for this answer should be
First name the variables and then a small explanation of each of these variables:NameUseRegisterThen give a brief explanation for each of these variables.Name is a placeholder that is used by other objects.Use defines the "parent" object whose properties should be used.Register can have a value of 0 (indicating its only a template) and 1 (an actual object).The register value is never inherited.

### Meant by saying Nagios is Object Oriented
Answer to this question is pretty direct.I will answer this by saying, "One of the features of Nagios is object configuration format in that you can create object definitions that inherit properties from other object definitions and hence the name.This simplifies and clarifies relationships between various components."

### State Stalking in Nagios
I will advise you to first give a small introduction on State Stalking.It is used for logging purposes.When Stalking is enabled for a particular host or service, Nagios will watch that host or service very carefully and log any changes it sees in the output of check results.Depending on the discussion between you and interviewer you can also add, "It can be very helpful in later analysis of the log files.Under normal circumstances, the result of a host or service check is only logged if the host or service has changed state since it was last checked."

## Containerization and Virtualization
### Containers
My suggestion is to explain the need for containerization first, containers are used to provide consistent computing environment from a developer's laptop to a test environment, from a staging environment into production.Now give a definition of containers, a container consists of an entire runtime environment: an application, plus all its dependencies, libraries and other binaries, and configuration files needed to run it, bundled into one package.Containerizing the application platform and its dependencies removes the differences in OS distributions and underlying infrastructure.

### The advantages that Containerization provides over virtualization


### Below are the advantages of containerization over virtualization
Containers provide real-time provisioning and scalability but VMs provide slow provisioningContainers are lightweight when compared to VMsVMs have limited performance when compared to containersContainers have better resource utilization compared to VMs

### How exactly are containers (Docker in our case) different from hypervisor virtualization (vSphere)? What are the benefits
Given below are some differences.

### Make sure you include these differences in your answer


### Docker image


### I suggest that you go with the below mentioned flow
Docker image is the source of Docker container.In other words, Docker images are used to create containers.Images are created with the build command, and they'll produce a container when started with run.Images are stored in a Docker registry such as registry.hub.docker.com because they can become quite large, images are designed to be composed of layers of other images, allowing a minimal amount of data to be sent when transferring images over the network.Tip: Be aware of Dockerhub in order to answer questions on pre-available images.

### Docker container
This is a very important question so just make sure you don't deviate from the topic.

### I advise you to follow the below mentioned format
Docker containers include the application and all of its dependencies but share the kernel with other containers, running as isolated processes in user space on the host operating system.Docker containers are not tied to any specific infrastructure: they run on any computer, on any infrastructure, and in any cloud.Now explain how to create a Docker container, Docker containers can be created by either creating a Docker image and then running it or you can use Docker images that are present on the Dockerhub.Docker containers are basically runtime instances of Docker images.

### Docker hub
Answer to this question is pretty direct.Docker hub is a cloud-based registry service which allows you to link to code repositories, build your images and test them, stores manually pushed images, and links to Docker cloud so you can deploy images to your hosts.It provides a centralized resource for container image discovery, distribution and change management, user and team collaboration, and workflow automation throughout the development pipeline.

### How is Docker different from other container technologies


### According to me, below points should be there in your answer
Docker containers are easy to deploy in a cloud.It can get more applications running on the same hardware than other technologies, it makes it easy for developers to quickly create, ready-to-run containerized applications and it makes managing and deploying applications much easier.You can even share containers with your applications.If you have some more points to add you can do that but make sure the above the above explanation is there in your answer.

### Docker Swarm
You should start this answer by explaining Docker Swarn.It is native clustering for Docker which turns a pool of Docker hosts into a single, virtual Docker host.Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.

### I will also suggest you to include some supported tools
DokkuDocker ComposeDocker MachineJenkins

### Dockerfile used for
This answer according to me should begin by explaining the use of Dockerfile.Docker can build images automatically by reading the instructions from a Dockerfile.Now I suggest you to give a small definition of Dockerfle.A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.Using docker build users can create an automated build that executes several command-line instructions in succession.

### Can I use json instead of yaml for my compose file in Docker
You can use json instead of yaml for your compose file, to use json file with compose, specify the filename to use for eg:docker-compose -f docker-compose.json up

### Tell us how you have used Docker in your past position
Explain how you have used Docker to help rapid deployment.Explain how you have scripted Docker and used Docker with other tools like Puppet, Chef or Jenkins.If you have no past practical experience in Docker and have past experience with other tools in similar space, be honest and explain the same.In this case, it makes sense if you can compare other tools to Docker in terms of functionality.

### Create Docker container
I will suggest you to give a direct answer to this.

### We can use Docker image to create Docker container by using the below command
docker run -t -i <image name> <command name>This command will create and start container.You should also add, If you want to check the list of all running container with status on a host use the below command:docker ps -a

### Stop and restart the Docker container


### In order to stop the Docker container you can use the below command
docker stop <container ID>

### Now to restart the Docker container you can use
docker restart <container ID>Course CurriculumDevOps Certification TrainingWeekday / Weekend Batches

### How far do Docker containers scale
Large web deployments like Google and Twitter, and platform providers such as Heroku and dotCloud all run on container technology, at a scale of hundreds of thousands or even millions of containers running in parallel.

### What platforms does Docker run on
I will start this answer by saying Docker runs on only Linux and Cloud platforms and then I will mention the below vendors of Linux:Ubuntu 12.04, 13.04 et alFedora 19/20+RHEL 6.5+CentOS 6+GentooArchLinuxopenSUSE 12.3+CRUX 3.0+

### Cloud
Amazon EC2Google Compute EngineMicrosoft AzureRackspaceNote that Docker does not run on Windows or Mac.

### Do I lose my data when the Docker container exits
You can answer this by saying, no I won't lose my data when the Docker container exits.Any data that your application writes to disk gets preserved in its container until you explicitly delete the container.The file system for the container persists even after the container halts.

# .NET Framework
## .NET
### .NET Framework:
The .NET framework is a programming framework from Microsoft.Developers can use .NET Framework to develop applications, install and run the application on Windows operating systems.

### Advantages Of .NET:
Good Design, Object-Oriented Programming, Language Independence, Efficient Data Access,Code Sharing, Improved Security, Support Dynamic Web Pages and Support for Web Services.

### In detail, the advantages of .NET are
Good DesignObject-Oriented Programming: Using C# and .NET which are based on object-oriented Concepts.Language Independence: All the languages which are supported by .NET (VB .NET, C#, J#, and managed C++) are compiled into common Intermediate Language (IL).So IL makes sure that languages are interoperable.Efficient Data Access: ADO .NET provides fast and efficient way to access RDBMS, file system etc.Code Sharing: To share code between applications, a new concept called assembly is introduced. Assemblies supports versioning.Improved SecuritySupport Dynamic Web Pages: Using ASP .NETSupport for Web Services

## Value Types And Reference Types
### Value Types And Reference Types:
There are two types of data types in .NET, Value types and Reference types.Value types: are stored in stack part of the memory.Reference types: are stored in managed heap.Let have a look at the example for better understanding.Int iCount = 0; Value Typeint NewiCount = iCount; Reference Type

### Boxing And Unboxing:
Boxing: Converting a value type to reference type is called Boxing. Boxing is value to reference.Unboxing: Converting a reference type to value type is called Unboxing. Unboxing is reference back to value.

## Other
### Common Language Specification or CLS:
Common Language Specification (CLS) is used for Language Interoperability intandem with CTS to ensure the interoperability of the languages.CLS defines a set of minimum standards that all compilers targeting dot net must support.For example, VB .NET is not case sensitive.So attribute EmployeeName and employeename is considered same.But C# is case sensitive.So for language interoperability, C# doesn't allow two variables which differ only in case.

### System Exceptions vs Application Exceptions
System exceptions: are common exceptions thrown by the CLR of .NET Framework. System exceptions come from the CLR.Application exceptions: can be user defined exceptions thrown by the application.

### Code Access Security
CODE Access security is a security model that let us grant or deny execution permissions to an assembly according to its "properties," called evidence, such as its strong name or publisher.

### Prevent my .NET DLL from being Decompiled:
We can prevent .NET DLL to be decompiled upto an extent by Obfuscate Source code, asymmetric encryption and encrypted W 32 wrapper application.

### Native Image Generator or ngen.exe:
Ngen.exe creates compiled processor-specific machine code called native images which are files and installs them into the native image cache on the local computer.The runtime will use native images from the cache rather than using the JIT compiler to compile the original assembly.

### Code Document Object Model or code DOM:
Code Document Object Model are code generators which are used to minimize repetitive coding tasks, and to minimize the number of human-generated source code lines.

## Garbage Collector
### Garbage Collector:
Garbage Collector is used in dot net Framework for memory management.While running an application, applications make a request for memory for its internal use.Framework allocates memory from the heap.Once the process is completed, allocated memory needs to be reclaimed for future use.The process of reclaiming unused memory is taken care by the Garbage Collector.

### Invoke Garbage Collector Programmatically:
To call garbage collector from a program, use code GC.Collect()

## JIT
### Types of JIT:
Different Types of JIT are: Pre-JIT, Econo-JIT and Normal-JIT.Pre-JIT: Complies complete source code into native code at the time of deployment.Econo-JIT: Complies methods that are called at runtime.Normal-JIT: Complies methods that are called at runtime and get stored in cache. Next time when the same method is called, it will be taken from cache.

## MSIL
### MSIL or microsoft Intermediate Language:
When a program is complied in .NET, the source code will be converted into an intermediate language called Microsoft Intermediate Language (MS-IL).This is done by Just-In time Compiler (JIT).The dot net framework is built in such a way that the code is Just-In time complied, which means that it get complied when it is called rather than compiling entire code at the start up.A portion of the code will get complied only once and it will exist till the application exit.This will have a significant improvement in performance since the entire section of the code won't get executed in most cases.

### Managed Code:
Managed code is code that can be executed and managed by .NET Framework Common Language Runtime.All codes based on the intermediate language(IL) executes as managed code.

### Common Language Runtime or CLR:
Common Language Runtime or CLR is the run-time execution environment of .NET Framework.Converting MSIL into platform or OS specific code is done by the CLR.Currently, .NET programs will run only on windows.

### Common Type System or CTS:
.NET uses Common Type System (CTS) for Language Interoperability.CTS defines the predefined data types that are available in IL, so that all languages that target the .NET framework will produce the compiled code that is ultimately based on these types.CTS ensures that a data type defined in a VB .NET will be understood by C#.For example, VB .NET uses Integer to define the data type Integer.C# uses int to define the data type Integer.When VB .NET code is compiled, it will convert the Integer to Int32.Since C# refers Int to Int32, VB .NET code will be understood by C#.

## Assemblies and Namespace
### Assembly:
Assemblies are self-describing logical unit which consists of one or more files targeted at dot net.An assembly can be stored across single file such as a single DLL or EXE that includes metadata, or it canbe stored in multiple files.For example, resource files like meta data, DLL's, and an EXE.Assemblies support versioning.

### Assembly Manifest:
Part of the assembly which contains assembly meta data that describes the assembly itself is known as manifest.Assembly manifest contains Assembly Name, Version Number, Culture, Strong name, List of files inside the assembly and Reference information.

### Assembly Types:
The two types of Assemblies are Shared and Private.

### Private Assembly:
Private Assemblies are intended to be used by the program for which it is made for.Reason behind this is that, the application will only load private assemblies that are located in the same folder or in the sub folder of the main executable.

### Shared Assembly:
Shared Assemblies contain Common Libraries which are intended to be used by multiple applications.While making shared assemblies, name collisions and overwriting existing assemblies need to be taken care.Name Collisions can be taken care by strong name.Global assembly cache can be used to avoid assembly overwriting.

### View Assembly Information:
By using Ildasm.exe, which is an MSIL Disassembler one can view attributes, references to other modules and assemblies.The Assembly Version Information is Stored: In the Manifest.

### Namespace:
A namespace is a logical grouping of related classes and types.Every class should have a NameSpace.

### Between Namespace vs Assembly:
Namespace: Forms the logical boundary for a Group of classes. It is a Collection of names where each name is Unique. The namespace must be specified in Project Properties.Assembly: Assemblies are Self-Describing. It is an Output Unit. It is a unit of deployment and is used for versioning. Assemblies contain MSIL code.

### Global Assembly Cache or GAC:
While using shared assemblies, to avoid Assembly being overwritten by a different version of the same assembly, shared assemblies are placed in a special directory subtree of the file system known as the GAC.Placing shared assemblies can only be done by a special .NET Utilities.

### Strong Names and Assemblies:
While using shared assemblies, in order to avoid name collisions strong names are used.Strong Names are based on private key cryptography.Private assemblies are simply given the same name as their main file name.

### Add And Remove an Assembly From the GAC:
To install assembly in Cache, use Gacutil.To run Gacutil, goto "Visual Studio Command Prompt" and type "gacutil -i <assembly_name>", where (assembly_name) is the DLL name of the project.To uninstall assembly, type gacutil -u <assembly name> in Visual Studio Command Prompt.

### Reflection
Reflection is used to dynamically load a class, create object and invoke methods at runtime.It can also be used to read its own meta data to find assemblies, modules and type information at runtime.

### Delay Signing:
To create a strong named assembly and to make sure that this assembly can used by someone else, we partially build this assembly by providing a Public Key.We write this Public Key in the AssemblyInfo.vb OR .cs file.We also add an attribute by the name <Assembly:AssemblyDelaySignAttribute(true)> to the assembly info file.This makes it sure that when we build the assembly, it would be containing the information only about the public key before we deliver it to our clients.This is a partial strong named assembly that we have created, and hence it is called Delayed Assembly.

### A Satellite Assembly
A satellite assembly are used when multilingual (UI) application are created.Satellite assembly is a compiled library that contains localized resources which provides us with the capability of designing and deploying solutions to multiple cultures, rather than hard coding texts, bitmaps etc

## .NET
### .NET Components.
Some components of .NET are theCommon Language Runtime or CLR,.NET Class library,.NET framework,Common Type System,Application domain,and Profiling.

### CLR.
The CLR is the Common Language Runtime.The CLR has application building blocks.An application built using C# gets compiled by its own compiler and is converted into an Intermediate language which is, then, targeted to the CLR.The CLR handles memory management.The CLR handles security checks.The CLR handles thread management.The CLR loads assemblies.The CLR provides a secure execution environment for applications.

### .NET Class Library.
The .NET Class Library has classes to access common functionality.

### .NET framework.
The .NET framework is a platform for building various applications on windows.The .NET framework has a list of inbuilt functionalities in the form of class, library, and APIs which are used to build, deploy and run web services and different applications.The .NET framework supports different languages such as C# VB .NET, Cobol, Perl, etc.The .NET framework supports the object-oriented programming model.

### CTS.
CTS is the Common Type System.The CTS has a set of rules which state how a data type should be declared, defined and used in the program.The CTS describes the data types that are to be used in the application.We can design our own classes and values by following the rules that are present in the CTS.The CTS rules are made so that the data type declared using a programming language can be called by an application that is developed using a different language.

### CLS.
CLS stands for Common Language Specification.With the rules mentioned under CLS, the developers are made to use the components that are inter-language compatible.They are reusable across all the .NET Compliant languages.

### JIT.
JIT stands for Just In Time.JIT is a compiler that converts Intermediate Language to a Native code.The code is converted into Native language during execution.Native code is nothing but hardware specifications that can be read by the C P U.The native code can be stored so that it is accessible for subsequent calls.MSIL.MSIL stands for Microsoft Intermediate Language.The MSIL provides instructions for calling methods, initializing and storing values, operations such as memory handling, exception handling and so on.All .NET codes are first compiled to I L.Managed and Unmanaged code.The code that is managed by the CLR is called Managed code.This code runs inside the CLR.Hence, it is necessary to install the .NET framework in order to execute the managed code.CLR manages the memory through garbage collection and also uses the other features like CAS and CTS for efficient management of the code.Unmanaged code is any code that does not depend on CLR for execution.It means it is developed by any other language independent of .NET framework.It uses its own runtime environment for compiling and execution.Though it is not running inside the CLR, the unmanaged code will work properly if all the other parameters are correctly followed.

### Follow these steps while executing a Managed code
Choose a language compiler depending on the language in which the code is written.Convert the above code into Intermediate language by its own compiler.The IL is then targeted to CLR which converts the code into native code with the help of JIT.Execution of Native code.ASP.NET.ASP.NET is a part of .NET technology and it comprises of CLR, too.ASPstands for Active Server Pages.ASP.NET is an open-source server-side technology that enables the programmers to build powerful web services, websites and web applications.ASP.NET State Management.State Management means maintaining the state of the object.The object here refers to a web page/control.There are two types of State management, Client Side, and Server side.Client-Side Storing the information in the Page or Client's System.They are reusable, simple objects.Server Side Storing the information on the Server.It is easier to maintain the information on the Server rather than depending on the client for preserving the state.Assemblies and Assembly Types.An Assembly is a collection of logical units.Logical units refer to the types and resources which are required to build an application and deploy them using the .NET framework.The CLR uses this information for type implementations.An assembly is a collection of E X Es and D L Ls.It is portable and executable.There are two types of Assemblies, Private and Shared.A Private Assembly: is accessible only to the application.

### Follow these steps while executing a Managed code (part 2)
It is installed in the installation directory of the application.A Shared Assembly: can be shared by multiple applications. It is installed in the GAC.Different parts of an Assembly.Manifest: It contains the information about the version of an assembly.

### Follow these steps while executing a Managed code (part 3)
It is also called as assembly metadata.Type Metadata: Binary information of the program.MSIL: Microsoft Intermediate Language code.E X Es and a D L Ls.E X Es and D L Ls are Assembly executable modules.An E X E is an executable file.This runs the application for which it is designed.An E X E is generated when we build an application.Hence, the assemblies are loaded directly when we run an E X E.However, an Exe cannot be shared with the other applications.D L L stands for Dynamic Link Library.It is a library that consists of code that needs to be hidden.The code is encapsulated inside this library.An application can consist of many D L Ls.These can be shared with the other applications as well.Other applications which share this D L L need not worry about the code intricacies as long as it is able to call the function on this D L L.Caching.Caching means storing data temporarily in the memory so that the application can access the data from the cache instead of looking for its original location.This increases the performance of the application and its speed.System dot Runtime dot Caching namespace is used for Caching information in .NET.Caching Types: Page Caching, Data Caching and Fragment Caching.MVC.MVC stands for Model View Controller.It is an architectural model for building the .NET applications.Models: Model objects store and retrieve data from the database for an application.They are usually the logical parts of an application that is implemented by the application's data domain.Views: These are the components that display the view of the application in the form of UI.The view gets the information from the model objects for their display.They have components like buttons, drop boxes, combo box, etc.Controllers: They handle user interactions.They are responsible for responding to the user inputs, work with the model objects, and pick a view to be rendered to the user.Functions and Stored Procedures.

### Follow these steps while executing a Managed code (part 4)


### Stored Procedure
A Stored Procedure is always used to perform a specific task.It can return zero, one or more value.It can have both input and output parameters.Exception handling can be done using a try-catch block.A function can be called from a Procedure.

### Functions (Part 1)
Functions must return a single value.It can only have the input parameter.Exception handling cannot be done using a try-catch block.A Stored procedure cannot be called from a function.Explain C A S (Code Access Security)..NET provides a security model that prevents unauthorized access to resources.C A S is a part of that security model.C A S is present in the CLR.C A S enables the users to set permissions at a granular level for the code.The CLR then executes the code depending on the available permissions.C A S can be applied only to the managed code.Unmanaged code runs without C A S.If C A S is used on assemblies, then the assembly is treated as partially trusted.Such assemblies must undergo checks every time when it tries to access a resource.The C A S components are: Code group, Permissions and Evidence.Evidence To decide and assign permissions, the CAS and CLR depend on the specified evidence by the assembly.The examination of the assembly provides details about the different pieces of evidence.Some common evidence include Zone, URL, Site, Hash Value, Publisher and Application directory.Code Group Depending on the evidence, codes are put into different groups.Each group has specific conditions attached to it.Any assembly that matches those condition is put into that group.Permissions Each code group can perform only specific actions.They are called Permissions.When CLR loads an assembly, it matches them to one of the code groups and identifies what actions those assemblies can do.Some of the Permissions include Full Trust, Everything, Nothing, Execution, Skip Verification, and the Internet.GAC.GAC stands for Global Assembly Cache.Whenever CLR gets installed on the machine, GAC comes as a part of it.GAC specifically stores those assemblies which will be 

### Functions (Part 2)
shared by many applications.A Developer tool called Gacutil.exe is used to add any file to GAC.Globalization and Localization.Internationalization is the process of designing applications that support multiple languages.This is divided into Localization and Globalization.Globalization is nothing but developing applications to support different languages.Existing applications can also be converted to support multiple cultures.Whereas Localization means changing the already globalized app to cater to a specific culture or language Microsoft dot Extensions dot Localization is used for localizing the app content.Some of the other keywords that are used for Localization are I H T M L Localizer, I String Localizer, I View Localizer and so on.Garbage Collector.Garbage collection is a .NET feature to free the unused code objects in the memory.The memory heap is divided into three generations: Generation 0, Generation 1 and Generation 2.Generation 0  This is used to store short-lived objects.Garbage Collection happens frequently in this Generation.Generation 1  This is for medium-lived objects.Usually, the objects that get moved from generation 0 are stored in this.Generation 2  This is for long-lived objects.Collecting a Generation refers to collecting the objects in that generation and all its younger generations.Garbage collection of Generation 2 means full garbage collection, it collects all the objects in Generation 2 as well as Generation 1 and Generation 0.During the Garbage collection process, as the first phase, the list of live objects is identified.In the second phase, references are updated for those objects which will be compacted.And in the last phase, the space occupied by dead objects are reclaimed.The remaining objects are moved to an older segment.


### Functions (part 2)


### ASP.Net
It is a framework developed by Microsoft on which we can develop new generation web sites using web forms(aspx), MVC, HTML, Javascript, CSS etc.Its successor of Microsoft Active Server Pages(ASP). Currently there is ASP.NET 4.0, which is used to develop web sites.There are various page extensions provided by Microsoft that are being used for web site development.Eg: aspx, asmx, ascx, ashx, cs, vb, html, XML etc.

### The use of Response.Output.Write()
We can write formatted output using Response.Output.Write().

### In which event of page cycle is the ViewState available
After the Init() and before the Page_Load().

### The difference between Server.Transfer and Response.Redirect
In Server.Transfer page processing transfers from one page to the other page without making a round-trip back to the client's browser.This provides a faster response with a little less overhead on the server.The clients url history list or current url Server does not update in case of Server.Transfer.Response.Redirect is used to redirect the user's browser to another page or site.It performs trip back to the client where the client's browser is redirected to the new page.The user's browser history list is updated to reflect the new address.

### From which base class all Web Forms are inherited
Page class.

### The different validators in ASP.NET
Required field ValidatorRange ValidatorCompare ValidatorCustom ValidatorRegular expression ValidatorSummary Validator

### Which validator control you use if you need to make sure the values in two different controls matched
Compare Validator control.

### ViewState
ViewState is used to retain the state of server-side objects between page post backs.

### The viewstate is stored after the page postback
ViewState is stored in a hidden field on the page at client side.ViewState is transported to the client and back to the server, and is not stored on the server or any other external source.

### How long the items in ViewState exists
They exist for the life of the current page.

### The different Session state management options available in ASP.NET
In-ProcessOut-of-Process.In-Process stores the session in memory on the web server.Out-of-Process Session state management stores data in an external server.The external server may be either a SQL Server or a State Server.All objects stored in session are required to be serializable for Out-of-Process state management.

### How you can add an event handler
Using the Attributes property of server side control.e.g.btnSubmit dot Attributes dot Add("onMouseOver","JavascriptCode();")

### Caching
Caching is a technique used to increase performance by keeping frequently accessed data or files in memory.The request for a cached file/data will be accessed from cache instead of actual location of that file.

### The different types of caching


### ASP.NET has 3 kinds of caching
Output Caching,Fragment Caching,Data Caching.

### Which type if caching will be used if we want to cache the portion of a page instead of whole page
Fragment Caching: It caches the portion of the page generated by the request.

### For that, we can create user controls with the below code
<%@  OutputCache Duration="120" VaryByParam="CategoryID;SelectedID"%>List the events in page life cycle.1) Page_PreInit2) Page_Init3) Page_InitComplete4) Page_PreLoad5) Page_Load6) Page_LoadComplete7) Page_PreRender8) Render

### Can we have a web application running without web.Config file
Yes

### It possible to create web application with both webforms and mvc
Yes.We have to include below mvc assembly references in the web forms application to create hybrid application.System dot Web dot MvcSystem dot Web dot RazorSystem dot ComponentModel dot DataAnnotations

### Can we add code files of different languages in App_Code folder
No.The code files must be in same language to be kept in App_code folder.

### Protected Configuration
It is a feature used to secure connection string information.

### Write code to send e-mail from an ASP .NET application
MailMessage mailMess = new MailMessage ();mailMess dot From = "abc @ gmail dot com";mailMess dot To = "xyz @ gmail dot com";mailMess dot Subject = "Test email";mailMess dot Body = "Hi This is a test mail.";SmtpMail dot SmtpServer = "localhost";SmtpMail dot Send (mailMess);MailMessage and SmtpMail are classes defined System dot Web dot Mail namespace.

### We prevent browser from caching an ASPX page
We can SetNoStore on HttpCachePolicy object exposed by the Response object's Cache property:Response dot Cache dot SetNoStore ();Response dot Write (DateTime dot Now dot ToLongTimeString ());

### The good practice to implement validations in aspx page
Client-side validation is the best way to validate data of a web page.It reduces the network traffic and saves server resources.

### Global dot a s a x file Event Handlers


### Application Events
Application_Start,Application_End,Application_AcquireRequestState,Application_AuthenticateRequest,Application_AuthorizeRequest,Application_BeginRequest,Application_Disposed,Application_EndRequest,Application_Error,Application_PostRequestHandlerExecute,Application_PreRequestHandlerExecute,Application_PreSendRequestContent,Application_PreSendRequestHeaders,Application_ReleaseRequestState,Application_ResolveRequestCache,Application_UpdateRequestCache.

### Session Events
Session_Start,Session_End. HTTP Protocol.HTTP Protocol is used to call a Web service.web config and machine config.

### Web config
The Web config file is specific to a web applicationThere can be multiple web config files to an application.

### Machine config
The machine config is specific to a machine or server.There can be only one machine config file on a server.Role based security.Role Based Security is used to implement security based on roles assigned to user groups in the organization.Then we can allow or deny users based on their role in the organization.Windows defines several built-in groups, including Administrators, Users, and Guests.Cross Page Posting.When we click submit button on a web page, the page post the data to the same page.The technique in which we post the data to different pages is called Cross Page posting.This can be achieved by setting POSTBACKURL property of the button that causes the postback.Findcontrol method of PreviousPage can be used to get the posted values on the page to which the page has been posted.

### Apply Themes to an asp.net application
We can specify the theme in web dot config file.

### Code example to apply a theme
<configuration> <system.web> <pages theme="Windows7" /> </system.web> </configuration>RedirectPermanent in ASP.NET.RedirectPermanent Performs a permanent redirection from the requested URL to the specified URL.Once the redirection is done, it also returns 301 Moved Permanently responses.

### MVC
MVC is a framework used to create web applications.The web application base builds on Model-View-Controller pattern which separates the application logic from UI, and the input and events from the user will be controlled by the Controller.Passport authentication.First, it checks passport authentication cookie.If the cookie is not available then the application redirects the user to Passport Sign on page.Passport service authenticates the user details on sign on page and if valid then stores the authenticated cookie on client machine and then redirect the user to requested page.

### Passport authentication advantages
All the websites can be accessed using single login credentials.So no need to remember login credentials for each web site.Users can maintain his/ her information in a single location.

### ASP.NET Security Controls
<asp:Login>: Provides a standard login capability that allows the users to enter their credentials<asp:LoginName>: Allows you to display the name of the logged-in user<asp:LoginStatus>: Displays whether the user is authenticated or not<asp:LoginView>: Provides various login views depending on the selected template<asp:PasswordRecovery>: email the users their lost password

### You register JavaScript for webcontrols
We can register javascript for controls using <CONTROL -name>Attribtues.Add(scriptname,scripttext) method.

### In which event are the controls fully loaded
Page load event.Boxing and Unboxing.Boxing is assigning a value type to reference type variable.Unboxing is reverse of boxing, assigning a reference type variable to a value type variable.

### Strong typing and Weak typing
In strong typing, the data types of variable are checked at compile time. In strong typing, there is no chance of compilation error.In weak typing, the variable data types are checked at runtime.

### Force all the validation controls to run
The Page dot Validate method is used to force all the validation controls to run and to perform validation.

### Repeater Control Templates
Item TemplateAlternating Item TemplateSeparator TemplateHeader TemplateFooter Template

### ASP.NET built-in objects in ASP.NET
Application, Request, Response, Server, Session, Context, Trace.

### The appSettings Section in the web.config file
The appSettings block in web config file sets the user-defined values for the whole application.For example, in the following code snippet, the specified ConnectionString section is used throughout the project for database connection:<em><configuration><appSettings><add key="ConnectionString" value="server=local; pwd=password; database=default" /></appSettings></em>

### Which data type does the RangeValidator control support
The data types supported by the RangeValidator control are Integer, Double, String, Currency, and Date.

### The difference between an HtmlInputCheckBox control and an HtmlInputRadioButton control
In HtmlInputCheckBoxcontrol, multiple item selection is possible whereas in HtmlInputRadioButton controls, we can select only single item from the group of items.

### Which namespaces are necessary to create a localized application
System dot GlobalizationSystem dot Resources

### The different types of cookies in ASP.NET
Session Cookie - Resides on the client machine for a single session until the user does not log out.Persistent Cookie - Resides on a user's machine for a period specified for its expiry, such as 10 days, one month, and never.

### The file extension of web service
Web services have file extension .asmx..

### ADO.NET Components
The components of ADO.NET are Dataset, Data Reader, Data Adaptor, Command, connection.Execute Scalar and Execute Non Query.Execute Scalar returns an output value.ExecuteNonQuery does not return any value. Instead, it returns the number of rows affected by the query.Execute Scalar used for fetching a single value.ExecuteNonQuery used to execute INSERT and UPDATE statements.

# .NET Core
### The Purpose Of the Webhostbuilder() Function
It is use to build up the HTTP pipeline via webHostBuilder.Use() chaining it all together with WebHostBuilder.Build() by using the builder pattern.It is available within the Microsoft.ASP.Hosting namespace.The purpose of the Build method is to build the required services and a Microsoft.ASP.Hosting.IWebHost which hosts a web application.

### Useiisintegration
UseIISIntegration configures the port and base path the server should listen on when running behind ASP.The app will also be configured to capture startup errors.WebHostBuilder uses the UseIISIntegration for hosting in IIS and IIS Express.

### Configureservices In .NET Core 1.0
ConfigureServices defines the services used by the application like ASP .NET MVC Core framework, Entity Framework Core, CORS,Logging, MemoryCaching etc.

### Configure Method
Configure method defines the middleware in the Http request pipeline.The software components that are assembled into an application pipeline to handle requests and responses are the middlewares.Usedeveloperexceptionpage: MethodThis method belongs to the Microsoft.ASP.Builder namespace of USEDeveloperExceptionPage Extensions static class.The purpose of this function is to capture synchronous and asynchronous System.Exception instances from the pipeline and generates HTML error responses.It returns a reference to the app after the operation is completed.We use the UseDeveloperException() extension method to render the exception during the development mode.

### Addsingleton Method
The AddSingleton method, adds a singleton service of the type specified in TService with an implementation type specified in TImplementation to the specified Microsoft.Extensions.DependencyInjection.IServiceCollection.It returns a reference to this instance after the operation has completed.Services can be registered with the container in several ways.In this case we are using Singleton Service by using the AddSingleton<IService, Service>() method.Singleton lifetime services are created the first time they are requested and then every subsequent request will use the same instance.If the application requires singleton behavior, allowing the services container to manage the service's lifetime is recommended instead of implementing the singleton design pattern and managing the object's lifetime in the class.

### Transfer-encoding
The encoding used to transfer the entity to the user.It is set to Chunked indicating that Chunked transfer encoding data transfer mechanism of the Hypertext Transfer Protocol (HTTP) is initiated in which data is sent in a series of "chunks".

### X-sourcefiles
It is the custom header.It contains the base64-encoded path to the source file on disk and is used to link a page's generated output back to that source file.It's only generated for localhost requests.

### Scaffold Model From Existing Database
To scaffold models from existing database in ASP .NET MVC Core, go to Tools > NuGet Package Manager > Package Manager Console

### Now execute following command
Scaffold-DbContext "Server=datbase-PC;Database=TrainingDatabase;Trusted_Connection=True;MultipleActiveResultSets=true;" Microsoft.EntityFrameworkCore.SqlServer -OutputDir ModelsIf you get an error "The term 'Scaffold-DbContext' is not recognized as the name of a cmdlet" , simply Close the Visual Studio and open again.This creates DOT CS files related with all database tables into Models folder of your project.This also creates a database context (in this case the name will be TrainingDatabaseContext.cs as the database name is TrainingDatabase).

### Dependency Injection
Dependency Injection comes as a part of .NET Core Framework and everything is built around it.When you want to use some tool and its services, you usually add the NuGet package and you use one of its extension methods to add the package to the .NET Core's DI container.You can extend the current DI with a container of your choice (AutoFac, StructureMap, CastleWindsor etc).

### Configuration
Configuration is part of Dependency Injection.Use it anywhere in your code with an option to reload on changes of configuration values from sources (appsettings.json, environment variables, command line arguments, etc.).It is also easy to override, extend and customize the Configuration.No more extensive configurations in web.config, the preferred way now is appsettings.json in combination with a mix of Environment variables and cmd-line args.

### Logging
Logging is built-in and you get access to structured logs from the .NET Core host itself to your application.With tools like Serilog, you can extend your logging easily and save your logs to file, Azure, Amazon or any other output provider.You can configure verbosity and log levels via configuration (appsettings.json by default), and you can configure log levels by different categories.

### Startup Process
Everything starts from Program.cspublic static void Main(string[] args){    BuildWebHost(args).Run();}public static IWebHost BuildWebHost(string[] args) =>    WebHost.CreateDefaultBuilder(args)        .UseStartup()        .Build();CreateDefaultBuilder extension method will create a default configuration which will look first into appsettings.json files then will look for Environment variables and at the end, it will use command line arguments.This part will also set up default logger sources (debug and console) and load the settings for logging from appsettings.json.After the CreateDefaultBuilder finishes, then Startup class is executed.First, the constructor code is executed.After that, services are added to DI container via AddServices method that lives in Startup class.After that, an order of middleware that will handle every incoming request is set up.

### DOT CS Proj File
The dot CS proj file is now used as a place where we manage the NuGet packages for your application.File explorer and project explorer are now in sync.For .NET Core projects, you can easily drop a file from file explorer into a project or delete it from the file system and it will be gone from the project.No more source files in a dot c s proj file.You can now edit the dot c s proj file directly without unloading the project.

### Razor Pages
Razor Pages is a new feature of .NET Core that makes coding page-focused scenarios easier and more productive.With Razor Pages, you have this one Razor file (.cshtml), and the code for a single page lives inside of that file, and that file also represents the URL structure of the app (more about this later).Therefore, you got everything inside of one file, and it just works.However, you CAN separate your code to the code behind file with .cshtml.cs extension.You would usually have your view model and handlers (like action methods in MVC) in that file and handle the logic there.Of course, you could also have your view model moved to separate place.Since Razor Pages is part of the MVC stack, you can use anything that comes with MVC inside of our Razor Pages.

### Static Files In .NET Core MVC
All static files are now (by default) located inside of wwwroot folder.You store your CSS, JS, images, fonts  and others static content inside of it.

### Startup.cs
In ASP .NET, Global.asax acts as the entry point for your application.In .NET Core,startup.cs is the entry point for your application.In Startup.cs fileThe constructor loads the AppSettings.json file using ConfigurationBuilder classThe ConfigureServices() method adds the services required by the application.For example, here you add MVC and Entity Framework to the services collection.The Configure() method specifies and configures the services added earlier for application's use.

### Json Files
Some JSON files are: global, launchsettings, appsettings, bungleconfig, project and bowser.global.json: can define solution level settings in global.json filelaunchsettings.json: can define project specific settings associated with each profile Visual Studio is configured to launch the application, including any environment variables that should be used.You can define framework for your project for compliation and debugging for specific profiles.appsettings.json: to store custom application setting, DB connection strings,Logging etcbundleconfig.json: can define the configuration for bundling and minification for the project.project.json: storing all project level configuration settingsbower.json: Bower is a package manager for the web.Bower manages components that contain HTML, CSS, JavaScript, fonts or even image files.Bower installs the right versions of the packages you need and their dependencies

### .NET Core
.NET Core is a newer version of .NET, which is cross-platform, supporting Windows, MacOS and Linux, and can be used in device, cloud, and embedded/IoT scenarios.

### .NET Core characteristics
Flexible deployment: Can be included in your app or installed side-by-side user or machine-wide.Cross-platform: Runs on Windows, MacOS and Linux; can be ported to other OSes. The supported Operating Systems (OS), CPUs and application scenarios will grow over time, provided by Microsoft, other companies, and individuals.Command-line tools: All product scenarios can be exercised at the command-line.Compatible: .NET Core is compatible with .NET Framework, Xamarin and Mono, via the .NET Standard Library.

## ASP .NET Core
### ASP .NET Core Overview
The following example defines 2 inline middleware using app.Use and one using app.Run.The first middleware defined using app.Use writes HTML to response object asynchronously, calls next middleware and again writes closing HTML.And middleware defined using app.Run writes message and then returns.And after app.Run middlware, we defined another inline middleware using app.Use and also using some of the built-in middleware. is the next version of ASP .NET. It is open source andcross-platform framework (supports for Windows, Mac and Linux) suitable forbuilding cloud based internet connected applications like web apps, IoT appsand mobile apps. ASP .NET Core apps can run on .NET Core or on the full .NET Framework.

### The newly introduced functionalities in ASP .NET Core
Read Quick summary of what's changed in ASP .NET Core. ASP .NET Core 2.0is already out and there are few changes and new things introduced. ReadWhat's new in ASP .NET Core 2

### Use ASP .NET Core for Web Application Development
ASP .NET Core is an robust, and feature-rich framework that providesfeatures to develop super-fast APIs for web apps. ASP .NET Core should be prefered for following reason:ASP .NET Core is faster compare to traditional ASP .NET.Cross-platform: Runs on Windows, MacOS and Linux; can be ported to other OSes. The supported Operating Systems (OS), CPUs and application scenarios will grow over time, provided by Microsoft, other companies, and individuals.Flexible deployment: Can be included in your app or installed side-by-side user or machine-wide.

### Use ASP .NET Core for Web Application Development (continued)
Runs on IIS or can be self-hosted in your own process.Built-in support for dependency injection.ASP .NET Core is cloud-ready and has improved support for cloud deployment.Provides Support for Popular JavaScript Frameworks.Unification Of Development Models which allows the MVC and Web API development models to use the same base class Controller.Razor Pages makes coding page-focused scenarios easier and more productive.Environment based configuration supported for cloud deployment.Built in logging support.In ASP .NET we had modules and handlers to deal with requests. In ASP dotNET Core we have middleware which provides more control how the request should be processed as they are executed in the order in which they are added.

### ASP .NET Core Middleware and How it is different from HttpModule
Read my post about How ASP .NET Core 1.0 Middleware is different from HttpModule

### The various JSON files in ASP .NET Core
Read my post about Various JSON files in ASP .NET Core

### Startup.cs
In ASP .NET, Global.asax (though optional) acts as the entry point for yourapplication. Startup.cs, it is entry point for application itself. The Startupclass configures the request pipeline that handles all requests made to theapplication. Read this read this excellent post The Startup.cs File in ASP .NET Core 1.0.

### Startup.cs CongigureServices() Method
This method is optional. It is the place to add services required by the application. For example, if you wish to use Entity Framework in your application then you can add in this method.public void ConfigureServices(IServiceCollection services){    services.Configure<AppSettings>(Configuration.GetSubKey("AppSettings"));    services.AddEntityFramework()            .AddSqlServer()            .AddDbContext<SchoolContext>();    // Add MVC services to the services container.    services.AddMvc();}

### Startup.cs Congigure() Method
The Configure method is used to specify how the ASP .NET application willrespond to HTTP requests. The request pipeline is configured by addingmiddleware components to an IApplicationBuilder instance that is provided bydependency injection. There are some built-in middlewares for error handling,authentication, routing, session and diagnostic purpose. Highlighted lines inbelow code, are built-in Middleware with ASP .NET Core 1.0.

### Services.AddTransient vs service.AddScope methods
SP.NET Core out of the box supports dependency injection.These 3 methods allows to register the dependency.However, they offers different lifetime for registered service.Transient objects are created for every request (when requested).This lifetime works best for lightweight, stateless services.Scoped objects are the same within a request, but different across different requests.Singleton objects created the first time they're requested (or when ConfigureServices is run and an instance is specified with the service registration).

### Kestral
Kestrel is a cross-platform web server for ASP .NET Core based on libuv, a cross-platform asynchronous I/O library.Kestrel is the web server that is included by default in ASP .NET Core new project templates.If your application accepts requests only from an internal network, you can use Kestrel by itself.If you expose your application to the Internet, you must use IIS, Nginx, or Apache as a reverse proxy server.A reverse proxy server receives HTTP requests from the Internet and forwards them to Kestrel after some preliminary handling.The most important reason for using a reverse proxy for edge deployments (exposed to traffic from the Internet) is security.Kestrel is relatively new and does not yet have a full complement of defenses against attacks.WebListenerASP .NET Core ships two server implementations Kestral and WebListener.WebListener is also a web server for ASP .NET Core that runs only on Windows.It's built on the Http.Sys kernel mode driver.WebListener is an alternative to Kestrel that can be used for direct connection to the Internet without relying on IIS as a reverse proxy server.

### ASP .NET Core Module (ANCM)
ASP .NET Core Module (ANCM) lets you run ASP .NET Core applications behind IIS and it works only with Kestrel; it isn't compatible with WebListener.ANCM is a native IIS module that hooks into the IIS pipeline and redirectstraffic to the backend ASP .NET Core application.ASP .NET Core applications run in a process separate from the IIS worker process, ANCM also does process management.ANCM starts the process for the ASP .NET Core application when the first request comes in and restarts it when it crashes.In short, it sits in IIS and routes the request for ASP .NET Core application to Kestral.

## Middleware
### Middleware Overview
The first middleware defined using app.Use writes HTML to response object asynchronously, calls next middleware and again writes closing HTML.And middleware defined using app.Run writes message and then returns.And after app.Run middlware, we defined another inline middleware using app.Use and also using some of the built-in middleware.Diagnostics MiddlewareMiddleware is the heart of an ASP .NET Core application.You can think of middleware as small connectors which makes a pipeline to accept requests and send responses.Anything which your ASP .NET core application does is performed by middleware.Middleware are small application components that can be incorporated into an HTTP request pipeline like HttpHandlers and HttpModules.But middleware are different from HttpModules.ASP .NET Core comes with many built-in and ready to use middleware, and you add them to your application in the Startup.Configure method.These built-in middleware can be classified in the following categories.Built-in MiddlewareAuthentication: Provides authentication support.CORS: Configures Cross-Origin Resource Sharing.Routing: Define and constrain request routes.Session: Provides support for managing user sessions.Routing: Provides support for serving static files, and directory browsing.Diagnostics: Includes support for error pages and runtime information.

### Built-in Middleware Methods
UseDeveloperExceptionPage()UseDatabaseErrorPage()UseExceptionHandler()UseStatusCodePages()UseWelcomePage()UseElmPage() and UseElmCapture()In any ASP .NET Core 1.0 RTM web application, you will find many built-in middleware are already added to the HTTP request pipeline.You can verify this in Startup.cs file -> configure() method.

### Host
ASP .NET Core apps require a host in which to execute.The host is responsible for application startup and lifetime management.Other responsibility of host's includes ensuring the application's services and the server are available and properly configured.Don't confuse yourself with a Server.The host is responsible for starting the app and its management, where the server is responsible for accepting HTTP requests.The host is configured to use a particular server; the server is unaware of its host.The host is typically created using an instance of a WebHostBuilder, which builds and returns a WebHost instance.The WebHost references the server that will handle requests.   var host = new WebHostBuilder() dot UseKestrel() dot UseContentRoot(Directory dot GetCurrentDirectory()) dot UseIISIntegration() dot UseStartup<Startup>() dot Build();   host dot Run();In ASP .NET Core 2.0, it is changed.

### It looks like this
public static void Main(string[] args)    {        BuildWebHost(args).Run();    }    public static IWebHost BuildWebHost(string[] args) => WebHost dot CreateDefaultBuilder(args) dot UseStartup<Startup>() dot Build();}

### WebHost dot CreateDefaultBuilder()
Configure the app to use Kestrel as web server.Specify to use the current project directory as root directory for the application.Setup the configuration sub-system to read setting from appsettings.json and appsettings.{env}.json to environment specific configuration.Set Local user secrets storage only for the development environment.Configure environment variables to allow for server-specific settings.Configure command line arguments (if any).Configure logging to read from the Logging section of the appsettings.json file and log to the Console and Debug window.Configure integration with IISConfigure the default service provider.You can take a look at the code of this method here.

### IHostingEnvironment interface
ASP .NET Core offers an interface named IHostingEnvironment, allows you to programmatically retrieve the current environment so you can have an environment-specific behaviour.By default, ASP .NET Core has 3 environments Development, Staging, and Production.Previously, the developers have to build the application differently for each environment (Staging, UAT, Production) due to dependency on config file sections and the preprocessor directive applicable at compile time.ASP .NET Core takes a different approach and uses IHostingEnvironment to retrieve the current environment.You can also define a custom environment like QA or UAT.

### Handle 404 error
To handle the error, both the solution are using configure() method ofStartup.cs class. For those who are not aware about Startup.cs, it is entrypoint for application itself. You can read this excellent post The Startup.csFile in ASP .NET Core 1.0. to know more about startup.cs. And within thestartup.cs file, you will also find static void main() which generally you usewith windows/console applications. Read my post Why static void main in ASP.NET 5 startup.csNow coming back to our solution 1, within configure method define a custom middleware via app.Use which checks for status code value in response object. And if is 404 then it redirects to Home controller. See highlighted code.Solution 2The other solution is to use a built-in middlware StatusCodePagesMiddleware. This middleware can be used to handle the response status code is between 400 and 600. This middleware allows to return a generic error response or allows you to also redirect to any controller action or another middleware. See below all different variations of this middleware.

### ...UseIISIntegration
This tells ASP .NET that IIS will be working as a reverse proxy in front ofKestrel. As if you expose your application to the Internet, you must use IIS,Nginx, or Apache as a reverse proxy server. When you wish to deploy your ASP.NET Core application on windows, you need to tell ASP .NET Core Host to use IIS integration.UseKestrel and UseIISIntegration must be used in conjunction as UseKestrel creates the web server and hosts the code. UseIISIntegration specifies IIS as the reverse proxy server.var host = new WebHostBuilder()         .UseKestrel()         .UseContentRoot(Directory.GetCurrentDirectory())         .UseIISIntegration()         .UseStartup<Startup>()         .Build();Note that code making call to UseIISIntegration() does not affect code portability.

### Bundling and minification
Use Gulp, BundlerMinifier, Web Optimizer or Grunt.

### Gulp
Gulp was the default choice for ASP .NET Core till beta versions. Later it was removed due to performance and speed issue and replaced with BundlerMinifier. Read this post to find out the reasons of this decision.

### BundlerMinifier
BundleMinifier is a Visual Studio extension and it's default choice now. Youshould see bundleconfig.json file in your default template. Read this post toknow more about bundling and minification in ASP .NET Core.

### ASP .NET Core Web Optimizer
ASP .NET Core middleware for bundling and minification of CSS and JavaScript files at runtime.

### Grunt
Grunt can also be used with ASP .NET Core.

### Launchsetting.json
Holds project specific settings associated with each debug profile, Visual Studio is configured to use to launch the application, including any environment variables that should be used.You can define framework for your project for compilation and debugging for specific profiles.This file is placed in Properties folder.

### Wwwroot folder
In ASP .NET Core, all the static resources, such as CSS, JavaScript, and image files are kept under the wwwroot folder (default).You can also change the name of this folder.

### Razor pages
Razor Pages is a new feature of ASP .NET Core and it was released with ASP.NET Core 2.0 release.Razor Pages are simple pages or views without controllers and introduced with the intent of creating page focused scenarios where there is no real logic is involved.You will find razor pages similar to ASP .NET Web Forms.They work on the convention and need to be placed in Pages folder and the extension is .cshtml.Razor pages uses handler methods to deal with incoming HTTP request.Read this post to find out more about handler methods.

### Tag helper
Tag Helpers enable server-side code to participate in creating and renderingHTML elements in Razor files. For example, the built-in ImageTagHelper canappend a version number to the image name. There are many built-in tag helperslike From, Image, Anchor and many others. Read How to use image tag helper inASP .NET Core and How to use select tag helper in ASP .NET Core. Read more about Tag Helpers @ official documentation.

### New in .NET Core 2.1 and ASP .NET Core 2.1
ASP .NET Core 2.1 introduces supports for SignalR, HTTPS by default, introduction of HttpClientFactory and many other.https://www.talkingdotnet.com/quick-summary-whats-new-asp-net-core-2-1/

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0
1) ASP .NET CORE MVC 1.0 is Cross Platform.2) ASP .NET Core MVC 1.0 is Cloud Ready.3) MVC + Web API + Web Pages = ASP .NET Core MVC 1.04) ASP .NET Core MVC 1.0 doesn't need IIS for hosting.Since ASP .NET Core is to cross platform so you can host ASP .NET 5 applications not only on IIS but they can be self hosted or use kestrel web server on linux.5) ASP .NET Core MVC 1.0 has inbuilt support for Dependency Injection.ASP .NET Core MVC includes a simple built-in container (represented by the IServiceProvider interface) that supports constructor injection by default, and MVC makes certain services available through DI.6) ASP .NET Core MVC 1.0 has a new project solution structure.There is no App_Start, App_Data, Global.asax and root web.config file.App_Start is replaced by Startup.cs and web.config is replaced by appsetting.json.There is also a new configuration system, where JSON is preferred over XML for configuration settings.7) Roslyn compiler for compiling code dynamically.Now no need to compile your code, on any code changes that you make. Thanks to Roslyn in memory compilation.

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0 (part 2)
Just make changes -> save it and view in browser.8) In ASP .NET Core MVC 1.0 "wwwroot" is now place for static files.wwwroot directory in project is for static content like css, Js, images.And it's the default root of your server.If a request comes in for a static file on disk, if the file is in this folder then it can go back to client.The name can be changed from project.json file.9) The new Project.json file defines dependencies, runtime to use, and definesbuild and publish setup, instead of dot c s proj file.10) Everything is Nuget package in Core MVC 1.0. There is no dll by default.11) Bundling and minification is done using Grunt or Gulp, unlike defining bundles in BundleConfig file.12) Manage client side dependencies via NPM and Bower.13) ASP .NET MVC 5 Child actions are gone.

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0 (part 3)
They are now replaced with View Components.14) Introduction of _ViewImports.cshtml in Core MVC 1.0It provides namespaces which can be used by all other views.In previous MVC projects, this was provided by the web.config file in the Views folder; since the web.config no longer exists, global namespaces are now provided by this file.15) Introduction of Tag helpers.Tag Helpers allows to enable server-side code to participate in creating and rendering HTML elements in Razor files.16) It also support RESTful style routes with attribute routingThat means you can even declare RESTful like routes like [HttpGet("Our Route")] and [HttpPost("Our Route")]17) In Core MVC 1.0, routes have new [controller] and [action] tokens.These tokens allows you to reference controller and action names in the route template.These token are helpful when in future if you rename the controller or action, there is no need to update the routes.

### .NET Core
A cross-platform version of .NET, that supports almost all things that .NET supported (except things like WPF, Windows Forms, Web Forms and Active Directory)It is leaner, faster and improved version of .NET .NET Core and .NET Core are FREE and Open Source but also they are supported by Microsoft.It is kinda the new .NET frameworkMain framework that Microsoft has been focusing on is .NET CoreThe .NET Core Runtime installation file is only about 20 MBs .NET Core provides .NET CLI command line interface.NET Core is a brand new cross-platform web framework built with .NET Core framework.It is not an update to existing ASP .NET framework.It is a complete rewrite of the ASP .NET framework.It was built from scratch in the effort to make a modular, scalable, super fast, configurable, cross-platform and easily extended web framework..NET Core (on Linux!) itself can handle over 2 Million requests per second for plaintext request/response scenarios..NET Core MVC can handle over 1 million requests per second!

### .NET Core (part 2)
Compared to Node.js, which can handle about 400 000 requests per second, this is an amazing effort.It works with .NET Framework..NET Core is much cleaner and easier to work with.You only need to write 20 to 30 lines of code and you have the web server ready to run.It also works smoothly with your file system, so can just copy and paste files to your project folder.And no, you don't need to reference these files from a DOT CS proj file..NET Core Characteristics- DI Container which is quite simple and built-in: You can extend it with other popular DI containers.- Built-in and extensible structured logging: You can redirect output to as many sources as you want (file, Azure, AWS, console).- Extensible strongly typed configuration, which can also be used to reload at run-time.- Kestrel  new, cross-platform and super fast web server which can stand alone without IIS, Nginx or Apache.- New, fully async pipeline: It is easily configured via middleware.- ASP .NET All meta package which improves development speed, and enables you to reference all Microsoft packages for .NET Core and it will deploy only those that are being used by your code.- There is no web.config: We now use appsettings.json file in combination with other sources of configuration (command line args, environment variables, etc.)- There is no Global.asax: We have Startup.cs which is used to set up Middleware and services for DI Container.

### .NET Core (part 3)


### .NET Standard
.NET Standard is a set of APIs that all .NET platforms have to implement. This unifies the .NET platforms and prevents future fragmentation. .NET Standard 2.0 is implemented by .NET Framework, .NET Core, and Xamarin. For .NET Core, this added many of the existing APIs that have been requested. .NET Standard 2.0 includes a compatibility shim for .NET Framework binaries, significantly increasing the set of libraries that you can reference from your .NET Standard libraries. .NET Standard will replace Portable Class Libraries (PCLs) as the tooling story for building multi-platform .NET libraries..NET Core advantages: NuGet-based, Well layered and Free of problematic technology.

### - NuGet-based
.NET Core is distributed as a set of NuGet packages that allow app-local deployments.In contrast, the .NET Framework is always installed in a system-wide location.This difference doesn't matter so much for class libraries; but it matters for applications as those are expected to deploy the closure of their dependencies.But we expect this model to change how quickly class library authors can take advantage of new functionality.Since the applications can simply deploy a new version (as opposed to having to wait until a given .NET Framework version is widely adopted), there is less of a penalty for component authors to take advantage of the latest features.

### - Well layered
.NET Core was specifically designed to be layered.The goal was to create a .NET stack that can accommodate a wide variety of capabilities and system constraints without forcing customers to recompile their binaries and/or produce new assets.This means that we had to remove certain APIs because they tied lower level components to higher level components.In those cases, we provide alternatives, often in the form of extension methods.

### - Free of problematic tech
.NET Core doesn't include certain technologies we decided to discontinue because we found them to be problematic, for instance AppDomain and sandboxing.If the scenario still makes sense for .NET Core, our plan is to have replacements.For example, AssemblyLoadContext replaces AppDomains for loading and isolating assemblies.Discontinuted Technologies: Reflection, Appdomain, Remoting, Binary serialization and Sandboxing.

### Nuget Packages: Advantages Of inclusion in .NET Core 1.0
The inclusion of Nuget Packages will make the applications to be optimized as we need to include only those packages that we need.

### The benefits includes
Better performance gainSecured ApplicationImproved and reduced servicingPay for what you use modelLightweight

### .NET Core 1.0
.NET Core1.0 is the next version of ASP .NET which is 5.0.It is open source and cross-platform framework (supports for Windows, Mac and Linux) suitable for building cloud based internet connected applications like web apps, IoT apps and mobile apps. .NET Core has made itself independent of System.Web.dll and is heavily based on the modular NuGet packages.

### The Purpose Of the Webhostbuilder() Function
It is use to build up the HTTP pipeline via webHostBuilder.Use() chaining it all together with WebHostBuilder.Build() by using the builder pattern.It is available within the Microsoft.ASP.Hosting namespace.The purpose of the Build method is to build the required services and a Microsoft.ASP.Hosting.IWebHost which hosts a web application.

### Useiisintegration
UseIISIntegration configures the port and base path the server should listen on when running behind ASP.The app will also be configured to capture startup errors.WebHostBuilder uses the UseIISIntegration for hosting in IIS and IIS Express.

### Configureservices In .NET Core 1.0
ConfigureServices defines the services used by the application like ASP .NET MVC Core framework, Entity Framework Core, CORS,Logging, MemoryCaching etc.

### Configure Method
Configure method defines the middleware in the Http request pipeline.The software components that are assembled into an application pipeline to handle requests and responses are the middlewares.Usedeveloperexceptionpage: MethodThis method belongs to the Microsoft.ASP.Builder namespace of USEDeveloperExceptionPage Extensions static class.The purpose of this function is to capture synchronous and asynchronous System.Exception instances from the pipeline and generates HTML error responses.It returns a reference to the app after the operation is completed.We use the UseDeveloperException() extension method to render the exception during the development mode.

### Addsingleton Method
The AddSingleton method, adds a singleton service of the type specified in TService with an implementation type specified in TImplementation to the specified Microsoft.Extensions.DependencyInjection.IServiceCollection.It returns a reference to this instance after the operation has completed.Services can be registered with the container in several ways.In this case we are using Singleton Service by using the AddSingleton<IService, Service>() method.Singleton lifetime services are created the first time they are requested and then every subsequent request will use the same instance.If the application requires singleton behavior, allowing the services container to manage the service's lifetime is recommended instead of implementing the singleton design pattern and managing the object's lifetime in the class.

### Transfer-encoding
The encoding used to transfer the entity to the user.It is set to Chunked indicating that Chunked transfer encoding data transfer mechanism of the Hypertext Transfer Protocol (HTTP) is initiated in which data is sent in a series of "chunks".

### X-sourcefiles
It is the custom header.It contains the base64-encoded path to the source file on disk and is used to link a page's generated output back to that source file.It's only generated for localhost requests.

### Scaffold Model From Existing Database
To scaffold models from existing database in ASP .NET MVC Core, go to Tools > NuGet Package Manager > Package Manager Console

### Now execute following command
Scaffold-DbContext "Server=datbase-PC;Database=TrainingDatabase;Trusted_Connection=True;MultipleActiveResultSets=true;" Microsoft.EntityFrameworkCore.SqlServer -OutputDir ModelsIf you get an error "The term 'Scaffold-DbContext' is not recognized as the name of a cmdlet" , simply Close the Visual Studio and open again.This creates DOT CS files related with all database tables into Models folder of your project.This also creates a database context (in this case the name will be TrainingDatabaseContext.cs as the database name is TrainingDatabase).

### Dependency Injection
Dependency Injection comes as a part of .NET Core Framework and everything is built around it.When you want to use some tool and its services, you usually add the NuGet package and you use one of its extension methods to add the package to the .NET Core's DI container.You can extend the current DI with a container of your choice (AutoFac, StructureMap, CastleWindsor etc).

### Configuration
Configuration is part of Dependency Injection.Use it anywhere in your code with an option to reload on changes of configuration values from sources (appsettings.json, environment variables, command line arguments, etc.).It is also easy to override, extend and customize the Configuration.No more extensive configurations in web.config, the preferred way now is appsettings.json in combination with a mix of Environment variables and cmd-line args.

### Logging
Logging is built-in and you get access to structured logs from the .NET Core host itself to your application.With tools like Serilog, you can extend your logging easily and save your logs to file, Azure, Amazon or any other output provider.You can configure verbosity and log levels via configuration (appsettings.json by default), and you can configure log levels by different categories.

### Startup Process
Everything starts from Program.cspublic static void Main(string[] args){    BuildWebHost(args).Run();}public static IWebHost BuildWebHost(string[] args) =>    WebHost.CreateDefaultBuilder(args)        .UseStartup()        .Build();CreateDefaultBuilder extension method will create a default configuration which will look first into appsettings.json files then will look for Environment variables and at the end, it will use command line arguments.This part will also set up default logger sources (debug and console) and load the settings for logging from appsettings.json.After the CreateDefaultBuilder finishes, then Startup class is executed.First, the constructor code is executed.After that, services are added to DI container via AddServices method that lives in Startup class.After that, an order of middleware that will handle every incoming request is set up.

### DOT CS Proj File
The dot CS proj file is now used as a place where we manage the NuGet packages for your application.File explorer and project explorer are now in sync.For .NET Core projects, you can easily drop a file from file explorer into a project or delete it from the file system and it will be gone from the project.No more source files in a dot c s proj file.You can now edit the dot c s proj file directly without unloading the project.

### Razor Pages
Razor Pages is a new feature of .NET Core that makes coding page-focused scenarios easier and more productive.With Razor Pages, you have this one Razor file (.cshtml), and the code for a single page lives inside of that file, and that file also represents the URL structure of the app (more about this later).Therefore, you got everything inside of one file, and it just works.However, you CAN separate your code to the code behind file with .cshtml.cs extension.You would usually have your view model and handlers (like action methods in MVC) in that file and handle the logic there.Of course, you could also have your view model moved to separate place.Since Razor Pages is part of the MVC stack, you can use anything that comes with MVC inside of our Razor Pages.

### Static Files In .NET Core MVC
All static files are now (by default) located inside of wwwroot folder.You store your CSS, JS, images, fonts  and others static content inside of it.

### Startup.cs
In ASP .NET, Global.asax acts as the entry point for your application.In .NET Core,startup.cs is the entry point for your application.In Startup.cs fileThe constructor loads the AppSettings.json file using ConfigurationBuilder classThe ConfigureServices() method adds the services required by the application.For example, here you add MVC and Entity Framework to the services collection.The Configure() method specifies and configures the services added earlier for application's use.

### Json Files
Some JSON files are: global, launchsettings, appsettings, bungleconfig, project and bowser.global.json: can define solution level settings in global.json filelaunchsettings.json: can define project specific settings associated with each profile Visual Studio is configured to launch the application, including any environment variables that should be used.You can define framework for your project for compliation and debugging for specific profiles.appsettings.json: to store custom application setting, DB connection strings,Logging etcbundleconfig.json: can define the configuration for bundling and minification for the project.project.json: storing all project level configuration settingsbower.json: Bower is a package manager for the web.Bower manages components that contain HTML, CSS, JavaScript, fonts or even image files.Bower installs the right versions of the packages you need and their dependencies

### .NET Core
.NET Core is a newer version of .NET, which is cross-platform, supporting Windows, MacOS and Linux, and can be used in device, cloud, and embedded/IoT scenarios.

### .NET Core characteristics
Flexible deployment: Can be included in your app or installed side-by-side user or machine-wide.Cross-platform: Runs on Windows, MacOS and Linux; can be ported to other OSes. The supported Operating Systems (OS), CPUs and application scenarios will grow over time, provided by Microsoft, other companies, and individuals.Command-line tools: All product scenarios can be exercised at the command-line.Compatible: .NET Core is compatible with .NET Framework, Xamarin and Mono, via the .NET Standard Library.

## ASP .NET Core
### ASP .NET Core Overview
The following example defines 2 inline middleware using app.Use and one using app.Run.The first middleware defined using app.Use writes HTML to response object asynchronously, calls next middleware and again writes closing HTML.And middleware defined using app.Run writes message and then returns.And after app.Run middlware, we defined another inline middleware using app.Use and also using some of the built-in middleware. is the next version of ASP .NET. It is open source andcross-platform framework (supports for Windows, Mac and Linux) suitable forbuilding cloud based internet connected applications like web apps, IoT appsand mobile apps. ASP .NET Core apps can run on .NET Core or on the full .NET Framework.

### The newly introduced functionalities in ASP .NET Core
Read Quick summary of what's changed in ASP .NET Core. ASP .NET Core 2.0is already out and there are few changes and new things introduced. ReadWhat's new in ASP .NET Core 2

### Use ASP .NET Core for Web Application Development
ASP .NET Core is an robust, and feature-rich framework that providesfeatures to develop super-fast APIs for web apps. ASP .NET Core should be prefered for following reason:ASP .NET Core is faster compare to traditional ASP .NET.Cross-platform: Runs on Windows, MacOS and Linux; can be ported to other OSes. The supported Operating Systems (OS), CPUs and application scenarios will grow over time, provided by Microsoft, other companies, and individuals.Flexible deployment: Can be included in your app or installed side-by-side user or machine-wide.

### Use ASP .NET Core for Web Application Development (continued)
Runs on IIS or can be self-hosted in your own process.Built-in support for dependency injection.ASP .NET Core is cloud-ready and has improved support for cloud deployment.Provides Support for Popular JavaScript Frameworks.Unification Of Development Models which allows the MVC and Web API development models to use the same base class Controller.Razor Pages makes coding page-focused scenarios easier and more productive.Environment based configuration supported for cloud deployment.Built in logging support.In ASP .NET we had modules and handlers to deal with requests. In ASP dotNET Core we have middleware which provides more control how the request should be processed as they are executed in the order in which they are added.

### ASP .NET Core Middleware and How it is different from HttpModule
Read my post about How ASP .NET Core 1.0 Middleware is different from HttpModule

### The various JSON files in ASP .NET Core
Read my post about Various JSON files in ASP .NET Core

### Startup.cs
In ASP .NET, Global.asax (though optional) acts as the entry point for yourapplication. Startup.cs, it is entry point for application itself. The Startupclass configures the request pipeline that handles all requests made to theapplication. Read this read this excellent post The Startup.cs File in ASP .NET Core 1.0.

### Startup.cs CongigureServices() Method
This method is optional. It is the place to add services required by the application. For example, if you wish to use Entity Framework in your application then you can add in this method.public void ConfigureServices(IServiceCollection services){    services.Configure<AppSettings>(Configuration.GetSubKey("AppSettings"));    services.AddEntityFramework()            .AddSqlServer()            .AddDbContext<SchoolContext>();    // Add MVC services to the services container.    services.AddMvc();}

### Startup.cs Congigure() Method
The Configure method is used to specify how the ASP .NET application willrespond to HTTP requests. The request pipeline is configured by addingmiddleware components to an IApplicationBuilder instance that is provided bydependency injection. There are some built-in middlewares for error handling,authentication, routing, session and diagnostic purpose. Highlighted lines inbelow code, are built-in Middleware with ASP .NET Core 1.0.

### Services.AddTransient vs service.AddScope methods
SP.NET Core out of the box supports dependency injection.These 3 methods allows to register the dependency.However, they offers different lifetime for registered service.Transient objects are created for every request (when requested).This lifetime works best for lightweight, stateless services.Scoped objects are the same within a request, but different across different requests.Singleton objects created the first time they're requested (or when ConfigureServices is run and an instance is specified with the service registration).

### Kestral
Kestrel is a cross-platform web server for ASP .NET Core based on libuv, a cross-platform asynchronous I/O library.Kestrel is the web server that is included by default in ASP .NET Core new project templates.If your application accepts requests only from an internal network, you can use Kestrel by itself.If you expose your application to the Internet, you must use IIS, Nginx, or Apache as a reverse proxy server.A reverse proxy server receives HTTP requests from the Internet and forwards them to Kestrel after some preliminary handling.The most important reason for using a reverse proxy for edge deployments (exposed to traffic from the Internet) is security.Kestrel is relatively new and does not yet have a full complement of defenses against attacks.WebListenerASP .NET Core ships two server implementations Kestral and WebListener.WebListener is also a web server for ASP .NET Core that runs only on Windows.It's built on the Http.Sys kernel mode driver.WebListener is an alternative to Kestrel that can be used for direct connection to the Internet without relying on IIS as a reverse proxy server.

### ASP .NET Core Module (ANCM)
ASP .NET Core Module (ANCM) lets you run ASP .NET Core applications behind IIS and it works only with Kestrel; it isn't compatible with WebListener.ANCM is a native IIS module that hooks into the IIS pipeline and redirectstraffic to the backend ASP .NET Core application.ASP .NET Core applications run in a process separate from the IIS worker process, ANCM also does process management.ANCM starts the process for the ASP .NET Core application when the first request comes in and restarts it when it crashes.In short, it sits in IIS and routes the request for ASP .NET Core application to Kestral.

## Middleware
### Middleware Overview
The first middleware defined using app.Use writes HTML to response object asynchronously, calls next middleware and again writes closing HTML.And middleware defined using app.Run writes message and then returns.And after app.Run middlware, we defined another inline middleware using app.Use and also using some of the built-in middleware.Diagnostics MiddlewareMiddleware is the heart of an ASP .NET Core application.You can think of middleware as small connectors which makes a pipeline to accept requests and send responses.Anything which your ASP .NET core application does is performed by middleware.Middleware are small application components that can be incorporated into an HTTP request pipeline like HttpHandlers and HttpModules.But middleware are different from HttpModules.ASP .NET Core comes with many built-in and ready to use middleware, and you add them to your application in the Startup.Configure method.These built-in middleware can be classified in the following categories.Built-in MiddlewareAuthentication: Provides authentication support.CORS: Configures Cross-Origin Resource Sharing.Routing: Define and constrain request routes.Session: Provides support for managing user sessions.Routing: Provides support for serving static files, and directory browsing.Diagnostics: Includes support for error pages and runtime information.

### Built-in Middleware Methods
UseDeveloperExceptionPage()UseDatabaseErrorPage()UseExceptionHandler()UseStatusCodePages()UseWelcomePage()UseElmPage() and UseElmCapture()In any ASP .NET Core 1.0 RTM web application, you will find many built-in middleware are already added to the HTTP request pipeline.You can verify this in Startup.cs file -> configure() method.

### Host
ASP .NET Core apps require a host in which to execute.The host is responsible for application startup and lifetime management.Other responsibility of host's includes ensuring the application's services and the server are available and properly configured.Don't confuse yourself with a Server.The host is responsible for starting the app and its management, where the server is responsible for accepting HTTP requests.The host is configured to use a particular server; the server is unaware of its host.The host is typically created using an instance of a WebHostBuilder, which builds and returns a WebHost instance.The WebHost references the server that will handle requests.   var host = new WebHostBuilder() dot UseKestrel() dot UseContentRoot(Directory dot GetCurrentDirectory()) dot UseIISIntegration() dot UseStartup<Startup>() dot Build();   host dot Run();In ASP .NET Core 2.0, it is changed.

### It looks like this
public static void Main(string[] args)    {        BuildWebHost(args).Run();    }    public static IWebHost BuildWebHost(string[] args) => WebHost dot CreateDefaultBuilder(args) dot UseStartup<Startup>() dot Build();}

### WebHost dot CreateDefaultBuilder()
Configure the app to use Kestrel as web server.Specify to use the current project directory as root directory for the application.Setup the configuration sub-system to read setting from appsettings.json and appsettings.{env}.json to environment specific configuration.Set Local user secrets storage only for the development environment.Configure environment variables to allow for server-specific settings.Configure command line arguments (if any).Configure logging to read from the Logging section of the appsettings.json file and log to the Console and Debug window.Configure integration with IISConfigure the default service provider.You can take a look at the code of this method here.

### IHostingEnvironment interface
ASP .NET Core offers an interface named IHostingEnvironment, allows you to programmatically retrieve the current environment so you can have an environment-specific behaviour.By default, ASP .NET Core has 3 environments Development, Staging, and Production.Previously, the developers have to build the application differently for each environment (Staging, UAT, Production) due to dependency on config file sections and the preprocessor directive applicable at compile time.ASP .NET Core takes a different approach and uses IHostingEnvironment to retrieve the current environment.You can also define a custom environment like QA or UAT.

### Handle 404 error
To handle the error, both the solution are using configure() method ofStartup.cs class. For those who are not aware about Startup.cs, it is entrypoint for application itself. You can read this excellent post The Startup.csFile in ASP .NET Core 1.0. to know more about startup.cs. And within thestartup.cs file, you will also find static void main() which generally you usewith windows/console applications. Read my post Why static void main in ASP.NET 5 startup.csNow coming back to our solution 1, within configure method define a custom middleware via app.Use which checks for status code value in response object. And if is 404 then it redirects to Home controller. See highlighted code.Solution 2The other solution is to use a built-in middlware StatusCodePagesMiddleware. This middleware can be used to handle the response status code is between 400 and 600. This middleware allows to return a generic error response or allows you to also redirect to any controller action or another middleware. See below all different variations of this middleware.

### ...UseIISIntegration
This tells ASP .NET that IIS will be working as a reverse proxy in front ofKestrel. As if you expose your application to the Internet, you must use IIS,Nginx, or Apache as a reverse proxy server. When you wish to deploy your ASP.NET Core application on windows, you need to tell ASP .NET Core Host to use IIS integration.UseKestrel and UseIISIntegration must be used in conjunction as UseKestrel creates the web server and hosts the code. UseIISIntegration specifies IIS as the reverse proxy server.var host = new WebHostBuilder()         .UseKestrel()         .UseContentRoot(Directory.GetCurrentDirectory())         .UseIISIntegration()         .UseStartup<Startup>()         .Build();Note that code making call to UseIISIntegration() does not affect code portability.

### Bundling and minification
Use Gulp, BundlerMinifier, Web Optimizer or Grunt.

### Gulp
Gulp was the default choice for ASP .NET Core till beta versions. Later it was removed due to performance and speed issue and replaced with BundlerMinifier. Read this post to find out the reasons of this decision.

### BundlerMinifier
BundleMinifier is a Visual Studio extension and it's default choice now. Youshould see bundleconfig.json file in your default template. Read this post toknow more about bundling and minification in ASP .NET Core.

### ASP .NET Core Web Optimizer
ASP .NET Core middleware for bundling and minification of CSS and JavaScript files at runtime.

### Grunt
Grunt can also be used with ASP .NET Core.

### Launchsetting.json
Holds project specific settings associated with each debug profile, Visual Studio is configured to use to launch the application, including any environment variables that should be used.You can define framework for your project for compilation and debugging for specific profiles.This file is placed in Properties folder.

### Wwwroot folder
In ASP .NET Core, all the static resources, such as CSS, JavaScript, and image files are kept under the wwwroot folder (default).You can also change the name of this folder.

### Razor pages
Razor Pages is a new feature of ASP .NET Core and it was released with ASP.NET Core 2.0 release.Razor Pages are simple pages or views without controllers and introduced with the intent of creating page focused scenarios where there is no real logic is involved.You will find razor pages similar to ASP .NET Web Forms.They work on the convention and need to be placed in Pages folder and the extension is .cshtml.Razor pages uses handler methods to deal with incoming HTTP request.Read this post to find out more about handler methods.

### Tag helper
Tag Helpers enable server-side code to participate in creating and renderingHTML elements in Razor files. For example, the built-in ImageTagHelper canappend a version number to the image name. There are many built-in tag helperslike From, Image, Anchor and many others. Read How to use image tag helper inASP .NET Core and How to use select tag helper in ASP .NET Core. Read more about Tag Helpers @ official documentation.

### New in .NET Core 2.1 and ASP .NET Core 2.1
ASP .NET Core 2.1 introduces supports for SignalR, HTTPS by default, introduction of HttpClientFactory and many other.https://www.talkingdotnet.com/quick-summary-whats-new-asp-net-core-2-1/

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0
1) ASP .NET CORE MVC 1.0 is Cross Platform.2) ASP .NET Core MVC 1.0 is Cloud Ready.3) MVC + Web API + Web Pages = ASP .NET Core MVC 1.04) ASP .NET Core MVC 1.0 doesn't need IIS for hosting.Since ASP .NET Core is to cross platform so you can host ASP .NET 5 applications not only on IIS but they can be self hosted or use kestrel web server on linux.5) ASP .NET Core MVC 1.0 has inbuilt support for Dependency Injection.ASP .NET Core MVC includes a simple built-in container (represented by the IServiceProvider interface) that supports constructor injection by default, and MVC makes certain services available through DI.6) ASP .NET Core MVC 1.0 has a new project solution structure.There is no App_Start, App_Data, Global.asax and root web.config file.App_Start is replaced by Startup.cs and web.config is replaced by appsetting.json.There is also a new configuration system, where JSON is preferred over XML for configuration settings.7) Roslyn compiler for compiling code dynamically.Now no need to compile your code, on any code changes that you make. Thanks to Roslyn in memory compilation.

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0 (part 2)
Just make changes -> save it and view in browser.8) In ASP .NET Core MVC 1.0 "wwwroot" is now place for static files.wwwroot directory in project is for static content like css, Js, images.And it's the default root of your server.If a request comes in for a static file on disk, if the file is in this folder then it can go back to client.The name can be changed from project.json file.9) The new Project.json file defines dependencies, runtime to use, and definesbuild and publish setup, instead of dot c s proj file.10) Everything is Nuget package in Core MVC 1.0. There is no dll by default.11) Bundling and minification is done using Grunt or Gulp, unlike defining bundles in BundleConfig file.12) Manage client side dependencies via NPM and Bower.13) ASP .NET MVC 5 Child actions are gone.

### ASP .NET MVC 5 vs ASP .NET MVC Core 1.0 (part 3)
They are now replaced with View Components.14) Introduction of _ViewImports.cshtml in Core MVC 1.0It provides namespaces which can be used by all other views.In previous MVC projects, this was provided by the web.config file in the Views folder; since the web.config no longer exists, global namespaces are now provided by this file.15) Introduction of Tag helpers.Tag Helpers allows to enable server-side code to participate in creating and rendering HTML elements in Razor files.16) It also support RESTful style routes with attribute routingThat means you can even declare RESTful like routes like [HttpGet("Our Route")] and [HttpPost("Our Route")]17) In Core MVC 1.0, routes have new [controller] and [action] tokens.These tokens allows you to reference controller and action names in the route template.These token are helpful when in future if you rename the controller or action, there is no need to update the routes.==========================================================================

# DISCPLINE: E-Commerce
## E-Commerce [Setup]
### Set Up An Ecommerce System
E-commerce Web sites are not easy to set up.With a plethora of e-commerce solutions in the market, entrepreneurs have to make a few key decisions:The entrepreneur has to decide on the initial amount of investment required for an e-commerce Web site, as well as the volume of business of an e-commerce Web site over the Internet.Investment factors and business objectives dictate the type of software, database, or other applications that are required to set up the e-commerce Web site.There are specific elements involved in an e-commerce system.These elements range from domain name for the site to the merchant account for e-commerce transactions.Each of these elements requires a certain amount of scrutiny before setting up an e-commerce Web site.Before launching the e-commerce Web site on the Internet, it requires rigorous testing.Some of the important and common types of testing include security testing, software and hardware reliability, and compatibility between all the elements of the system.

### The Basic Steps Involved In Becoming Commerce Enabled Are
1. Getting an Internet Merchant Bank Account2. Web Hosting3. Obtaining a Digital Certificate4. Finding a Provider of Online Transactions5. Creating or Purchasing a Shopping Cart Software

### E-commerce benefits are
More secure than a check.Fast as transactions take a few secondsAlways on with 24 7 purchases.Convenient with ease of purchasing.Reduced cost as marketing and advertising costs are reduced.

## E-Commerce [B2B, B2C, C2B, C2C]
### E-Commerce [B2B, B2C, C2B, C2C] Overview
Business-to-business electronic commerce is conducted between two separate businesses, such as a large company needing office supplies and an office supply company.Business-to-consumer electronic commerce is between one individual and a company selling goods or services.

### The Online Shopping Application
Online Shopping Application provides business gateway between Product vendors and Customers.Examples: Walmart, Amazon, Ebay, etc.

## E-Commerce [The Electronic Payment Procedure.
### E-Commerce [The Electronic Payment Procedure. Overview
The merchant entites, consisting of the [Merchant], [Merchant's Bank Account] and [Merchant Bank's Processor].The credit card entites, consisting of the [Credit Card Issuer] and [Credit Card Interchange].And the [Payment Gateway].One more time, the [Electronic Payment Procedure entities] are the Customer, Customer's Bank Account, Customer's Credit Card Issuer,the Merchant, Merchant's Bank Account, Merchant Bank's Processor, the Payment Gateway, and the Credit Card Interchange.

### Here is the [Electronic Payment Procedure] in 7 steps
(1) A [Secure Connection] is used by the: Merchant, Payment Gateway, Merchant Bank's Processor, Credit Card Interchange, and Credit Card Issuer.(2) The [Customer] has a [Credit Card Issuer].The [Customer] gives (credit card info) to the [Merchant](3) The [Merchant] obtains a (secure connection) from a [Website]The [Merchant] creates a (transaction with the credit card info)The [Merchant] routes the (transaction) to the [Payment Gateway].(4) The [Payment Gateway] routes the (transaction) to the [Merchant Bank's Processor].The [Merchant Bank's Processor] routes the (transaction) to the [Credit Card Interchange].The [Credit Card Interchange] routes the (transaction) to the [Credit Card Issuer].(5) The [Credit Card Issuer] processes the (transaction) based on the customer's (available funds).(6) The [Credit Card Issuer] routes the (transaction results and funds) to the [Credit Card Interchange].The [Credit Card Interchange] routes the (transaction results) to the [Merchant Bank's Processor].The [Merchant Bank's Processor] routes the (transaction results) to the [Payment Gateway].The [Payment Gateway] stores the (transaction results)The [Payment Gateway] routes the (transaction results) to the [Customer and/or Merchant].(7) The [Credit Card Interchange] routes the (transaction funds) to the [Merchant's Bank Processor]The [Merchant's Bank Processor] deposits the (funds) into the [Merchant's Bank Account].The [Merchant's Bank Processor] deposits the (funds), within 2 to 4 days, into the [Customer's Bank Account].

## E-Commerce [The Entities
## E-Commerce [Web Portals and Payment Gateways
## E-Commerce [Testing
### Testing Payment Gateways In Web Portals
Using dummy card ids, we can test Payment Gateways.

### How is Testing Crucial In Ecommerce
Testing is crucial to e-commerce because e-commerce sites are both business critical and highly visible to their users;any failure can be immediately expensive in terms of lost revenue and even more expensive in the longer term if disaffected users seek alternative sites.Yet the time pressures in the e-commerce world militate against the thorough testing usually associated with business criticality, so a new approach is needed to enable testing to be integrated into the development process and to ensure that testing does not present a significant time burden.

### Electronic Commerce Drawbacks
Increased vulnerability to fraud;difficulty protecting intellectual property;risks to confidentiality; problems over taxation;customs requirements;regulations; credit card fraud;security;trust problems, and constant availability.

### Software Reliability In Ecommerce
E-commerce requires software that performs critical tasks, such as creating storefront and a shopping cart, collecting customer data, and providing the payment gateway.This software needs to function correctly.Testing assures the organization of the quality and integrity of the e-commerce solution.

### System Assurance In Ecommerce
The main purpose of system assurance is to deliver a quality product.Conformance to requirements increases the organization's confidence in the system.An e-commerce system deals with three parties: the bank, the transaction clearinghouse, and the customer.The interdependency of these three parties makes the process of buying and selling over the Internet more critical than in real life.If the faith of any of these parties dwindles in the e-commerce site, the entrepreneurs can lose a lot of money, as well as their reputation.For example, in the case of a faulty e-commerce system, the credit card of the customer may be billed immediately for the complete order, when only a partial order has been filled.Testing must assure that partial order fulfillment and billing are done correctly.

## E-Commerce [Features and Comparisons
### E-Commerce [Features and Comparisons Overview
That includes all of the opportunities, challenges, and distinctions that come with selling online versus brick and mortar.Break down a few distinctions between ecommerce and traditional commerce.Even better if you can relate it back to the company you're interviewing with (e.g., if they have retail locations and an online store).

### To help you answer this question, think through


### The core differences between those two channels


### Have specific experience


### How would you drive more sales through different channels


### Here are some additional points to think through
Traditional commerce transactions are manually processed, where ecommerce transactions are automatically processed.Traditional commerce is limited to specific hours of the day and a limited geographical scope of businesses, where ecommerce is available all day, every day, and their customer base can reach worldwide.While traditional commerce is focused predominantly on the supply side, ecommerce is focused on the demand side.Traditional commerce provides instant gratification in the delivery of goods, where ecommerce requires the customer to wait for orders to be delivered.Being able to answer this question will demonstrate how much you know about ecommerce.

## E-Commerce [Payment Models
### Mention and describe a few ecommerce models
Ecommerce hiring managers are asking this question to understand how well you understand the ecommerce industry.There are a ton of different models that they could be referring to, from omnichannel to direct-to-consumer (DTC) models.This is a great opportunity for you to speak to your experience, both professionally and what you've seen or read online.Perhaps you have years of B2B SaaS experience, but you're applying as an ecommerce marketer for a B2C online retailer.Help the hiring manager understand that you understand how marketing strategies differ in ecommerce.To help you answer this question, try filling in the blanks in this hypothetical statement: I have [blank] years of experience in the [blank] industry doing [blank], but my personal experience as a consumer has compelled me to want to create better experiences for the DTC space.

### Some key metrics to track in any ecommerce model
Ecommerce is still commerce, so selling product is the end goal as it always has been.Especially when it comes to selling products online, sales can come from efforts across many channels (hence the popular term, omnichannel).So having basic to advanced knowledge of what those channel metrics are and how to set KPIs for each channel is imperative.

### In the ecommerce marketing role, some of those include
Customer acquisition cost (CAC),ROAS (return on advertising spend),Email / SMS open and click-through rates,Customer retention.Pick a few metrics you're familiar with and have experience measuring.

### For instance
If you're in social media marketing, talk to hitting numbers for reach, engagement, and CPC (cost per click).If you're an email marketer, speak to optimizing email click-throughs, open rates, and list segmentation.The more you can speak to metrics directly related to ecommerce, the better.These metrics include average order value (AOV), customer lifetime value (CLV), and repeat customer rate.

### Disadvantages of ecommerce as a business model
You can expect this question from a company who wants to see your thought process in solving some of the challenges of ecommerce.Some of the challenges include the option to interact with the product before purchasing; privacy and security concerns; and the inability to create a brand-centric, in-person buying experience.In short, make ecommerce the hero of the story.So many brands, particularly in the DTC space as of late, have made their online-only platform work for them.For instance, Casper mattresses (back when they were 100% ecommerce-led) allowed customers a 100-night sleep test with a money-back guarantee.Pull from popular ecommerce brands as examples and showcase why ecommerce doesn't have to feel like a simple transaction.

## [What I think]
### Web Marketing Create A More Personalized Approach Than Radio Or Television Advertising
By allowing users to select the ads they would like to pursue; in radio and television advertising, the viewer or listener is more of a passive recipient of the information.

### Mention any examples of ecommerce companies that inspire you? And why
Anyone who is an online consumer has found a brand or two they love and return to time and time again.They have also probably found a brand or two they can't afford to purchase from (or don't have any particular need to purchase from), but they admire what they do anyway.Draw on personal examples and scour the news for relevant stories, too.This is a chance for the company to learn more about who you are as a person, and it helps them to better understand what you're drawn to as a consumer, and then as a marketer.Here are some examples on how to answer this question.Example 1: My guilty pleasure is Chipotle, and I love that the brand is focused on sustainable sourcing and partnering with small farms around the country.Recently, they released a merch line that was dyed with upcycled avocado pits.Now I don't feel as bad about paying extra for my guac!Example 2: I identify as female, but I admire how Hims has encouraged an open, honest conversation around men's health and wellness. 'Self care' has always been a female-driven narrative, and Hims makes both curated products and information around them more accessible to the male population.Choose an online brand you love and explain why.

### We notice that customer churn is on the rise, how would you boost repeat purchase rates and increase customer retention
Ecommerce hiring managers want to see that you already have a plan for improving key metrics before you've even stepped in the door.Or, at least have a solid way to think through core problems and get things done to test and improve metrics.

### The plan have to be entirely successful? Of course not! But to land a job as an ecommerce professional, you need at least a basic understanding of the customer mindset.
This involves knowing ways to scale the customer experience and leverage both new and existing channels to drive results.Now's a good time to seed your experience on how to retain customers.Briefly walk them through the problem, the strategy, and the outcome.Be sure to state what KPIs you measured and the tools you used to succeed.If you don't have relevant experience in growing customer retention rates, that's okay, too.Find an opportunity in their current marketing strategy and offer it up as a suggestion, such as creating a blog with articles related to the product and/or brand, or how you would improve the brand's marketing emails.Offering actionable ways you can help improve the brand's marketing strategy can help show the hiring manager the value you can bring to the table.

### What would you say are some technologies that have streamlined the ecommerce experience
This question helps the hiring manager understand how much experience you have using and implementing technology.Having working knowledge of ecommerce platforms like Shopify and BigCommerce to marketing platforms like Facebook and AdWords is helpful here.If that's not possible, you should know what these tools (and others) have done to change the online shopping game.Here are a couple examples on how to best answer this question.Example 1: While not particularly new or novel, I've loved the implementation of technologies like virtual try-ons to reduce the amount of returns and exchanges.Example 2: SaaS platforms have done an incredible job of making ecommerce easier for the thousands of entrepreneurs, but they also make it harder from a competitive point of view for those entrepreneurs.So, tools like MarketerHire that help you find great marketing talent are incredibly helpful, or tools like Later that help you schedule Instagram posts all while being able to keep an eye on the grid view is fantastic.These kinds of things give brands the differentiation they need in the market, since so much of the technology has already been democratized.

### You maintain a positive customer experience throughout an ecommerce business model
As mentioned before, ecommerce is still commerce.Customers expect a personalized shopping experience that they won't forget.Maintaining a positive customer experience is embedded in the job description of every ecommerce professional.Customers notice the smallest things, especially when they aren't walking into a physical store.For example, Glossier sends every customer a sample of another product and a set of branded stickers.These additions cost pennies on the dollar to a company, but they mean more than their share to the customer on the other end.Talk about ways to implement a better customer service experience like employing community management on customer reviews and social media sites.

### Essential ecommerce third-party partnerships to a successful ecommerce business
For ecommerce, it's all about creating an end-to-end ecommerce experience.With this questions, the hiring manager is looking for your experience in working with ecommerce platforms like Shopify, BigCommerce, and Squarespace, to third-party logistics like ShipBob.Review old work or projects and draw on experiences

### What can you learn from your old work? Remember that the hiring manager wasn't a part of your previous experience.
Be sure to walk them through a problem you faced, the steps you took to find a solution, and ultimately what the outcome was.Numbers and statistics are always appreciated.

### Get to know the company
You should know about the company you're interviewing with and not just what they do, but what their needs are and ways you can apply your experience to foster the solutions they are looking for.

### Research ecommerce companies who are crushing it
Take the time to do your research on the top ecommerce companies and why they are the top.

### What marketing tools, channels, and strategies are they using


### There any case studies that you can read and learn from
Present these as fodder for the hiring manager to chew on.=======================================================================

### DISCIPLINE: Docker
I have categorized these 50 questions into: Basic Qs, Basic Commands, Advanced QsThis category of Docker IQs consists of questions that you're expected to know.These are the most basic questions.An interviewer will start with these and eventually increase the difficulty level.Let's have a look at them.

### Hypervisor
A hypervisor is a software that makes virtualization possible.It is also called Virtual Machine Monitor.It divides the host system and allocates the resources to each divided virtual environment.You can basically have multiple OS on a single host system.

### There are two types of Hypervisors
Type 1: It's also called Native Hypervisor or Bare metal Hypervisor.It runs directly on the underlying host system.It has direct access to your host's system hardware and hence does not require a base server operating system.Type 2: This kind of hypervisor makes use of the underlying host operating system.It's also called Hosted Hypervisor.

### Virtualization
Virtualization is the process of creating a software-based, virtual version of something(compute storage, servers, application, etc.).These virtual versions or environments are created from a single physical hardware system.Virtualization lets you split one system into many different sections which act like separate, distinct individual systems.A software called Hypervisor makes this kind of splitting possible.The virtual environment created by the hypervisor is called Virtual Machine.

### Containerization
Let me explain this is with an example.Usually, in the software development process, code developed on one machine might not work perfectly fine on any other machine because of the dependencies.This problem was solved by the containerization concept.So basically, an application that is being developed and deployed is bundled and wrapped together with all its configuration files and dependencies.This bundle is called a container.Now when you wish to run the application on another system, the container is deployed which will give a bug-free environment as all the dependencies and libraries are wrapped together.Most famous containerization environments are Docker and Kubernetes.Difference between virtualization and containerizationOnce you've explained containerization and virtualization, the next expected question would be differences.The question could either be differences between virtualization and containerization or differences between virtual machines and containers.Either way, this is how you respond.Containers provide an isolated environment for running the application.The entire user space is explicitly dedicated to the application.Any changes made inside the container is never reflected on the host or even other containers running on the same host.Containers are an abstraction of the application layer.Each container is a different application.Whereas in Virtualization, hypervisors provide an entire virtual machine to the guest(including Kernal).Virtual machines are an abstraction of the hardware layer.Each VM is a physical machine.

### Docker
Since its a Docker interview, there will be an obvious question about what is Docker.Start with a small definition.Docker is a containerization platform which packages your application and all its dependencies together in the form of containers so as to ensure that your application works seamlessly in any environment, be it development, test or production.Docker containers, wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries, etc.It wraps basically anything that can be installed on a server.This guarantees that the software will always run the same, regardless of its environment.

### A Docker Container
Docker containers include the application and all of its dependencies.It shares the kernel with other containers, running as isolated processes in user space on the host operating system.Docker containers are not tied to any specific infrastructure: they run on any computer, on any infrastructure, and in any cloud.Docker containers are basically runtime instances of Docker images.

### Docker Images
When you mention Docker images, your very next question will be "what are Docker images".Docker image is the source of Docker container.In other words, Docker images are used to create containers.When a user runs a Docker image, an instance of a container is created.These docker images can be deployed to any Docker environment.

### Docker Hub
Docker images create docker containers.There has to be a registry where these docker images live.This registry is Docker Hub.Users can pick up images from Docker Hub and use them to create customized images and containers.Currently, the Docker Hub is the world's largest public repository of image containers.

### Explain Docker Architecture
Docker Architecture consists of a Docker Engine which is a client-server application with three major components:A server which is a type of long-running program called a daemon process (the docker command).A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.A command line interface (CLI) client (the docker command).The CLI uses the Docker REST API to control or interact with the Docker daemon through scripting or direct CLI commands.Many other Docker applications use the underlying API and CLI.Refer to this blog, to read more about Docker Architecture.

### A Dockerfile
Let's start by giving a small explanation of Dockerfile and proceed by giving examples and commands to support your arguments.Docker can build images automatically by reading the instructions from a file called Dockerfile.A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.Using docker build, users can create an automated build that executes several command-line instructions in succession.The interviewer does not just expect definitions, hence explain how to use a Dockerfile which comes with experience.Have a look at this tutorial to understand how Dockerfile works.Tell us something about Docker Compose.Docker Compose is a YAML file which contains details about the services, networks, and volumes for setting up the Docker application.So, you can use Docker Compose to create separate containers, host them and get them to communicate with each other.Each container will expose a port for communicating with other containers.

### Docker Swarm
You are expected to have worked with Docker Swarm as it's an important concept of Docker.Docker Swarm is native clustering for Docker.It turns a pool of Docker hosts into a single, virtual Docker host.Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.

### A Docker Namespace
A namespace is one of the Linux features and an important concept of containers.Namespace adds a layer of isolation in containers.Docker provides various namespaces in order to stay portable and not affect the underlying host system.Few namespace types supported by Docker - PID, Mount, IPC, User, Network

### The lifecycle of a Docker Container
This is one of the most popular questions asked in Docker interviews.

### Docker containers have the following lifecycle
Create a containerRun the containerPause the container(optional)Un-pause the container(optional)Start the containerStop the containerRestart the containerKill the containerDestroy the container

### Docker Machine
Docker machine is a tool that lets you install Docker Engine on virtual hosts.These hosts can now be managed using the docker-machine commands.Docker machine also lets you provision Docker Swarm Clusters.

### Docker Basic Commands
Once you've aced the basic conceptual questions, the interviewer will increase the difficulty level.So let's move on to the next section of this Docker IQs article.

## Docker: [Common Commands]
### Check for Docker Client and Docker Server version
The following command gives you information about Docker Client and Server versions:$ docker version

### You get the number of containers running, paused and stopped
You can use the following command to get detailed information about the docker installed on your system.$ docker info

### If you vaguely remember the command and you'd like to confirm it, how will you get help on that particular command
The following command is very useful as it gives you help on how to use a command, the syntax, etc.$ docker --helpThe above command lists all Docker commands.

### If you need help with one specific command, you can use the following syntax
$ docker <command> --help

### Login into docker repository


### You can use the following command to login into hub.docker.com
$ docker loginYou'll be prompted for your username and password, insert those and congratulations, you're logged in.

### If you wish to use a base image and make modifications or personalize it, how do you do that
You pull an image from docker hub onto your local system

### It's one simple command to pull an image from docker hub
$ docker pull <image_name>

### You create a docker container from an image
Pull an image from docker repository with the above command and run it to create a container.

### Use the following command
$ docker run -it -d <image_name>

### Most probably the next question would be, what does the '-d' flag mean in the command
-d means the container needs to start in the detached mode.Explain a little about the detach mode.Have a look at this blog to get a better understanding of different docker commands.

### You list all the running containers


### The following command lists down all the running containers
$ docker psSuppose you have 3 containers running and out of these, you wish to access one of them.

### You access a running container


### The following command lets us access a running container
$ docker exec -it <container id> bashThe exec command lets you get inside a container and work with it.

### Start, stop and kill a container


### The following command is used to start a docker container
$ docker start <container_id>

### And the following for stopping a running container
$ docker stop <container_id>

### Kill a container with the following command
$ docker kill <container_id>

### Use a container, edit it, and update it? Also, how do you make it a new and store it on the local system
Of course, you can use a container, edit it and update it.This sounds complicated but its actually just one command.$ docker commit <conatainer id> <username/imagename>

### Once you've worked with an image, how do you push it to docker hub
$ docker push <username/image name>

### Delete a stopped container


### Use the following command to delete a stopped container
$ docker rm <container id>

### Delete an image from the local storage system


### The following command lets you delete an image from the local system
$ docker rmi <image-id>

### Build a Dockerfile
Once you've written a Dockerfile, you need to build it to create an image with those specifications.

### Use the following command to build a Dockerfile
$ docker build <path to docker file>

### The next question would be when do you use ".dockerfile_name" and when to use the entire path
Use ".dockerfile_name" when the dockerfile exits in the same file directory and you use the entire path if it lives somewhere else.

### Know why docker system prune is used? What does it do
$ docker system pruneThe above command is used to remove all the stopped containers, all the networks that are not used, all dangling images and all build caches.It's one of the most useful docker commands.

## Docker [Advanced Qs]
### You lose your data, when a docker container exists
No, you won't lose any data when Docker container exits.Any data that your application writes to the container gets preserved on the disk until you explicitly delete the container.The file system for the container persists even after the container halts.

### All do you think Docker is being used
When asked such a question, respond by talking about applications of Docker.

### Docker is being used in the following areas
Simplifying configuration: Docker lets you put your environment and configuration into code and deploy it.Code Pipeline Management: There are different systems used for development and production.As the code travels from development to testing to production, it goes through a difference in the environment.Docker helps in maintaining the code pipeline consistency.Developer Productivity: Using Docker for development gives us two things - We're closer to production and development environment is built faster.Application Isolation: As containers are applications wrapped together with all dependencies, your apps are isolated.They can work by themselves on any hardware that supports Docker.Debugging Capabilities: Docker supports various debugging tools that are not specific to containers but work well with containers.Multi-tenancy: Docker lets you have multi-tenant applications avoiding redundancy in your codes and deployments.Rapid Deployment: Docker eliminates the need to boost an entire OS from scratch, reducing the deployment time.

### How is Docker different from other containerization methods
Docker containers are very easy to deploy in any cloud platform.It can get more applications running on the same hardware when compared to other technologies, it makes it easy for developers to quickly create, ready-to-run containerized applications and it makes managing and deploying applications much easier.You can even share containers with your applications.

### Can I use JSON instead of YAML for my compose file in Docker
You can use JSON instead of YAML for your compose file, to use JSON file with compose, specify the JSON filename to use, for eg:$ docker-compose -f docker-compose.json up

### How have you used Docker in your previous position
Explain how you have used Docker to help rapid deployment.Explain how you have scripted Docker and used it with other tools like Puppet, Chef or Jenkins.If you have no past practical experience in Docker and instead have experience with other tools in a similar space, be honest and explain the same.In this case, it makes sense if you can compare other tools to Docker in terms of functionality.

### How far do Docker containers scale? Are there any requirements for the same
Large web deployments like Google and Twitter and platform providers such as Heroku and dotCloud, all run on container technology.Containers can be scaled to hundreds of thousands or even millions of them running in parallel.Talking about requirements, containers require the memory and the OS at all the times and a way to use this memory efficiently when scaled.

### What platforms does docker run on
This is a very straightforward question but can get tricky.Do some company research before going for the interview and find out how the company is using Docker.Make sure you mention the platform company is using in this answer.

### Docker runs on various Linux administration
Ubuntu 12.04, 13.04 et alFedora 19/20+RHEL 6.5+CentOS 6+GentooArchLinuxopenSUSE 12.3+CRUX 3.0+It can also be used in production with Cloud platforms with the following services:Amazon EC2Amazon ECSGoogle Compute EngineMicrosoft AzureRackspace

### There a way to identify the status of a Docker container
There are six possible states a container can be at any given point - Created, Running, Paused, Restarting, Exited, Dead.

### Use the following command to check for docker state at any given point
$ docker psThe above command lists down only running containers by default.

### To look for all containers, use the following command
$ docker ps -a

### Remove a paused container from Docker
The answer is no.You cannot remove a paused container.The container has to be in the stopped state before it can be removed.

### Can a container restart by itself
No, it's not possible for a container to restart by itself.By default the flag -restart is set to false.

### It better to directly remove the container using the rm command or stop the container followed by remove container
Its always better to stop the container and then remove it using the remove command.$ docker stop <coontainer_id>$ docker rm -f <container_id>Stopping the container and then removing it will allow sending SIG_HUP signal to recipients.This will ensure that all the containers have enough time to clean up their tasks.This method is considered a good practice, avoiding unwanted errors.

### Cloud overtake the use of Containerization
Docker containers are gaining popularity but at the same time, Cloud services are giving a good fight.In my personal opinion, Docker will never be replaced by Cloud.Using cloud services with containerization will definitely hype the game.Organizations need to take their requirements and dependencies into consideration into the picture and decide what's best for them.Most of the companies have integrated Docker with the cloud.This way they can make the best out of both the technologies.

### How many containers can run per host
There can be as many containers as you wish per host.Docker does not put any restrictions on it.But you need to consider every container needs storage space, CPU and memory which the hardware needs to support.You also need to consider the application size.Containers are considered to be lightweight but very dependant on the host OS.

### It a good practice to run stateful applications on Docker
The concept behind stateful applications is that they store their data onto the local file system.You need to decide to move the application to another machine, retrieving data becomes painful.I honestly would not prefer running stateful applications on Docker.Suppose you have an application that has many dependant services.

### Docker compose wait for the current container to be ready to move to the running of the next service
The answer is yes.Docker compose always runs in the dependency order.These dependencies are specifications like depends_on, links, volumes_from, etc.

### How will you monitor Docker in production
Docker provides functionalities like docker stats and docker events to monitor docker in production.Docker stats provides CPU and memory usage of the container.Docker events provide information about the activities taking place in the docker daemon.

### It a good practice to run Docker compose in production
Yes, using docker compose in production is the best practical application of docker compose.When you define applications with compose, you can use this compose definition in various production stages like CI, staging, testing, etc.

### What changes are expected in your docker compose file while moving it to production
These are the following changes you need make to your compose file before migrating your application to the production environment:Remove volume bindings, so the code stays inside the container and cannot be changed from outside the container.Binding to different ports on the host.Specify a restart policyAdd extra services like log aggregator

### Have you used Kubernetes? If you have, which one would you prefer amongst Docker and Kubernetes
Be very honest in such questions.If you have used Kubernetes, talk about your experience with Kubernetes and Docker Swarm.Point out the key areas where you thought docker swarm was more efficient and vice versa.Have a look at this blog for understanding differences between Docker and Kubernetes.You Docker interview questions are not just limited to the workarounds of docker but also other similar tools.Hence be prepared with tools/technologies that give Docker competition.One such example is Kubernetes.

### You aware of load balancing across containers and hosts? How does it work
While using docker service with multiple containers across different hosts, you come across the need to load balance the incoming traffic.Load balancing and HAProxy is basically used to balance the incoming traffic across different available(healthy) containers.If one container crashes, another container should automatically start running and the traffic should be re-routed to this new running container.Load balancing and HAProxy works around this concept.

## Kubernetes
## Kubernetes - Basic
### How is Kubernetes different from Docker Swarm
Features	Kubernetes	Docker SwarmInstallation & Cluster Config	Setup is very complicated, but once installed cluster is robust.	Installation is very simple, but the cluster is not robust.GUI	GUI is the Kubernetes Dashboard.	There is no GUI.Scalability	Highly scalable and scales fast.	Highly scalable and scales 5x faster than Kubernetes.Auto-scaling	Kubernetes can do auto-scaling.	Docker swarm cannot do auto-scaling.Load Balancing	Manual intervention needed for load balancing traffic between different containers and pods.	Docker swarm does auto load balancing of traffic between containers in the cluster.Rolling Updates & Rollbacks	Can deploy rolling updates and does automatic rollbacks.	Can deploy rolling updates, but not automatic rollback.DATA Volumes	Can share storage volumes only with the other containers in the same pod.	Can share storage volumes with any other container.Logging & Monitoring	In-built tools for logging and monitoring.	3rd party tools like ELK stack should be used for logging and monitoring.

### Kubernetes
Kubernetes is an open-source container management tool that holds the responsibilities of container deployment, scaling & descaling of containers & load balancing.Being Google's brainchild, it offers excellent community and works brilliantly with all the cloud providers.So, we can say that Kubernetes is not a containerization platform, but it is a multi-container management solution.

### How is Kubernetes related to Docker
It's a known fact that Docker provides the lifecycle management of containers and a Docker image builds the runtime containers.But, since these individual containers have to communicate, Kubernetes is used.So, Docker builds the containers and these containers communicate with each other via Kubernetes.So, containers running on multiple hosts can be manually linked and orchestrated using Kubernetes.

### The difference between deploying applications on hosts and containers
Refer to the above diagram.The left side architecture represents deploying applications on hosts.So, this kind of architecture will have an operating system and then the operating system will have a kernel that will have various libraries installed on the operating system needed for the application.So, in this kind of framework you can have n number of applications and all the applications will share the libraries present in that operating system whereas while deploying applications in containers the architecture is a little different.This kind of architecture will have a kernel and that is the only thing that's going to be the only thing common between all the applications.So, if there's a particular application that needs Java then that particular application we'll get access to Java and if there's another application that needs Python then only that particular application will have access to Python.The individual blocks that you can see on the right side of the diagram are basically containerized and these are isolated from other applications.So, the applications have the necessary libraries and binaries isolated from the rest of the system, and cannot be encroached by any other application.

### Container Orchestration
Consider a scenario where you have 5-6 microservices for an application.Now, these microservices are put in individual containers, but won't be able to communicate without container orchestration.So, as orchestration means the amalgamation of all instruments playing together in harmony in music, similarly container orchestration means all the services in individual containers working together to fulfill the needs of a single server.

### The need for Container Orchestration
Consider you have 5-6 microservices for a single application performing various tasks, and all these microservices are put inside containers.Now, to make sure that these containers communicate with each other we need container orchestration.As you can see in the above diagram, there were also many challenges that came into place without the use of container orchestration.So, to overcome these challenges the container orchestration came into place.

### The features of Kubernetes


### The features of Kubernetes, are as follows


### Kubernetes simplify containerized Deployment
As a typical application would have a cluster of containers running across multiple hosts, all these containers would need to talk to each other.So, to do this you need something big that would load balance, scale & monitor the containers.Since Kubernetes is cloud-agnostic and can run on any public/private providers it must be your choice simplify containerized deployment.

### What do you know about clusters in Kubernetes
The fundamental behind Kubernetes is that we can enforce the desired state management, by which I mean that we can feed the cluster services of a specific configuration, and it will be up to the cluster services to go out and run that configuration in the infrastructure.So, as you can see in the above diagram, the deployment file will have all the configurations required to be fed into the cluster services.Now, the deployment file will be fed to the API and then it will be up to the cluster services to figure out how to schedule these pods in the environment and make sure that the right number of pods are running.So, the API which sits in front of services, the worker nodes & the Kubelet process that the nodes run, all together make up the Kubernetes Cluster.

### Google Container Engine
Google Container Engine (GKE) is an open-source management platform for Docker containers and clusters.This Kubernetes based engine supports only those clusters which run within Google's public cloud services.

# Kubernetes
### Heapster
Heapster is a cluster-wide aggregator of data provided by Kubelet running on each node.This container management tool is supported natively on Kubernetes cluster and runs as a pod, just like any other pod in the cluster.So, it basically discovers all nodes in the cluster and queries usage information from the Kubernetes nodes in the cluster, via on-machine Kubernetes agent.

### Minikube
Minikube is a tool that makes it easy to run Kubernetes locally.This runs a single-node Kubernetes cluster inside a virtual machine.

### Kubectl
Kubectl is the platform using which you can pass commands to the cluster.So, it basically provides the CLI to run commands against the Kubernetes cluster with various ways to create and manage the Kubernetes component.

### Kubelet
This is an agent service which runs on each node and enables the slave to communicate with the master.So, Kubelet works on the description of containers provided to it in the PodSpec and makes sure that the containers described in the PodSpec are healthy and running.

## Kubernetes - Architecture-Based
### The different components of Kubernetes Architecture
The Kubernetes Architecture has mainly 2 components - the master node and the worker node.As you can see in the below diagram, the master and the worker nodes have many inbuilt components within them.The master node has the kube-controller-manager, kube-apiserver, kube-scheduler, etcd.Whereas the worker node has kubelet and kube-proxy running on each node.

### What do you understand by Kube-proxy
Kube-proxy can run on each and every node and can do simple TCP/UDP packet forwarding across backend network service.So basically, it is a network proxy that reflects the services as configured in Kubernetes API on each node.So, the Docker-linkable compatible environment variables provide the cluster IPs and ports which are opened by proxy.

### Brief on the working of the master node in Kubernetes
Kubernetes master controls the nodes and inside the nodes the containers are present.Now, these individual containers are contained inside pods and inside each pod, you can have a various number of containers based upon the configuration and requirements.So, if the pods have to be deployed, then they can either be deployed using user interface or command-line interface.Then, these pods are scheduled on the nodes, and based on the resource requirements, the pods are allocated to these nodes.The kube-apiserver makes sure that there is communication established between the Kubernetes node and the master components.

### The role of kube-apiserver and kube-scheduler
The kube - apiserver follows the scale-out architecture and, is the front-end of the master node control panel.This exposes all the APIs of the Kubernetes Master node components and is responsible for establishing communication between Kubernetes Node and the Kubernetes master components.The kube-scheduler is responsible for the distribution and management of workload on the worker nodes.So, it selects the most suitable node to run the unscheduled pod based on resource requirement and keeps a track of resource utilization.It makes sure that the workload is not scheduled on nodes that are already full.

### Brief about the Kubernetes controller manager
Multiple controller processes run on the master node but are compiled together to run as a single process which is the Kubernetes Controller Manager.So, Controller Manager is a daemon that embeds controllers and does namespace creation and garbage collection.It owns the responsibility and communicates with the API server to manage the end-points.Course CurriculumKubernetes Certification TrainingInstructor-led SessionsAssessmentsLifetime Access24 x 7 Expert Support

### So, the different types of controller manager running on the master node are


### ETCD
Etcd is written in Go programming language and is a distributed key-value store used for coordinating distributed work.So, Etcd stores the configuration data of the Kubernetes cluster, representing the state of the cluster at any given point in time.

### The different types of services in Kubernetes


### The following are the different types of services used


### What do you understand by load balancer in Kubernetes
A load balancer is one of the most common and standard ways of exposing service.There are two types of load balancer used based on the working environment i.e.either the Internal Load Balancer or the External Load Balancer.The Internal Load Balancer automatically balances load and allocates the pods with the required configuration whereas the External Load Balancer directs the traffic from the external load to the backend pods.

### Ingress network, and how does it work
Ingress network is a collection of rules that acts as an entry point to the Kubernetes cluster.This allows inbound connections, which can be configured to give services externally through reachable URLs, load balance traffic, or by offering name-based virtual hosting.So, Ingress is an API object that manages external access to the services in a cluster, usually by HTTP and is the most powerful way of exposing service.Now, let me explain to you the working of Ingress network with an example.There are 2 nodes having the pod and root network namespaces with a Linux bridge.In addition to this, there is also a new virtual ethernet device called flannel0(network plugin) added to the root network.Now, suppose we want the packet to flow from pod1 to pod 4.Refer to the below diagram.So, the packet leaves pod1's network at eth0 and enters the root network at veth0.Then it is passed on to cbr0, which makes the ARP request to find the destination and it is found out that nobody on this node has the destination IP address.So, the bridge sends the packet to flannel0 as the node's route table is configured with flannel0.Now, the flannel daemon talks to the API server of Kubernetes to know all the pod IPs and their respective nodes to create mappings for pods IPs to node IPs.The network plugin wraps this packet in a UDP packet with extra headers changing the source and destination IP's to their respective nodes and sends this packet out via eth0.Now, since the route table already knows how to route traffic between nodes, it sends the packet to the destination node2.The packet arrives at eth0 of node2 and goes back to flannel0 to de-capsulate and emits it back in the root network namespace.Again, the packet is forwarded to the Linux bridge to make an ARP request to find out the IP that belongs to veth1.The packet finally crosses the root network and reaches the destination Pod4.

### Ingress network, and how does it work (part 2)


### What do you understand by Cloud controller manager
The Cloud Controller Manager is responsible for persistent storage, network routing, abstracting the cloud-specific code from the core Kubernetes specific code, and managing the communication with the underlying cloud services.It might be split out into several different containers depending on which cloud platform you are running on and then it enables the cloud vendors and Kubernetes code to be developed without any inter-dependency.So, the cloud vendor develops their code and connects with the Kubernetes cloud-controller-manager while running the Kubernetes.

### The various types of cloud controller manager are as follows


### Container resource monitoring
As for users, it is really important to understand the performance of the application and resource utilization at all the different abstraction layer, Kubernetes factored the management of the cluster by creating abstraction at different levels like container, pods, services and whole cluster.Now, each level can be monitored and this is nothing but Container resource monitoring.

### The difference between a replica set and replication controller
Replica Set and Replication Controller do almost the same thing.Both of them ensure that a specified number of pod replicas are running at any given time.The difference comes with the usage of selectors to replicate pods.Replica Set use Set-Based selectors while replication controllers use Equity-Based selectors.Equity-Based Selectors: This type of selector allows filtering by label key and values.So, in layman terms, the equity-based selector will only look for the pods which will have the exact same phrase as that of the label.Example: Suppose your label key says app=nginx, then, with this selector, you can only look for those pods with label app equal to nginx.Selector-Based Selectors: This type of selector allows filtering keys according to a set of values.So, in other words, the selector based selector will look for pods whose label has been mentioned in the set.Example: Say your label key says app in (nginx, NPS, Apache).Then, with this selector, if your app is equal to any of nginx, NPS, or Apache, then the selector will take it as a true result.

### A Headless Service
Headless Service is similar to that of a 'Normal' services but does not have a Cluster IP.This service enables you to directly reach the pods without the need of accessing it through a proxy.

### The best security measures that you can take while using Kubernetes
The following are the best security measures that you can follow while using Kubernetes:

### Federated clusters
Multiple Kubernetes clusters can be managed as a single cluster with the help of federated clusters.So, you can create multiple Kubernetes clusters within a data center/cloud and use federation to control/manage them all at one place.The federated clusters can achieve this by doing the following two things.Refer to the below diagram.

## Kubernetes - Scenario-Based
### You think the company shifted from monolithic to microservices and deploy their services containers


### Solution
As the company's goal is to shift from their monolithic application to microservices, they can end up building piece by piece, in parallel and just switch configurations in the background.Then they can put each of these built-in microservices on the Kubernetes platform.So, they can start by migrating their services once or twice and monitor them to make sure everything is running stable.Once they feel everything is going good, then they can migrate the rest of the application into their Kubernetes cluster.Scenario 2: Consider a multinational company with a very much distributed system, with a large number of data centers, virtual machines, and many employees working on various tasks.

### You think can such a company manage all the tasks in a consistent way with Kubernetes


### Solution
As all of us know that I.T.departments launch thousands of containers, with tasks running across a numerous number of nodes across the world in a distributed system.In such a situation the company can use something that offers them agility, scale-out capability, and DevOps practice to the cloud-based applications.So, the company can, therefore, use Kubernetes to customize their scheduling architecture and support multiple container formats.This makes it possible for the affinity between container tasks that gives greater efficiency with an extensive support for various container networking solutions and container storage.Scenario 3: Consider a situation, where a company wants to increase its efficiency and the speed of its technical operations by maintaining minimal costs.The company can implement the DevOps methodology, by building a CI/CD pipeline, but one problem that may occur here is the configurations may take time to go up and running.So, after implementing the CI/CD pipeline the company's next step should be to work in the cloud environment.Once they start working on the cloud environment, they can schedule containers on a cluster and can orchestrate with the help of Kubernetes.This kind of approach will help the company reduce their deployment time, and also get faster across various environments.Scenario 4:  Suppose a company wants to revise it's deployment methods and wants to build a platform which is much more scalable and responsive.

### You think this company can achieve this to satisfy their customers


### Solution
In order to give millions of clients the digital experience they would expect, the company needs a platform that is scalable, and responsive, so that they could quickly get data to the client website.Now, to do this the company should move from their private data centers (if they are using any) to any cloud environment such as AWS.Not only this, but they should also implement the microservice architecture so that they can start using Docker containers.Once they have the base framework ready, then they can start using the best orchestration platform available i.e.Kubernetes.This would enable the teams to be autonomous in building applications and delivering them very quickly.Scenario 5: Consider a multinational company with a very much distributed system, looking forward to solving the monolithic code base problem.

### You think the company can solve their problem


### Solution
Well, to solve the problem, they can shift their monolithic code base to a microservice design and then each and every microservices can be considered as a container.So, all these containers can be deployed and orchestrated with the help of Kubernetes.Scenario 6: All of us know that the shift from monolithic to microservices solves the problem from the development side, but increases the problem at the deployment side.

### The company solve the problem on the deployment side


### Solution
The team can experiment with container orchestration platforms, such as Kubernetes and run it in data centers.So, with this, the company can generate a templated application, deploy it within five minutes, and have actual instances containerized in the staging environment at that point.This kind of Kubernetes project will have dozens of microservices running in parallel to improve the production rate as even if a node goes down, then it can be rescheduled immediately without performance impact.Scenario 7:  Suppose a company wants to optimize the distribution of its workloads, by adopting new technologies.

### The company achieve this distribution of resources efficiently


### Solution
The solution to this problem is none other than Kubernetes.Kubernetes makes sure that the resources are optimized efficiently, and only those resources are used which are needed by that particular application.So, with the usage of the best container orchestration tool, the company can achieve the distribution of resources efficiently.Scenario 8: Consider a carpooling company wants to increase their number of servers by simultaneously scaling their platform.

### You think will the company deal with the servers and their installation


### Solution
The company can adopt the concept of containerization.Once they deploy all their application into containers, they can use Kubernetes for orchestration and use container monitoring tools like Prometheus to monitor the actions in containers.So, with such usage of containers, giving them better capacity planning in the data center because they will now have fewer constraints due to this abstraction between the services and the hardware they run on.Scenario 9: Consider a scenario where a company wants to provide all the required hand-outs to its customers having various environments.

### You think they can achieve this critical target in a dynamic manner


### Solution
The company can use Docker environments, to put together a cross-sectional team to build a web application using Kubernetes.This kind of framework will help the company achieve the goal of getting the required things into production within the shortest time frame.So, with such a machine running, the company can give the hands-outs to all the customers having various environments.Scenario 10: Suppose a company wants to run various workloads on different cloud infrastructure from bare metal to a public cloud.

### How will the company achieve this in the presence of different interfaces


### Solution
The company can decompose its infrastructure into microservices and then adopt Kubernetes.This will let the company run various workloads on different cloud infrastructures.

## Kubernetes - [Multiple Choice]
### Minions in the Kubernetes cluster
They are components of the master node.They are the work-horse / worker node of the cluster.[Ans]They are monitoring engine used widely in kubernetes.They are docker container service.

### Kubernetes cluster data is stored in which of the following
Kube-apiserverKubeletEtcd[Ans]None of the above

### Which of them is a Kubernetes Controller
Course CurriculumKubernetes Certification TrainingWeekday / Weekend BatchesReplicaSetDeploymentRolling UpdatesBoth ReplicaSet and Deployment[Ans]

### Which of the following are core Kubernetes objects
PodsServicesVolumesAll of the above[Ans]

### The Kubernetes Network proxy runs on which node
Master NodeWorker NodeAll the nodes[Ans]None of the above

### The responsibilities of a node controller
To assign a CIDR block to the nodesTo maintain the list of nodesTo monitor the health of the nodesAll of the above[Ans]

### The responsibilities of Replication Controller
Update or delete multiple pods with a single commandHelps to achieve the desired stateCreates a new pod, if the existing pod crashesAll of the above[Ans]

### Define a service without a selector
Specify the external name[Ans]Specify an endpoint with IP Address and portJust by specifying the IP addressSpecifying the label and api-version

### What did the 1.8 version of Kubernetes introduce
Taints and Tolerations[Ans]Cluster level LoggingSecretsFederated Clusters

### The handler invoked by Kubelet to check if a container's IP address is open or not is
HTTPGetActionExecActionTCPSocketAction[Ans]None of the above

# MongoDB
### MongoDB:
Mongo-DB is a document database which provides high performance, high availability and easy scalability.

### Namespace:
MongoDB stores BSON (Binary Interchange and Structure Object Notation) objects in the collection.The concatenation of the collection name and database name is called a namespace.

### Sharding:
The procedure of storing data records across multiple machines is referred as Sharding.It is a MongoDB approach to meet the demands of data growth.It is the horizontal partition of data in a database or search engine.Each partition is referred as shard or database shard.

### You see the connections used by Mongos
To see the connection used by Mongos use db_adminCommand (connPoolStats);

### Replica set
A replica set is a group of mongo instances that host the same data set.In replica set, one node is primary, and another is secondary.From primary to the secondary node all data replicates.

### Replication
Across multiple servers, the process of synchronizing data is known as replication.It provides redundancy and increase data availability with multiple copies of data on different database server.Replication helps in protecting the database from the loss of a single server.

### While creating Schema in MongoDB what are the points need to be taken in consideration
Design your schema according to user requirements.Combine objects into one document if you use them together.Otherwise, separate them.Do joins while write, and not when it is on read.For most frequent use cases optimize your schema.Do complex aggregation in the schema.

### The syntax to create a collection and to drop a collection in MongoDB
Syntax to create collection in MongoDB is db.createCollection(name,options).Syntax to drop collection in MongoDB is db.collection.drop().

### Profiler:
MongoDB database profiler shows performance characteristics of each operation against the database.You can find queries using the profiler that are slower than they should be.

### You can move old files in the moveChunk directory
It is possible to move old files in the moveChunk directory, during normal shard balancing operations these files are made as backups and can be deleted once the operations are done.

### Journaling:
Journaling is the feature in MongoDB that you can use to do safe backups.

### Objecld:
Objectld is composed of: Timestamp, Client machine ID, Client process ID and a 3 byte incremented counter,

### Command syntax for inserting a document:
For inserting a document command syntax is database.collection.insert (document).

### Inspect the source code of a function:
To inspect a source code of a function, without any parentheses, the function must be invoked.Command syntax that tells you whether you are on the master server or not.Command syntax Db.isMaster() will tell you whether you are on the master server or not.

### How many master does MongoDB allow
MongoDB allows only one master server, while couchDB allows multiple masters.

### Command syntax to view Mongo is using the link
The command syntax that is used to view mongo is using the link is db._adminCommand(connPoolStats.)

### Indexes:
Indexes are special structures in MongoDB, which stores a small portion of the data set in an easy to traverse form.Ordered by the value of the field specified in the index, the index stores the value of a specific field or set of fields.

### The basic syntax to use index in MongoDB
The basic syntax to use in MongoDB is db.COLLECTION_NAME.ensureIndex ( {KEY:1} ).In here the key is the the name of the COLUMN (or KEY:VALUE pair) which is present in the documents.

### GridFS:
For storing and retrieving large files such as images, video files and audio files GridFS is used.By default, it uses two files fs.files and fs.chunks to store the file's metadata and the chunks.

### Alternatives to MongoDB: Cassandra, CouchDB, Redis, Riak and Hbase.


# Multi Threading
### Thread:
A thread is basically a separate sequence of instruction designed to performing a specific task in the program.

### Multithreading:
Performing multiple task at same time during the execution of a program.

### Multithreading Namespace:
System.Threading;

### Multithreading Advantages:
1. Optimize the use of computer resources such as memory. 2. Save time

### System.Threading Namespace classes:
Thread, Thread Pool, Monitor and Mutex.

## Thread Class
### Thread Class:
The Thread class is used to perform tasks such as creating and setting the priority of a thread.

### Thread Class Properties:
Priority, Thread State, IsAlive, Current, Thread Name, etc.

### Thread Class Methods:
Join, Resume, sleep, Spin Wait, Suspended, Start and Interrupt.

## Thread Pool Class
### Thread Pool Class:
The Thread Pool class is used to perform task such as processing of asynchronous I/O and waiting on behalf of another thread.

### Thread Pool Class Methods:
Gettype, Equals, SetMaxThreads and QueueUserWorkItem.

## Monitor Class
### Monitor Class:
The Monitor class is used to access an object by granting a lock for the object to a single thread.

### Monitor Class Methods:
Enter, Exit, TryEnter, Wait and GetType.

### Monitor.enter vs Monitor.exit:
C#'s lock statement is in fact a syntactic shortcut for a call to the methods Monitor.Enter and Monitor.Exit with a try/finally block.

### Calling Monitor.Exit without first calling Monitor.Enter on the same object throws an exception.


### Invalidmonitorstateexception Thrown
This exception is thrown when you try to call wait()/notify()/notifyAll() any of these methods for an Object from a point in your program where u are NOT having a lock on that object.(i.e. u r not executing any synchronized block/method of that object and still trying to call wait()/notify()/notifyAll()) wait(), notify() and notifyAll() all throw IllegalMonitorStateException.Since This exception is a subclass of RuntimeException so we r not bound to catch it (although u may if u want to).And being a RuntimeException this exception is not mentioned in the signature of wait(), notify(), notifyAll() methods.

## Mutexs and Semaphores
### Mutex Class
A Mutex is used to perform interprocess synchronization and a thread to have exclusive access to shared resources.

### Mutex Class Methods:
Equals, close, OpenExisting, SetAccessControl and Release Mutex.

### Mutex:
A Mutex is like a lock, but it can work across multiple processes.In other words, Mutex can be computer-wide as well as application-wide.With a Mutex class, you call the WaitOne method to lock and ReleaseMutex to unlock.Closing or disposing a Mutex automatically releases it.Just as with the lock statement, a Mutex can be released only from the same thread that obtained it.A common use for a cross-process Mutex is to ensure that only one instance of a program can run at a time.

### Semaphore:
A semaphore is like a nightclub: it has a certain capacity, enforced by a bouncer.Once it's full, no more people can enter, and a queue builds up outside.Then, for each person that leaves, one person enters from the head of the queue.The constructor requires a minimum of two arguments: the number of places currently available in the nightclub and the club's total capacity.A semaphore with a capacity of one is similar to a Mutex or lock, except that the semaphore has no owner.It is thread-agnostic.Any thread can call Release on a Semaphore, whereas with Mutex and lock, only the thread that obtained the lock can release it.Semaphores can be useful in limiting concurrency, preventing too many threads from executing a particular piece of code at once.If the Sleep statement was instead performing intensive disk I/O, the Semaphore would improve overall performance by limiting excessive concurrent hard-drive activity.A Semaphore, if named, can span processes in the same way as a Mutex.

## Threads
### Creating And Starting A Thread:


### First define a delegate
Public delegate void start_thread();

### Create a new thread
Thread thread_name = new Thread(new start_thread(method_name));

### Scheduled A Thread:
We can scheduled the  thread with the help of priority property of the Thread class.

### Priority Values Used For Scheduling A Thread:
Highest, Normal, AboveNormal, BelowNormal and Lowest.

### Thread Types:
Foreground thread and Background thread.

### Join vs Sleep:
You can wait for another thread to end by calling its Join method.

### For example
Thread t = new Thread (Go);t.Start();t.Join();static void Go()You can include a timeout when calling Join, either in milliseconds or as a TimeSpan.It then returns true if the thread ended or false if it timed out.

### Threads Vs Processes:
A thread is analogous to the operating system process in which your application runs.Just as processes run in parallel on a computer,threads run in parallel within a single process.Processes are fully isolated from each other; threads have just a limited degree of isolation.In particular, threads share (heap) memory with other threads running in the same application.This, in part, is why threading is useful: one thread can fetch data in the background, for instance, while another thread can display the data as it arrives.

### Naming Threads:
Each thread has a Name property that you can set for the benefit of debugging.This is particularly useful in Visual Studio, since the thread's name is displayed in the Threads Window and Debug Location toolbar.You can set a thread's name just once; attempts to change it later will throw an exception.The static Thread.CurrentThread property gives you the currently executing thread.Example:Thread.CurrentThread.Name = mainThread worker = new Thread (Go)worker.Name = "worker";worker.Start();Go();static void Go()

### Synchronization In Respect To Multi-threading:
With respect to multi-threading, synchronization is the capability to control the access of multiple threads to shared resources.Without synchronization, it is possible for one Java thread to modify a shared variable while another thread is in the process of using or updating same shared variable.This usually leads to erroneous behavior or program.

### Different Ways Of Using Thread:
A Java thread could be implemented by using Runnable interface or by extending the Thread class.The Runnable is more advantageous, when you are going for multiple inheritance.

### Thread.start() vs Thread.run() Method:
Thread.start() method (native method) of Thread class actually does the job of running the Thread.run() method in a thread.If we directly call Thread.run() method it will executed in same thread, so does not solve the purpose of creating a new thread.

### Do We Need Run() & Start() Method? Can We Achieve It With Only Run Method
We need run() & start() method both because JVM needs to create a separate thread which can not be differentiated from a normal method call.So this job is done by start method native implementation which has to be explicitly called.Another advantage of having these two methods is we can have any object run as a thread if it implements Runnable interface.This is to avoid Java multiple inheritance problems which will make it difficult to inherit another class with Thread.

### Threadlocal Class:


### Below are some key points about ThreadLocal variables
A thread-local variable effectively provides a separate copy of its value for each thread that uses it.ThreadLocal instances are typically private static fields in classes that wish to associate state with a threadIn case when multiple threads access a ThreadLocal instance, separate copy of Threadlocal variable is maintained for each thread.Common use is seen in DAO pattern where the DAO class can be singleton but the Database connection can be maintained separately for each thread.(Per Thread Singleton)

### Sleep() vs Suspend() vs Wait():
Thread.sleep(): takes the current thread to a "Not Runnable" state for specified amount of time.The thread holds the monitors it has acquired.For example, if a thread is running a synchronized block or method and sleep method is called then no other thread will be able to enter this block or method.The sleeping thread can wake up when some other thread calls t.interrupt on it.Note that sleep is a static method, that means it always affects the current thread (the one executing sleep method).A common mistake is trying to call t2.sleep() where t2 is a different thread; even then, it is the current thread that will sleep, not the t2 thread.thread.suspend(): is deprecated method.Its possible to send other threads into suspended state by making a suspend method call.In suspended state a thread keeps all its monitors and can not be interrupted.This may cause deadlocks therefore it has been deprecated.object.wait(): call also takes the current thread into a "Not Runnable" state, just like sleep(), but with a slight change.Wait method is invoked on a lock object, not thread.

### Immutable Object. How Does It Help In Writing Concurrent Application
An object is considered immutable if its state cannot change after it is constructed.Maximum reliance on immutable objects is widely accepted as a sound strategy for creating simple, reliable code.Immutable objects are particularly useful in concurrent applications.Since they cannot change state, they cannot be corrupted by thread interference or observed in an inconsistent state.Examples of immutable objects from the JDK include String and Integer.Immutable objects greatly simplify your multi threaded program, since they are simple to construct, test, and use.Automatically thread-safe and have no synchronization issues.To create a object immutable You need to make the class final and all its member final so that once objects gets crated no one can modify its state.You can achieve same functionality by making member as non final but private and not modifying them except in constructor.

### Synchronizing the Run Method:
The run method of a runnable class can be synchronized.If you make run method synchronized then the lock on runnable object will be occupied before executing the run method.In case we start multiple threads using the same runnable object in the constructor of the Thread then it would work.But until the 1st thread ends the 2nd thread cannot start and until the 2nd thread ends the next cannot start as all the threads depend on lock on same object.

## Thread Leaks
### Thread leak is when a application does not release references to a thread object properly.
Due to this some Threads do not get garbage collected and the number of unused threads grow with time.Thread leak can often cause serious issues on a Java application since over a period of time too many threads will be created but not released and may cause applications to respond slow or hang.

### I Trace Whether The Application Has A Thread Leak
If an application has thread leak then with time it will have too many unused threads. Try to find out what type of threads is leaking out.

### This can be done using following ways
Give unique and descriptive names to the threads created in application. - Add log entry in all thread at various entry and exit points in threads.Change debugging config levels (debug, info, error etc) and analyze log messages.When you find the class that is leaking out threads check how new threads are instantiated and how they're closed.Make sure the thread is Guaranteed to close properly by doing following - Handling all Exceptions properly.Make sure the thread is Guaranteed to close properly by doing followingHandling all Exceptions properly.releasing all resources (e.g. connections, files etc) before it closes.

## Thread Pools
### Thread Pool? Why Should We Use Thread Pools
A thread pool is a collection of threads on which task can be scheduled.Instead of creating a new thread for each task, you can have one of the threads from the thread pool pulled out of the pool and assigned to the task.When the thread is finished with the task, it adds itself back to the pool and waits for another assignment.One common type of thread pool is the fixed thread pool.This type of pool always has a specified number of threads running;if a thread is somehow terminated while it is still in use, it is automatically replaced with a new thread.Below are key reasons to use a Thread PoolUsing thread pools minimizes the JVM overhead due to thread creation.Thread objects use a significant amount of memory, and in a large-scale application, allocating and de-allocating many thread objects creates a significant memory management overhead.You have control over the maximum number of tasks that are being processed in parallel (= number of threads in the pool).Most of the executor implementations in java.util.concurrent use thread pools, which consist of worker threads.This kind of thread exists separately from the Runnable and Callable tasks it executes and is often used to execute multiple tasks.

## Deadlocks
### Deadlocks:
A deadlock happens when two threads each wait for a resource held by the other, so neither can proceed.More elaborate deadlocking chains can be created with three or more threads.Deadlocking is one of the hardest problems in multithreading, especially when there are many interrelated objects.Fundamentally, the hard problem is that you can't be sure what locks your caller has taken out.So, you might innocently lock private field a within your class x, unaware that your caller (or caller's caller) has already locked field b within class y.Meanwhile, another thread is doing the reverse, creating a deadlock.Ironically, the problem is exacerbated by (good) object-oriented design patterns,because such patterns create call chains that are not determined until runtime.The popular advice, lock objects in a consistent order to avoid deadlocks, although helpful in our initial example,is hard to apply to the scenario just described.A better strategy is to be wary of locking around calling methods in objects that may have references back to your own object.Also, consider whether you really need to lock around calling methods in other classes(often you do as we'll see later.

### Deadlocks: (part 2)
But, sometimes there are other options).Relying more on declarative and data parallelism, immutable types, and nonblocking synchronization constructs, can lessen the need for locking.Deadlock is a situation where two or more threads are blocked forever, waiting for each other.This may occur when two threads, each having a lock on one resource, attempt to acquire a lock on the other's resource.Each thread would wait indefinitely for the other to release the lock, unless one of the user processes is terminated.

### In terms of Java API, thread deadlock can occur in following conditions
1. When two threads call Thread.join() on each other.2. When two threads use nested synchronized blocks to lock two objects and the blocks lock the same objects in different order.

### Starvation And Livelock:
Starvation and livelock are much less common a problem than deadlock, but are still problems that every designer of concurrent software is likely to encounter.

### LiveLock:
Livelock occurs when all threads are blocked, or are otherwise unable to proceed due to unavailability of required resources, and the non-existence of any unblocked thread to make those resources available.

### In terms of Java API, thread livelock can occur in following conditions:
1. When all the threads in a program execute Object.wait(0) on an object with zero parameter.   The program is live-locked and cannot proceed until one or more threads call Object.notify() or Object.notifyAll() on the relevant objects.   Because all the threads are blocked, neither call can be made.2. When all the threads in a program are stuck in infinite loops.

### Starvation:
Starvation describes a situation where a thread is unable to gain regular access to shared resources and is unable to make progress.This happens when shared resources are made unavailable for long periods by "greedy" threads.For example, suppose an object provides a synchronized method that often takes a long time to return.If one thread invokes this method frequently, other threads that also need frequent synchronized access to the same object will often be blocked.Starvation occurs when one thread cannot access the CPU because one or more other threads are monopolizing the CPU.In Java, thread starvation can be caused by setting thread priorities inappropriately.A lower-priority thread can be starved by higher-priority threads if the higher-priority threads do not yield control of the CPU from time to time.

### FindMonitorDeadlockedThreads()
This method can be used to detect cycles of threads that are in deadlock waiting to acquire object monitors.It returns an array of thread IDs that are deadlocked waiting on monitor.

### FindDeadlockedThreads()
It returns an array of thread IDs that are deadlocked waiting on monitor or ownable synchronizers.

# MVC
## Important areas
### MVC is a pattern for splitting application logic into 3 components: Models, Views and Controllers.


### About the Model.
The Model is a business entity. It represents the application data.

### About the Controller.
The Controller handles the business logic.The Routing logic sends User Requests to Controller Action method entry points.

### Actions processes business logic which may include
accessing the Model and, or,   sending data to a View or another Controller.Model data may be inserted into a ViewModel which is sent to the View.The Controller redirects to that View using the View() method.Controllers redirect to other Controllers via the RedirectToAction() Action method.

### About the View.
The View is the MVC presentation layer and is associated with a Request URL.The Controller sends data to the View via the ViewModel, ViewBag, ViewData or TempData.The View maps that data to page controls.The View sends requests to the Controller via JSON, Ajax or JavaScript.

### MVC Advantages.


### MVC advantages are
SOC,Improved code structure,Easier testing andImproved reuseability.

### MVC 3 has:
JSON binding,the Dependency Resolver for simplified dependency injection,Razor .cshtml to compile View code into the assembly.

### MVC 4 has:
Templates for Mobile and Web API,Asynchronous controller task support,JavaScript bundling and segregating of configs for routing,Web API,Bundling,etc.

### MVC 5 has:
Attribute routing.

### Dependency Injection Advantages:
DIReduces class coupling,Increases code reusing,Improves code maintainability andImproves application testing.

### Controller attributes:
Authentication, Authorization, HandleError, OutputCache.

### Action attributes:
NonAction, ChildActionOnly, ActionName

### Action Filters:
Authentication, Authorization, HandleError, OutputCache.

### ActionResult subtypes:
ViewResult, PartialViewResult, RedirectToRouteResult, RedirectResult, JavascriptResult, JSONResult, FileResult, HTTPStatusCodeResult.

### Scaffolding types:
Empty, Create, Delete, Details, Edit and List.

### Ajax helpers options are: URL, Confirm, On Begin, On Complete, On Success, On Failure, and Update Target ID.


### Partial Views are rendered with: Html.Partial() and Html.RenderPartial().


### MVC Unit Test Tools: NUnit, xUnit.NET, Ninject 2, Moq.


## MVC
### MVC is a pattern for splitting application logic into 3 components: Models, Views and Controllers.


### About the Model.
The Model is a business entity. It represents the application data.

### About the Controller.
The Controller handles the business logic.The Routing logic sends User Requests to the Controller.Actions are entry points into the Controller.In the Actions, the Controller processes business logic.The Business logic may include accessing the Model and, or, sending data to aView or another Controller.The Controller may create ViewModel data from data received from the Model.Their is a View associated with the Request URL. The Controller redirects to that View using the View() method.

### Some Controller Action return types, or return Results, are
Content Result,   JSON Result,   Redirect Result,   JavaScript Result and   View Result.

### About the View.
The View is the MVC presentation layer.The View is driven by the Controller which may send data in the form of a ViewModel, ViewBag, ViewData or TempData.The View maps that data to page controls.JavaScript may send requests back to the Controller.It is common to use Ajax requests to communicate with the Controller.

### MVC advantages are:
SOC,   Improved code structure,   Easier testing,   Improved reuseability and   It is lightweight because it does not use the View State.

### In terms of HTTP verbs
The GET action requests data from resources.The POST action submits data to resources for processing.1. SOC: MVC Provides a clean separation of concerns among the UI, Controller and Model.2. Improved code structure because code layout is modular. The UI is the Presentation layer. The Controller handles the Business Logic. The Model contains Transfer objects, Domain Objects and Entities.3. Easier testing: MVC is easy to UnitTest. Routes can be tested with a tool called glimpse. Test projects can be created to unittest Controllers and Models. Controller unit tests use Assert statements, checking for Is Not Null, Is True, Is Equal, etc. Views can be tested with the Razor Generator which generates source code from .cshtml Razor files,   allowing them to be compiled into your assemblies. It supports MVC, Web Pages and standalone templates. Testing Views is frowned upon. Views can change in the smallest ways and maintaining unit tests can be very time consuming.4.

### In terms of HTTP verbs (continued)
Improved reuseability: Models and Views are reused. Models and Views have a many-to-many relationship. Multiple Models can be accessed by the same View. Multiple Views can access the same Model.MVC uses SOC to separate content from presentation and data-processing from content.

### Dependency Resolution.
The Dependency Resolver is a simplified use of dependency injection.This turn to be easier and useful for decoupling the application components and making them easier to test and more configurable.

### MVC Bundling: Bundle DOT config In MVC 4.
BundleConfig.cs in MVC 4 is used to register the bundles by the bundling and minification system.Many bundles are added by default including jQuery libraries like - jquery.validate, Modernizr, and default CSS references.

### Important MVC Namespaces.


### Below are the important namespaces used in MVC
System.Web DOT ASP .NET MVC.System.Web DOT ASP .NET DOT MVC.Ajax, HTML and Async.

### MVC Dependency Injection.


### Dependency Injection Advantages
DIReduces class coupling,Increases code reusing,Improves code maintainability andImproves application testing.

### MVC life cycle steps are:
Application initialization,Routing,Instantiation and execution of the Controller,Locating and invoking Controller Action andInstantiating and rendering View.

## MVC Routing
### MVC Routing Overview
The RouteConfig class contains the RegisterRoutes() method.RegisterRoutes() receives the Route Collection.RegisterRoutes() calls   routes DOT IgnoreRoute(),   routes DOT MapRoute() and   routes.Map ASP .NET MVC AttributeRoutes();RegisterRoutes() is called from Application_Start() in the global DOT A S A X file.The default URL pattern is Controller / Action / ID.The ID can be specified as optional.The ID can have Constraints, such as using RegEx to mandate only decimals.

### Related classes and methods are
MvcRouteHandler,   RoutValueDictionary(),   GetHttpHandler() and   URL Routing Module.Incoming Requests enter the URL Routing Module which is an HTTP module.It parses the URL to find a suitable match in the routing table.It selects the Controller,   obtains the Controller instance   and calls the Controller's Execute method.

### MVC Routing: DOT glimpse.
Glimpse is an open source tool for debugging the routes in MVC .It is the client side debugger.Glimpse has to be turned on by visiting to local url link - http://localhost:portname//glimpse.axd This is a popular and useful tool for debugging which tracks the speed details, url details etc.

### The components to Create A Route are
Name: Name is the name of the route.URL Pattern: Specify URL pattern placeholders to match the request URL pattern.Defaults: Defaults specify the default Controller, Action and Parameter layout.

### Add constraints to routes in following ways
Using Regular Expressions.Using an object which implements interface - IRouteConstraint.

## MVC View Model
## MVC Models
## MVC Controllers
## MVC Controller Actions
### Actions are the methods in the Controller class which is responsible for returning the view or json data.
The Action will mainly have the return type ActionResult and it will be invoked from the InvokeAction() method called by the controller.How to change the Action Name.The ActionName attribute can be used for changing the action name.Example:[ActionName("TestActionNew")]public ActionResult TestAction() {return View();}Here, TestAction is the original action name and in the ActionName attribute, the name, TestActionNew, is given.The caller of this action method will use the name TestActionNew to call this action.Action Filters allow us to execute the code before or after action has been executed.This can be done by decorating the action methods of Controllers with MVC attributes.

### Action Filters are:
Authentication.Authorization.HandleError.OutputCache.

### Child Actions.
To create reusable widgets child actions are used and this will be embedded into the parent views.In MVC, Partial views are used to have reusability in the application.Child action mainly returns the partial views.

### Invoke Child Actions.
The ChildActionOnly attribute is decorated over action methods to indicate that action method is a child action.

### For example
[ChildActionOnly]public ActionResult MenuBar() {//Logic herereturn PartialView();}

### Actionresult subtypes.
ActionResult is used to represent the action method result.

### ActionResult has the following subtypes
View Result.Partial View Result.Redirect To Route Result.Redirect Result.Javascript Result.JSON Result.File Result.HTTP Status Code Result.

### Again, ActionResult has the following subtypes
View Result.Partial View Result.Redirect To Route Result.Redirect Result.Javascript Result.JSON Result.File Result.HTTP Status Code Result.

### ActionResult: How to return a String Result from an action.
Return the results of the Content() method.The Content() method returns a string.

### A code snippet to return a string from an Action method is
public ActionResult TestAction() {   return Content("Hello Test !!");}

### ActionResult: How to return a JSON from an action method.
Return the results of the JSON() method.The JSON() method returns JSON.

### A code snippet to return a JSON from an Action method is
public ActionResult TestAction() {   return JSON(new { prop1 = "Test1", prop2 = "Test2" });}

### Determine if an Action is invoked from HTTP GET Or HTTP POST
Determine the Action request type using the HttpRequestBase clase and HttpMethod method.

### Controller Actions JSON Binding.
JavaScript Object Notation (JSON) binding support started from MVC 3 onwards via the new JsonValueProviderFactory,which allows the action methods to accept and model-bind data in JSON format.This is useful in Ajax scenarios like client templates and data binding that need to post data back to the server.

## MVC Methods
## MVC Views
### The 'page Lifecycle' Of MVC Works


### Below is the process
Initialize Routing.Instantiate and execute controller.Locate and invoke controller action.Instantiate and render view.

### MVC Views MVC Views shared across multiple Controllers.
Yes we can share a view across multiple controllers.We can put the view in the Shared folder.When we create a new MVC Project we can see the Layout page will be added in the shared folder, which is because it is used by multiple child pages.

### MVC Sections
Sections are the part of HTML which is to be rendered in layout page.

### In the Layout page, we will use the below syntax for rendering the HTML
@RenderSection("TestSection") And in child pages we are defining these sections as shown below:@section TestSection { }If any child page does not have this section defined, then an error will be thrown so to avoid that we can render the HTML like this:@RenderSection("TestSection", required: false)

### .CSHTML is a Razor View extension.
Renderbody And Renderpage.RenderBody is like ContentPlaceHolder in web forms.This will exist in layout page and it will render the child pages and views.Layout page will have only one RenderBody() method.RenderPage also exists in Layout page and multiple RenderPage() can be there in Layout page.

### Viewstart Page.
This page is used to make sure common layout page will be used for multiple views.Code written in this file will be executed first when application is being loaded.Methods to Render Views from an Action.Render Views with these methods: View(), PartialView(), Redirect(), RedirectToAction() and RedirectToRoute().View(): Returns the view from action.PartialView(): Returns the partial view from action.Redirect(): Similar to Response.Redirect() in webforms, used to redirect to specified URL.RedirectToAction(): Redirects to different action which can be in same controller or in different controller.RedirectToRoute(): Redirects to an action from the specified URL where the URL in the route table has been matched.Code Blocks: Use the @ sign to insert code blocks into the View.Layouts: Specify the path to the Layout in the code block. Layouts are master pages shared amongs all Views.Sections: Specify Sections in the code block.

## MVC Views MVC Partialviews, Scaffolding and Templates
### Partialview.
PartialView is similar to UserControls in traditional web forms.For re-usability purpose partial views are used.Since it's been shared with multiple views these are kept in shared folder.

### Partial Views can be rendered in following ways
Html.Partial()   Html.RenderPartial()

### HTML DOT partial.
This method is used to render the specified partial view as an HTML string.This method does not depend on any action methods.

### We can code it as


### HTML DOT renderpartial.
Result of the RenderPartial method is directly written to the HTML response.This method does not return anything (void).This method also does not depend on action methods.The RenderPartial() method calls Write() internally and we have to make sure that the RenderPartial method is enclosed in the bracket.

### Below is the sample code snippet
@{Html.RenderPartial("TestPartialView"); }

### Partial View versus Display Templates versus Edit Templates.
Display Templates: These are model centric.Meaning it depends on the properties of the view model used.It uses convention that will only display like divs or labels.

### Edit Templates: Edit templates are also model centric but will have editable controls like Textboxes.
Partial View: Partial Views are view centric.These will differ from templates by the way they render the properties (Id's).For example: CategoryViewModel has Product class property then it will be rendered as Model.Product.ProductName.But, in case of templates if we CategoryViewModel has List then @Html.DisplayFor(m => m.Products) works and it renders the template for each item of this list.

### Scaffold Templates.
Scaffolding in MVC is used to generate the Controllers, Model and Views for create, read, update, and delete crud functionality in an application.The scaffolding will know the naming conventions used for models, controllers and views.Scaffolding types are: Empty, Create, Delete, Details, Edit and List.Again, Scaffolding types are: Empty, Create, Delete, Details, Edit and List.

## MVC Views MVC Viewdata and Viewbag
### MVC Views MVC Viewdata.


### Viewdata contains the key, value pairs as dictionary and this is derived from the class ViewDataDictionary.
In action method we are setting the value for viewdata and in view the value will be fetched by typecasting.

### MVC Views MVC Viewbag versus MVC Viewdata.


### ViewBag is a wrapper around ViewData, which allows to create dynamic properties.
The advantage of viewbag over viewdata will be: In ViewBag no need to typecast the objects as in ViewData.ViewBag will take advantage of the dynamic keyword which is introduced in version 4.0.But before using ViewBag we have to keep in mind that ViewBag is slower than ViewData.Session is maintained in these constructs.

## MVC Views MVC TempData
### TempData
TempData is again a key, value pair as ViewData.This is derived from the TempDataDictionary class.TempData is used when the data is to be used in two consecutive requests, this could be between the actions or between the controllers.This requires typecasting in the view.

### Tempdata hold data for other requests
If Tempdata is assigned data in the current request, then it will be available for the current request and, conditionally, the subsequent request.If Tempdata data is read, then it will not be available for the subsequent requests.If Tempdata data is not read, then it will be available for the subsequent requests.

### TempData: Keep Method.
If Tempdata data has not been read in the current request, use the Keep method save the data for the subsequent request.@TempData["TestData"];TempData.Keep("TestData");

### TempData: Peek Method.
Similar to the Keep method, the Peek method is used for the same purpose.Peek is used to read Tempdata data and, thereby, maintains the data for the subsequent request.string mystring = TempData.Peek("TT").ToString();

## MVC Views MVC Areas
## MVC Views MVC JavaScript and HTML
### Razor is the first major update to render HTML in MVC 3.
Razor was designed specifically for view engine syntax.Example:@model ASP .NET MVC MusicStore.Models.Customer@{ViewBag.Title = "Get Customers";}< div class="cust">@Model.CustomerNameHow to Call A JavaScript Function On The Change Of A Dropdown List.

### Create a JavaScript method


### Function DrpIndexChanged() { } Invoke the method
<%:Html.DropDownListFor(x => x.SelectedProduct, new SelectList(Model.Customers, "Value", "Text"),  "Please Select a Customer", new { id = "ddlCustomers", onchange=" DrpIndexChanged ()" })%>Unobtrusive JavaScript doesn't inter mix JavaScript code in your page markup.For example: Instead of using events like onclick and onsubmit, the unobtrusive JavaScript attaches to elements by their ID or class based on the HTML data attributes.Again, unobtrusive JavaScript attaches to elements by their ID or class based on the HTML data attributes.

### Razor Code.
We can use the razor code in javascript in CSHTL by using <text> element.< script type="text/javascript">@foreach (var item in Model) {< text >javascript goes here which uses the server values</ text >}</script>

### Submit multiple submit buttons.
Below is the scenario and the solution to solve multiple submit buttons issue.It uses Html.BeginForm, input buttons and an ActionResult.

### Scenario
@using (Html.BeginForm("MyTestAction","MyTestController"){    <input type="submit" value="MySave" />    <input type="submit" value="MyEdit" />}

### Solution
Public ActionResult MyTestAction(string submit) { }Submit will have value either MySave or MyEdit.

## MVC Views MVC Helpers
### HTML Helpers are like controls in traditional web forms.
But HTML helpers are more lightweight compared to web controls as it does not hold viewstate and events.HTML Helpers returns the HTML string which can be directly rendered to HTML page.Custom HTML Helpers also can be created by overriding the HtmlHelper class.

### Ajax Helpers are used to create Ajax enabled elements like as Ajax enabled forms and links which performs the request asynchronously and these are extension methods of AjaxHelper class which exists in namespace - System.Web.ASP .NET MVC .
Ajax Helpers Options Configuration.Ajax helpers options are: URL, Confirm, On Begin, On Complete, On Success, On Failure, and Update Target ID.URL:         is the request URL.Confirm:     is used to specify the message which is to be displayed in confirm box.On Begin:    is the JavaScript method name to be given here and this will be called before the Ajax request.On Complete: is the JavaScript method name to be given here and this will be called at the end of Ajax request.On Success:  is the JavaScript method name to be given here and this will be called when Ajax request is successful.On Failure:  is the JavaScript method name to be given here and this will be called when Ajax request is failed.UpdateTarget ID: is the Target element which is populated from the action returning HTML.

### Again
URL:         is the request URL.Confirm:     is used to specify the message which is to be displayed in confirm box.On Begin:    is the JavaScript method name to be given here and this will be called before the Ajax request.On Complete: is the JavaScript method name to be given here and this will be called at the end of Ajax request.On Success:  is the JavaScript method name to be given here and this will be called when Ajax request is successful.On Failure:  is the JavaScript method name to be given here and this will be called when Ajax request is failed.UpdateTarget ID: is the Target element which is populated from the action returning HTML.The Helper Page.IsAjax property gets a value that indicates whether Ajax is being used during the request of the Web page.

## MVC Views CSS
### Add CSS in MVC.
Below is the sample code snippet to add CSS to razor views : < link rel="StyleSheet" href="/@Href(~Content/Site.css")" type="text/css"/>

## MVC Validation
### Validation Annotations.
Data annotations are attributes which can be found in the "System.ComponentModel.DataAnnotations" namespace.These attributes will be used for server-side validation and client-side validation is also supported.Four attributes - Required, String Length, Regular Expression and Range are used to cover the common validation scenarios.

### Check if Client Validation is enabled.
In Web.Config there are tags called : "ClientValidationEnabled" and "UnobtrusiveJavaScriptEnabled".We can set the client side validation just by setting these two tags "true", then this setting will be applied at the application level.< add key="ClientValidationEnabled" value="true" />< add key="UnobtrusiveJavaScriptEnabled" value="true" />

### Use J Query Plugins validation
We can use data annotations for validation in MVC .If we want to use validation during runtime using J Query then we can use J Query plugins for validation.

## MVC Testing
## MVC Versions
### MVC Versions Overview
4. Segregating the configs for MVC routing, Web API, Bundle, etc.DESCRIPTION: MVC 5 Features.Web API supports Attribute routing.Areas are used to organize Controllers, Models and Views into functional sections.The WebAPI programming interface can be either Browser API or Server API.The Browser API extends the functionalities of web browsers.The Server API extends the functionalities of web servers.

### DESCRIPTION: MVC Routing Why To Use "{resource}.axd/{*pathinfo}"
Using this default route - {resource}.axd/{*pathInfo}, we can prevent therequests for the web resources files like - WebResource.axd or ScriptResource.axd from passing to a controller.Representational State Transfer, or REST.REST is an architectural style which uses HTTP protocol methods like GET, POST, PUT, and DELETE to access the data.MVC works in this style.In MVC 4 there is a support for Web API which uses to build the service using HTTP verbs.Html.Partial method is applied for rendering a specific partial view in the form of a HTML string. This methodology does not rely on Action Methods.Html.ActionLink method allows navigating between Views.

## Node JS
### Node JS Overview
Server moves to next API after calling it and a notification mechanism of Events of Node.js helps server to get response from the previous API call.

### Node.js benefits
Asynchronous and Event Driven, Very fast, Single Threaded, Highly scalable and No buffering.Asynchronous and Event Driven: All APIs of Node.js library are asynchronous that is non-blocking.It essentially means a Node.js based server never waits for a API to return data.Server moves to next API after calling it and a notification mechanism of Events of Node.js helps server to get response from the previous API call.Very Fast: Being built on Google Chrome's V8 JavaScript Engine, Node.js library is very fast in code execution.Single Threaded but highly Scalable: Node.js uses a single threaded model with event looping.Event mechanism helps server to respond in a non-bloking ways and makes server highly scalable as opposed to traditional servers which create limited threads to handle requests.Node.js uses a single threaded program and same program can services much larger number of requests than traditional server like Apache HTTP Server.No Buffering: Node.js applications never buffer any data.These applications simply output the data in chunks.

### Node.js free
Yes! Node.js is released under the MIT license and is free to use.

### Node a single threaded application
Yes! Node uses a single threaded model with event looping.

## REPL
### Can we evaluate simple expression using Node REPL
Yes.

### Using var vs not using var in REPL while dealing with variables
Use variables to store values and print later.if var keyword is not used then value is stored in the variable and printed.Whereas if var keyword is used then value is stored but not printed.You can use both variables later.

### The Underscore variable in REPL
Use _ to get the last result.var x = 10var y = 20x + y yields 30var sum = _console.log(sum) yields 30

## NPM
### NPM Overview
Here local mode refers to the package installation in node_modules directory lying in the folder where Node application is present.Locally deployed packages are accessible via require().To install a Node project locally following is the syntax.C:\Nodejs_WorkSpace>NPM install express

### Check the already installed dependencies which are globally installed using NPM
Use the following command -C:\Nodejs_WorkSpace>NPM ls -g

### Package.json
package.json is present in the root directory of any Node application/module and is used to define the properties of a package.

### Package.json attributes
name: name of the packageversion: version of the packagedescription: description of the packagehomepage: homepage of the packageauthor: author of the packagecontributors: name of the contributors to the packagedependencies: list of dependencies.NPM automatically installs all the dependencies mentioned here in the node_module folder of the package.repository: repository type and url of the packagemain: entry point of the packagekeywords: keywords

### Uninstall a dependency using NPM
NPM uninstall dependency-name

### Update a dependency
Update package.json and change the version of the dependency which to be updated and run the following command.C:\Nodejs_WorkSpace>NPM update

## Callbacks, blocking code and Events
### Callbacks, blocking code and Events Overview
If application has to wait for some I/O operation in order to complete its execution any further then the code responsible for waiting is known as blocking code.

### Node prevent blocking code
By providing callback function.Callback function gets called whenever corresponding event triggered.

### Event Loop
Node js is a single threaded application but it support concurrency via concept of event and callbacks.As every API of Node js are asynchronous and being a single thread, it uses async function calls to maintain the concurrency.Node uses observer pattern.Node thread keeps an event loop and whenever any task get completed, it fires the corresponding event which signals the event listener function to get executed.

### Event Emmitter
EventEmitter class lies in events module.It is accessibly via following syntax -//import events modulevar events = require('events');//create an eventEmitter objectvar eventEmitter = new events.EventEmitter();When an EventEmitter instance faces any error, it emits an 'error' event.When new listener is added, 'newListener' event is fired and when a listener is removed, 'removeListener' event is fired.EventEmitter provides multiple properties like on and emit.on property is used to bind a function with the event and emit is used to fire an event.

## Modules
### Modules Overview
Asynchronous methods takes a last parameter as completion function callback and first parameter of the callback function is error.It is preferred to use asynchronous method instead of synchronous method as former never block the program execution where the latter one does.

## Streams
### Piping:
Piping is a mechanism to connect output of one stream to another stream.It is normally used to get data from one stream and to pass output of that stream to another stream.There is no limit on piping operations.Consider the above example, where we've read test.txt using readerStream and write test1.txt using writerStream.Now we'll use the piping to simplify our operation or reading from one file and writing to another file.

### Streams:
Streams are objects that let you read data from a source or write data to a destination in continuous fashion.

### Types of streams:
Readable, Writeable, Duplex and Transform.Readable: Stream which is used for read operation.Writable: Stream which is used for write operation.Duplex: Stream which can be used for both read and write operation.Transform: A type of duplex stream where the output is computed based on input.

### Events fired by streams.
Each type of Stream is an EventEmitter instance and throws several events at different instance of times.

### Some of the commonly used events are
data: This event is fired when there is data is available to read.end: This event is fired when there is no more data to read.error: This event is fired when there is any error receiving or writing data.finish: This event is fired when all data has been flushed to underlying system

### Chaining:
Chanining is a mechanism to connect output of one stream to another stream and create a chain of multiple stream operations.It is normally used with piping operations.

## Files
### Files Overview
offset: This is the offset in the buffer to start writing at.length: This is an integer specifying the number of bytes to read.position: This is an integer specifying where to begin reading from in the file.If position is null, data will be read from the current file position.callback: This is the callback function which gets the three arguments, (err, bytesRead, buffer).

### Write a file
fs.writeFile(filename, data[, options], callback)This method will over-write the file if file already exists.If you want to write into an existing file then you should use another method available.path: This is string having file name including path.data: This is the String or Buffer to be written into the file.options: The third parameter is an object which will hold {encoding, mode, flag}.By default encoding is utf8, mode is octal value 0666 and flag is 'w'callback: This is the callback function which gets a single parameter err and used to to return error in case of any writing error.

### Close a file


### How will you get information about a file using Node
fs.stat(path, callback)path: This is string having file name including path.callback: This is the callback function which gets two arguments (err, stats) where stats is an object of fs.Stats type which is printed below in the example.

### Truncate a file
fs.ftruncate(fd, len, callback)fd: This is the file descriptor returned by file fs.open() method.len: This is the length of the file after which file will be truncated.callback: This is the callback function which gets no arguments other than a possible exception are given to the completion callback.

### Delete a file
fs.unlink(path, callback)path: This is the file name including path.callback: This is the callback function which gets no arguments other than a possible exception are given to the completion callback.

### Read/write operations flags
r: Open file for reading. An exception occurs if the file does not exist.r+: Open file for reading and writing. An exception occurs if the file does not exist.rs: Open file for reading in synchronous mode. Instructs the operating system to bypass the local file system cache. This is primarily useful for opening files on NFS mounts as it allows you to skip the potentially stale local cache. It has a very real impact on I/O performance so don't use this flag unless you need it. Note that this doesn't turn fs.open() into a synchronous blocking call. If that's what you want then you should be using fs.openSync()rs+: Open file for reading and writing, telling the OS to open it synchronously. See notes for 'rs' about using this with caution.w: Open file for writing. The file is created (if it does not exist) or truncated (if it exists).wx: Like 'w' but fails if path exists.w+: Open file for reading and writing.

### Read/write operations flags (continued)
The file is created (if it does not exist) or truncated (if it exists).wx+: Like 'w+' but fails if path exists.a: Open file for appending. The file is created if it does not exist.ax: Like 'a' but fails if path exists.a+: Open file for reading and appending. The file is created if it does not exist.ax+': Like 'a+' but fails if path exists.

## Directories
### Directories Overview
__filename variable:The __filename represents the filename of the code being executed.This is the resolved absolute path of this code file.For a main program this is not necessarily the same filename used in the command line.The value inside a module is the path to that module file.

### __dirname variable
The __dirname represents the name of the directory that the currently executing script resides in.

## Timeouts
### Timeouts Overview
This function returns an opaque value that represents the timer which can be used to clear the timer using the function clearInterval(t).

## Other
### The purpose of process object
The process object is used to get information on current process.Provides multiple events related to process activities.

## More to be added
### Node.js
Node.js is a Server side scripting which is used to build scalable programs.Its multiple advantages over other server side languages, the prominent being non-blocking I/O.

### How node.js works
Node.js works on a v8 environment, it is a virtual machine that utilizes JavaScript as its scripting language and achieves high output via non-blocking I/O and single threaded event loop.

### What do you mean by the term I/O
I/O is the shorthand for input and output, and it will access anything outside of your application.It will be loaded into the machine memory to run the program, once the application is started.

### Event-driven programming mean
In computer programming, event driven programming is a programming paradigm in which the flow of the program is determined by events like messages from other programs or threads.It is an application architecture technique divided into two sections 1) Event Selection 2) Event Handling.

### Can we use node.js
Node.js can be used for the following purposes.Web applications ( especially real-time web apps )Network applicationsDistributed systemsGeneral purpose applications

### The advantage of using node.js
It provides an easy way to build scalable network programsGenerally fastGreat concurrencyAsynchronous everythingAlmost never blocks

### The two types of API functions in Node.js
The two types of API functions in Node.js areAsynchronous, non-blocking functionsSynchronous, blocking functions

### Control flow function
A generic piece of code which runs in between several asynchronous function calls is known as control flow function.

### Explain the steps how Control Flow controls the functions calls
Control the order of executionCollect dataLimit concurrencyCall the next step in program

### Node.js is single threaded
For async processing, Node.js was created explicitly as an experiment.It is believed that more performance and scalability can be achieved by doing async processing on a single thread under typical web loads than the typical thread based implementation.

### Node run on windows
Yes, it does.Download the MSI installer from https://nodejs.org/download/

### Access DOM in node
No, you cannot access DOM in node.

### Using the event loop what are the tasks that should be done asynchronously
I/O operationsHeavy computationAnything requiring blocking

### Node.js is quickly gaining attention from JAVA programmers
Node.js is quickly gaining attention as it is a loop based server for JavaScript.Node.js gives user the ability to write the JavaScript on the server, which has access to things like HTTP stack, file I/O, TCP and databases.

### The two arguments that async.queue takes
The two arguments that async.queue takesTask functionConcurrency value

### An event loop in Node.js
To process and handle external events and to convert them into callback invocations an event loop is used.So, at I/O calls, node.js can switch from one request to another.

### Mention the steps by which you can async in Node.js
First class functionsFunction compositionCallback CountersEvent loops

### The pros and cons of Node.js
If your application does not have any CPU intensive computation, you can build it in Javascript top to bottom, even down to the database level if you use JSON storage object DB like MongoDB.Crawlers receive a full-rendered HTML response, which is far more SEO friendly rather than a single page application or a websockets app run on top of Node.js.Any intensive CPU computation will block node.js responsiveness, so a threaded platform is a better approach.Using relational database with Node.js is considered less favourable.

### How Node.js overcomes the problem of blocking of I/O operations
Node.js solves this problem by putting the event based model at its core, using an event loop instead of threads.

### The difference between Node.js vs Ajax
The difference between Node.js and Ajax is that, Ajax (short for Asynchronous Javascript and XML) is a client side technology, often used for updating the contents of the page without refreshing it.While,Node.js is Server Side Javascript, used for developing server software.Node.js does not execute in the browser but by the server.

### The Challenges with Node.js
Emphasizing on the technical side, it's a bit of challenge in Node.js to have one process with one thread to scale up on multi core server.

### It mean non-blocking in node.js
In node.js non-blocking means that its IO is non-blocking.Node uses libuv to handle its IO in a platform-agnostic way.On windows, it uses completion ports for unix it uses epoll or kqueue etc.So, it makes a non-blocking request and upon a request, it queues it within the event loop which call the JavaScript 'callback' on the main JavaScript thread.

### The command that is used in node.js to import external libraries
Command require is used for importing external libraries, for example, var http=require (http).This will load the http library and the single exported object through the http variable.

### Mention the framework most commonly used in node.js
Express is the most common framework used in node.js.

### 'Callback' in node.js
Callback function is used in node.js to deal with multiple requests made to the server.Like if you have a large file which is going to take a long time for a server to read and if you don't want a server to get engage in reading that large file while dealing with other requests, call back function is used.Call back function allows the server to deal with pending request first and call a function when it is finished.

# React JS
### Question 1. What Is Reactjs


### Answer
React is an open source JavaScript front end UI library developed by Facebook  for creating interactive, stateful & reusable UI components for web and mobile app. It is used by Facebook, Instagram and many more web apps.ReactJS is used for handling view layer for web and mobile applications. One of React's unique major points is that  it perform not only on the client side, but also can be rendered on server side, and they can work together inter-operably.

### Question 2. Why Reactjs Is Used


### Answer
React is used to handle the view part of Mobile application and Web application.

# AJAX
### Question 3. Does Reactjs Use Html


### Answer
No, It uses JSX which is simiar to HTM.

### Question 4. When Reactjs Released


### Answer
March 2013AJAX Tutorial

### Question 5. What Is Current Stable Version Of Reactjs


### Answer
Version: 15.5Release on: April 7, 2017

# Angular JS
### Question 6. What Are The Life Cycle Of Reactjs


### Answer
InitializationState/Property UpdatesDestruction

### Question 7. What Are The Feature Of Reactjs


### Answer
JSX: JSX is JavaScript syntax extension.Components : React is all about components.One direction flow: React implements one way data flow which makes it easy to reason about your app

# Ext JS Tutorial Ext JS
### Question 8. What Are The Advantages Of Reactjs


### Answer
React uses virtual DOM which is JavaScript object. This will improve apps performanceIt can be used on client and server sideComponent and Data patterns improve readability.Can be used with other framework also.

### Question 9. How To Embed Two Components In One Component


### Answer
import React from 'react';class App extends React.Component {   render() {      return (         <div>            <Header/>            <Content/>         </div>      );   }}class Header extends React.Component {   render() {      return (         <div>            <h1>Header</h1>         </div>      );

# CSS Advanced
### Question 10. What Are The Advantages Of Using Reactjs


### Answer


### Advantages of ReactJS
React uses virtual DOM which is JavaScript object. This improves application performance as JavaScript virtual DOM is faster than the regular DOM.React can be used on client and as well as server side too.Using React increases readability and makes maintainability easier. Component, Data patterns improves readability and thus makes it easier for manitaing larger apps.React can be used with any other framework (Backbone.js, Angular.js) as it is only a view layer.React's JSX makes it easier to read the code of our component. It's really very easy to see the layout. How components are interacting, plugged and combined with each other in app.CSS Advanced Tutorial

### Question 11. What Are The Limitations Of Reactjs


### Answer


### Limitations of ReactJS
React is only for view layer of the app so we still need the help of other technologies to get a complete tooling set for development.React is using inline templating and JSX. This can seem awkward to some developers.The library of react  is too  large.Learning curve  for ReactJS may be steep.

# Javascript Advanced
### Question 12. How To Use Forms In Reactjs


### Answer
In React's virtual DOM, HTML Input element presents an interesting problem. With the others DOM environment, we can  render the input or textarea and thus allows the browser maintain its   state that is (its value). we can then get and set the value implicitly with the DOM API.In HTML, form elements such as <input>, <textarea>, and <select> itself  maintain their own state and update its state  based on the input provided by user .In React, components' mutable state is handled by the state property  and is only updated by setState().HTML <input> and <textarea> components use the value attribute.HTML <input> checkbox and radio components, checked attribute is used.<option> (within <select>) components, selected attribute is used for select box.

# AJAX
### Question 13. How To Use Events In Reactjs


### Answer
React identifies every events so that it must  have common and consistent behavior  across all the browsers. Normally, in normal JavaScript or other frameworks, the onchange event is triggered after we have typed something into a Textfield and then "exited out of it". In  ReactJS we cannot do it in this way.

### The explanation is typical and  non-trivial
*"<input type="text" value="dataValue"> renders an input textbox initialized with the value, "dataValue".When the user changes the input in text field, the node's value property will update and change. However, node.getAttribute('value') will still return the value used at initialization time that is dataValue.

### Form Events
onChange: onChange event  watches input changes and update state accordingly.onInput: It is triggered on input dataonSubmit: It is triggered on submit button.

### Mouse Events
onClick: OnClick of any components event is triggered on.onDoubleClick: onDoubleClick of any components event is triggered on.onMouseMove: onMouseMove of any components, panel event is triggered on.onMouseOver: onMouseOver of any components, panel, divs event is triggered on.

### Touch Events
onTouchCancel: This event is for canceling an events.onTouchEnd: Time Duration attached to touch of a screen.onTouchMove: Move during touch device .onTouchStart: On touching a device event is generated.Javascript Advanced Tutorial

### Question 14. Give An Example Of Using Events


### Answer
import React from 'react';import ReactDOM from 'react-dom'; var StepCounter = React.createClass({                    getInitialState: function() { return {counter: this.props.initialCounter }; },                    handleClick: function() {                    this.setState({counter: this.state.counter + 1});  },                    render: function() {                    return <div onClick={this.handleClick}> OnClick Event, Click Here: {this.state.counter }</div>;            }}); ReactDOM.render(< StepCounter initialCounter={7}/>, document.getElementById('content'));

### Question 15. Explain Various Flux Elements Including Action, Dispatcher, Store And View


### Answer


### Flux can be better explained by defining its individual components
Actions - They are helper methods that facilitate passing data to the Dispatcher.Dispatcher - It is Central hub of app, it receives actions and broadcasts payloads to registered callbacks.

### Stores - It is said to be Containers for application state & logic that have callbacks registered to the dispatcher. Every store maintains particular state and it will update  when it is needed. It wakes up on a relevant dispatch to retrieve the requested data. It is accomplished by registering with the dispatcher  when constructed. They are  similar to  model in a traditional MVC (Model View Controller), but they manage the state of many objects?--? it does not represent a single record of data like ORM models do.
Controller Views - React Components  grabs the state from Stores and pass it down through props to child components to view to render application.

# EmberJS
### Question 16. What Is Flux Concept In Reactjs


### Answer
Flux is the architecture of an application that Facebook uses for developing client-side web applications. Facebook uses internally when working with React. It is not a framework or a library. This is simply a new technique that complements React and the concept of Unidirectional Data Flow.Facebook dispatcher library is a sort of global pub/sub handler technique which broadcasts payloads to registered callbacks.EmberJS Tutorial

### Question 17. Give An Example Of Both Stateless And Stateful Components With Source Code


### Answer
Stateless and Stateful componentsStateless: When a component is "stateless", it calculates state is calculated internally but it directly  never mutates it. With the same inputs, it will always produce the same output. It means it has no knowledge of the past, current or future state changes.var React = require('react');var Header = React.createClass({    render: function() {        return( <img src={this.props.imageSource} />   ); }});ReactDOM.render(<Header imageSource="myImage.png"/>, document.body);Stateful : When a component is "stateful", it is a central point that stores every information in memory about the app/component's state, do has the ability to change it. It has knowledge of past, current and potential future state changes.

### Answer (continued)
Stateful component  change the state, using this.setState method.var React = require('react');var Header = React.createClass({    getInitialState: function() {        return { imageSource: "header.png" };  },    changeImage: function() {        this.setState({imageSource: "changeheader.png"});    },    render: function() {        return(            <img src={this.state.imageSource} onClick={this.changeImage.bind(this)} />        );    }});module.exports = Header;

# Backbone.js
### Question 18. Explain Basic Code Snippet Of Jsx With The Help Of A Practical Example


### Answer
Your browsers does not understand JSX code natively, we need to convert it to JavaScript first which can be understand by our browsers. We have aplugin which handles including Babel 5's in-browser ES6 and JSX transformer called browser.js.Babel will understand and recognize JSX code in <script type="text/babel"></script> tags and transform/convert it to normal JavaScript code.In case of production we will need to pre-compile our JSX code into JS before deploying to production environment so that our app renders faster.<!DOCTYPE html><html lang="en">  <head><title>My First React JSX Example</title></head>  <body>    <div id="hello-world"></div>    <script src="https://fb.me/react-15.0.0.js"></script>    <script src="https://fb.me/react-dom-15.0.0.js"></script>   <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.min.js"></script>     <script type="text/babel">      var HelloWorld = React.createClass({        render: function() {          return ( <p>Hello, World</p> )        }      });      ReactDOM.render( <HelloWorld/>, document.getElementById('hello-world'));    </script>  </body></html>

# Angular JS
### Question 19. What Are The Advantages Of Using Jsx


### Answer
JSX is completely optional and its not mandatory, we don't need to use it in order to use React, but it has several advantages  and a lot of nice features in JSX.JSX is always faster as it performs optimization while compiling code to vanilla JavaScript.JSX is also type-safe, means it is strictly typed  and most of the errors can be caught during compilation of the JSX code to JavaScript.JSX always makes it easier and faster to write templates if we are familiar with HTML syntax.JasmineJS Tutorial

### Question 20. What Is Reactjs-jsx


### Answer
JSX (JavaScript XML), lets us to build DOM nodes with HTML-like syntax. JSX is a preprocessor step which adds XML syntax to JavaScript.Like XML, JSX tags have a tag name, attributes, and children JSX also has the same. If an attribute/property value is enclosed in quotes(""), the value is said to be string. Otherwise, wrap the value in braces and the value is the enclosed JavaScript expression. We can represent JSX as <HelloWorld/>.

# D3.js
### Question 21. What Are Components In Reactjs


### Answer
React encourages the idea of reusable components. They are widgets or other parts of a layout (a form, a button, or anything that can be marked up using HTML) that you can reuse multiple times in your web application.ReactJS enables us to create components by invoking the React.createClass() method  features a render() method which is responsible for displaying the HTML code.When designing interfaces, we have to break down the individual design elements (buttons, form fields, layout components, etc.) into reusable components with well-defined interfaces. That way, the next time we need to build some UI, we can write much less code. This means faster development time, fewer bugs, and fewer bytes down the wire.

### Question 22. How To Apply Validation On Props In Reactjs


### Answer
When the application is running in development mode, React will automatically check  for all props that we set on components to make sure they must right correct and right data type.For instance, if we say a component has a Message prop which is a string and is required, React will automatically check and warn  if it gets invalid string or number or boolean objects. For performance reasons this check is only done on dev environments  and on production it is disabled so that rendering of objects is done in fast manner .Warning messages are generated   easily  using a set of predefined options such as:React.PropTypes.stringReact.PropTypes.numberReact.PropTypes.funcReact.PropTypes.nodeReact.PropTypes.boolBackbone.js Tutorial

### Question 23. What Are State And Props In Reactjs


### Answer
State is the place where the data comes from. We must follow approach  to make our state as simple as possible and minimize number of stateful components.For example, ten components that need data from the state, we should create one container component that will keep the state for all of them.The state starts with a default value and when a Component mounts and then suffers from mutations in time (basically generated from user events).A Component manages its own state internally, but--besides setting an initial state--has no business fiddling with the stateof its children.

### Answer (continued)
You could say the state is private.import React from 'react';import ReactDOM from 'react-dom'; var StepCounter = React.createClass({ getInitialState: function() {         return {counter: this.props.initialCount};},  handleClick: function() {  this.setState({counter: this.state. counter + 1}); },  render: function() {  return <div onClick={this.handleClick}>{this.state.counter }</div>; }});ReactDOM.render(< StepCounter initialCount={7}/>, document.getElementById('content'));Props: They are immutable, this is why container component should define state that can be updated and changed. It is used to pass data down from our view-controller(our top level component).

### Answer (part 2)
When we need immutable data in our component we can just add props to reactDOM.render() function.import React from 'react';import ReactDOM from 'react-dom';class PropsApp extends React.Component {   render() {      return (         <div>            <h1>{this.props.headerProperty}</h1>            <h2>{this.props.contentProperty}</h2>         </div>      );   } }ReactDOM.render(<PropsApp headerProperty = "Header from props..." contentProperty = "Content   from props..."/>, document.getElementById('app'));}

# ExpressJS
### Question 24. What Is The Difference Between The State And Props In Reactjs


### Answer


### Props
Passes in from parent component.<PropsApp headerProperty = "Header from props..." contentProperty = "Content&nbsp;from props..."/>This properties are being read by  PropsApp component and sent to ReactDOM View.

### State
Created inside component by getInitialState.this.state reads the property of component and update its value it by this.setState() method and then returns to ReactDOM view.State is private within the component.

# Ext JS
### Question 25. What Are The Benefits Of Redux


### Answer


### Maintainability
Maintenance of Redux becomes easier due to strict code structure and organisation.

### Organization
Code organisation is very strict hence the stability of the code is high which intern increases the work to be much easier.Server rendering: This is useful, particularly to the preliminary render, which keeps up a better user experience or search engine optimization. The server-side created stores are forwarded to the client side.

### Developer tools
It is Highly traceable so changes in position and changes in the application all such instances make the developers have a real-time experience.

### Ease of testing
The first rule of writing testable code is to write small functions that do only one thing and that are independent. Redux's code is made of functions that used to be: small, pure and isolated.ExpressJS Tutorial

### Question 26. How Distinct From Mvc And Flux


### Answer
As far as MVC structure is concerned the data, presentation and logical layers are well separated and handled. here change to an application even at a smaller position may involve a lot of changes through the application. this happens because data flow exists bidirectional as far as MVC is concerned. Maintenance of MVC structures are hardly complex and Debugging also expects a lot of experience for it.Flux stands closely related to redux. A story based strategy allows capturing the changes applied to the application state, the event subscription, and the current state are connected by means of components. Call back payloads are broadcasted by means of Redux.

# Advanced jQuery
### Question 27. What Are Functional Programming Concepts


### Answer
The various functional programming concepts used to structure Redux are listed below:Functions are treated as First class objects.Capable to pass functions in the format of arguments.Capable to control flow using, recursions, functions and arrays.helper functions such as reduce and map filter are used.allows linking functions together.The state doesn't change.Prioritize the order of executing the code is not really necessary.

# CSS Advanced
### Question 28. What Is Redux Change Of State


### Answer
For a release of an action, a change in state to an application is applied, this ensures an intent to change the state will be achieved.Example:The user clicks a button in the application.A function is called in the form of componentSo now an action gets dispatched by the relative container.This happens because the prop (which was just called in the container) is tied to an action dispatcher using mapDispatchToProps (in the container).Reducer on capturing the action it intern executes a function and this function returns a new state with specific changes.The state change is known by the container and modifies a specific prop in the component as a result of the mapStateToProps function.

### Question 29. Where Can Redux Be Used


### Answer
Redux is majorly used is a combination with reacting. it also has the ability to get used with other view libraries too. some of the famous entities like AngularJS, Vue.js, and Meteor. can get combined with Redux easily. This is a key reason for the popularity of Redux in its ecosystem. So many articles, tutorials, middleware, tools, and boilerplates are available.

# Apache Tomcat
### Question 30. What Is The Typical Flow Of Data In A React + Redux App


### Answer
Call-back from UI component dispatches an action with a payload, these dispatched actions are intercepted and received by the reducers. this interception will generate a new application state. from here the actions will be propagated down through a hierarchy of components from Redux store. The below diagram depicts the entity structure of a redux+react setup.

### Question 31. What Is Store In Redux


### Answer
The store holds the application state and supplies the helper methods for accessing the state areregister listeners and dispatch actions. There is only one Store while using Redux. The store is configured via the create Store function. The single store represents the entire state.Reducers return a state via actionexport function configureStore(initialState) {return createStore(rootReducer, initialState);}The root reducer is a collection of all reducers in the application.const root Reducer = combineReducers({donors: donor Reducer,});

### Question 32. Explain Reducers In Redux


### Answer
The state of a store is updated by means of reducer functions. A stable collection of a reducers form a store and each of the stores maintains a separate state associated for itself. To update the array of donors, we should define donor application Reducer as follows.export default function donorReducer(state = [], action) {switch (action.type) {

### Case actionTypes.addDonor
return [...state, action.donor];

### Default
return state;}}The initial state and action are received by the reducers. Based on the action type, it returns a new state for the store. The state maintained by reducers are immutable. The below-given reducer it holds the current state and action as an argument for it and then returns the nextstate:function handelingAuthentication(st, actn){return _.assign({}, st,{auth: actn.pyload});}

### Question 33. What Are Redux Workflow Features


### Answer


### Reset
Allow to reset the state of the store

### Revert
Roll back to the last committed state

### Sweep
All disabled actions that you might have fired by mistake will be removed

### Commit
It makes the current state the initial state

# Javascript Advanced
### Question 34. Explain Action's In Redux


### Answer
Actions in Redux are functions which return an action object. The action type and the action data are packed in the action object. which also allows a donor to be added to the system. Actions send data between the store and application. All information's retrieved by the store are produced by the actions.export function addDonorAction(donor) {return {type: actionTypes.add Donor,donor,};}Internal Actions are built on top of Javascript objects and associate a type property to it.Redis Q&As

### Redis
Redis is an advanced key-value data store and cache.It is referred to as a data structure server.The keys contain strings, hashes, sets, lists, and sorted sets.Redis is an open source, in-memory data structure store, used as a database, cache and message broker.It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

### Redis
Redis, which stands for Remote Dictionary Server, is a fast, open-source, in-memory key-value data store for use as a database, cache, message broker, and queue.You can run atomic operations, like appending to a string; incrementing the value in a hash; pushing an element to a list;computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.In order to achieve performance, Redis works with an in-memory dataset.Depending on your use case, you can persist it either by dumping the dataset to disk every once in a while, or by appending each command to a log.Persistence can be optionally disabled, if you just need a feature-rich, networked, in-memory cache.Redis is a popular choice for caching, session management, gaming, leaderboards, real-time analytics, geospatial, ride-hailing, chat/messaging, media streaming, and pub/sub apps.When a relationship is established, data from the master is transferred to the slave.Once this is done, all changes to the master replicate to the slave.

### Online
redis.io.

### In-memory Database
The in-memory database is a database where it keeps the dataset in RAM.Means that for every interaction with database, you will only access the Main memory; No DISK operations involved during this interaction.Hence the operation will be faster as it directly aceess main memoery instead of any disk operation.

### Replication


### Redis supports simple master to slave replication.  Online
redis.io.

### Operation keys
TYPE key, TTL key, KEYS pattern, EXPIRE key seconds, EXPIREAT key timestamp, EXISTS key, DEL key.

### PHP module used with Redis
In PHP module, P Redis is more preferable than Redid PHP binding or Resident.

## Pluses and Minuses
## Durability
### Durability Overview
- Create a Registry of key prefixes that maps each of your internal documents for that application which own them.- For every class you put through into your Redis infrastructure: design, implement and test the mechanisms for garbage collection or data migration to archival storage.- Design, implement and test a sharding library before you have invested much into your application deployment and make sure that you keep a registry of shards replicated on each server.- Separate all your K/V store and related operations into your own library/API or service.

## Snapshotting
### Isn't the Redis data lost if there's a system crash
To avoid data loss in case of system crash Redis provides persistence by Snapshotting & AOF(Append-only files).

### How Redis achieve persistence by Snapshotting
Snapshot takes the data as it exists at one moment in time & writes it to the disk, will be written to the file referenced as dbfilename.

### 5 steps to initiate snapshots:
The 5 snapshot initiation steps are: BGSAVE, SAVE, Configuration files, SHUTDOWN, Sync with other Redis.a. BGSAVE: When redis client initiate BGSAVE, redis will create a fork so that child process will write a the snapshot to the disk where master interacts with commands.b. SAVE: When redis client initiate SAVE, redis will stop responding any commands until snapshot completes

### C. From Configuration Files
Example: Configuration as SAVE 60 10000   BGSAVE will be called if 10000 writes occure within 60 secondsd. SHUTDOWN: When redis client sends a SHUTDOWN, redis will perform SAVE operations, blocks all operations, shutdowns later.e. Sync with other Redis: If a Redis server connects to another server, it issues SYNC, then master Redis will start BGSAVE.

### How redis achives persistence by AOF
AOF copies incoming write command to disk as they happen.

### It provides file synch options as follows
a. always: Every writes to redis, writes to disk which usually affect redis' performance.b. every sec: Writes to disk every secondc. no: Let OS control syncing to disk

### Growing files
Files will keep on growing as long as AOF executed.

### Won't it consume more memory? What is the solution provided by redis
Redis provides command BG REWRITE AOF which rewrites the existing AOF with the shortest sequence of commands needed to rebuild the current dataset in memory.

## MORE
### Redis persist data
Redis supports so-called "snapshots".This means that it will do a complete copy of whats in memory at some points in time (e.g. every full hour).When you lose power between two snapshots, you will lose the data from the time between the last snapshot and the crash (doesn't have to be a power outage..).Redis trades data safety versus performance, like most NoSQL-DBs do.

### Redis saves data in one of the following cases
automatically from time to timewhen you manually call BGSAVE commandwhen redis is shutting down

### But data in redis is not really persistent, because
crash of redis process means losing all changes since last saveBGSAVE operation can only be performed if you have enough free RAM (the amount of extra RAM is equal to the size of redis DB)

### Redis just a cache


### Like a cache Redis offers
in memory key-value storage

### But unlike a cash Redis
Supports multiple datatypes (strings, hashes, lists, sets, sorted sets, bitmaps, and hyperloglogs)It provides an ability to store cache data into physical storage (if needed).Supports pub-sub modelRedis cache provides replication for high availability (master/slave)Supports ultra-fast lua-scripts.Its execution time equals to C commands execution.Can be shared across multiple instances of the application (instead of in-memory cache for each app instance)

### Redis support transactions
MULTI, EXEC, DISCARD and WATCH are the foundation of transactions in Redis.They allow the execution of a group of commands in a single step, with two important guarantees:All the commands in a transaction are serialized and executed sequentially.It can never happen that a request issued by another client is served in the middle of the execution of a Redis transaction.This guarantees that the commands are executed as a single isolated operation.Either all of the commands or none are processed, so a Redis transaction is also atomic.

### How are Redis pipelining and transaction different
Pipelining is primarily a network optimization.It essentially means the client buffers up a bunch of commands and ships them to the server in one go.The commands are not guaranteed to be executed in a transaction.The benefit here is saving network round trip time for every command.Redis is single threaded so an individual command is always atomic, but two given commands from different clients can execute in sequence, alternating between them for example.Multi/exec, however, ensures no other clients are executing commands in between the commands in the multi/exec sequence.

### Redis handle multiple threads (from different clients) updating the same data structure in Redis
Redis is actually single-threaded, which is how every command is guaranteed to be atomic.While one command is executing, no other command will run.A single-threaded program can definitely provide concurrency at the I/O level by using an I/O (de)multiplexing mechanism and an event loop (which is what Redis does).The fact that Redis operations are atomic is simply a consequence of the single-threaded event loop.The interesting point is atomicity is provided at no extra cost (it does not require synchronization between threads).

### The difference between Redis replication and sharding
Sharding, also known as partitioning, is splitting the data up by key.Sharding is useful to increase performance, reducing the hit and memory load on any one resource.While replication, also known as mirroring, is to copy all data.Replication is useful for getting a high availability of reads.If you read from multiple replicas, you will also reduce the hit rate on all resources, but the memory requirement for all resources remains the same.Any key-value store (of which Redis is only one example) supports sharding, though certain cross-key functions will no longer work.Redis supports replication out of the box.

### The advantage of Redis vs using memory
- Redis is a remote data structure server.It is certainly slower than just storing the data in local memory (since it involves socket roundtrips to fetch/store the data).

### However, it also brings some interesting properties
- Redis can be accessed by all the processes of your applications, possibly running on several nodes (something local memory cannot achieve).- Redis memory storage is quite efficient, and done in a separate process.If the application runs on a platform whose memory is garbage collected (node.js, java, etc ...), it allows handling a much bigger memory cache/store.In practice, very large heaps do not perform well with garbage collected languages.- Redis can persist the data on disk if needed.- Redis is a bit more than a simple cache: it provides various data structures, various item eviction policies, blocking queues, pub/sub, atomicity, Lua scripting, etc ...- Redis can replicate its activity with a master/slave mechanism in order to implement high-availability.Basically, if you need your application to scale on several nodes sharing the same data, then something like Redis (or any other remote key/value store) will be required.

### To use Redis Lists data type
Redis lists are ordered collections of strings.They are optimized for inserting, reading, or removing values from the top or bottom (aka: left or right) of the list.Redis provides many commands for leveraging lists, including commands to push/pop items, push/pop between lists, truncate lists, perform range queries, etc.Lists make great durable, atomic, queues.These work great for job queues, logs, buffers, and many other use cases.

### To use Redis Sets
Sets are unordered collections of unique values.They are optimized to let you quickly check if a value is in the set, quickly add/remove values, and to measure overlap with other sets.These are great for things like access control lists, unique visitor trackers, and many other things.Most programming languages have something similar (usually called a Set).This is like that, only distributed.Redis provides several commands to manage sets.Obvious ones like adding, removing, and checking the set are present.So are less obvious commands like popping/reading a random item and commands for performing unions and intersections with other sets.

### To use Redis over MongoDB
It depends on kind of dev team you are and your application needs but some notes when to use Redis is probably a good idea:CachingCaching using MongoDB simply doesn't make a lot of sense.It would be too slow.If you have enough time to think about your DB design.You can't simply throw in your documents into Redis.You have to think of the way you in which you want to store and organize your data.One example are hashes in Redis.They are quite different from "traditional", nested objects, which means you'll have to rethink the way you store nested documents.One solution would be to store a reference inside the hash to another hash (something like key: [id of second hash]).Another idea would be to store it as JSON, which seems counter-intuitive to most people with a *SQL-background.Redis's non-traditional approach requires more effort to learn, but greater flexibility.If you need really high performance.Beating the performance Redis provides is nearly impossible.Imagine you database being as fast as your cache.That's what it feels like using Redis as a real database.If you don't care that much about scaling.Scaling Redis is not as hard as it used to be.For instance, you could use a kind of proxy server in order to distribute the data among multiple Redis instances.Master-slave replication is not that complicated, but distributing you keys among multiple Redis-instances needs to be done on the application site(e.g. using a hash-function, Modulo etc.).Scaling MongoDB by comparison is much simpler.

# RESTful
### SOA
SOA means Service Oriented Application.

## RESTful Services
### RESTful Web Services
REST stands for REpresentational State Transfer.The underlying protocol for REST is HTTP.RESTful services expose the server application's API in a secure, uniform, stateless manner to the calling client.RESTful services are: Loosely Coupled HTTP applications that are Lightweight, maintainable and scalable.RESTful services have: SOC as in Cient-server seperation, a Uniform interface or contract, a Layerd system design and Code-on-demand.From the Client's view, RESTful services are: Stateless to the Client and Cacheable by the Client.

### RESTful services are Stateless
Communications are based on the HTTP Protocol.The server response can be cached by the clients, but no client context is stored on the server.It's up to the client to ensure that all the required information is provided to the server.The server does not maintain information between client requests.Stateless means it is s a very simple, independent question-answer sequence.The client asks a question, the server answers it.The client will ask another question.The server will not remember the previous question-answer scenario and will need to answer the new question independently.

### RESTful services are Cacheable
Responses may be cached.Caching improves performance and scalability.The client caches requests.The Cache concept is to help with the problem of stateless which was described in the last point.Since each server client request is independent in nature, sometimes the client might ask the server for the same request again.This is even though it had already asked for it in the past.This request will go to the server, and the server will give a response.This increases the traffic across the network.The cache is a concept implemented on the client to store requests which have already been sent to the server.So if the same request is given by the client, instead of going to the server, it would go to the cache and get the required information.This saves the amount of network traffic between the client and server.

### RESTful services are Loosely Coupled HTTP applications with clear client-server separation or Separation of Concerns.
Applications do not require a recompile when a service update is available.The applications do not maintain any state with the service.The applications can cache requests on the client-side, saving bandwith.To the application, the service is just a set of GET, PUT, POST and DELETE verbs.

### RESTful services have Uniform Interface
The uniform interface is obtained via a contract using HTTP verbs.Operations are limited, defined using the HTTP Verbs: GET, PUT, POST, Delete, etc.Code-On-Demand: TBDLayered System Design: TBD

## WCF
### WCF.
WCF is Microsoft  .NET framework, Windows Communication Foundation for creating S O As.WCF can be RESTful: With extra configuration.WCF protocols: HTTP, T C P, M S M Q and Named Pipes.WCF returns: only data.WCF hosting: Can be self-hosted or I I S Server hosted.WCF bandwith: WCF is heavy and requires a greater bandwith.WCF is a SOAP-based service.

## MVC
### ASP.NET MVC.
MVC is used to create web applications which return both data and Views.MVC requests are mapped to Action Methods.

## Web API
### ASP.NET Web API.
Web API was introduced in .NET Framework 4.Use Web API to create: S O A, RESTful, HTTP services for clients such as Browsers, mobile and I o T devices.Web API is: HTTP protocol, only.Web API returns: Data, not views.Web API hosting: Can be self-hosted or I I S Server hosted.

### Have a limited bandwidth? Web API is lightweight and good for devices with a limited bandwith.
Web API requests: Request Action Verbs are mapped to Actions.Web API is not a SOAP-based service.

### ASP.NET Web API 2.0 features:
1. Attribute Routing.2. CORS (Cross-Origin Resource Sharing).3. OWIN self-hosting. OWIN means Open Web Interface for .NET.4. IHttpActionResult.5. Web API OData, etc.

### Request Verbs or HTTP Verbs.
RESTful services can perform CRUD operations: Create, Read, Update, Delete.HTTP POST creates a new resource on the resources.HTTP GET retrieves the existing resource.HTTP PUT updates the existing resource.HTTP DELETE deletes an existing resource.

### Web API Parameter Binding.
When Web API calls a method on a controller, it must set the values for the parameters. This is Parameter Binding.

### Default Web API parameter binding rules are From U R I and From Body
From U R I: If the parameter is a Simple type, then Web API tries to get the value from the U R I.Simple Type includes .NET Primitive types like int, double, DateTime, TimeSpan, GUID, string, any type which can be converted from the string type.From Body: If the parameter is a Complex type, then Web API will try to bind the values from the message body.

### Web API Content Negotiation.
Content Negotiation is the process of selecting the best representation for a given response when there are multiple representations available.Two headers responsible for Content Negotiation are the Content-Type header and the Accept header:Accept: The content-type header tells the server about the data, the server is going to receive from the client whereas another way to use Accept-Header, which tells the format of data requested by the Client from a server.

### Web API Media-Type Formatter.
Media-Type formatter are classes responsible for serializing the response data in the format that the client asked for.Media-Type formatter is an abstract class from which JsonMediaTypeFormatter and XmlMediaTypeFormatter class derived from.JsonMediaTypeFormatter handles JSON format.XmlMediaTypeFormatter handles X M L format.

## Autentication and Authorization.
### Authorize Attribute.
Web API has an authorization filter using the Authorize Attribute to determine if the user is authenticated.If the user is not authenticated, the 401 Unauthorized HTTP Status Code is returned.

### HTTP Authentication.
In Basic HTTP Authentication, the user is authenticated through the service in which the client passes username and password in the HTTP Authorization request headers.The credentials are formatted as the string username colon password.

## Routing
### Web API HTTP request Routing to the MVC Controller.
The HTTP request maps to the controller.To determine which action to invoke, the Web API framework uses a routing table.

## Versioning
### Web API Versioning.


### For Web API versioning, use
1. the URI.2. the Query String Parameter.3. the Custom Header Parameter.4. the Accept Header Parameter.

## Exception handling
## SOLID
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
Stored procedure boosts application performance.Stored procedure execution plans can be reused as they cached in SQL Server's memory which reduces server overhead.They can be reused.It can encapsulate logic.You can change the stored procedure code without affecting clients.They provide better security for your data.

### Recursive stored procedure
SQL Server supports recursive stored procedure which calls by itself.Recursive stored procedure can be defined as a method of problem solving wherein the solution is arrived repetitively.It can nest up to 32 levels.

### The differences between Stored Procedure and the dynamic SQL
Stored Procedure is a set of statements which is stored in a compiled form.Dynamic SQL is a set of statements that dynamically constructed at runtime and it will not be stored in a Database and it simply execute during run time.

### Which SQL server table is used to hold the stored procedure scripts
Sys.SQL_Modules is a SQL Server table used to store the script of stored procedure.Name of the stored procedure is saved in the table called Sys.Procedures.

### The command used to Recompile the stored procedure at run time
Stored Procedure can be executed with the help of keyword called RECOMPILE.Example: Exe <SPName>  WITH RECOMPILEOr we can include WITHRECOMPILE in the stored procedure itself.

### It possible to call a stored procedure within a stored procedure
Yes, we can call a stored procedure within a stored procedure.It is called the recursion property of the SQL server and these types of stored procedures are called nested stored procedures.

## TRIGGERS
### A Trigger and types of a trigger
The trigger allows us to execute a batch of SQL code when table event occurs (INSERT, UPDATE or DELETE command executed against a specific table).Triggers are stored in and managed by DBMS.Triggers can execute a stored procedure.Name 3 types of triggers available in the SQL Server.DML Triggers: DML or Data Manipulation Language triggers are invoked whenever any of the DML commands like INSERT, DELETE or UPDATE happens on the table or the view.DDL Triggers: DDL or Data Definition Language triggers are invoked whenever any changes occur in the definition of any of the database objects instead of actual data.DDL Triggers are very helpful to control the production and development of database environments.Logon Triggers: These are very special triggers that fire in case of the logon event of the SQL Server.Logon Triggers are fired before the setup of a user session in the SQL Server.

### A Trigger
Triggers are used to execute a batch of SQL code when insert or update or delete commands are executed against a table.Triggers are automatically triggered or executed when the data is modified.It can be executed automatically on insert, delete and update operations.

### The 4 types of Triggers
INSERT, DELETE, UPDATE, INSTEAD OF.

### What will be query used to get the list of triggers in a database
Query to get the list of triggers in database-SELECT * FROM sys.objects WHERE type='tr'

## TRANSACTIONS
### Describe SAVEPOINT.
Suppose there are set of transactions performed on the tables and some of the transactions are very stable.Set a SAVEPOINT after the stable transactions so we can rollback to that safe point.Example: Command: TRANSACTION Safe   transaction 1. SAVEPOINT S1.         Command: TRANSACTION Unsafe transaction 2. SAVEPOINT S2.         Command: TRANSACTION Unsafe transaction 3. SAVEPOINT S3.         Command: ROLLBACK TO S1. This rolls back the two unsave transactions. Only the safe transaction will persist.Describe AUTOCOMMIT.The AUTOCOMMIT command automatically commits each transaction after its execution.If AUTOCOMMIT is set, then there is no need to explicitly issue COMMIT.If AUTOCOMMIT is on, we cannot rollback transactions,AUTOCOMMIT needs to be SET or UNSET before we begin any transactions.

### The properties of a transaction
Generally, these properties are referred to as ACID properties.AtomicityConsistencyIsolationDurabilityACID

### Atomicity
All or None: Within a transaction: Either all the SQL Statements will be executed or none will be executed.

### Consistency
Only valid data is written into the DB. Within a transaction: If any SQL statement violates DB rules or constraints, all statements will be rolled back. A transaction never leaves the DB in a half-finished state.

### Isolation
Transactions will not interfere with each other. 1st tx must complete and commit before 2nd tx begins.

### Durability
Once the tx is committed, the DB should not be lost in case of s/w or h/w failures. Use DB backups and tx logs. The DB will keep track of pending changes such that the server can recover from an abnormal termination.SQL SERVER QUESTIONS and ANSWERS

## GENERAL
### GENERAL Overview
XML Datatype: XML data type is used to store XML documents by creating columns and variables and storing XML instances.Change Data Capture: CDC captures recently changed data. CDC is in SQL server 2008.

### Collation
Collasion rules: specify Data Comparison, Data Sorting, Table Sort Order, Character Sorting to create character sequences.Collation Character options: specify case-sensitivity, accent marks, kana character types and character width.Collation Data sorting types: Case sensitive, Case Insensitive and Binary.

### Replication
Replication is required.Replication synchronizes data among multiple servers with the help of a replica set.Replication allows selecting among multiple servers to perform the read/write operations.Replication increases reading capacity.

## VERSIONS
### Which is the latest version of SQL server and when it is released
SQL Server 2019 is the latest version of SQL server that is available in the market and Microsoft launched this on November 4th, 2019 with the support of the Linux O/S.

### The various editions of SQL server 2019 that are available in the market
SQL Server 2019 is available in 5 editions.Enterprise: The Enterprise edition  delivers comprehensive high-end datacenter capabilities with blazing-fast performance, unlimited virtualization, and end-to-end business intelligence for mission-critical workloads and end-user access to data insights.Standard: The Standard edition delivers basic data management and business intelligence database for departments and small organizations to run their applications and supports common development tools for on-premises and cloud-enabling effective database management.Web: The Web edition is a low total-cost-of-ownership option for Web hosters and Web VAPs to provide scalability, affordability, and manageability capabilities for small to large-scale Web properties.Express: The Express edition is the entry-level, free database and is ideal for learning and building desktop and small server data-driven applications.Developer:  The Developer edition lets developers build any kind of application on top of SQL server.The Developer edition includes all the functionality of Enterprise edition, but is licensed for use as a development and test system, not as a production server.

## COPY, BULK COPY, BULK INSERT and MIRRORING
### COPY, BULK COPY, BULK INSERT and MIRRORING Overview
Transaction Log records are sent from the principal server to the secondary server to keep the secondary server up to date.

### Mirroring advantages
More robust: Mirroring is more robust and efficient than Log shipping.Failover: Mirroring has an automatic failover mechanism.The secondary server is synced with the primary in near real-time.

## LOG SHIPPING, RECOVERY MODELS and LOG BACKUP
### LOG SHIPPING, RECOVERY MODELS and LOG BACKUP Overview
Full Backup contains part of the transaction log so that it can be recovered.

## SQL INJECTION
## AUTHENTICATION, USERS and LOGIN
## AGENTS, JOBS and TASKS
## LINKED SERVERS
## PERFORMANCE
### PERFORMANCE Overview
The QUERY OPTIMIZER: generates multiple QUERY PLANS for a single query and determines the most efficient plan to run.

### An EXECUTION PLAN
An execution plan is a graphical or textual way of showing how the SQL server breaks down a query to get the required result.It helps a user to determine why queries are taking more time to execute and based on the investigation user can update their queries for the maximum result.Query Analyzer has an option, called Show Execution Plan (located on the Query drop-down menu).If this option is turned on, it will display a query execution plan in a separate window when the query is run again.

## EXCEPTIONS
### How exceptions can be handled in SQL server Programming
Exceptions are handled using TRY----CATCH constructs and it is handles by writing scripts inside the TRY block and error handling in the CATCH block.

## NORMALIZATION
### Normalization
The process of table design to minimize the data redundancy is called normalization.We need to divide a database into two or more tables and define relationships between them.Normalization usually involves dividing a database into two or more tables and defining relationships between the tables.

### Normalization forms
1NF  Eliminate Repeating Groups:                          Make a separate table for each set of related attributes, and give each table a primary key. Each field contains at most one value from its attribute domain.2NF  Eliminate Redundant Data:                            If an attribute depends on only part of a multi-valued key, remove it to a separate table.3NF  Eliminate Columns Not Dependent On Key:              If attributes do not contribute to the description of the key, remove them to a separate table.

### Normalization forms (part 2)
All attributes must be directly dependent on the primary key.BCNF Boyce-Codd Normal Form:                              If there are non-trivial dependencies between candidate key attributes, separate them into distinct tables.4NF  Isolate Independent Multiple Relationships:          No table may contain two or more 1:n or n:m relationships that are not directly related.5NF  Isolate Semantically Related Multiple Relationships: There may be practical constraints on information that justifies separating logically related many-to-many relationships.ONF  Optimal Normal Form:                                 A model limited to only simple (elemental) facts, as expressed in Object Role Model notation.DKNF Domain-Key Normal Form:                              A model free from all modification is said to be in DKNF.

### De-normalization
De-normalization is the process of adding redundant data to a database to enhance the performance of it.It is a technique to move from higher to lower normal forms of database modeling to speed up database access.SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.

## TYPES
## CLAUSES: HAVING, WHERE and FOR
## COMMANDS: UNION, MINUS, INTERSECT
## COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR
### COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR Overview
SET NOCOUNT OFF - Display the number of records affected when commands are executed.        SET NOCOUNT ON  - Do not display the number of records affected. Default setting.    RAISERROR command.        RAISEERROR is used for user defined error messages.        RAISEERROR generates and initiates error processing for a given session.        Those user defined messages are stored in sys.messages table.

## LOCAL and GLOBAL VARIABLES - SYSTEM DEFINED FUNCTIONS
## FUNCTIONS
### Functions in the SQL server
Functions are the sequence of the statements which accept inputs, process the inputs to perform some specific task and then provide the outputs.Functions should have some meaningful name but these should not start with a special character such as %, #, @, etc.Functions: SUBSTR and CHARINDEX.SUBSTR    returns a specific portion of string in a given string.CHARINDEX returns the character position in a given string.SUBSTRING('Smiley',1,3)     returns: SmiCHARINDEX('i', 'Smiley',1)  returns: 3 as result as I appears in 3rd position of the string.Function: FLOOR.FLOOR rounds up a non-integer value to the previous least integer.Example: FLOOR(6.7) Returns 6.Function: SIGN.SIGN determines whether the number specified is Positive, Negative or Zero.SIGN returns +1, -1 or 0.Example: SIGN(-35) returns -1Function: ISNULL().ISNULL function checks whether value given is NULL or not NULL.ISNULL provides to replace a value with the NULL.Function: COALESCE.COALESCE returns the first non-null expression within the arguments.COALESCE returns a non-null from more than one column in the arguments.Example: SELECT COALESCE(empno, empname, salary) FROM employee;

## USER-DEFINED FUNCTIONS
## PRE-DEFINED FUNCTIONS
## SUBQUERIES
### SUBQUERIES Overview
Multiple row sub query:    returns multiple rows.Multiple column sub query: returns multiple columns to the main query. With the sub query result, the main query is executed.

## TABLES and COLUMNS
### Table records: How can we get count of the number of records in a table
SELECT * from <tablename>SELECT COUNT(*) from <tablename>SELECT rows FROM sysindexes WHERE id=OBJECT_ID(tablename) AND indid<2

### Relational table properties
Values are atomic, Column values are of the same kind, Each row is unique, The sequence of columns is insignificant, The sequence of rows is insignificant, Each column has a unique name.

### Identity
An identity column in the SQL automatically generates numeric values.We can be defined as a start and increment value of the identity column.Identity columns do not need to be indexed.

### Rename a column in the output of the SQL query
SELECT column_name AS new_name FROM table_name;SECT returns all distinct rows selected by both queries.

### TABLESAMPLE
TABLESAMPLE extracts a sample of rows randomly that are all necessary for the application.The sample rows taken are based on the percentage of rows.

## DELETE and TRUNCATE
## LOCAL and GLOBAL TEMPORARY TABLES
## VIEWS
## COLUMNS
### COLUMNS Overview
When a one table's PRIMARY KEY is added to related tables to create the common field which relates the two tables, it is called a FOREIGN KEY.The FOREIGN KEY constraint enforces referential integrity.

### CHECK Constraint
The CHECK constraint limits the values or type of data that can be stored in a column.The CHECK constraint enforces domain integrity.

## INDEXES
### INDEXES Overview
SELECT rows     FROM indexes WHERE id = OBJECT_ID(tableName) AND indid less than 2;Heap: A table that does not contains no clustered or non-clustered indexes.Filtered Index: An index with a WHERE clause.Filtered Index filters some portion of rows in a table to improve query performance, index maintenance and reduces index storage costs.

### Maximum indexes per table
100 Indexes per table for SQL server 2008.1000 Indexes per table: 1 Clustered Index and 999 Non-clustered indexes per table.

## CONSTRAINTS
### CONSTRAINTS Overview
DEFAULT: The DEFAULT constraint provides some default value that can be inserted in the column if no value is specified for that column.UNIQUE: The UNIQUE constraint puts a constraint that each row of a particular column must have a unique value. More than one unique constraint can be applied to a single table.PRIMARY KEY: The PRIMARY KEY constraint puts a constraint to have a primary key in the table to identify each row of a table uniquely. This cannot be null or duplicate data.FOREIGN KEY: The FOREIGN KEY constraint puts a constraint that the foreign key should be there.A Primary key in one table is the foreign key of another table.Foreign Key is used to create a relation between 2 or more tables.

## SQL SERVER COMMANDS IN 4 LOGICAL GROUPS
### Which language is supported by SQL server
SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.Name the 4 types of SQL commands.DML or Data Manipulation Language.DDL or Data Definition Language.DCL or Data Control Language.TCL or Transaction Control Language.

### Using these commands we can
1. Define structure of our database.2. INSERT or UPDATE the data.3. Can control database access and privileges.Describe DML, or Data Manipulation Language, commands.DML commands manipulate table records.

### DML commands are
SELECT records,INSERT new records,UPDATE existing records,DELETE existing records.UPDATE or DELETE without the WHERE clause will UPDATE or DELETE all records in the table.Describe DDL, or Data Definition Language, commands.DDL commands design and define the database structure.DDL commands define and create database objects such as Tables, Procedures, Views, etc.

### DDL commands are
CREATE. Create a new table, database, procedure, view, or trigger.ALTER.  Use alter commands for editing database objects such as table, procedure, view etc, add or delete column from table.DROP.   Delete database objects.RENAME. Rename an database object existing.CREATE TABLE table-name: will create a new table. In the body of this command we enter the table's columns and attributes.Similar syntax is also for creating new Views, Procedures or Triggers.ALTER: Edit an object. For example, add a new column or attribute in a table.DROP: Delete database objects.Describe DCL, or Data Control Language, commands.DCL commands perform user access control and permission management by allowng or denying user actions on tables or records.

### DCL commands are


### GRANT
GRANT permissions on the table, and other objects, for certain users of database.GRANT example: Give privileges to a user to SELECT, INSERT, UPDATE and DELETE on a table.

### DENY
DENY permissions from users.

### REVOKE
REVOKE permissions from users.REVOKE takes back privilege to the default permission.REVOKE example: Take back INSERT permissions on a table for a user.

### Describe TCL, or Transaction Control Language, commands.
TCL commands manage and control T SQL transactions.TCL commands ensure that our transaction is successfully done.TCL commands ensure that the database integrity is not violated.

### TCL commands are
BEGIN TRAN: BEGIN TRAN marks the beginning of a transaction.COMMIT TRAN: COMMIT TRAN commits the completed transaction.COMMIT TRAN permentantly saves the transaction in the database.ROLLBACK: ROLLBACK goes back to beginning if something was not right in transaction.ROLLBACK rolls back changes. For example: (Transactional Log backup, Copy Only backup, File and Filegroup backup)SAVE TRAN: SAVE TRAN saves the transaction to provide the convenience that the transaction can be rolled back to the point wherever required.

### COMMIT vs ROLLBACK
When COMMIT is executed, statements between BEGIN and COMMIT become persistent to database.When ROLLBACK is executed, statements between BEGIN and ROLLBACK are reverted to the state before the BEGIN statement.

### Magic Tables
Magic tables are created to hold values during DML operations like INSERT, DELETE, and UPDATE.Magic tables are used inside the triggers for data transaction.

## STORED PROCEDURES
### STORED PROCEDURES Overview
Stored procedure names are stored in table Sys.Procedures.Stored procedure scripts are stored in table Sys.SQL_Modules.k

### RECOMPILE: Command to recompile the stored procedure at run time
Run: exe Stored Procedure Name WITH RECOMPILEOr:  Include WITHRECOMPILE within the stored procedure.

### Recursion or nested stored procedures
Call a stored procedure within a stored procedure.

## TRIGGERS
### A Trigger and types of a trigger
The trigger allows us to execute a batch of SQL code when table event occurs (INSERT, UPDATE or DELETE command executed against a specific table).Triggers are stored in and managed by DBMS.Triggers can execute a stored procedure.Name 3 types of triggers available in the SQL server.DML Triggers: DML or Data Manipulation Language triggers are invoked whenever any of the DML commands like INSERT, DELETE or UPDATE happens on the table or the view.DDL Triggers: DDL or Data Definition Language triggers are invoked whenever any changes occur in the definition of any of the database objects instead of actual data.DDL Triggers are very helpful to control the production and development of database environments.Logon Triggers: These are very special triggers that fire in case of the logon event of the SQL server.Logon Triggers are fired before the setup of a user session in the SQL server.

### A Trigger
Triggers are used to execute a batch of SQL code when insert or update or delete commands are executed against a table.Triggers are automatically triggered or executed when the data is modified.It can be executed automatically on insert, delete and update operations.

### The 4 types of Triggers
INSERT, DELETE, UPDATE, INSTEAD OF.

### What will be query used to get the list of triggers in a database
Query to get the list of triggers in database-SELECT * FROM sys.objects WHERE type='tr'

## TRANSACTIONS
### Describe SAVEPOINT.
Suppose there are set of transactions performed on the tables and some of the transactions are very stable.Set a SAVEPOINT after the stable transactions so we can rollback to that safe point.EX: Command: TRANSACTION Safe   transaction 1. SAVEPOINT S1.EX: Command: TRANSACTION Unsafe transaction 2. SAVEPOINT S2.EX: Command: TRANSACTION Unsafe transaction 3. SAVEPOINT S3.EX: Command: ROLLBACK TO S1. This rolls back the two unsave transactions. Only the safe transaction will persist.

### Describe AUTOCOMMIT.
The AUTOCOMMIT command automatically commits each transaction after its execution.If AUTOCOMMIT is set, then there is no need to explicitly issue COMMIT.If AUTOCOMMIT is on, we cannot rollback transactions,AUTOCOMMIT needs to be SET or UNSET before we begin any transactions.

### ACID or Transaction Properties
Atomicity, Consistency, Isolation, Durability.

# SQL SERVER
## GENERAL ...
### RDBMs
RDBMs: are Relational Database Management Systems.RDBMs: use tables to maintain data.RDBMs: have data usage tools.RDBMs: create table relationships.RDBMs: recombine data items from different files.SQL: is a declarative language.A database engine: is a SQL server service which starts when the Operating System starts.MS SQL server: is an RDBMS that stores and manages information in the database.Port 1433: By default, SQL server runs on TCP/IP port 1433.OLTP: Online Transaction Processing uses data normalization rules to ensure data integrity, simplifying complex information into a simple structure.Duplicate rows: Delete duplicate rows with CTE and ROW NUMER.Locks: Check database locks with sp_lock.XML Datatype: XML data type is used to store XML documents by creating columns and variables and storing XML instances.Change Data Capture: CDC captures recently changed data. CDC is in SQL server 2008.

### Collation
Collasion rules: specify Data Comparison, Data Sorting, Table Sort Order, Character Sorting to create character sequences.Collation Character options: specify case-sensitivity, accent marks, kana character types and character width.Collation Data sorting types: Case sensitive, Case Insensitive and Binary.

## NORMALIZATION
### Normalization
The process of table design to minimize the data redundancy is called normalization.We need to divide a database into two or more tables and define relationships between them.Normalization usually involves dividing a database into two or more tables and defining relationships between the tables.

### #### Normalization forms
1NF:  Eliminate Repeating Groups: Make a separate table for each set of related attributes, and give each table a primary key.      Each field contains at most one value from its attribute domain.2NF:  Eliminate Redundant Data: If an attribute depends on only part of a multi-valued key, remove it to a separate table.3NF:  Eliminate Columns Not Dependent On Key: If attributes do not contribute to the description of the key, remove them to a separate table.      All attributes must be directly dependent on the primary key.BCNF: Boyce-Codd Normal Form: If there are non-trivial dependencies between candidate key attributes, separate them into distinct tables.4NF:  Isolate Independent Multiple Relationships: No table may contain two or more 1:n or n:m relationships that are not directly related.5NF:  Isolate Semantically Related Multiple Relationships: There may be practical constraints on information that justifies separating logically related many-to-many relationships.ONF:  Optimal Normal Form: A model limited to only simple (elemental) facts, as expressed in Object Role Model notation.DKNF: Domain-Key Normal Form: A model free from all modification is said to be in DKNF.

### Repeating 1NF, 2NF and 3NF
1NF:  Eliminate Repeating Groups: Make a separate table for each set of related attributes, and give each table a primary key.      Each field contains at most one value from its attribute domain.2NF:  Eliminate Redundant Data: If an attribute depends on only part of a multi-valued key, remove it to a separate table.3NF:  Eliminate Columns Not Dependent On Key: If attributes do not contribute to the description of the key, remove them to a separate table.      All attributes must be directly dependent on the primary key.#### De-NormalizationDe-normalization is the process of adding redundant data to a database to enhance the performance of it.It is a technique to move from higher to lower normal forms of database modeling to speed up database access.SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.

## TYPES: VARCHAR and N VARCHAR ...
## CLAUSES: HAVING, WHERE and FOR ...
## COMMANDS: UNION, MINUS, INTERSECT ...
### UNION
UNION Returns all distinct rows selected by either query.UNION is similar to the JOIN command, select related information from two tables UNION command is used.

### UNION ALL
UNION ALL Returns all rows selected by either query, including all duplicates.UNION ALL is equal to the UNION command, except that UNION ALL selects all values.UNION ALL will not remove duplicate rows.UNION ALL, instead, retrieves all rows from all tables.

### MINUS
MINUS Returns all distinct rows selected by the first query but not by the second.

### INTERSECT
INTERSECT Returns all distinct rows selected by both queries.

## AUTHENTICATION, USERS and LOGIN
## AGENTS, JOBS and TASKS ...
### SQL server agent
Allows us to schedule the jobs and scripts.Plays a vital role in day to day tasks of SQL server administrator(DBA).Is helpful in implementing the day to day DBA tasks by automatically executing them on a scheduled basis.Implements the tasks easily with the scheduler engine which allows jobs scheduling.Scheduled tasks or jobs: Automates tasks to run at specified times and intervals and order. Nighttime work is reduced. Feeds can be scheduled.

## LOCAL and GLOBAL VARIABLES - SYSTEM DEFINED FUNCTIONS ...
### @ is for a local variable


### @@ is for a global variable or function.
@@ is prefixed to global variables maintained by the server.Global variables are system-defined functions.EX: Global variables or functions: @@IDENTITY, @@ROWCOUNT, @@TRANCOUNT

### @@SPID
Syntax: SELECT @@SPID - returns the session ID of the current user process.   @@VERSIONSyntax: SELECT @@VERSION - returns the SQL server version.   @@ROWCOUNT       @@ROWCOUNT is a system variable that is used to return the number of rows that are affected by the last executed statement in the batch.

## FUNCTIONS ...
### Functions in the SQL server
Functions are the sequence of the statements which accept inputs, process the inputs to perform some specific task and then provide the outputs.Functions should have some meaningful name but these should not start with a special character such as %, #, @, etc.Functions: SUBSTR and CHARINDEX.SUBSTR returns a specific portion of string in a given string.CHARINDEX returns the character position in a given string.SUBSTRING('Smiley',1,3)     returns: SmiCHARINDEX('i', 'Smiley',1)  returns: 3 as result as I appears in 3rd position of the string.Function: FLOOR.FLOOR rounds up a non-integer value to the previous least integer.Example: FLOOR(6.7) Returns 6.Function: SIGN.SIGN determines whether the number specified is Positive, Negative or Zero.SIGN returns +1, -1 or 0.Example: SIGN(-35) returns -1Function: ISNULL.ISNULL function checks whether value given is NULL or not NULL.ISNULL provides to replace a value with the NULL.Function: COALESCE.COALESCE returns the first non-null expression within the arguments.COALESCE returns a non-null from more than one column in the arguments.Example: SELECT COALESCE(empno, empname, salary) FROM employee;

## USER-DEFINED FUNCTIONS
## PRE-DEFINED FUNCTIONS ...
## SUBQUERIES
### SUBQUERIES Overview
Multiple row sub query:    returns multiple rows.Multiple column sub query: returns multiple columns to the main query. With the sub query result, the main query is executed.

## TABLES and COLUMNS ...
### Table records: How can we get count of the number of records in a table
SELECT * from <tablename>SELECT COUNT(*) from <tablename>SELECT rows FROM sysindexes WHERE id=OBJECT_ID(tablename) AND indid less than 2

### Relational table properties
Values are atomic,Column values are of the same kind,Each row is unique,The sequence of columns is insignificant,The sequence of rows is insignificant,Each column has a unique name.

### Again, the relational table properties are
Values are atomic,Column values are of the same kind,Each row is unique,The sequence of columns is insignificant,The sequence of rows is insignificant,Each column has a unique name.

### Identity
An identity column in the SQL automatically generates numeric values.We can be defined as a start and increment value of the identity column.Identity columns do not need to be indexed.

### Rename a column in the output of the SQL query
SELECT column_name AS new_name FROM table_name;SECT returns all distinct rows selected by both queries.

### TABLESAMPLE
TABLESAMPLE extracts a sample of rows randomly that are all necessary for the application.The sample rows taken are based on the percentage of rows.

## DELETE and TRUNCATE ...
## LOCAL and GLOBAL TEMPORARY TABLES ...
## VIEWS ...
## COLUMNS ...
### COLUMNS ... Overview
When a one table's PRIMARY KEY is added to related tables to create the common field which relates the two tables, it is called a FOREIGN KEY.The FOREIGN KEY constraint enforces referential integrity.

### CHECK Constraint
The CHECK constraint limits the values or type of data that can be stored in a column.The CHECK constraint enforces domain integrity.

## INDEXES ...
### INDEXES ... Overview
SELECT rows     FROM indexes WHERE id = OBJECT_ID(tableName) AND indid less than 2;Heap: A table that does not contains no clustered or non-clustered indexes.Filtered Index: An index with a WHERE clause.Filtered Index filters some portion of rows in a table to improve query performance, index maintenance and reduces index storage costs.

### Maximum indexes per table
100 Indexes per table for SQL server 2008.1000 Indexes per table: 1 Clustered Index and 999 Non-clustered indexes per table.

## CONSTRAINTS ...
### CONSTRAINTS ... Overview
DEFAULT: The DEFAULT constraint provides some default value that can be inserted in the column if no value is specified for that column.UNIQUE: The UNIQUE constraint puts a constraint that each row of a particular column must have a unique value. More than one unique constraint can be applied to a single table.PRIMARY KEY: The PRIMARY KEY constraint puts a constraint to have a primary key in the table to identify each row of a table uniquely. This cannot be null or duplicate data.FOREIGN KEY: The FOREIGN KEY constraint puts a constraint that the foreign key should be there.A Primary key in one table is the foreign key of another table.Foreign Key is used to create a relation between 2 or more tables.

## SQL SERVER COMMANDS IN 4 LOGICAL GROUPS ...
### Which language is supported by SQL server
SQL Server is based upon the implementation of the SQL also known as Structured Query Language to work with the data inside the database.Name the 4 types of SQL commands, DML, DDL, DCL and TCL.DML or Data Manipulation Language.DDL or Data Definition Language.DCL or Data Control Language.TCL or Transaction Control Language.Again,DML is Data Manipulation Language.DDL is Data Definition Language.DCL is Data Control Language.TCL is Transaction Control Language.

### Using these commands we can
1. Define structure of our database.2. INSERT or UPDATE the data.3. Can control database access and privileges.DML, or Data Manipulation Language, commands.DML commands manipulate table records.

### DML commands are
SELECT records,INSERT new records,UPDATE existing records,DELETE existing records.UPDATE or DELETE without the WHERE clause will UPDATE or DELETE all records in the table.DDL, or Data Definition Language, commands.DDL commands design and define the database structure.DDL commands define and create database objects such as Tables, Procedures, Views, etc.

### DDL commands are
CREATE. Create a new table, database, procedure, view, or trigger.ALTER.  Use alter commands for editing database objects such as table, procedure, view etc, add or delete column from table.DROP.   Delete database objects.RENAME. Rename an database object existing.CREATE TABLE table-name: will create a new table. In the body of this command we enter the table's columns and attributes.Similar syntax is also for creating new Views, Procedures or Triggers.ALTER: Edit an object. For example, add a new column or attribute in a table.DROP: Delete database objects.DCL, or Data Control Language, commands.DCL commands perform user access control and permission management by allowng or denying user actions on tables or records.

### DCL commands are


### GRANT
GRANT permissions on the table, and other objects, for certain users of database.GRANT example: Give privileges to a user to SELECT, INSERT, UPDATE and DELETE on a table.

### DENY
DENY permissions from users.

### REVOKE
REVOKE permissions from users.REVOKE takes back privilege to the default permission.REVOKE example: Take back INSERT permissions on a table for a user.TCL, or Transaction Control Language, commands.TCL commands manage and control T SQL transactions.TCL commands ensure that our transaction is successfully done.TCL commands ensure that the database integrity is not violated.

### TCL commands are
BEGIN TRAN: BEGIN TRAN marks the beginning of a transaction.COMMIT TRAN: COMMIT TRAN commits the completed transaction.COMMIT TRAN permentantly saves the transaction in the database.ROLLBACK: ROLLBACK goes back to beginning if something was not right in transaction.ROLLBACK rolls back changes. For example: (Transactional Log backup, Copy Only backup, File and Filegroup backup)SAVE TRAN: SAVE TRAN saves the transaction to provide the convenience that the transaction can be rolled back to the point wherever required.

### COMMIT vs ROLLBACK
When COMMIT is executed, statements between BEGIN and COMMIT become persistent to database.When ROLLBACK is executed, statements between BEGIN and ROLLBACK are reverted to the state before the BEGIN statement.

### Magic Tables
Magic tables are created to hold values during DML operations like INSERT, DELETE, and UPDATE.Magic tables are used inside the triggers for data transaction.

## STORED PROCEDURES ...
### STORED PROCEDURES ... Overview
Stored procedure names are stored in table Sys.Procedures.Stored procedure scripts are stored in table Sys.SQL_Modules.k

### RECOMPILE: Command to recompile the stored procedure at run time
Run: exe Stored Procedure Name WITH RECOMPILEOr:  Include WITHRECOMPILE within the stored procedure.

### Recursion or nested stored procedures
Call a stored procedure within a stored procedure.

## TRIGGERS ...
### A Trigger and types of a trigger
The trigger allows us to execute a batch of SQL code when table event occurs (INSERT, UPDATE or DELETE command executed against a specific table).Triggers are stored in and managed by DBMS.Triggers can execute a stored procedure.Name 3 types of triggers available in the SQL server, DML Triggers, DDL Triggers and Logon Triggers.DML Triggers: DML or Data Manipulation Language triggers are invoked whenever any of the DML commands like INSERT, DELETE or UPDATE happens on the table or the view.DDL Triggers: DDL or Data Definition Language triggers are invoked whenever any changes occur in the definition of any of the database objects instead of actual data.DDL Triggers are very helpful to control the production and development of database environments.Logon Triggers: These are very special triggers that fire in case of the logon event of the SQL server.Logon Triggers are fired before the setup of a user session in the SQL server.

### A Trigger
Triggers are used to execute a batch of SQL code when insert or update or delete commands are executed against a table.Triggers are automatically triggered or executed when the data is modified.It can be executed automatically on insert, delete and update operations.The 4 types of Triggers are: INSERT, DELETE, UPDATE and INSTEAD OF.To get the list of triggers in a database: SELECT * FROM sys.objects WHERE type='tr'

## TRANSACTIONS ...
### TRANSACTIONS ... Overview
ACID or Transaction properties: Atomicity, Consistency, Isolation, Durability.

## RECOVERY MODELS, BACKUP, LOG SHIPPING and REPLICATION ...
## Recovery models
## Backup types:
## Log Shipping
### Log Shipping Overview
The secondary database can be used as a read-only purpose.   Multiple secondary standby servers are possible.   Low maintenance.

## Replication
## COPY, BULK COPY, BULK INSERT and MIRRORING ...
### COPY, BULK COPY, BULK INSERT and MIRRORING ... Overview
Transaction Log records are sent from the principal server to the secondary server to keep the secondary server up to date.

### Mirroring advantages
More robust: Mirroring is more robust and efficient than Log shipping.Failover: Mirroring has an automatic failover mechanism.The secondary server is synced with the primary in near real-time.

## COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR ...
### COMMANDS: GETDATE, SYSDATETIME, UPDATE_STATISTICS, CREATEDATABASE, SERVERPROPERTY, SET NOCOUNT, RAISERROR ... Overview
SET NOCOUNT ON  - Do not display the number of records affected. Default setting.RAISERROR command.RAISEERROR is used for user defined error messages.RAISEERROR generates and initiates error processing for a given session.Those user defined messages are stored in sys.messages table.

## EXCEPTIONS ...
### How exceptions can be handled in SQL server Programming
Exceptions are handled using TRY----CATCH constructs and it is handles by writing scripts inside the TRY block and error handling in the CATCH block.

## VERSIONS ...
### VERSIONS ... Overview
Web: The Web edition is a low total-cost-of-ownership option for Web hosters and Web VAPs to provide scalability, affordability, and manageability capabilities for small to large-scale Web properties.Express: The Express edition is the entry-level, free database and is ideal for learning and building desktop and small server data-driven applications.Developer:  The Developer edition lets developers build any kind of application on top of SQL server.The Developer edition includes all the functionality of Enterprise edition, but is licensed for use as a development and test system, not as a production server.

## SQL INJECTION
## LINKED SERVERS
## PERFORMANCE
### PERFORMANCE Overview
The QUERY OPTIMIZER: generates multiple QUERY PLANS for a single query and determines the most efficient plan to run.

### An EXECUTION PLAN
An execution plan is a graphical or textual way of showing how the SQL server breaks down a query to get the required result.It helps a user to determine why queries are taking more time to execute and based on the investigation user can update their queries for the maximum result.Query Analyzer has an option, called Show Execution Plan (located on the Query drop-down menu).If this option is turned on, it will display a query execution plan in a separate window when the query is run again.


