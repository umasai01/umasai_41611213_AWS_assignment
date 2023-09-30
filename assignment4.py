#Create various data types and experiment its attribute
#1) Name = “some name” Convert above string into, upper, lower and capitalize Replace ‘e’ with ‘E’ using attribute

name = "some name"
upper_name = name.upper()
print("Uppercase:", upper_name)
lower_name = name.lower()
print("Lowercase:", lower_name)
capitalized_name = name.capitalize()
print("Capitalized:", capitalized_name)
replaced_name = name.replace('e', 'E')
print("Replaced:", replaced_name)

#2) L = [1,2,3] Extend above list by using [5,6,7] and remove 5th value

L = [1, 2, 3]
L.extend([5, 6, 7])
del L[4]
print("Extended List:", L)

#3) d = {‘mango’: 10, ‘banana’: 0, ‘apple’: 15, ‘orange’: 0, ‘pineapple’: 20} Remove out of stock fruits from above dictionary

d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

out_of_stock = [fruit for fruit, quantity in d.items() if quantity == 0]
for fruit in out_of_stock:
    del d[fruit]
#update mango and pineapple
d['mango'] = 15
d['pineapple'] -= 5

print("Updated Dictionary:", d)





