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

* Adapter - Match conflicting interfaces
* Decorator - Add additional functionality to objects without changing their interface or implementation
* Facade Pattern - Hide complexity behind a simplified interface
* Proxy Pattern - Masquerade an object as another, hiding the original object
