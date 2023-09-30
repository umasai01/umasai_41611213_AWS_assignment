#Write a program to find the power of a given number:
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = 2
exponent = 3

result = power(base, exponent)
print(f"{base} to the power of {exponent} is {result}")



#Explain left/right shift with examples
num = 5
shifted_num = num << 2 
print('left_shift:',shifted_num)  
num = 20
shifted_num = num >> 2 
print('right_shift:',shifted_num)  

#How & bitwise operator works
a = 5   
b = 3   

result_1 = a & b
print('& bitwise :',result_1)

#How and operator, & operator defers each other
#and operator- it is logical operator
x = True
y = False
result_2 = x and y
print('and operator:',result_2) 
# & operator-it is a bitwise operator
a = 5   
b = 3   

result_3 = a & b
print('& bitwise :',result_3)