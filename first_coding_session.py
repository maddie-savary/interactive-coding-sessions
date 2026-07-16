print("Hello World") # in our python file (also called Pythin script).
print("Hello friends") #final way of running Python code: run a script in full.

# What are the big variable types in Python?
this_string = "Quentin" # This is a string. 
# I assigned the value "Quentin" to the variable this_string
#this operation does not return anything

this_float = 3.14 # this is a float
this_int = 12 #this is an int
this_bool = False #note the case-sensitive

#What can you do with variables?
# only after the line is executed do the variables exist in Python's memory
print(this_float) # tab to autocomplete the current selection
print(this_string) 

#what else can you print?
print(this_string) #you can print a varibale
print("Hello")
print(12) # you are not storing it into a variable, you are directly printing an input
print(12 + 5) #printing an expression
# SKILL: Being able to 'trace the code'. Meaning reconstruct the steps of a code 
# another example of an expression: 
print(this_float + 5) # here we can again trace the steps

#what is print()?
# print() is a gunction. a function is a way of doing somnething in Python
# functions are 'called' using ()
# functionsd take a number of arguyments (what goes inside the parentheses)
# some functions take zero, some take many.

# How many arguments does print() take?
# it can take one
print(this_float)
# ... but it can take more
print(this_float, this_int, this_string)
# print is printing all of its arguments on the same line. 

# lets do some calculations
print(2 + 3)
print(2*5)
print(2 + 3 * 5)
print( (2+3) * 5) # PEMDAS

print(0.1 + 0.2)

print((0.1 + 0.2) == 0.3)
# floating point error. operations with decimal numbers are, but default, not mathematically 
# 'exact'

# How can we avoid this?
# one way is to round:
my_rounded_sum = round(0.1 + 0.2, 1)
print(my_rounded_sum)
print(my_rounded_sum == 0.3) # this is now true 

# more logical comparisons
print(1 < 2)
print(1>2)
print (1>=2)
print(1<=2)
print(1 != 2)

# You can also create more complex comparisons
print((1 < 2) and (3 > 2))
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) # both true, so true
print(condition_1 and condition_3) # false, so true and false
# AND requires all conditions to be true 
# what about OR?
print(condition_1 or condition_2)
print(condition_1 or condition_3) #true, why?
# at least one of them is true
# OR requires at least one condiiton to be true 
# very important!

print(False + False) # ???
print(False + True)
print(True + True) # now this is very weird
print(True == 1)
print(False == 0)

print(False * 5)
print(True * 3+1) # simple stand ins for 0 and 1

# lets continue the weirdness
greeting = "Hello " + "world!"
print(greeting) # this meaning of '+' changes when you apply it to 
# a string
# +, when applied to strings means concatenation: bringing them
# #into a single string

laugh = "ha" * 3 
print(laugh) # here, * means repeat when applied to a string

weird_laugh = "ha" * 3.14 # does not work

my_age = 39 
my_intro = "I'm Quentin and I'm " + my_age # does not work 
# retunrs a TypeError.
# when you want types to work nicely with each other, you
# will need to convert them first

#lets see type conversions
my_age_as_a_string = "39"
my_intro = "I'm Quentin and I'm " + my_age_as_a_string 
print(my_intro)

# a better way to do that is to convert one type to the other
# using four nifty functions: str(), int(), float(), bool()

# how do we use them:
print(str(42))
# is this really a stirng?
type(str(42))
#let's try others
str(3.14)
str(False)
str(0.1 + 0.2)
# we can convert pretty much anything to a string: int, bool, float

# lets try float:
float('Hello')
float('32')
float(False)
float(40)
float('fifteen')
# for float, its sometimes going to work, sometimes not.

# int?
int('Hello')
int(True)
int('32')
int(3.14) # is it rounding or cutting off the decimal part
int(3.9) # option 2, not rounding
round(3.9) # given us 4, not 3
# ANOTHER GREAT SKILL: running experiments on your code 
