
# create a program that asks a user for his employee id number, if the number exists, ask him the informaton he wants to access. If his level reaches the information access level, show him the information.

employee_database = {
		1001 : {'name' : "John", "age" : 32, "Dept" : "Human Resource", "Access level" : 2},
		1002 : {'name' : 'Paul', 'age' : 28, 'Dept' : 'Payroll', 'Access level' : 3},
		1003 : {'name' : 'Esther', 'age' : 40, 'Dept' : 'Logistics', 'Access level' : 1}
		}

company_database = {
    "salary": {"description": "Company salary details.", "required_level": 3},
    "projects": {"description": "Current company projects.", "required_level": 2},
    "logistics": {"description": "Confidential company transportation and logistics document.", "required_level": 1},
		}
employee_id = int(input("Enter yor employee id: "))

if employee_id in employee_database:
	info = input("What company informnation do you want to access: ").lower()
	if info in company_database.keys():
		required_level = company_database[info]['required_level']
		print(f"The information you want exists and requires level  {required_level} to access it") 
		if employee_database[employee_id]['Access level'] >= required_level:
			print(company_database[info]['description'])
		else:
	 		print("You do not have the required access level to view this information")
	else:
		print("Information requested not available in company database")
else:
	print("Invalid employee id")
