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
