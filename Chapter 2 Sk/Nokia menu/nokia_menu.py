

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

def message():
    print("""
    1: Write Messages
    2: Inbox
    3: Outbox
    4: Picture Messages
    5: Templates
    6: Smileys
    7: Message Settings**
    8: Info Service
    9: Voice Mailbox Number
    10: Service Command Editor   
    """)

def write():
    print("""
    1: Input Message  
    """)

def inbox():
    print("""
    INBOX 
    """)

def received_messages():
    print("""
    1: Obi is a boy
    2: Abigail is a Software Engineer
    3: Cohort 25 is the best set in SemiColon Africa
    4: I can do all things
    5: Nothing is impossible
    """)

def message_settings():
    print("""
    1. Set 1
    2. Common
    """)

def chat():
    print("""
    1: Facebook
    2: weChat  
    3: MyChat
    4: 2go
    5: Instagram
    6: SnapChat
    7: X 
    """)

def call_register():
    print("""
    1: Missed Calls
    2: Recieved Calls 
    3: Dialled Numbers
    4: Erase Recent Call Lists
    5: Show Call Duration**
    6: Show Call Costs**
    7: Call Cost Settings**
    8: Prepaid Credit     
    """)

def tones():
    print("""
    1: Ringing Tone
    2: Ringing Volume
    3: Incoming Call Alert
    4: Composer
    5: Message Alert Tone
    6: Keypad Tones
    7: Warning And Game Tones
    8: Vibrating Alert
    9: Screen Saver  
    """)

def settings():
    print("""
    1: Call Settings**
    2: Phone Settings
    3: Security Settings
    4: Restore Factory Settings   
    """)

def call_settings():
    print("""
    1: Automatic Redial
    2: Speed Dialling
    3: Call Waiting Options
    4: Own Number Sending
    5: Phone Line In Use
    6: Automatic Answer   
    """)

def phone_settings():
    print("""
    1: Language
    2: Cell Info Display
    3: Welcome Note
    4: Network Selection
    5: Lights
    6: Confirm SIM Service Actions  
    """)

def security_settings():
    print("""
    1: PIN Code Request
    2: Call Barring Service
    3: Fixed Dialling
    4: Closed User Group
    5: Phone Security
    6: Change Access Codes
    """)

def clock():
    print("""
    1: Alarm Clock
    2: Clock Settings
    3: Date Setting
    4: Stopwatch
    5: Countdown Timer
    6: Auto Update of Date and Time
    """)

def set_1():
    print("""
    1: Set 1
    2. Common
    """)

def common():
    print("""
    1: Delivery Reports
    2: Reply Via Same Centre
    3: Character Support
    """)

def options():
    print("""
    1: Type of View
    2: Memory Status
    """)


