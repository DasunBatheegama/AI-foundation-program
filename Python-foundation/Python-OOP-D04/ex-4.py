def print_name(age=10, name="AB"):
    print("Hello World", name, age)


print(print_name)

def print_name(age):
    print("Hello World", age)

print(print_name)    

print_name(name="AI")
print_name(12)