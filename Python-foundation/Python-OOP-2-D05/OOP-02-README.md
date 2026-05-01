# Python OOP-2 D05

## Screenshot

![Terminal Error Screenshot](../../Images/Screenshot%202026-04-29%20095435.png)

## Why `NameError: name 'calculate_grade' is not defined` Happens

This error occurs when you try to use or call a function, class, or variable before it has been defined in your code. 

In `ex-3.py`, the following line runs before the function's creation:

```python
print("Functions")

print(calculate_grade) # This causes the error!
```

Because Python executes code sequentially from top to bottom, at the moment `print(calculate_grade)` runs, the interpreter hasn't reached the `def calculate_grade(marks):` block yet. Therefore, Python doesn't know what `calculate_grade` means and throws a `NameError`.

## How to Fix It

You must define the function first, before you attempt to call, print, or use it in the code:

```python
print("Functions")

# 1. Define the function first
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# 2. Now you can safely use or print it
print(calculate_grade)
print(type(calculate_grade))
```

## Functions in Memory

![Function Output Screenshot](../../Images/Screenshot%202026-04-29%20100028.png)

### Understanding the Output

If you print the function name and its type after defining it, you will see output like this in the terminal:

```text
<function calculate_grade at 0x0000027278ED1440>
<class 'function'>
```

- **Functions are Objects:** In Python, functions are saved in the computer just like variables. They are first-class objects.
- **Memory Address:** The hex value (e.g., `0x0000027278ED1440`) is the memory address where the `calculate_grade` function is physically stored in your computer's RAM.
- **Function Type:** The output `<class 'function'>` shows that the type of `calculate_grade` is indeed a `function`.

## Calling the Function vs. Referencing It

![Calling Function Screenshot](../../Images/Screenshot%202026-04-29%20101954.png)

When you write `calculate_grade` (without parentheses), you are just referencing the function object stored in memory.

When you add parentheses, like `calculate_grade()`, you are instructing Python to **execute (call)** the function so it can process data. 

**The Core Concept of a Function:**
1. **Input:** You give it data (e.g., passing `(57)`).
2. **Process:** The function runs its internal code block (calculating the grade based on marks).
3. **Output:** The function returns a useful result (e.g., `"F"` or `"B"`).

## Missing Return Value: Why do we get `None`?

![Missing Return Screenshot](../../Images/Screenshot%202026-04-29%20112607.png)

In the `ex-4.py` code above, the output is:
```text
Hello Dasun
None
```

### Why did it output `None`?

If you look closely at the `print_name` function, it only has a `print()` statement, but it does **not** have a `return` keyword:

```python
def print_name(name="world"):
    print(f"Hello {name}")  # <--- This just shows text on the screen
```

**What happens to the answer?**
1. When you execute `return_value = print_name("Dasun")`, the function runs.
2. Inside the function, the `print()` statement displays `"Hello Dasun"` on the screen. 
3. But `print()` does not pass any data back. Since Python reaches the end of the function without seeing a `return` statement, it automatically gives back a default value called `None`.
4. Therefore, the variable `return_value` receives `None`, which is why `print(return_value)` outputs `None` on the next line.

**Summary:** 
`print()` merely shows data to the human user. `return` is what actually hands data back to the rest of your computer program. If you need to store the function's result in a variable, you **must** use `return`.

## ex-6 exercise: `AttributeError: type object 'Box' has no attribute 'length'`

![ex-6 Error Screenshot](../../Images/Screenshot%202026-04-30%20115125.png)

### Why this happens

In the provided `ex-6.py` script, Python encounters an error: `AttributeError: type object 'Box' has no attribute 'length'`.

This error occurs because the `length` property is defined outside of the `Box` class's indentation block. Because of the missing indentation, `length = 0` is treated as a standalone module-level variable rather than a property of the `Box` class. 

When you try to access `Box.length` (or `b1.length`), Python throws an `AttributeError` because the `Box` class only contains `width` and `height`.

### How to Fix It

To fix the issue, correct the indentation so that `length = 0` is properly grouped inside the `Box` class:

```python
class Box:
    width = 0
    height = 0
    length = 0  # <--- Indented correctly inside the class
```

### The Three Types of Functions/Methods

![ex-6 Multi Volume Screenshot](../../Images/Screenshot%202026-04-30%20120612.png)

When you define a function inside a class versus outside, and when you access it differently, Python treats them distinctly:

1. **`print(volume)` -> Global Function**:
   Since there is a `volume` function defined completely outside the `Box` class (at the top of your file), this prints out the global standalone function: `<function volume ...>`.

2. **`print(Box.volume)` -> Unbound Class Function**:
   When you access the `volume` function defined *inside* the `Box` class via the class name (`Box`), Python just sees it as a nested function belonging to the `Box` namespace: `<function Box.volume ...>`.

