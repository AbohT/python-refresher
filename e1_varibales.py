'''
# Variables are memory locations that staore data
num = 1
print(num)

# To check memory location of variables use id() with the variable name inside brackets
print(id(num))

#Biodata
firstname = "ThankGod"
lastname = "Audu"
age = 26
is_married = False
height = 1.8
print(firstname, lastname, age, is_married, height)

print(type(1))
print(type(1.))
print(type(False))
print(type(True))
print(type("m"))
true = "True"
print(type(true))
true = True
print(type(true))


a = 1
b = 2
c = 4
print(id(a))
print(id(c))
c = a
print(id(c))
#a = b
print(id(a))
print(id(b))
#print(id(c))
c = 4
print(a,c)
print(id(c))
'''

'''
m = "M"
n = "n"
d = "m"
print(id(m))
print(id(n))
print(id(d))

num = "1"
num = num + str(2)
print(num)
print(type(num))
'''

d = 1/2
e = -1 // 2
print(d, type(d))
print(e, type(e))
