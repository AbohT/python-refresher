# We use loops to automate boring tasks
# A loop is program that start and end at the same point
# Print 1 - 50
'''print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
print(11)
print(12)
print(13)
print(14)
print(15)
print(16)
print(17)
print(18)
print(19)
print(20)
print(21)
print(22)
print(23)
print(24)
print(25)
print(26)
print(27)
print(28)
print(29)
print(30)
print(31)
print(32)
print(33)
print(34)
print(35)
print(36)
print(37)
print(38)
print(39)
print(40)
print(41)
print(42)
print(43)
print(44)
print(45)
print(46)
print(47)
print(48)
print(49)
print(50)
'''
# Using a loop makes the process easier.
# Loops are used to iterate over a data set. You need to know your starting point, stop point, and important updater to not run into an infinite loop.
'''
for a in range(1,51):
	print(a)
condition = True
x = 1
while condition:
	if x <=10:
		print(x)
		x +=1
		print(" ")
	else:
		condition = False
x = 1
while x <= 10:
	print(x)
	x +=1

steps = 10
while steps <=10 and steps >0:
	print(steps)
	steps -=1
	print("")

foot = 10
while foot > 0:
	print(foot)
	foot -=1
	

x = 1
while x <= 10:
	if x !=5:
		print(x)
	x+=1

x = 1
odd_number = []
even_number = []
while x <=10:
	if x % 2 == 0:
		even_number.append(x)
	else:
		odd_number.append(x)
	x +=1
print(odd_number)
print(even_number)

i = 0
while i < 101:
	if i % 10 == 0 and i !=0:
		print(i)
	i+=10

# Create a program to increment by 10 and also 5
i = 0
shouldIncrementBy10 = True
while i < 100:
	if shouldIncrementBy10:
		i+=10
		print(i)
		shouldIncrementBy10 = False
	else:
		i+=5
		print(i)
		shouldIncrementBy10 = True
'''
# Create a program to increment by 10,5 and 15
i = 0
shouldIncrementBy10 = True
shouldIncrementBy5 = True
while i < 100:
	if shouldIncrementBy10:
		i+=10
		print(i)
		shouldIncrementBy10 = False
	elif shouldIncrementBy5:
		i+=5
		print(i)
		shouldIncrementBy5 = False
	else:
		i+=15
		print(i)
		shouldIncrementBy10 = True
		shouldIncrementBy5 = True