3. **`print(b1.volume)` -> Bound Method**:
   When you create a specific `Box` object instance (`b1 = Box()`) and access `b1.volume`, Python automatically "binds" that function to the specific instance. This converts it into a bound method, meaning any call to it will automatically pass the `b1` instance as its first argument (usually called `self`): `<bound method Box.volume of <__main__.Box object at ...>>`.

### Understanding `self` and Method Arguments

When defining a function inside a class (a method), it behaves differently from a regular function when called from an object. 

![Argument Count Error](../../Images/Screenshot%202026-04-30%20122250.png)

#### 1. Why `takes 3 positional arguments but 4 were given` happens
In the first screenshot, the error is:
`TypeError: Box.volume() takes 3 positional arguments but 4 were given`

When you call `b1.volume(b1.length, b1.width, b1.height)`, you explicitly pass **three** arguments. However, because `b1.volume` is a bound method, Python automatically inserts the object itself (`b1`) as the **first** hidden argument.
So, Python actually sends **four** arguments to the function: `(b1, b1.length, b1.width, b1.height)`.
Since your function signature `def volume(length, width, height):` was only built to receive three items, Python crashes.

![Unsupported Operand Error](../../Images/Screenshot%202026-04-30%20122407.png)

#### 2. Why `unsupported operand type(s) for *: 'Box' and 'int'` happens
In the second screenshot, you attempted to fix this by adding a fourth parameter (`last_one`):
`def volume(length, width, height, last_one):`

While this prevents the previous error by accepting four arguments, look at how the arguments line up when Python passes them:
1. `length` receives the object `b1` (e.g., `<__main__.Box object...>`)
2. `width` receives `b1.length` (20)
3. `height` receives `b1.width` (30)
4. `last_one` receives `b1.height` (10)

When the function then tries to execute `return length * width * height`, it's actually interpreting it as calculating `Box_Object * 20 * 30`. Multiplying a custom class object by an integer is invalid, causing the `Unsupported operand type(s)` error.

#### The Fix: The `self` Keyword
To correctly define a method inside a class (acting as a template), you **must** use the `self` keyword as the very first parameter. `self` serves as a dedicated placeholder to catch the object instance that Python automatically passes in.

```python
class Box:
    # ... attributes ...
    
    # Correctly adding 'self' catches the passed object, preventing errors!
    def volume(self, length, width, height):
        return length * width * height
```

#### What is `self` and Why is it a Variable?

1. **What does `self` mean?**
   `self` simply means "the current object." When `b1.volume()` runs, `self` becomes `b1`. If you had `b2.volume()`, `self` would become `b2`. It's Python's way of knowing *which* specific box is currently doing the calculation.

2. **What is `self` used for?**
   It allows a method to access the object's unique attributes and other methods from within the class. Instead of passing `b1.length` as an argument from the outside, you could simply write `self.length` inside the method to grab that specific box's length directly.

3. **Why is `self` just a variable?**
   Under the hood, `self` is nothing but a normal parameter (a local variable) in your method definition. Python has no special reserved keyword called `self`—it is just a strong naming convention used by all Python programmers. You could technically name it `this_box` or `me` (e.g., `def volume(me, length, width, height):`), and it would still work exactly the same way, catching the object instance as the first argument. However, sticking to `self` is highly recommended so other developers can easily read your code.

### Calling Methods from the Class vs the Object

![Calling from Class Error](../../Images/Screenshot%202026-04-30%20123338.png)

#### 1. Why `Box.volume() missing 1 required positional argument: 'height'` happens
In this example, you called the method using the class name itself: `Box.volume(b1.length, b1.width, b1.height)`.

When you call a method directly from the `Box` class (instead of from the `b1` object), Python **does not** automatically pass any object into the `self` parameter. It treats it as a completely standard, unbound function calling for four explicit arguments: `(self, length, width, height)`.
Because you only passed three numbers, Python matches them up like this:
1. `self` receives `b1.length` (20)
2. `length` receives `b1.width` (30)
3. `width` receives `b1.height` (10)
4. `height` receives **nothing**, causing the `missing 1 required positional argument` error!

![Calling from Class Fix](../../Images/Screenshot%202026-04-30%2045667.png)

#### 2. The Fix: Manually Passing the Object
To fix this while still calling the method from the class template (`Box.volume`), you have to explicitly provide the object yourself as the first argument:

```python
# Manually passing the b1 object into the 'self' parameter
b1_volume_3 = Box.volume(b1, b1.length, b1.width, b1.height)
```

This perfectly models what Python usually does for you behind the scenes. When you type `b1.volume(...)` normally, Python secretly translates it into exactly `Box.volume(b1, ...)`. Both approaches yield the exact same successful result, but calling it from the object directly is much cleaner and easier to read!

