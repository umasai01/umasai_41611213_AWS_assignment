def replicate_upper(string): #replicate .upper() and .lower() functions

    result = ''
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def replicate_lower(string):
    result = ''
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


text = "Hello World"
upper_text = replicate_upper(text)
lower_text = replicate_lower(text)
print('upper_text:',upper_text)  
print('lower_text:',lower_text) 



#Create a odd sequence from given sequence [1,2,34,65,1,2,65,66,44,33,22,87,123412,09,78,76]
sequence = [1, 2, 34, 65, 1, 2, 65, 66, 44, 33, 22, 87, 123412, 9, 78, 76]
odd_sequence = [num for num in sequence if num % 2 != 0]

print('odd_sequence:',odd_sequence)


#{‘apple’: 10, ‘mango’: 20, ‘pineapple’: 25, ‘orange’: 30, ‘strawberry’: 50, ‘jackfruit’: 10} Generate a comprehension fruits which has more than 20 

fruit_dict = {
    'apple': 10,
    'mango': 20,
    'pineapple': 25,
    'orange': 30,
    'strawberry': 50,
    'jackfruit': 10
}

fruits = {}

for fruit, quantity in fruit_dict.items():
    if quantity > 20:
        fruits[fruit] = quantity

print('fruits greaterthan 20:',fruits)
