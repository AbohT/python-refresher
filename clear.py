
persons = {
		"Joe" : {"isStudent" : True, "age" : 24},
		"Tom" : {"isStudent" : True, "age" : 34},
		"Dan" : {"isStudent" : False, "age" : 26}
	}
definitions = {
	"a" : "blesdf",
	"b" : "callifornia",
	"c" : "ccccd",
	"d" : "astafigurrallah",	
		}
name = input("enter you name: ")
if name in persons: 
   if persons[name]["isStudent"]:
       keyword = input("Enter your keyword: ")
       if keyword in definitions.keys():
           print(definitions.get(keyword))
   else:
        print("Not a student")
else:
    print("User not found")

