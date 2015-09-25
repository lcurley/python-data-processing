__author__ = 'laurenbutlercurley'

# use 4 space indentation
# wrap lines so they aren't more than 79 characters
# use blank lines to separate blocks of code
# comment on separate lines if possible
# use spaces around operators, after commas
#       but not inside bracketing constructs


# assigning variables
x = 2
y = 3
z = x+y

#strings
print 'print string: Hello World'

#printing multiple lines - strings
>>> hello = "This is a long string\n\
... I'm using backslash-n-backslash\n\
...       to return to a new line\n\
... white space is important\n\
...       <-- see here,\n\
... great!"
>>> print hello

#strings with three quotes / r
>>> print """
... tripel quotes use: to print things
... and more things
... and a few more things
... ok now I'm done.
... """

secondhello = r"This is a long string beginning with an r"
print secondhello

#concatenate words and strings
word = 'Hello ' + 'Buddy'

'str' 'ing' #will be concatenated

#index strings
print word[4] #prints 4th letter
print word[:2] #prints first two letters
print word[2:] # prints all but first two letters
#can also index backwards
print word[-1] #prints first letter from the end
print word[:-2] #prints everything but the last two

# len() returns length of string
s = 'supercalifragilisticexpialidocious'
print len(s)
# 34

# lists
# slicing, replacing items, nesting
a = ['spam', 'eggs', 100, 1234]
print a
print a[0]
print a[-2]
print a[1:-1] # prints everything but first and last item
print 3*a[:3] + ['Boo!']

print a[:] #prints the whole list of items

# replacing or modifying elements
a[2] = a[2] +23 #add 23 to the designated item

a[0:2] = [1,12] # replaces first two items
a[0:2] = [] # empties the first two items

a[1:1] = ['bleh', 'xyz'] #adds items
a[:0] = a #insert copy of itself at beginning
a[:] = [] #clears the list

# Fibonacci series:
# sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print b,
    a, b = b, a+b

# prints 1, 1, 2, 3, 5, 8 in a column
# if you put a comma after [print b],
# the output is a row rather than a column

# printing results
i = 256*256
print 'The value of i is', i
# prints 65536

# if statements
x = int(raw_input("Please enter an integer: "))
if x<0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'One'
else:
    print 'More than one'

# for statements
# measure a string
words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

# prints each word and its length
# [for w in words] is used as a 'true' statement
# i.e. while 'true', do this

# range function
range (10)
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range (5,10)
# prints integers 5 to 10: [5, 6, 7, 8, 9]
range (-10, -100, -30)
# prints from -10 to -100 in 30 step intervals
# [-10, -40, -70]

