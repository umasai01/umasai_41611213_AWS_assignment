import assignment12

# Palindrome 
word1 = "racecar"
word2 = "hello"

if assignment12.is_palindrome(word1):
    print(f"'{word1}' is a palindrome.")
else:
    print(f"'{word1}' is not a palindrome.")

if assignment12.is_palindrome(word2):
    print(f"'{word2}' is a palindrome.")
else:
    print(f"'{word2}' is not a palindrome.")

# Fibonacci Sequence
n1 = 10
n2 = 5

fib_sequence1 = assignment12.fibonacci(n1)
print(f"The first {n1} Fibonacci numbers are: {fib_sequence1}")

fib_sequence2 = assignment12.fibonacci(n2)
print(f"The first {n2} Fibonacci numbers are: {fib_sequence2}")

# factorial
num1 = 5
num2 = 0

fact1 = assignment12.factorial(num1)
print(f"The factorial of {num1} is: {fact1}")

fact2 = assignment12.factorial(num2)
print(f"The factorial of {num2} is: {fact2}")





























