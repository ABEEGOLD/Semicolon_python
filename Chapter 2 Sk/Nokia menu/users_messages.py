users_messages = input("Enter your message: ")
if users_choice is not range( 1, 14):
            print("Invalid input. Please enter a number.")
			continue
users_messages = int(users_messages)


match users_messages:
          case 1:
              print("""

MESSAGES
1. Write messages
2. Inbox
3. Out box
4. Picture messages
5. Templates
6. Smileys
7. Message settings
""")
