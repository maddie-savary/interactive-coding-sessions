# Let's first re-create a variable or two
my_integer = 10 
my_str = "Hello world"
# i told you before that you can always see the type of variab le using type()
type(my_integer)
type (my_str)

# what is stored inside these objects?
my_str.upper # upper is a METHOD that is attached to all the objects of class string
# a method is like a function, so it needs tot be CALLED. How do we call a function?
# we put () after it
my_str.upper() # retunring the upper, capitalized verison of the string 
my_str.upper() # what does it mean return a copy?
# it means the original stirng is unchanged :
my_str
# let's try another one:
my_str.lower()
#what else is in there
my_str.endswith('!') # does not end with a !
my_str.endswith('orld') # returns true
# methods are a way of pairing functions to specific types of objects

# some objects have other things than methods: properties. 
#properties are information about the objects that was created. 
my_integer.denominator # white wrenches are properities of the object
my_integer.numerator # do we put parentheses? no
# properties are only meant to be read. they don't do anything. they just exist
#if something doe snot requre any calculoation to be given to you, 
# and does not do anyhthing, it is probably a property
# but to be sure: look at the icon. 
