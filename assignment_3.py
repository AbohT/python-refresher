'''
Create a student database with student 1 to student 10,000
Convert engine bash assignment to python

Name car
D ----> Start
P ----> Stop
R ----> Start

start , stop
'''
# Create a student database wuth students from 1 to 10,000
x = 1
while x <= 10000:
	print(f"student{x:,}")
	x+=1

# Engine assignment
car = input("what is the name of your car: ")
print(f'{car} registered successfully')

should_execute = True
car_is_on = False
park = False
reverse = False
drive = False

while should_execute:
	print(f'''
		AVAILABLE COMMANDS
		start: to start {car}
		d: to drive {car}
		r: to reverse {car}
		p: to park {car}
		stop: to stop {car}
		exit: to quit  execution
		help: to display available commands\n
		''')
	command = input(f"Enter available commands to use {car}: ").lower()

	# START
	if command == 'start' and car_is_on == False:
		car_is_on = True
		print(f"{car} started successfully")
	elif command == 'start' and car_is_on == True:
		print(f'{car} is already ON')
	
	# STOP
	elif command == 'stop' and car_is_on == True:
		car_is_on = False
		reverse = False
		park = False
		drive = False
		print(f"turning off {car}")
	elif command == 'stop' and car_is_on == False:
		print(f"{car} is already OFF")


	# DRIVE
	elif command == 'd' and car_is_on == True and drive == False:
		drive = True
		reverse = False
		park = False
		print(f"Drive gears activated successfully for {car}")
	elif command == 'd' and car_is_on == True and drive == True:
		print(f"{car} is already in drive mode")
	elif command == 'd' and car_is_on == False:
		print(f"Start {car} first to be able to drive")

	# REVERSE
	elif command == 'r' and car_is_on == True  and reverse == False:
		reverse = True
		drive = False
		park = False
		print(f"Reversing {car}")
	elif command == 'r' and car_is_on == True and reverse == True:
		print(f"{car} is already reversing, can't use reverse again")
	elif command == 'r' and car_is_on == False:
		print(f"Start {car} first before reversing")
	
	# PARK
	elif command == 'p' and car_is_on == True and park == False:
		park = True
		drive = False
		reverse = False
		print(f"{car} is now parked")
	elif command == 'p' and car_is_on == True and park == True:
		print(f"{car} is already parked")
	elif command == 'p' and car_is_on == False:
		print(f"Start {car} first before parking")
	
	# HELP
	elif command == 'help':
		print(f'''
		AVAILABLE COMMANDS
		start: to start {car}
		d: to drive {car}
		r: to reverse {car}
		p: to park {car}
		stop: to stop {car}
		exit: to quit execution
		help: to display available commands\n
		''')
	
	# EXIT
	elif command == 'exit':
		should_execute = False
		print("Goodbye")
	else:
		print("Invalid command. Use help to see available commands")

