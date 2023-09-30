def is_palindrome(word):
    word = word.lower().replace(" ", "")  
    return word == word[::-1]

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:n]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
