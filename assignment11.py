def range(start, stop, step=1):            #Create a Generator function to replicate range():
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step

print('Generator function:')
for i in range(1, 10, 2):
    print(i)

#Create a Recursive function to replicate range():
def range_recursive(start, stop, step=1):
    if start < stop if step > 0 else start > stop:
        yield start
        yield from range_recursive(start + step, stop, step)

print('Recursive function:')
for i in range_recursive(1, 10, 2):
    print(i)

#Create a Recursive and lambda function for Greatest Common Divisor (GCD):
gcd_recursive = lambda a, b: a if b == 0 else gcd_recursive(b, a % b)


result = gcd_recursive(48, 18)
print("GCD:", result)


#Create a module using an Editor/IDE:


def say_hello(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b
