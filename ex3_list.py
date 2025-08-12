# A list is an ordered sequence of elements grouped together
# List uses STACK data structure. It uses the concept of LIFO (Last In, First Out)
'''
noise_makers = []
print(noise_makers, len(noise_makers))
noise_makers.append("Dorcas") # TO add items at end of list
print(noise_makers, len(noise_makers))
noise_makers.append('Bethel')
print(noise_makers, len(noise_makers))

# .pop is used to remove last item on list using LIFO
colors = ["blue", "black", "white", "red", "black", "yellow", "green"]
print(colors, len(colors))
colors.pop() # .pop is used to remove last item on list using LIFO

# INSERT USES SYNTAX; array.insert(index, item)
colors.insert(1, "orange")
print(colors)

# Remove uses syntax; array.remove(item)
#colors.remove("violet")
#print(colors)

# To replace or reassign in list ensure the index exist the use the syntax; array[index] = 'item'
fruits = ["orange", "mango", "apple", "pear"]
print(fruits)
fruits[1] = 'grapes'
print(fruits)

# For Languages like Golang without .pop() use this method of index swapping to move item you want to swap to last item. 
fruits[0], fruits[-1] = fruits[-1], fruits[0]
# Then reassign the items you want(execept the last one) using slice and reassign back to the array. that is; array = array[indexa:indexb]
fruits = fruits[0:3]
print(fruits)
# To ensure data integrity avoid this method although it works
# fruits[0], fruits[-1] = 'pear', 'orange'
#print(fruits) 

# Naviagtig through nested lists
a = [1,2,3,[4,5,[6,7,[8],9]]]
# 1. get the value 8
print(a[3][2][2][0])

# 2. get the value of 9
print(a[3][2][3])

# 3. the last index of variable a
print(a[3])
'''

y =[1,2,['yusuf', False, "9"]]
print(y[2], type(y[2])) # Use index to bring out the list/array needed
print(y[2][2], type(y[2][2]))
# Add 5 to yusuf score 9
y[2][2] = int(y[2][2]) + 5 # Since you cant concatenate str to int, convert to int so you can increment
print(y[2][2])
print(y)
print(y[2][2], type(y[2][2]))
y[2][2] = str(y[2][2]) # To change back to str
print(y)



















