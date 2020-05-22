# Common Design Patterns

This repository contains some of the common design patterns that are used in software development, the examples are all written in python 3.

## Why should we use design patterns

A design pattern is a repeatable solution to a common problem encountered during software development and use of them can help to prevent subtle issues that can cause problems as development progresses.

Design patterns help to promote loosely coupled code and provide a well known and well understood answer to a common problem, they help you to adhere to some of the common programming principles such as **SOLID**, **DRY** and **KISS** and hopefully they discourage you from creating your own ***anti-patterns***. 

Similar common acronyms  for principles include **WET** or **Write everything twice** and **DIE** or **Duplication is evil**.

Instead of creating your own solution to a common problem it is better to apply an existing and well understood solution that is easily testable and will be understood by other developers long after you have left the project.

Generally design patterns are broken down into three main categories, behavioural, creational and structural patterns.

### Behavioural

* Command Pattern - Encapsulate a command as an object
* Observer Pattern - Notify other objects of changes in state
* Strategy Pattern - Encapsulate an algorithm as an object

### Creational

* Builder Pattern - Build complex objects by separating object construction from the implementation and provide a fluent interface
* Factory Pattern - Create an instance of several derived classes
* Singleton Pattern - Ensure that only one instance of a class can exist

### Structural

* Adapter Pattern - Match conflicting interfaces
* Decorator Pattern - Add additional functionality to objects without changing their interface or implementation
* Facade Pattern - Hide complexity behind a simplified interface
* Proxy Pattern - Masquerade an object as another, hiding the original object

## When are these patterns useful

## Adapter Pattern

The adapter pattern is useful when:

* You want to provide decoupling of objects
* You have an existing object which fulfills your needs and it is incompatible with an existing API and do not want to make code changes to the API
* You have an existing object and you want to pass it to a third party API you have no control over

## Builder Pattern

The builder pattern is useful when:

* You need to build complex objects but you dont want to pass all arguments into a large constructor
* You want to decouple the building of objects and add additional functionality over time without changes to the objects constructor
* You want to have more flexible control over the way objects are built and dont or cant use multiple constructors

## Command Pattern

The command pattern defines ***what*** needs to done and is useful when:

* A history of commands is needed (undo functionality for example)
* You need callback functionality
* You want to send a command to a remote function to be executed
* Requests need to be handled at variant times or in variant orders
* The invoker should be decoupled from the object handling the invocation.

## Decorator Pattern

Decorators are supported out of the box when using python, and python also supports passing functions as arguments to another function.

The decorator pattern is useful when:

* You want to add additional functionality to an existing object without changing it (Open Closed Principle)
* You do not want to sub class but still need to extend an object
* You want to dynamically modify an objects properties and functionality

## Facade Pattern

The facade pattern is useful when:

* You want to hide complexity from a caller
* You want to wrap functionality into single method without changing the original code
* You want to hide functionality from callers behind a simple interface

## Factory Pattern

## Observer Pattern

The observer pattern is useful when:

* You are programming GUI's (swing, android etc) and you need a listener to call back when state changes (e.g register a callback with a button component)
* You need an event listener for any other reason

## Proxy Pattern

## Strategy Pattern

The strategy pattern defines ***how*** something should be done is useful when:

* You want to create algorithms as objects and use them at runtime via a generic method that simply runs the algorithm
* A good example would be a preference setting for how to save something
* A sorting algorithm
