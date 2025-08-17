# Comparison Operators
# Equal:		==
# Not Equal:		!=
# Greater than:		>
# Less Than:		<
# Greater or equal:	>=
# Less or equal:	<=
# Object Identity:	is (use id()

## Logical Operators
# and
# or
# not

'''
user = 'admin'
logged_in = True
if not logged_in:
	print('Please Log In')
else:
	print("Welcome")
a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a==b)
print(a is b)
'''

## False Values;
# False
condition = False

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# None (Works also as false)
statement = None
if statement:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# Zero of any numeric type (0)
condition = 0
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')
# Any empty sequence. For example , '', (), []
condition = ''
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# Any empty mapping. For example, {}
condition = {}
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

