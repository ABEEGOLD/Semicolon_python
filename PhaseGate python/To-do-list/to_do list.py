to_do list = to_do[] 

def list_menu():
    print("""
        list menu options
        1 -> Add a task
        2 -> view tasks
        3 -> mark task as complete
        4 -> delete a task
       	6 -> Exit
    """)

def Add_a_task():
	print("""
	1 -> laundry
	2 -> get breakfast
	3 -> read
	4 -> prepare lunch
	5 -> nap
	6 -> go out 
	""")

while True:
       list_menu()
    users_choice = input("Enter your choice: ")
	match user_chioce:
		case "1":
		   print("""
		   Add a task
		   1 -> laundry
	           2 -> get breakfast
	           3 -> read
	           4 -> prepare lunch
	           5 -> nap
	           6 -> go out
		   """)
		   Add_a_task_choice = (input("Enter choice:"))

		   match Add_a_task_choice:
		       case "1":
			  print("[x]" "laundry" )
		       case "2":
			   print("[]" "get breakfast")
		       case "3":
			   print("[x]" "read")
		       case "4":
			   print("[x]" "prepare")
		       case "5":
			   print("[]" "nap")
		       case "6":
			   print("[]" "go out")
		       case _:
		           print("invalid option in task")

			
			
	
