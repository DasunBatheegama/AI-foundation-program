def get_min(a, b):
    if a< b:
        return a
    else:
        return b

print(get_min(10, 20))
result = get_min(10, 20)
print(result)

print(get_min(*[10, 20]))

def get_min(*numbers):
    print(type(numbers))
    if numbers[0] < numbers[1]:
        return numbers[0]
    else:
        return numbers[1]

print(get_min(10, 20, 30))
result = get_min(10, 20)
print(result)

print(get_min(*[10, 20]))