# Ordered sequence of items or elements but cant be changed once declared(immutable)
# Can be sliced, indexed.
scores = ()
'''
print(scores, type(scores))
a  = (1)
print(a, type(a))
b = (1,)
print(b, type(b))
c = 1,
print(c, type(c))
'''
# Manipulation of data
noise_makers1 = ('Dorcas', 'Bethel', 'Yusuf')
print(noise_makers1[0])
#noise_makers1[0] = 'TK' this can never work because tuples are immutable
#print(noise_makers1)

#1. To change data in tuples as it is immutable, change it to list using typecasting then revert back to tuples
noise_makers1 = list(noise_makers1)
print(noise_makers1, type(noise_makers1))

#2. Effect change now
noise_makers1[0] = 'TK'
noise_makers1 = tuple(noise_makers1)
print(noise_makers1, type(noise_makers1))

# Unpacking tuples
a,b,c = noise_makers1
print(a)
print(b)
print(c)
# use asterisks to pass extra to othr ones
##kingpin, others = noise_makers1 #Will throw a ValueError too many values to unpack 
kingpin, *others = noise_makers1
print(kingpin, type(kingpin))
print(others, type(others)) # Output of unpacking using * sends data types as list

*kingpin, others = noise_makers1
print(kingpin)
print(others)