while True:
    nokia_Menu()
    users_choice = input("Enter your choice: ")
    match users_choice:
        case "1":
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
            phone_book_choice =  (input("Enter choice: "))

            match phone_book_choice:
                case "1":
                    print("Search")
                case "2":
                    print("Service Nos.")
                case "3":
                    print("Add name")
                case "4":
                    print("Erase")
                case "5":
                    print("Edit")
                case "6":
                    print("Assign Tone")
                case "7":
                    print("Send b'card")
                case "8":
                    print("""
                    OPTIONS
                    "1". Type of view
                    "2". Memory status
                    """)
                    options = (input("Enter number: "))
                    match options:
                        case "1":
                            print("Type of view")
                        case "2":
                            print("Memory status")
                        case _:
                            print("Invalid option in Options menu.")
                case "9":
                    print("Speed dials")
                case "10":
                    print("Voice Tags")
                case _:
                    print("Invalid option in Phonebook.")

        case "2":
            print(message())
            message = (input("Enter your number: "))
            match message:
                case "1":
                    print("Write Message")
                    print(write())

                    print("Enter number: ")

                case "2":
                    print(inbox())
                    print(received_messages())

                case "3":
                    print("Outbox")
                case "4":
                    print("Picture Messages")
                case "5":
                    print("Templates")
                case "6":
                    print("Smileys")
                case "7":
                    print("Message Settings")
                    print(message_settings())

                    message_settings_choice = (input("Enter number: "))
                    match message_settings_choice:
                        case "1":
                            print("Set 1")
                            print(set_1())

                            set_1_choice = (input("Enter number: "))
                            match set_1_choice:
                                case "1":
                                    print("Message Centre Number")
                                case "2":
                                    print("Message sent as")
                                case "3":
                                    print("Message validity")

                        case "2":
                            print("Common")
                            print(common())
                            print("Enter number: ")
                            common_choice = (input("Enter number: "))

                            match common_choice:
                                case "1":
                                    print("Delivery Reports ")
                                case "2":
                                    print("Reply Via Same Centre")
                                case "3":
                                    print("Character Support")
                case "8":
                    print("Options")
                    print(options())
                    options_choice = (print("Enter number: "))
                    match options_choice:
                        case "1":
                            print("Type of View")
                        case "2":
                            print("Memory status")
                case "9":
                    print("Speed dials")
                case "10":
                    print("Voice Tags")

        case "3":
            print("CHAT")
            print(chat())
            chat_choice = (input("Enter number: "))
            match chat_choice:
                case "1":
                    print("FaceBook")
                case "2":
                    print("weChat")
                case "3":
                    print("MyChat")
                case "4":
                    print("2go")
                case "5":
                    print("Instagram")
                case "6":
                    print("SnapChat")
                case "7":
                    print("X")

        case "4":
            print("CALL REGISTER")
            print(call_register())
            call_register_choice = (input("Enter number: "))
            match call_register_choice:
                case "1":
                    print("Missed calls")
                case "2":
                    print("Received calls")
                case "3":
                    print("Dialled numbers")
                case "4":
                    print("Erase recent call lists")
                case "5":
                    print("Show call duration")
                    call_duration_choice = (input("Enter number: "))

                    match call_duration_choice:
                        case "1":
                            print("Last call duration")
                        case "2":
                            print("All Call's duration")
                        case "3":
                            print("Received call's duration")
                        case "4":
                            print("Dialled call's duration")
                        case "5":
                            print("Clear timers")

                case "6":
                    print("Show Call Costs")
                    call_cost_choice = (input("Enter number: "))

                    match call_cost_choice:
                        case "1":
                            print("Last call cost")
                        case "2":
                            print("All call's cost")
                        case "3":
                            print("Clear counter")

                case "7":
                    print("Call cost settings")
                    call_cost_settings_choice = (input("Enter number: "))
                    match call_cost_settings_choice:
                        case "1":
                            print("Call cost limit")
                        case "2":
                            print("Show costs in")

                case "8":
                    print("Prepaid Credit")

        case "5":
            print("TONES")
            print(tones())
            tone_choice = (input("Enter number: "))
            match tone_choice:
                case "1":
                    print("Ringing Tone")
                case "2":
                    print("Ringing Volume")
                case "3":
                    print("Incoming Call Alert")
                case "4":
                    print("Composer")
                case "5":
                    print("Message Alert Tone")
                case "6":
                    print("Keypad Tones")
                case "7":
                    print("Warning and Game Tone")
                case "8":
                    print("Vibrating Alert")
                case "9":
                    print("Screen Saver")

        case "6":
            print("SETTINGS")
            print(settings())
            settings_choice = (input("Enter number: "))
            match settings_choice:
                case "1":
                    print("Call Settings")
                    print(call_settings())
                    call_settings_choice = (input("Enter number: "))
                    match call_settings_choice:
                        case "1":
                            print("Automatic redial")
                        case "2":
                            print("Speed dialling")
                        case "3":
                            print("Call waiting options")
                        case "4":
                            print("Own number sending")
                        case "5":
                            print("Phone line in use")
                        case "6":
                             print("Automatic answer")

                case "2":
                    print("Phone Settings")
                    print(phone_settings())
                    phone_settings_choice = (input("Enter number: "))
                    match phone_settings_choice:
                        case "1":
                            print("Language")
                        case "2":
                            print("Cell info display")
                        case "3":
                            print("Network selections")
                        case "4":
                            print("Welcome note")
                        case "5":
                            print("Confirm SIM Service actions")

                case "3":
                    print("Security settings")
                    print(security_settings())
                    security_settings_choice = (input("Enter number: "))
                    match security_settings_choice:
                        case "1":
                            print("PIN code request")
                        case "2":
                            print("Call barring service")
                        case "3":
                            print("Fixed dialling")
                        case "4":
                            print("Closed user group")
                        case "5":
                            print("Phone security")
                        case "6":
                            print("Change access code")

                case "4":
                    print("Restore Factory Settings")

        case "7":
            print("CALL DIVERT")
            print("Call divert")
        case "8":
            print("GAMES")
            print("Games")
        case "9":
            print("CALCULATOR")
            print("Calculator")
        case "10":
            print("REMINDERS")
            print("Reminders")
        case "11":
            print("CLOCK")
            print(clock())
            clock_choice = (input("Enter number: "))
            match clock_choice:
                case "1":
                    print("Alarm Clock")
                case "2":
                    print("Clock Settings")
                case "3":
                    print("Date Setting")
                case "4":
                    print("Stopwatch")
                case "5":
                    print("Countdown Timer")
                case "6":
                    print("Auto Update Of Date & Time")

        case "12":
            print("PROFILES")
            print("Profiles")
        case "13":
            print("SIM SERVICES")
            print("Sim services")

        case _:
            print("Invalid")
            print("Do you want to continue, enter NO or YES to continue!")
            user_input = input()