### Putting it all together: Utilizing `self` Inside the Method

![Using self inside method](../../Images/Screenshot%202026-04-30%20124004.png)

Now that you know `self` serves as a placeholder for your object (`b1`), you no longer need to pass the dimensions as separate parameters from the outside. You can update your method to handle it all internally!

```python
class Box:
    width = 0
    height = 0
    length = 0
    
    def volume(self):
        # self acts exactly like b1 does outside!
        return self.length * self.width * self.height
```

#### What is happening here?
1. **Empty Parameters:** The `volume` method now only takes `self`. It does not ask for `length`, `width`, or `height` inside the parentheses.
2. **Using the Attributes:** Because `self` is currently capturing the `b1` object, `self.length` exactly evaluates to `b1.length`. This allows the function to reach right back into the object itself and pull the required `10`, `20`, and `30` values to calculate the answer.
3. **Calling the Method:** You can now just call `b1.volume()`. Python automatically inserts `b1` into `self`, the method grabs the internal variables, calculates the math, and returns `6000` — perfectly clean Object-Oriented code! And, as shown previously, `Box.volume(b1)` does the exact same thing manually.

### Initializing Objects: The `__init__` Method

In the latest iteration of `ex-6.py`, you will notice a special method called `__init__`:

```python
class Box:
    width = 0
    height = 0
    length = 0

    # The constructor method
    def __init__(self, width, height, length):
        print("Box created", width, height, length)
        self.width = width
        self.height = height
        self.length = length
```

When you create a new box with `b1 = Box(30, 10, 20)`, Python automatically executes this `__init__` (initialization) method right away. 

#### How it works:
1. **Automatic Execution:** You do not need to call `b1.__init__()` manually. As soon as `Box()` is called, the `__init__` method runs.
2. **Accepting Arguments:** `Box(30, 10, 20)` passes those three numbers directly into the `__init__` method's `width`, `height`, and `length` parameters (with the `b1` object itself automatically passed into `self`, as usual).
3. **Setting Instance Attributes:** Notice the variables `self.width = width` inside the method. This takes the value handed to the function (`width`) and assigns it permanently to the object's personal attribute (`self.width`). 

This means that `b1` immediately starts its life with the correct dimensions assigned, resulting in cleaner code and fewer manual assignments!

### Common Error: "NameError: name 'X' is not defined" when instantiating

![NameError syntax issue](../../Images/Screenshot%202026-05-01%20082433.png)

#### Why it happens
If you accidentally write `b0. Box(10, 20, 30)` instead of `b0 = Box(10, 20, 30)`, Python interprets the `.` as an attempt to access an attribute or method of an object named `b0`. 

Because you haven't actually created the `b0` object yet (which is what the `=` assignment operator is supposed to do), Python looks for `b0` in memory, fails to find it, and throws a `NameError: name 'b0' is not defined`.

#### The Fix
Simply ensure you use the assignment operator `=` to assign the newly created `Box` object to the variable `b0`:

```python
# Incorrect: Uses a dot (.)
# b0. Box(10, 20, 30)

# Correct: Uses an equals sign (=)
b0 = Box(10, 20, 30)
```

## ex-7 exercise: Removing Class Attributes for Best Practices

### The Old Way vs The New Way

![ex-6 code with class attributes](../../Images/Screenshot%202026-05-01%20083514.png)

In `ex-6`, our `Box` class had class attributes (`width = 0`, `height = 0`, `length = 0`) defined right under the class declaration, and *then* we reassigned them inside the `__init__` method. While this works, it is technically redundant. 

![ex-7 code without class attributes](../../Images/Screenshot%202026-05-01%20083458.png)

In `ex-7`, we removed those initial class attributes completely! 

```python
class Box:
    # No more width = 0, height = 0, length = 0 here!

    def __init__(self, width=0, height=0, length=0):
        print("Box created", width, height, length)
        self.width = width
        self.height = height
        self.length = length
```

### Why is this a Best Practice?

1. **Don't Repeat Yourself (DRY):** Defining variables at the class level and then immediately overwriting them locally inside `__init__` means you are creating the variables twice. 
2. **Class vs Instance Attributes:** Variables declared directly under `class Box:` are **Class Attributes** (shared across all boxes). Variables created inside `__init__` using `self.*` are **Instance Attributes** (unique to each individual box). Since each box expects to have its own unique dimensions, they should exclusively be Instance Attributes. 
3. **Default Parameters:** Instead of relying on `0` class defaults, `ex-7` uses default parameters in the constructor (`def __init__(self, width=0, height=0, length=0):`). This safely achieves the same fallback behavior without cluttering the class namespace. If we do `b1 = Box(30, 10)`, `length` safely defaults to `0`.
