# We hav eseen many functions already:
print('Hello world')
print(len('Hello'))
print(abs(-7))
print(str(3.14))
print(int('294'))
# What we're going to do is dissect what functions are doing, and what they are. 
# a function is like a machine. It typically takes inputs (between 0 and many), 
# it is running comands, doing things. And most often it RETURNS something to the user.

# You can think of most functions as a conveyor belt. 

# If I use the len function():
my_str = 'Hello world'
len_of_my_str = len(my_str) # Takes a single argument, here a string
# Returns to the user the length of that string. 
print(len_of_my_str)
# A function that returns something is useful, because it goves you something back
# that you can store into a variable and reuse for other purposes later.

# Not all functions are like that! Not all fucntions are conveyor belts.
# Other are more like engines. They take inputs (gas, and oxygen), they do things;
# but they do not return anything to the user.

print('Hello world') # Everytime I run this, it is going to print to the REPL.
what_is_this = print('Hello world') # Execute the function print('hello world') and
# store whatever it returns into the what_is_this variable. 
what_is_this # That's odd, it does not show anything
print(what_is_this)
# There is nothing in what is this. 

print(2+3) # If I run this, I will see: 5
my_result = print(2+3)
print(my_result) # Contains none, again, print does not reutrn anything. 

# One last thing we need to know about functions before we practice 
# writing them:

#Functions take arguments. We can supp;ky the arguments to functions
#in two different ways
#1. By postiion
print(round(3.14,2)) # the first argument is the number to be rounded
# THe second is the number of digits after the decimal you want.
# The order matters:
print(round(1, 3.14)) # An error.  
# The second way is to include what are called name arguments. 
# Do you remember the print function?
print('A', 'B', 'C', 'D') # you gave give it many arguments in sequence
# and it will print them all 
# The print function also takes 'secret' arguments that have degault   
#values. Meaning when you do not specify them, they already have 
# a default value:
print('A', 'B', 'C', 'D', sep='*')
#Another one:
print('A','B','C','D', sep='*', end='!')
# Named arguments must always come last. 
#Otherwise you get an errror. 

# one final thing: you can use names to elimanate all
# ambiguity about positional arguments:
round(number=3.14, ndigits=1)
# This is the same thing as round(3.14,1)
# to know the name of the arguments, use the () in VSCode.

# Let's practice writing our own functions now. 
# We write functions when we want to have a list of actions
# that we can easily reuse in different places. 

# Create a function that can calculate a price increase 
# when given a rate: 

# We say that we DEFINE a function: 
def show_price_increase(base_price, rate_increase):
    # The body of your function is what will happen 
    # everytime the function is called
    new_price = base_price * (1 + rate_increase)
    print(new_price)
    #We are now done, we press Shift + Enter to define it.

# now the function exists, we can call it!
show_price_increase(10,.1)
show_price_increase(30, .2)
# What kind of function did we create here?
#A conveyor belt or an engine? 
# an engine! the function is not RETURNING anything.
new_price = show_price_increase(10,.2)
print(new_price) 

#How can we modify our function to return a value
#that we can reuse instead?

def calculate_price_increase(base_price, rate_increase):
    # The body of your function is what will happen 
    # everytime the function is called
    new_price = base_price * (1 + rate_increase)
    return new_price # This is what you hand back to the user. 

my_new_price = calculate_price_increase(5,.25)
print(my_new_price) # This time we got something back, that we could 
# store into a variable. 
# Whatever happens inside a funciton is LOST after the function is done
# running. So if you want to get it back, ask the function to return it. 

#One final thing with functions. 

def show_total(price, quantity):
    print("Starting to calculate the price...")
    total = price*quantity
    return total # Engine or conveyor belt? Return, so conveyor belt!
    #After return, my job here is done.
    print("Finished calculating the price") # Any line after a return will never
    #be executed. 

total = show_total(.99,10)