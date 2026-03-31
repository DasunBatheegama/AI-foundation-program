# Python OOP D04

## Screenshot

![Terminal Error Screenshot](../../Images/Screenshot%202026-03-31%20073700.png)

## Why `KeyError: 0` Happens

`KeyError: 0` happens because the dictionary does not have a key named `0` at the moment you try to read it.

If you run this line before creating key `0`, Python raises an error:

```python
print(eng_sinhala_dic[0])
```

## How to Fix It

Create key `0` first, then read it:

```python
eng_sinhala_dic[0] = "Test"
print(eng_sinhala_dic[0])
```

Now the output is:

```text
Test
```

## Extra Notes

- A hashable object has a hash value that does not change during its lifetime.
- Dictionary keys must be hashable.
- Mutable objects are usually not hashable.
- Immutable objects are usually hashable.
- A list is mutable, so it is not hashable.
- A tuple can be hashable, but only if all items inside the tuple are hashable.
- In collections:
	- Set elements are unique.
	- Dictionary keys are unique.
	- Lists and tuples allow duplicate values.

## Ex-2 Theory Notes

Programming languages are used to give instructions to a computer: we provide input, and the computer gives output.

Example idea:
- A user has data.
- The program processes that data (like a calculator).
- The user gets useful output.

Data flow in many scenarios:

`Data -> Organized Data -> Information -> Analysis -> Knowledge`

Programming helps organize data and solve problems using different structures and methods.

There are two main programming paradigm ideas:

1. Imperative programming paradigm:
   - We think step by step and tell the computer exactly how to do the task.
2. Declarative programming paradigm:
   - We describe what result we want, not the full step-by-step process.
   - Example: SQL, CSS.

Imperative programming includes three common styles:

1. Procedural programming
2. Structured programming
3. Object-oriented programming

## Ex-3 OOP Theory Notes

In object-oriented programming (OOP), a class is a template (blueprint) used to create objects.

- A class defines the structure and behavior.
- An object is a copy (instance) created from that class template.
- Example idea: `Student` is a class, and `st1 = Student()` creates an object from it.

### Explanation of `st1 = Student()`

- `Student()` creates a new object from the `Student` class template.
- That object is stored in memory (RAM).
- `st1` is the variable that refers to that object.

### Explanation of `st1.name = "john Doe"`

- The dot (`.`) operator is used to access data inside an object.
- `st1.name` means "look for the `name` member in object `st1`."
- If `name` does not exist yet, Python creates it when this assignment runs.
- `name` is called an attribute (an object variable/property).

### Ex-3 Error Screenshot (`AttributeError`)

![Ex-3 AttributeError Screenshot](../../Images/Screenshot%202026-03-31%20095341.png)

### Why This Error Happened (Earlier)

Error shown:

```text
AttributeError: 'Student' object has no attribute 'name'
```

This happens because:

- You created `st2 = Student()`.
- But you did not set `st2.name` before printing it.
- So when Python runs `print(st2.name)`, it cannot find the `name` attribute in `st2`.

### How It Is Fixed Now

Current code in Ex-3 uses a default class attribute:

```python
class Student:
	name = "DEFAULT"
```

Because `name` already exists in the class, every object (including `st2`) can read `name`.
So `print(st2.name)` now prints `DEFAULT` instead of raising `AttributeError`.

### Other Valid Fix Methods

Set the attribute before using it:

```python
st2 = Student()
st2.name = "Jane Doe"
print(st2.name)
```

Or define `name` for every object inside `__init__`:

```python
class Student:
	def __init__(self):
		self.name = ""
```

## Ex-4 Exercise (Function Arguments)

### Ex-4 Error Screenshot (`TypeError`)

![Ex-4 TypeError Screenshot](../../Images/Screenshot%202026-03-31%20105303.png)

### Why This Error Happens

Error shown:

```text
TypeError: print_name() missing 1 required positional argument: 'name'
```

This happens because:

- The function is defined as `def print_name(name):`
- So Python expects one required argument (`name`) when calling the function.
- But the call is `print_name()` with no value, so Python raises `TypeError`.

### How It Is Fixed Now

You fixed the error by passing an argument when calling the function:

```python
def print_name(name):
	print("Hello World", name)

print("First ")
print_name("AI")
```

Now Python receives the required `name` argument, so no `TypeError` is raised.

### Latest Update: Fixed with a Default Value

You also fixed Ex-4 by assigning a default value in the function parameter:

```python
def print_name(name="AB"):
	print("Hello World", name)

print_name("AI")
print_name()
```

Why this works:

- `name="AB"` makes the parameter optional.
- If you pass a value, Python uses that value (`"AI"`).
- If you do not pass a value, Python uses the default (`"AB"`).

