import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, resp1, resp2):
    while True:
        response = input(prompt).lower()
        if resp1 == response:
            break
        elif resp2 == response:
            break
        else:
            print_pause("Sorry, please try again.")
    return response


def intro():
    print_pause("You have just arrived at the train station!")
    print_pause("There's a robber and employee attacking people, so be cautious.")
    print_pause("You have your jiu jitsu to protect yourself.")
    print_pause("You're greeted by an employee of Starline Locomotives.")
    
    
def ride_catwalk():
    response = valid_input("Where would you like to go? "
                           "You can go to main car with 1 or passenger car with 2.\n",
                           "1", "2")
    if "1" == response:
        print_pause("You are your taken to main car!")
    elif "2" == response:
        print_pause("You are taken to passenger car!")
    else:
        print_pause("Sorry, please try again.")


def main_car(options):
    print_pause(f"{options} attacks you. ")     
    response = valid_input("Would you fight yes or no?\n",
                           "yes", "no")
    if "yes" == response:
        print_pause("You fight with your jiu jitsu and you win!")
    elif "no" == response:
        print_pause("You head back to catwalk!")
    else:
        print_pause("Sorry, please try again.")
    ride_catwalk()
    
    
def passenger_car():
    response = valid_input("You get your passport! "
                           "Would you like to be seated, yes or no?\n",
                           "yes", "no")
    if "yes" == response:
        print_pause("You are your seated and win the game!")
        play_again()
    elif "no" == response:
        print_pause("You head back to catwalk!")
    else:
        print_pause("Sorry, please try again.")
        
    
def play_again():
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" == response:
        print_pause("OK, thank you and goodbye!")
    elif "yes" == response:
        print_pause("Good job, I'm happy to start the game again.")
        play_traingame()
    else:
        print_pause("Sorry, please try again.")


def play_traingame():
    options = random.choice(["robber", "employee"])
    intro()
    ride_catwalk()
    main_car(options)
    passenger_car()

    
play_traingame()
  