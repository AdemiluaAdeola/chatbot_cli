#usr/bin/env python 3.10.12

"""
This project is made to simulate the USSD feature on phones
"""

import time
from bot import BotBackend

def chat():

    running = True

    name = input("Hi. Please enter your name to continue")

    baby = BotBackend(name)

    while running:
        print(baby.welcome_mess())
        choice = input("Pick between numbers 0 and 4")
        time.sleep(0.5)
        print("")
        print("Loading........")
        print("")


        time.sleep(2)

        if choice == "0":
            print("")
            running = False
        
        elif choice == "1":
            print("So you wanna book a ride")
            
        elif choice == "2":
            print("What typa appointment are you interested in?")

        elif choice == "3":
            print("A joke")

        elif choice == "4":
            print("lets play")

        else:
            print("Not within the given options")

chat()