# break and continue statements
for n in range (2,10):
    for x in range (2,n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding factor
        print n, 'is a prime number'

# prints:
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

for num in range(2,10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num

# prints:
# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9

# pass statements
# don't do anything: used for syntactic purposes

while True:
    pass


# defining functions
# write fibonacci series up to n
def fib(n):
    """Print a Fibonaaci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(2000)

# function that returns a list rather than printing

def fib2(n):
    """ Return a list containing Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib2(100)

# default argument values
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y','ye', 'yes'): # 'in' tests whether sequence contains something
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint


# This function can be called in several ways:
#
# giving only the mandatory argument: ask_ok('Do you really want to quit?')
# giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

#prints:
# [1]
# [1, 2]
# [1, 2, 3]

def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

    # accepts one required argument (voltage) and three optional (state, action, type)

parrot(1000)
parrot(189, 'blargh')
parrot(92374, 'monster', 'leap', 'hummingbird')

# lambda expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0) # prints 42
f(1) # prints 43 etc.

def my_lazy_function(): """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


# LIST FUNCTIONS:

# list.append(x)
#   add item x to end of list

# list.extend(L)
#   extend list by appending items in given list

# list.insert(i,x)
#   insert item at given position

# list.remove(x)
#   remove first item whose value is x
# list.pop([1])
#   remove item at given position

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25)
a.insert(2, -1)
a.append(333)
print a
a.index(333)
a.remove(333)
print a
a.sort()

# list.index(x)
#   return index in list of first item whose value is x

# list.count(x)
#   number of times x appears in list

# list.sort()
#   sort items of list, in place

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
stack.pop()
stack.pop()
print stack

# Built-in functions for lists
# filter()
# map()
# reduce()

# filter(function, sequence) returns a sequence
# of those items for which function(item) is true

def f(x): return x % 2 != 0 and x % 3 != 0

filter(f, range(2, 25))
# prints [5, 7, 11, 13, 17, 19, 23]
# factors not divisible by 2 or 3

# map(function, sequence) calls function(item) for each
# item in the sequence list and returns the values

def cube(x): return x*x*x

map(cube, range(1, 11))
# prints [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# cubed value of numbers 1 to 11

# reduce(function, sequence) returns a single value
# by calling function on the first two items, then on
# the result and the next tiem, and so on

seq = range(8)
def add(x, y): return x+y

map(add, seq, seq)
# prints [0, 2, 4, 6, 8, 10, 12, 14]

reduce(add, range(1, 11))
# prints 55

squares = []
for x in range(10):
    squares.append(x**2)

# the above code is equivalent to:

squares2 = [x**2 for x in range(10)]

# prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# combines the elements of two lists if they are not equal:
[(x,y) for x in [1,2,3] for y in [3, 1, 4] if x != y]

# above code is equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

# prints: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# list comprehensions with complex expressions and nested functions:
from math import pi
[str(round(pi,i)) for i in range(1,6)]

# prints: ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# transpose rows and columns in a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]
# prints: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# the above code is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

zip(*matrix)
# prints same thing: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

#del function
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
# removes -1
print a

# can also delete entire variables
del a

# playing with tuples

t = 1234, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5) # tuples can be nested
print u
# prints ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# cannot replace items in a tuple
# i.e. t[0] = 8888 returns an error

empty = ()
singleton = 'hello',         # trailing comma
len(empty)
# 0
len(singleton)
# 1
print singleton
#('hello',)

# sets
# an unordered collection with no duplicate elements
# curly braces or the set() function is used to create sets

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit  = set(basket)
# prints set(['orange', 'pear', 'apple', 'banana'])
'orange' in fruit
# True

a = set('abracadabra')
b = set('alacazam')

a                                  # unique letters in a
    # set(['a', 'r', 'b', 'c', 'd'])
a - b                              # letters in a but not in b
    # (['r', 'd', 'b'])
a | b                              # letters in either a or b
    # set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
a & b                              # letters in both a and b
    # set(['a', 'c'])
a ^ b                              # letters in a or b but not both
    # set(['r', 'd', 'b', 'm', 'z', 'l'])

a = {x for x in 'abracadabra' if x not in 'abc'}
# a
# set(['r', 'd'])

# dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel['jack']
# prints 4098
del tel['sape']
tel['irv'] = 4127
te.keys()
# prints ['guido', 'irv', 'jack']
'guido' in tel
# prints True

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# prints {'sape': 4139, 'jack': 4098, 'guido': 4127}

dict(sape=4139, guido=4127, jack=4098)
# prints {'sape': 4139, 'jack': 4098, 'guido': 4127}

# Looping techniques
for i, v in enumerate (['tic', 'tac', 'toe']):
    print i,v

# prints
# 0 tic
# 1 tac
# 2 toe

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

# prints
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

for i in reversed(xrange(1,10,2)):
    print i

# prints
# 9
# 7
# 5
# 3
# 1

# print sorted list without altering source
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

# prints
# apple
# banana
# orange
# pear

# change sequence in loop, first make a copy (looping does not make a copy)
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
     if len(w) > 6:
         words.insert(0, w)

# print words
# ['defenestrate', 'cat', 'window', 'defenestrate']

# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

dir()
# list of names currently defined

# import modules from a package
# import sound.effects.echo
# from sound.effects import echo

# formatting output
s = 'Hello World'
str(s) # 'Hello World'
repr(s) # " 'Hello World' "

x = 10 * 3.25
y = 200 * 300
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s
# The value of x is 32.5, and y is 60000...

# repr() of a string adds string quotes and backslashes

for x in range(1, 11):
     print repr(x).rjust(2), repr(x*x).rjust(3),
     # Note trailing comma on previous line
     print repr(x*x*x).rjust(4)

#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

print 'We are the {} who say "{}!"'.format('knights', 'Ni')
# We are the knights who say "Ni!"

print '{0} and {1}'.format('spam', 'eggs')
# spam and eggs
print '{1} and {0}'.format('spam', 'eggs')
# eggs and spam

import math
print 'The value of PI is approximately {0:.3f}.'.format(math.pi) # format to 3 decimals
# The value of PI is approximately 3.142.


# importing and reading fles
f = open('workfile', 'w')
print f
# <open file 'workfile', mode 'w' at 80a0960>

# w = writing, r = reading, a = appending

f.read()
# 'This is the entire file.\n'
f.read()
# ''
# end of the file returns ''

f.readline()
# 'This is the first line of the file.\n'
f.readline()
# 'Second line of the file\n'
# reads each line of the file

for line in f:
        print line,

# This is the first line of the file.
# Second line of the file

# write something that isn't a string
# needs to be converted toa  string first
value = ('the answer', 42)
s = str(value)
f.write(s)


