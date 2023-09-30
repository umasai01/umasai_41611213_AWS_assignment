#Create a function to replicate built-in -sum()
def replication_sum(iterable):
    result = 0
    for item in iterable:
        result += item
    return result


numbers = [1, 2, 3, 4, 5]
result = replication_sum(numbers)
print('sum:',result)

#Create a function to replicate string attribute like, ljust(), rjust()
def ljust(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    return string + (fillchar * (width - len(string)))

def rjust(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    return (fillchar * (width - len(string))) + string

text = "hello umasai"
left_justified = ljust(text, 10, '-')
right_justified = rjust(text, 10, '*')
print('ljust:',left_justified)
print('rjust:',right_justified)


#Create a function to find, Palindrome, Fibo and Factorials:

# Palindrome
def is_palindrome(string):
    return string == string[::-1]

# Fibonacci
def fibonacci(n):
   fib_sequence = [0, 1]
   while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
   return fib_sequence[:n]

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print('palindrome or not:',is_palindrome("racecar"))
print('fibo:',fibonacci(10))
print('factorial:',factorial(5))


#Create a function to generate range of numbers
def range(start, stop, step=1):
    result = []
    current = start
    while current < stop if step > 0 else current > stop:
        result.append(current)
        current += step
    return result


numbers = range(1, 10, 2)
print('gen_range:',numbers)



