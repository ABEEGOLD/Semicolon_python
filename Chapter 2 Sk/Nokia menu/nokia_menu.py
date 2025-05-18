def nokia_Menu():
    print("""
Your Nokia Menu App
1. Phonebook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock 
12. Profiles
13. Sim Services
0. Exit
""")


while True:
    nokia_Menu()
    users_choice = input("Enter your choice: ")

    if not users_choice.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    users_choice = int(users_choice)

    if users_choice not in range(0, 14):
        print("Invalid choice. Please enter a number from 0 to 13.")
        continue

    match users_choice:
        case 1:
            print("""
PHONE BOOK
1. Search 
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign Tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
""")
            phone_book_choice = input("Enter choice: ")

            if not phone_book_choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            phone_book_choice = int(phone_book_choice)

            match phone_book_choice:
                case 1:
                    print("Search")
                case 2: 
                    print("Service Nos.")
                case 3: 
                    print("Add name")
                case 4:
                    print("Erase")
                case 5: 
                    print("Edit")
                case 6: 
                    print("Assign Tone")
                case 7: 
                    print("Send b'card")
                case 8: 
                    print("""
OPTIONS
1. Type of view
2. Memory status
""")
                    options = input("Enter number: ")
                    if not options.isdigit():
                        print("Invalid input. Please enter a number.")
                        continue
                    options = int(options)
                    match options: 
                        case 1: 
                            print("Type of view")
                        case 2: 
                            print("Memory status")
                        case _:
                            print("Invalid option in Options menu.")
                case 9: 
                    print("Speed dials")
                case 10:
                    print("Voice Tags")
                case _:
                    print("Invalid option in Phonebook.")

        case 2:
            message = input("Enter your message: ")
            print(f"Message saved: {message}")

        case 0:
            print("Exiting Nokia Menu App. Goodbye!")
            break

        case _:
            print("Invalid main menu option.")