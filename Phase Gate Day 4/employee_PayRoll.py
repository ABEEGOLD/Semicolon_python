def employee_PayRoll():
    print("""Semicolon Employee PayRoll
        1 -> Add Employee PayRoll
        2 -> View Employee PayRoll
        3 -> Update Employee payrol
       	4 -> Exit
    """)

users_choice = input("Enter 1-4: ")
match users_choice:
	case "1":
		print("1.Add Employee PayRoll")
		Employee_name =input("Employee name:")
		work_Hourly = input("Number of hour worked in a week:")
		hourly_pay = input("Hourly pay rate:")
		federal_pay = input("federal tax pay with holding rate:")
		state_pay = input("State tax withholding rate:")
		
 		
			
	case "2":
		print("2.View Employee PayRoll")
			name = ' '
			name = 'Ada'
		print("	Employee name:"+name)
		float  hourly  = 40
			if hourly == 40 and hourly <1:
			print("hours worked:" +hourly)
					
		
	case "3":
		print("3.Update Employee payroll")
	case "4":
		print("Invalid")
		print("Do you want to continue, enter NO or YES to continue!")
		users_choice = input("Enter 1-4: ")


