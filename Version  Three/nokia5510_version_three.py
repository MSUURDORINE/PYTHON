main_menu = """
========== HOME MENU ==========

1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clocks
13. Profile
14. Services
15. SIM services

0. Exit
"""
while True:
        print(main_menu)
        main_menu_no = (input("Enter number: "))
        match main_menu_no:
            case "1":
                print("\nPhone book")
        phone_book_menu = """
        1. Search
        2. Service Nos
        3. Add name
        4. Erase
        5. Edit
        6. Copy
        7. Assign tone
        8. Send b'card
        9. Options
        10. Speed dials
        11. Voice tags
        0. Home
        """
        print(phone_book_menu)
        phone_book_no = (input("Enter number: "))
        match phone_book_no:
            case "1":
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("Add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Copy")
            case 7:
                print("Assign tone")
            case 8:
                print("Send b'card")
            case 9:
                print("Options")
                options_menu = """
                1. Memory in use
                2. Type of view
                3. Memory status
                0. Home
             """
                print(options_menu)
                options_no = (input("Enter number: "))
                match options_no:
                    case "1":
                        print("Memory in use")
                    case 2:
                        print("Type of view")
                    case 3:
                        print("Memory status")
                    case 0:
                        print("Returning to Home Menu...")
                    case _:
                        print("Invalid input")
                        break
            case 10:
                print("Speed dials")
            case 11:
                print("Voice tags")
            case 0:
                print("Returning to Home Menu...")
            case 2:
                print("Messages menu")
                messages_menu = """
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings
                8. Info service
                9. Voice mailbox number
                10. Service command editor
                0. Home
                """                
        print("messages menu")
        messages_no = (input("Enter number: "))
        match messages_no:
            case "1":
                print("Write messages")
            case 2:
                print("Inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture messages")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message settings")
            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")
            case 0:
                print("Returning to Home Menu...")
            
                print("Invalid input")
                
            case 3:
                print("Chat")
            case 4:
                print("Call register")
            case 5:
                print("Tones")
            case 6:
                print("Settings")
            case 7:
                print("Call divert")
            case 8:
                print("Music")
            case 9:
                print("Games")
            case 10:
                print("Calculator")
            case 11:
                print("Reminders")
            case 12:
                print("Clocks")
            case 13:
                print("Profile")
            case 14:
                print("Services")
            case 15:
                print("SIM services")
            case 0:
                print("Goodbye!")
            case _:
                print("Invalid input")                
                                          
