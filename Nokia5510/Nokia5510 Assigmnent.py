main_menu = """
List of menu function
1: Phone book
2: Message	
3: Chat
4: Call register
5: Tones
6: Settings
7: Call divert	
8: Music 
9: Game
10: Calculator
11: Reminders
12: Clock
13: Profiles
14: Services
15: SIM services
"""
print(main_menu)
main_prompt = int(input())
match(main_prompt):
   case 1: 
      print("phone book")
      phonebook_menu = """
List of phonebook functions
1: Search
2: Service Nos.
3: Add name
4: Erase
5: Edit
6: Copy
7: Assign
8: Send b' card
9: Options
10: Speed dials
11: Voice tags
"""
      print(phonebook_menu)
      phonebook_prompt = input()
      match(phonebook_prompt):
         case 1: print("search")
         case 2: print("services")
         case 3: print("Add name")
         case 4: print("Erase")
         case 5: print("Edit")
         case 6: print("Coppy")
         case 7: print("Assign")
         case 8: print("Send b' card")
         case 9:
            print ("Options")
            options_menu = """
List of Option functions
1: Memory in use
2: Type of view
3: Memory status
"""
            print(options_menu)
            options_menu = input()
            match(options_menu):
               case 1: print("Memory in use")
               case 2: print("Type of view")
               case 3: print("Memory status")

         case 10: print("Speed dials")
         case 11:print("voice tags")

   case 2:
      print('Message')
      message_menu = """
 List of Message functions

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
"""
      print(message_menu)
      message_prompt = input()
      match(message_prompt):
         case 1: print("Write messages")
         case 2: print("Inbox")
         case 3: print("Outbox")
         case 4: print("Picture messages")
         case 5: print("Templates")
         case 6: print("Smileys"); 
         case 7:
               print("messages settings")
               messagesetting_menu = """
List of messagesetting functions
1. Set1
2. Common
"""
               print(messagesetting_menu)
               messagesetting_prompt = input()
               match(messagesetting_prompt):
                  case 1:
                     print("set1")                                        
                     Set1_menu = """
                     List of set1 functions
1. Message centre number
2. Message sent as 
3. Message validityMessage sent as 
3. Message validity                                                                                        
"""
               print(Set1_menu)
               Set1_prompt = input()
               match(Set1_prompt):
                  case 1: print("Message centre number")
                  case 2: print("Message sent as" )
                  case 3: print("Message validity")
            
                  case 2: 
                     print("common_meun")
                     Command_menu = """
1. Delivery reports
2. Repiy via same centre
3. Character support 
""";
               print(common_menu)
               common_prompt = input()
               match(common_prompt):
                  case 1: print("Delivery reports") 
                  case 2: print("Repiy via same centre") 
                  case 3: print(" Character support")

         case 8: print("Info service");
         case 9: print("Voice mailbox number"); 
         case 10: print("Service command"); 
            
                
   case 3: print('Chat')
   case 4: 
      print('Call register')
      call_register_menu = """
1.Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call cost 
7. Call cost settings
8. Prepaid credit
"""
      print(call_register_menu)
      call_register_prompt = input()
      match(call_register_prompt):
            case 1: print("Missed calls")
            case 2: print("Received calls")
            case 3: print("Dialled numbers")
            case 4: print("Erase recent call lists")
            case 5:
               print("Show call duration")
               Show_call_duration_menu = """
1. Last call duration
2. All calls duration
3. Received calls duration
4. Dialled calls duration
5. Clear timers
"""
               print(Show_call_duration_menu)
               Show_call_duration_menu  = input()
               match(Show_call_duration_menu ):
                  case 1: print("Last call duration")
                  case 2: print("All calls duration")
                  case 3: print("Received calls duration")
                  case 4: print("Dialled calls duration")
                  case 5: print("Clear timers")

            case 6:
               print(" Show call cost ")
               Show_call_cost_menu = """
1. Last call cost
2. All calls cost
3. Clear counters
"""
               print(Show_call_cost_menu)                                 
               show_call_cost_menu = input()
               match(Show_call_cost_prompt):
                  case 1: print("Last call cost")
                  case 2: print(" All calls cost")
                  case 3: print("Clear counters") 
            case 7:
               print("Call cost settings") 
               call_cost_setting_menu = """
1. Call cost limit
2. Show cost in                         
""" 
               print(Call_cost_settings) 
               call_cost_setting_prompt = input() 
               match(Call_cost_settings_prompt):
                  case 1: print(" Call calls cost") 
                  case 2: print(" Show cost in ")

            case 8: print("Prepaid credit")

   case 5:
      print('Tones')
      tones_menu = """
1. Ringing tone 
2. Ringing Volume
3. Incoming Call alert 
4. Message alert tone
5. Keypad tones
6. Warning tones 
7. Vibrating alert
8. Screen Saver  
"""
      print(Tones)
      tones_prompt = input()
      match(String_tones_prompt):
         case 1: print(" Ringing tone")
         case 2: print("Ringing Volume")
         case 3: print("Incoming Call alert")
         case 4: print("Message alert tone")
         case 5: print("Keypad tones")
         case 6: print(" Warning tones")
         case 7: print("Vibrating alert")
         case 8: printl("Screen Saver")

   case 6: 
      print('Settings')
      settings_menu = """
1. Call settings
2. Phone Settings
3. Security Settings
4. Restore factory settings
"""
      print(Settings)
      settings_menu = input()
      match(Settings_settings_prompt):
         case 1: 
            print("Call settings")
            call_setting_menu = """
1. Automatic redial
2. Speed dialling
3. Call wating options
4. Own number sending
5. Phone line in use 
6. Automatic answer
""" 
            print("Call settings")
            call_setting_menu = input () 
            match(call_Settings_prompt):
               case 1: print("Automatic redial");
               case 2: print("Speed Dialling"); 
               case 3: print("Call wating options")
               case 4: print("Own number sending")
               case 5: print("Phone line in use")
               case 6: print("Automatic answer")
                        
         case 2:
            print("phone_settings")
            phone_setting_menu = """
1. Language
2. Call info display
3. Welcome note 
4. Network selection  
5. Comfirm SIM service
"""
            print(phone_settings)
            phone_setting_prompt = input()
            match(phone_Setting_prompt):
               case 1: print("Language")
               case 2: print(" Call info display")
               case 3: print(" Welcome note")
               case 4: print("Network selection")
               case 5: print("Comfirm SIM service") 
         case 3: 
            print("Security_Settings")
            security_Setting_menu = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access code
"""
            print(Security_Settings)
            security_Setting_prompt = input()
            match( security_Setting_prompt):
               case 1: print("PIN code request")
               case 2: print("Call barring service")
               case 3: print("Fixed dialling")
               case 4: print("Closed user group")
               case 5: print("Settings level")
               case 6: print("Change access code")

         case 4: print("Restore factory settings")

   case 7: print("Call divert")         
   case 8:
         print('Music')
         music_menu = """

1. Music player
2. Radio
3. Recorder
4. Track lists
"""
         print(music_menu)
         music_prompt = input()
         match(Music_prompt):
            case 1: print("Music player")
            case 2: print("Radio")
            case 3: print("Recorder")
            case 4: print("Track lists")

   case 9: print('Game')
   case 10: print('Calculator')
   case 11: print('Reminders')      
   case 12: 
      print('Clock')
      clock_menu = """
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
"""
      printl(clock_menu)
      clock = int(input())
      match(clock):
         case 1: print("Alarm clock")
         case 2: print("Clock settings")
         case 3: print("Date settings")
         case 4: print("Stopwatch")
         case 5: print("Countdown timer")
         case 6: print("Auto update of ")
      
   case 13: print('Profiles')
   case 14: print('Services')
   case 15: print('SIM services')











   
