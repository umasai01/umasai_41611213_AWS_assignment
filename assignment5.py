#Write Examples code for concatenation

str1 = "Hello, "
str2 = "world!"
result_1 = str1 + str2
print('str_concatenation:',result_1)  

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_2 = list1 + list2
print('list_concatenation:',result_2)  


#Write one Examples for each formatting techniques
# String formatting with %
name = "vazeed"
age = 30
formatted_str_1 = "My name is %s, and I am %d years old." % (name, age)
print('String formatting with %:',formatted_str_1)

# Using f-strings 
name = "Basheer"
age = 25
formatted_str_2 = f"My name is {name}, and I am {age} years old."
print(' Using f-strings:',formatted_str_2)

# Using .format() method
name = "siva"
age = 35
formatted_str_3 = "My name is {}, and I am {} years old.".format(name, age)
print('Using .format() method:',formatted_str_3)


#Write example for each arithmetic operators

a = 10
b = 5

# Addition
addition = a + b
print("Addition_operator:", addition)

# Subtraction
subtraction = a - b
print("Subtraction_operator:", subtraction)

# Multiplication
multiplication = a * b
print("Multiplication_operator:", multiplication)

# Division
division = a / b
print("Division_operator:", division)

# Modulus 
modulus = a % b
print("Modulus_operator:", modulus)

#Write Example for assignment operators (except: = & +=)

# Example of -= 
x = 10
x -= 5  
print("Subtraction :", x)

# Example of *= 
y = 8
y *= 3  
print("Multiplication :", y)

# Example of /= 
z = 15
z /= 2 
print("Division :", z)

# Example of %=
w = 17
w %= 4  
print("Modulus:", w)
