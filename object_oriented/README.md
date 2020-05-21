# Object Oriented Programming Examples Using Python3.8

## Key Concepts

### Classes

In object oriented programming a class is a template or blueprint for object construction. A class has methods\functions and variables, a class has a defined type and it can extend from other classes (inheritance).

### Objects

An object is a runtime instantiation of a class blueprint, it is `constructed` based on the definition of a class and is referred to by a pointer\reference.

### Polymorphism

The term `polymorphism` literally means to have many forms, this is applicable in object oriented programming because any object can be multiple different types.

### Inheritance

The term inheritance in object oriented programming is taken literally, it means that if there is an inheritance relationship between two objects a sub class will inherit the properties and methods of its parent. 

The inherited methods and properties can be restricted using access modifiers such as `private` or they can indicated to be private in python using `_` notation.

### Abstraction

Abstraction in object oriented programming is another term you can take literally, it means that some is abstract, it is not concrete. In the examples above we have declared a class `Mammal`, in real life nothing is ever just a `Mammal`, more so it is a specific type like `Human` and this is a sub class of `Mammal`.

It is therefore desirable to ensure or indicate that instances of such classes are not instantiated as they serve no real purpose except to provide functionality related to ***any*** class which might sub class it.

If a function is declared as `abstract` then you are indicating to anyone that might subclass the containing class that all child instances need to include this method but it is up to them how they decide to provide the concrete implementation for the function.

### Super, constructors and sub

These are terms you will encounter often in OO programming. The term `super` refers to a super class, i.e one that a given class extends from, `sub` refers to `subclasses`, that is classes further down the heirarchy. 

A `constructor` is a special kind of function that is called when a class is instantiated into an object. If your class is a sub class you will need to call the super class (this may be implicitly done for you) in a manner similar to this `super().__init__()`, via a call the the super classes constructor.

### Inheritance versus composition

A topic of debate, inheritance is often abused in programming languages and used simply to provide a mechanism for attaching functionality without duplicating code, and not specifically for defining a logical heirarchy of real objects.

Many technologists such as Joshua Bloch who wrote the very popular book `Effective Java` opt to prefer composition over inheritance unless there is a very clear need to use inheritance.

The difference between inheritance and composition is defined by examining the difference between a ***has-a*** versus an ***is-a*** relationship.

## Interesting points specific to Python

* Everything in Python is an `object` including primitives, this is in contrast to many other languages such as java which support the notion of `scalar types` which are primitive types such as `int`, `double`, `long` and `boolean`

* Python supports string interning which means that there is a pool of strings and as strings are immutable (cannot be changed) declaring a string `"Test"` and the declaring a string `"Test"` somewhere else in your code and comparing them for both equality and reference comparison

* Python is loosely typed so references are not bound to a particular type, this means that a pointer to a string can be re-pointed to an integer or any other runtime type

* Python doesnt allow you specify multiple class as being abstract like java does, so it is not possible to say Class A extends from Class B but both are abstract base classes