### Ex-4 New Error Screenshot (`SyntaxError`)

![Ex-4 SyntaxError Screenshot](../../Images/Screenshot%202026-03-31%20110607.png)

### Why This New Error Happens

Error shown:

```text
SyntaxError: parameter without a default follows parameter with a default
```

This happens because this function definition is invalid:

```python
def print_name(name="AB", age):
```

In Python, once you start giving default values in parameters, all parameters after that must also have defaults.

### How You Fixed It Now

You fixed the syntax error by putting the required parameter first and the default parameter second:

```python
def print_name(age, name="AB"):
	print("Hello World", name, age)

print_name("AI")
print_name(12)
```

Why this works:

- `age` is required and comes first.
- `name="AB"` is optional and comes after required parameters.
- This follows Python function parameter rules, so no `SyntaxError` appears.

## Theory Note (Argument Mapping in Python)

About this function:

```python
def print_name(age, name="AB"):
	print("Hello World", name, age)
```

When you call:

```python
print_name("AI")
```

Python maps positional arguments from left to right:

- First value (`"AI"`) goes to `age`.
- `name` is not passed, so it uses the default value `"AB"`.

So output becomes `Hello World AB AI`.

Important theory:

- This is not automatic assignment by data type.
- Python is dynamically typed, so a parameter can hold different types unless you add your own type checks.
- By default, function arguments are matched by position or by keyword name, not by type.

### Keyword Argument Call

You updated the function and call like this:

```python
def print_name(age=10, name="AB"):
	print("Hello World", name, age)

print_name(name="AI")
print_name(12)
```

Why this works:

- `print_name(name="AI")` uses a keyword argument, so Python directly sets `name` to `"AI"`.
- `age` is not passed in that call, so it uses the default value `10`.
- `print_name(12)` uses positional passing, so `12` goes to `age`, and `name` stays default `"AB"`.

### Ex-4 New Error Screenshot (`TypeError`: unexpected keyword)

![Ex-4 Unexpected Keyword Error Screenshot](../../Images/Screenshot%202026-03-31%20112841.png)

### Why This Error Happens

Error shown:

```text
TypeError: print_name() got an unexpected keyword argument 'name'
```

This happened because `print_name` was redefined later in the file:

```python
def print_name(age):
	print("Hello World", age)
```

After this second definition, Python uses the new function version only. That version accepts only `age`, not `name`, so `print_name(name="AI")` fails.

## Ex-5 Exercise (Functions, `*args`, and Redefinition)

### What You Did in Ex-5

You wrote this first function:

```python
def get_min(a, b):
	if a < b:
		return a
	else:
		return b
```

Then you called it in multiple ways:

- Normal call: `get_min(10, 20)`
- Store return value in variable: `result = get_min(10, 20)`
- List unpacking call: `get_min(*[10, 20])`

### Second Version Using `*numbers`

You redefined the same function name:

```python
def get_min(*numbers):
	print(type(numbers))
	if numbers[0] < numbers[1]:
		return numbers[0]
	else:
		return numbers[1]
```

In this version:

- `*numbers` collects arguments into a tuple.
- `type(numbers)` prints `<class 'tuple'>`.
- You compared the first two values (`numbers[0]` and `numbers[1]`).
- `get_min(10, 20, 30)` is accepted, but this code still checks only first two numbers.

### Important Theory

- In Python, if you define a function again with the same name, the latest definition replaces the old one.
- `*args` (like `*numbers`) means "accept many positional arguments" as a tuple.
- Using `*` in a function call (like `*[10, 20]`) unpacks list items into separate positional arguments.

## Final OOP Theory Notes (Attributes and Behaviors)

- In OOP, objects have two main parts:
  - Attributes (data/state), for example: `name`, `age`, `color`
  - Behaviors (actions/methods), for example: `move()`, `eat()`, `print_info()`
- Attributes help behaviors because methods use object data to do actions.

Example idea:

```python
class Student:
	def __init__(self, name):
		self.name = name

	def move(self):
		print(self.name, "is moving")
```

- `def` is the keyword used to define a function or method in Python.
- A basic function format is:

```python
def function_name():
	# code block instructions
	print("Hello")
```

- `print()` is an action statement that shows output on the screen.

### Additional Attribute Notes

- An object has attributes as variables (data fields).
- Attributes usually store each object's own values (unique state per object).
- Attribute values can be changed after object creation.

### Connection Between Behaviors and Functions

- In OOP, behavior means what an object can do (actions).
- Functions are reusable code blocks.
- When a function is written inside a class, it is called a method.
- Methods are used to implement object behaviors.
- So, behaviors are the concept, and methods (functions in a class) are the implementation.




