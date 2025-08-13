print('List Slcing Output\n')
# Lists
# Use slicing for the following list
# 1
list1 = [42, "hello", 3.14, True, None, [1, 2, 3], {"a": 1, "b": 2}]
print(list1[0:3])
print(list1[3:])
print(list1[:5])
print(list1[2:6])
print(list1[-3:])
print("\n")
# 2
list2 = ["apple", 10, False, [4, 5, 6], {"x": "y"}, 7.89, None]
print(list2[1:4])
print(list2[:2])
print(list2[3:])
print(list2[-4:-1])
print(list2[-2:])
print("\n")
# 3
list3 = [100, "banana", {"fruit": "mango"}, [9, 8, 7], True, 5.5, None, "end"]
print(list3[:4])
print(list3[4:])
print(list3[2:6])
print(list3[-5:])
print(list3[-7:-3])
print("\n")
# 4
list4 = [["nested", "list"], 25, None, {"key": "value"}, False, "string", 0.001]
print(list4[1:5])
print(list4[:3])
print(list4[3:])
print(list4[-4:])
print(list4[-6:-2])
print("\n")
# 5
list5 = [True, {"a": [1, 2]}, 50, "middle", 99.99, [10, 20, 30], None, "last"]
print(list5[:5])
print(list5[5:])
print(list5[2:7])
print(list5[-3:])
print(list5[-6:-1])
print("\n")
print('Tuples Slicing Output\n')
# Tuples
# Use slicing for the following tuples
# 1
tuple1 = (42, "hello", 3.14, True, None, [1, 2, 3], {"a": 1, "b": 2})
print(tuple1[0:3])
print(tuple1[3:])
print(tuple1[:5])
print(tuple1[2:6])
print(tuple1[-3:])
print("\n")
# 2
tuple2 = ("apple", 10, False, [4, 5, 6], {"x": "y"}, 7.89, None)
print(tuple2[1:4])
print(tuple2[:2])
print(tuple2[3:])
print(tuple2[-4:-1])
print(tuple2[-2:])
print("\n")
# 3
tuple3 = (100, "banana", {"fruit": "mango"}, [9, 8, 7], True, 5.5, None, "end")
print(tuple3[:4])
print(tuple3[4:])
print(tuple3[2:6])
print(tuple3[-5:])
print(tuple3[-7:-3])
print("\n")
# 4
tuple4 = (["nested", "list"], 25, None, {"key": "value"}, False, "string", 0.001)
print(tuple4[1:5])
print(tuple4[:3])
print(tuple4[3:])
print(tuple4[-4:])
print(tuple4[-6:-2])
print("\n")
# 5
tuple5 = (True, {"a": [1, 2]}, 50, "middle", 99.99, [10, 20, 30], None, "last")
print(tuple5[:5])
print(tuple5[5:])
print(tuple5[2:7])
print(tuple5[-3:])
print(tuple5[-6:-1])
print("\n")

# LIST
# Given this list:
fruits = ["apple", "banana", "mango", "orange"]
'''
1. Add "grape" to the end of the list.
 2. Insert "cherry" at index 2.
 3. Remove "banana" from the list.
4. Replace "orange" with "watermelon".
 5. Extend the list with ["pear", "kiwi"].
'''
# SOLUTION
# 1. Add "grape" to the end of the list.
fruits.append("grape")
print(fruits)
# 2. Insert "cherry" at index 2.
fruits.insert(2, "cherry")
print(fruits)
# 3. Remove "banana" from the list.
fruits.remove("banana")
print(fruits)
# 4. Replace "orange" with "watermelon".
print(fruits[-2]) # Find the index of orange and ensure it is correct then replace via reassignment
fruits[-2] = "watermelon"
print(fruits)
#5. Extend the list with ["pear", "kiwi"].
fruits.append(["pear", "kiwi"])
print(fruits)
print("\n")
# Given this list:
data = [10, 20, 30, 40, 50]
'''
1. Append 60 to the list.
2. Insert 15 at index 1.
3. Remove the first element from the list.
 4. Change the value at index 3 to 45.
5. Add [70, 80] as separate elements to the list.
'''
#SOLUTION
# 1. Append 60 to the list.
data.append(60)
print(data)
# 2. Insert 15 at index 1.
data.insert(1, 15)
print(data)
# 3. Remove the first element from the list.
data.remove(10)
print(data)
#  4. Change the value at index 3 to 45.
print(data[3])
data[3] = 45
print(data[3])
print(data)
# 5. Add [70, 80] as separate elements to the list
data.append(70)
data.append(80)
print(data)
print("\n")


# TUPLES
# Given this tuple:
colors = ("red", "blue", "green", "yellow")
'''
1. Convert the tuple to a list.
2. Add "purple" to the end.
3. Replace "blue" with "black".
4. Convert it back to a tuple.
'''
# SOLUTION
#  1. Convert the tuple to a list.
colors = list(colors)
print(colors, type(colors))
#  2. Add "purple" to the end.
colors.append("purple")
print(colors)
# 3. Replace "blue" with "black"
colors[1] = "black"
print(colors)
#  4. Convert it back to a tuple.
colors = tuple(colors)
print(colors, type(colors))
print("\n")
# Given this tuple:
numbers = (1, 2, 3, 4, 5)
'''
1. Concatenate it with another tuple (6, 7, 8).
2. Slice the first four elements from the new tuple.
3. Convert the tuple to a list and remove the value 3.
4. Convert it back to a tuple.
'''
# SOLUTION
# 1. Concatenate it with another tuple (6, 7, 8).
numbers += (6, 7, 8)
print(numbers)
# 2. Slice the first four elements from the new tuple.
print(numbers[0:4])
# 3. Convert the tuple to a list and remove the value 3.
numbers = list(numbers)
numbers.remove(3)
print(numbers, type(numbers))
#  4. Convert it back to a tuple.
numbers = tuple(numbers)
print(numbers, type(numbers))

