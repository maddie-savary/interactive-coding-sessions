# Advanced topics in loops!

# Let's start with the concept of iterables. 
# We have seen that we can loop over lists with for loops:

for i in [1, 2, 3, 4]:
    print(i)

# We can loop with for over ANYTHING that is iterable: 
# Like a string!

for l in "Hello world": 
    print(l) # We get the characters one at a time!

# In fact, you already knew that strings are iterable: 
my_name = "Quentin"
my_name[0:4]

# What else can we iterate on? 
my_info = {"name": "Quentin",
           "age": 39,
           "city": "Boulder"}

for k in my_info:
    print(k) # going to get the keys! 

# Iterating over a dict returns the keys. 
# How can we get the value then? 

for key in my_info:
    value = my_info[key]
    print(f"The current key is {key}, and its associated value is {value}.") # How can we also get the value?

# It would be better if we could get both the key and the value
# when iterating over a dictionary. Right?
# Turns out there is a way!

# ... But first a small detour:
my_fruits = ["banana", "apple", "mango"] 
first_fruit, second_fruit, third_fruit = ["banana", "apple", "mango"]
name, age, city = "Quentin", 39, "Boulder" 
# UNPACKING.
print(first_fruit)

# Let's return to our dictionary: 

for (key, value) in my_info.items(): 
     print(f"The key is {key}, and associated value {value}")

# Let's revisit the example of looping on my name:
my_name = "Quentin"
for letter in my_name:
    print(letter)

# I would like to know the index of each letter in my name. 
# What is the position of each letter in my name?

# Whenever you face that, you have a great tool: enumerate()
# How does it work:
for (index, letter) in enumerate(my_name): 
    print(f"The letter at position {index} is {letter}")

# The only thing that you need to do is:
# replace ITERABLE by enumerate(ITERABLE)
# replace step_variable by (index, step_variable)
# You can again use any varaible name that you like, 
# but the first one will receive the idx, the second the element itself. 

a_list_of_food = ["pickle", "pepper", "peach"]
a_list_of_tastes = ["sour", "spicy", "sweet"]

# You can iterate over two lists (or multiple lists really in parallel). 
# All you have to do first is zip them. 
for (food, taste) in zip(a_list_of_food, a_list_of_tastes):
    print(f"A {food} tastes {taste}.")

# What if we also had the color of the foods?
a_list_of_colors = ["green", "red", "orange"]

for (food, taste, color) in zip(a_list_of_food, a_list_of_tastes, a_list_of_colors):
    print(f"A {food} is {color} and tastes {taste}.")