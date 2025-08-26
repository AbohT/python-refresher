#Conditionals always return a bool (True or False)
'''
students = ["TK", "TG", "Bethel", "Dre", "Dan", "Ben"]
print("tK" in students)
contacts = {
		"Nando" : "09085438234",
		"Jerry" : "08136709001",
		"Sis" : "09136709678",
		"Aboh" : "08088533876",
		"Godiya" : "07056895490",
		"Stephy" : "09080765543",
		"Caleb" : "08088421895", 
		}	
print("Jibrin" not in contacts)


isMarried = not True
web2class = True
isMale = True
favouriteNumber = 10
print(not isMarried and web2class and favouriteNumber == 10.0 or isMale)

print(10!=10.0)
print(10==10.0)

temp = 28
result = " "
if temp < 15:
	result = "cold"
elif temp >= 15 and temp <= 25:
	result = "warm"
else:
	result = "hot"
print(result)
'''
persons = {
    "name" : "Joseph",
    "student" : True,
    "age" : 23,
    "likes" : ["eating", "sleeping", "making money"]
	}
print(persons["likes"][1])
print(persons.get("likes")[0])
print(persons.values())
print(persons.items())
print(persons.keys())
persons.pop("age")
print(persons)
persons.popitem()
print(persons)
print(persons["age"])

#username = input("Enter your username: ")
#keyword = input("Enter your search keyword: ")
#if username == persons.get("name") and persons.get("student"):
#    print("You have libraray access"
#else:
#    print("No access")
print(persons.keys())
print(persons["age"])
if "age" in persons.keys():
	print(persons["age"])
else:
	print("None")



