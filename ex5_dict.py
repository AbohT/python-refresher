# A dictionary is an ordered sequence of data that has key value pairs.
# A dict is not indexable beacuse all the keys are unique and can't be repeated or changed. It is case sensitive (uses ASCII for every character)
e = {}
'''
pirint(e, type(e))

# List 10 contacts and their phone numbers as a dict
contacts = {
		"Nando" : "09085438234",
		"Jerry" : "08136709001",
		"Sis" : "09136709678",
		"Aboh" : "08088533876",
		"Godiya" : "07056895490",
		"Stephy" : "09080765543",
		"Caleb" : "08088421895", 
		"Jeff" : "08024567823",
		"Lily" : "07056899209",
		"Matthew" : "08123456543",
		"Matthew" : "08065778345",	#Will be reinitialized and assigned the last value for the key.
		" " : "0705679022234"
		}
print(len(contacts), type(contacts))
print(contacts)
print(contacts[" "])

trial = {
		True : "True",
		False : "False",
		4  : "Four",
		4.5 : "four point five",
		(1,2) : "One comma Two"
		}
print(trial[True], type(trial[True]))
print(trial[False])
print(trial[4])
print(trial[4.5])
print(trial[(1,2)])


# Reasssignment to items works in dict as it does in lists
# Update method only available in dict
contacts.update({"Adamu" : "09009998765678"})
print(contacts)

# Pop and popitems. dict.pop(key) is for specific items or elements while array.popitem() is last item 
contacts.popitem()
print(contacts)
contacts.pop("Caleb")
print(contacts)
del contacts["Aboh"]
print(contacts)

# TO get only keys or values use dict.keys() and dict.values()
'''

# Dorcas, Dan, Ben are sharing same laptop. each keystroke is matched to each individual using it. At the end of the day we should see what each individual uses.
# Method 1
"""
Dorcas = []
Ben = []
Dan = []
laptop = {
	"Dorcas" : Dorcas,
	"Ben" : Ben,
	"Dan" : Dan
		}
print(laptop)
Dorcas.append("qwerty")
Dorcas.append("1,2,3")
print(laptop)

"""
# Method 2
'''
laptop = {
	"Dorcas" : [],
	"Ben" : [],
	"Dan" : []
		}

laptop["Dorcas"].append(["a,e,c"])
print(laptop)
trial = {
		"scores" : (1,2)
		}
one, two = trial["scores"]
print(one, two)
'''
# Three friends walk to a supermarket and takes a cart to buy things. How do you represent this
cart = {}
Dan = Dre = Jibrin = cart
# What Dan took
Dan.update({"Peak Milk" : 4})
# What Dre took
Dre.update({"Garri" : 6})
# what  Jibrin took 
Jibrin.update({"Kuli kuli" : 9})
print(cart)

cart1 = cart.copy() # .copy() 
print(cart)
cart.clear() # .clear() empties the dict
print(cart) 
