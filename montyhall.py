# Python program for investigating the Monty Hall problem, see description here https://en.wikipedia.org/wiki/Monty_Hall_problem
import random

# Control variables
MONTY = False # set to True for Monty to tell you one of the False options and give you option to change
ALWAYSCHOOSE = 'n'  # set to 'y' if you always want to choose Monty's choice when in AUTO mode. Set to 'r' if the choice is to be random
AUTO = False # set to True for the computer to decide
AUTOLIMIT = 10 # max number of guesses if in auto mode
VERBOSE = False # if True print additional info on how the programme is running

def run_mh_simulator():
    results = [0,0] # count of guesses, [0] for correct guesses [1] for incorrect
    playing = True # keep prompting for user inputs while this is True
    count = 0 # count of guesses when in auto mode will stop when AUTOLIMIT reached
    
    while (playing):
        # randomly set the car door number (1 - 3)
        car_door = random.randint(1,3)
        # set goat door numbers i.e. to numers which are not the car door number
        goat_doors = [0,0]
        door = 1
        i = 0
        while door <= 3:
            if car_door != door:
                goat_doors[i] = door
                i += 1
            door += 1
        if VERBOSE:
            print(f"Car door is: {car_door}.")
            print(f"Goat doors are: {goat_doors}.")
        # Get the guessers choice or auto choose
        if AUTO:
            count += 1
            if count > AUTOLIMIT:
                choice = 0
            else:
                choice = random.randint(1,3)
        else:
            # request to choose one of the options (must convert input from a string to an int)
            choice = int(input("Enter your choice 1 - 3 or 0 to stop."))
        if choice == 0:
            #  stop playing
            playing = False
        else:
            # check choice is in range 1 - 3
            if (choice >= 1 and choice <= 3):
                if MONTY:
                    # let Monty select one of the goat doors, first set auto choose option
                    if AUTO:
                        if ALWAYSCHOOSE == 'r':
                            # make choice randomly
                            if random.randint(0,1) == 0:
                                ans = 'n'
                            else:
                                ans = 'y'
                        else:
                            ans = ALWAYSCHOOSE
                    # did they already choose the car?
                    if choice == car_door:
                        # randomly choose one of the goat doors
                        goat_door_index = random.randint(0,1)
                        if goat_door_index == 0:
                            other_door_index = 1
                        else:
                            other_door_index = 0
                        if not AUTO:
                            ans = input(f"Door {goat_doors[goat_door_index]} has a goat behind it, do you want to choose door {goat_doors[other_door_index]} instead? (y/n)")
                        if ans == 'y':
                            choice = goat_doors[other_door_index]
                    else:
                        # have chosen one of the goat doors so give them the option of choosing other goat door
                        if goat_doors[0] == choice:
                            goat_door_index = 1
                        else:
                            goat_door_index = 0
                        if not AUTO:
                            ans = input(f"Door {goat_doors[goat_door_index]} has a goat behind it, do you want to choose door {car_door} instead? (y/n)")
                        if ans == 'y':
                            choice = car_door
                # check if they chose well, only print results if not in AUTO mode
                if choice == car_door:
                    if not AUTO:
                        print("Congratulations, you got the car.")
                    results[0] = results[0] + 1
                else:
                    if not AUTO:
                        print("Bad luck, you got a goat.")
                    results[1] = results[1] + 1
            else:
                print("Invalid choice: {choice}.")
    print(f"You guessed correctly {results[0]} out of {results[0]+results[1]} times.")

############################
# Main program starts here #
############################
if __name__ == "__main__":
    # Set some variables.
    VERBOSE = True
    AUTO = True
    AUTOLIMIT = 5
    ALWAYSCHOOSE = 'r'
    MONTY = True
    if VERBOSE:
        print(f"AUTO: {AUTO}, AUTOLIMIT: {AUTOLIMIT}, ALWAYSCHOOSE: {ALWAYSCHOOSE}, MONTY: {MONTY}")
    # Run the main program
    run_mh_simulator()