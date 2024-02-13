import pywhatkit
from art import *


def banner_printer():
    # Print the banner using the text2art library
    banner = text2art("WHATs_SENDER")
    print(banner)
    print("The program to automate your whatsapp messages. All you have to do is follow the instructions provided. Happy surfing :)")


def send_message(phone_number,message_to_send, hour, minutes):
    pywhatkit.sendwhatmsg(phone_number,message_to_send,hour,minutes)

#def schedule_sender():
#    return

def main():
    print()
    print()
   
    print("1-) Schedule one person message")
    print("2-) Schedule multiple persons message (it'll be sent separately)")
    print("0-) Quit")
    user_choice = int(input("Select a number : "))

    if user_choice == 0:
        quit
    elif user_choice == 1:
        PHONE_NUMBER = input("Input the phone number Ex: +212642658974 : ")
        SENT_TIME = input("When do you want to send the message (Format HH:MM) : ")
        try:
            hour = int(SENT_TIME.split(':')[0])
            minutes = int(SENT_TIME.split(':')[1])
            print(f"Sent  TIME {hour} : {minutes}")
        except Exception as e:
            print("The provided time is incorrect ! Please try again ")
            main()
        
        SENT_MESSAGE = input("What do you want to send : ")
        
        send_message(PHONE_NUMBER,SENT_MESSAGE,hour,minutes)

    elif user_choice == 2:
        print("Now, you have to add the list of the phone numbers, you want to write to")
        cellphone_input = input("Please Provide the list of cellphone comma separated Ex: +212645375984,+212654987821 : ")
        cellphone_list = cellphone_input.split(',')

        SENT_TIME = input("When do you want to send the message (Format HH:MM) : ")
        try:
            hour = int(SENT_TIME.split(':')[0])
            minutes = int(SENT_TIME.split(':')[1])
        except Exception as e:
            print("The provided time is incorrect ! Please try again ")
            main()

        SENT_MESSAGE = input("What do you want to send : ")

        latence = 0
        # the messages will be sent with one minute interval
        for phone in cellphone_list:
            send_message(phone,SENT_MESSAGE,hour,minutes + latence)
            latence += 1
       
    else:
        print("The provided input is incorrect. Please follow the instructions !!!")
        main()

if __name__ == "__main__":
    banner_printer()
    main()
