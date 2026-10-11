def main_menu():
    while True:
        print("""
Nokia Phone Menu
1 Phone book
2 Messages
3 Chat
4 Call register
5 Tones
6 Settings
7 Call divert
8 Games
9 Calculator
10 Reminder
11 Clock
12 Profiles
13 SIM services
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                phonebook()
            case "2":
                messages()
            case "3":
                print("Chat")
            case "4":
                call_register()
            case "5":
                tones()
            case "6":
                settings()
            case "7":
                print("Call divert")
            case "8":
                print("Games")
            case "9":
                print("Calculator")
            case "10":
                print("Reminder")
            case "11":
                clock()
            case "12":
                print("Profiles")
            case "13":
                print("SIM services")
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice")


def phonebook():
    while True:
        print("""
Phonebook
1 Search
2 Service Nos
3 Add Name
4 Erase
5 Edit
6 Assign tone
7 Send b'card
8 Options
9 Speed dials
10 Voice tags
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Search")
            case "2":
                print("Service Nos")
            case "3":
                print("Add Name")
            case "4":
                print("Erase")
            case "5":
                print("Edit")
            case "6":
                print("Assign tone")
            case "7":
                print("Send b'card")
            case "8":
                print("Options")
            case "9":
                print("Speed dials")
            case "10":
                print("Voice tags")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def messages():
    while True:
        print("""
Messages
1 Set 1
2 Common
3 Chat
4 Call register
5 Show call duration
6 Show call cost
7 Call cost setting
8 Prepaid credit
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                set1()
            case "2":
                common()
            case "3":
                print("Chat")
            case "4":
                call_register()
            case "5":
                show_call_duration()
            case "6":
                show_call_cost()
            case "7":
                call_cost_setting()
            case "8":
                print("Prepaid credit")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def set1():
    while True:
        print("""
Set 1
1 Message centre number
2 Message sent as
3 Message validity
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Message centre number")
            case "2":
                print("Message sent as")
            case "3":
                print("Message validity")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def common():
    while True:
        print("""
Common
1 Delivery report
2 Reply via same centre
3 Character support
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Delivery report")
            case "2":
                print("Reply via same centre")
            case "3":
                print("Character support")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def call_register():
    while True:
        print("""
Call Register
1 Missed call
2 Received call
3 Dialled number
4 Erase recent call list
5 Show call duration
6 Show call cost
7 Call cost setting
8 Prepaid credit
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Missed call")
            case "2":
                print("Received call")
            case "3":
                print("Dialled number")
            case "4":
                print("Erase recent call list")
            case "5":
                show_call_duration()
            case "6":
                show_call_cost()
            case "7":
                call_cost_setting()
            case "8":
                print("Prepaid credit")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def show_call_duration():
    while True:
        print("""
Show Call Duration
1 Last call duration
2 All call duration
3 Received call duration
4 Dialled call duration
5 Clear timer
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Last call duration")
            case "2":
                print("All call duration")
            case "3":
                print("Received call duration")
            case "4":
                print("Dialled call duration")
            case "5":
                print("Clear timer")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def show_call_cost():
    while True:
        print("""
Show Call Cost
1 Last call cost
2 All call cost
3 Clear counter
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Last call cost")
            case "2":
                print("All call cost")
            case "3":
                print("Clear counter")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def call_cost_setting():
    while True:
        print("""
Call Cost Setting
1 Call cost limit
2 Show cost in
3 Clear counter
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Call cost limit")
            case "2":
                print("Show cost in")
            case "3":
                print("Clear counter")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def tones():
    while True:
        print("""
Tones
1 Ringing tone
2 Ringing volume
3 Incoming call alert
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Ringing tone")
            case "2":
                print("Ringing volume")
            case "3":
                print("Incoming call alert")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def settings():
    while True:
        print("""
Settings
1 Call settings
2 Phone settings
3 Security settings
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                call_settings()
            case "2":
                phone_settings()
            case "3":
                security_settings()
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def call_settings():
    while True:
        print("""
Call Settings
1 Automatic redial
2 Speed dialling
3 Call waiting
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Automatic redial")
            case "2":
                print("Speed dialling")
            case "3":
                print("Call waiting")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def phone_settings():
    while True:
        print("""
Phone Settings
1 Language
2 Cell info display
3 Welcome note
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Language")
            case "2":
                print("Cell info display")
            case "3":
                print("Welcome note")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def security_settings():
    while True:
        print("""
Security Settings
1 PIN code request
2 Call barring service
3 Fixed dialling
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("PIN code request")
            case "2":
                print("Call barring service")
            case "3":
                print("Fixed dialling")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


def clock():
    while True:
        print("""
Clock
1 Alarm clock
2 Clock settings
3 Date setting
4 Stopwatch
99 Back
0 Exit
""")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                print("Alarm clock")
            case "2":
                print("Clock settings")
            case "3":
                print("Date setting")
            case "4":
                print("Stopwatch")
            case "99":
                return
            case "0":
                exit()
            case _:
                print("Invalid choice")


main_menu()
