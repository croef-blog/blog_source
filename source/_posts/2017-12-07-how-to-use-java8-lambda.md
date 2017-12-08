---
title:  Java8 Lambda 速记手册
tags:
- java8
- lambda
date: 2017-12-07 22:12:22
---
## 作为参数使用

### `Function<T, R>` T作为输入，返回的R作为输出
``` java
Function<String, String> function = (x) -> {
  System.out.print(x+": ");
  return "Function";
};

String result = function.apply("hello world");
```
  

### `Predicate<T>` T作为输入，返回的boolean值作为输出
``` java
Predicate<String> pre = (x) ->{
  System.out.print(x);
  return false;
};


boolean result = pre.test("hello World");
```
 

### `Consumer<T>` T作为输入，执行某种动作但没有返回值
``` java
Consumer<String> consumer = (x) -> {System.out.println(x);};

consumer.accept("hello world");
```
 

### `Supplier<T>` 没有任何输入，返回T
``` java
Supplier<String> supp = () -> {return "Supplier";};

String result = supp.get();
```
 

### `BinaryOperator<T>` 两个T作为输入，返回一个T作为输出，对于“reduce”操作很有用
``` java
BinaryOperator<String> bina = (x, y) ->{
  return x + " " + y;	
};

String result = bina.apply("hello", "world");
```