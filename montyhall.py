# Python program for investigating the Monty Hall problem, see description here https://en.wikipedia.org/wiki/Monty_Hall_problem
import random
import sys
from timeit import default_timer as timer
import config
from readargs import read_args

# Control variables are in the config.yaml or can be passed via command line arguments
# "monty" set to True for Monty to tell you one of the false options and give you option to change
# "choose" set to 'y' if you always want to choose Monty's choice when in auto mode. Set to 'r' if the choice is to be random
# "auto" set to True for the computer to decide
# "limit" the max number of guesses if in auto mode
# "verbose" if True print additional info on how the programme is running

DOORSPERLINE = 10 # No. of doors to print per line

# Print the doors as a an array of 'num' items per line 
def print_doors(doors, num):
    i = 0
    while i < len(doors):
        print(doors[i:i+num])
        i += 10

# Main program that runs the Monty Hall simulator. 
# All arguments are set in the global dictionary: 'config.configdict' 
def run_mh_simulator():
    results = [0,0] # count of guesses, [0] for correct guesses [1] for incorrect
    playing = True # keep prompting for user inputs while this is True
    count = 0 # count of guesses when in auto mode will stop when limit reached
    start_time = timer() # timer for auto mode
    numdoors = config.configdict["doors"] # the number of doors to play with
    
    # check the number of doors is between 3 and 100.
    if numdoors < 3 or numdoors > 100:
        print("Number of doors must be between 3 and 100.")
        return
    # start the simulator
    while (playing):
        # randomly set the car door number (1 - numdoors)
        car_door = random.randint(1,numdoors)
        # initially hide what is behind all doors with a '?'
        all_doors = ['?'] * numdoors
        # show the number of closed doors (if not in auto)
        if not config.configdict["auto"]:
            print_doors(all_doors, DOORSPERLINE)
        if config.configdict["verbose"]:
            print(f"Randomly chosen car door is {car_door}")
        # if in auto mode choose a random door
        if config.configdict["auto"]:
            count += 1
            if count > config.configdict["limit"]:
                choice = 0
            else:
                choice = random.randint(1,numdoors)
        else:
            # not in auto so prompt to choose one of the doors 
            # (must convert input from a string to an int)
            try:
                choice = int(input(f"Enter your choice 1 - {numdoors} or 0 to stop."))
            except:
                print(f"Invalid input. Must be a number in the range 1 - {numdoors}")
                choice = 0
        if choice == 0:
            #  stop playing
            playing = False
        else:
            # check choice is in range 1 - numdoors
            if (choice >= 1 and choice <= numdoors):
                if config.configdict["monty"]:
                    # let Monty select one of the goat doors, first set auto choose option
                    if config.configdict["auto"]:
                        if config.configdict["choose"] == 'r':
                            # make choice randomly
                            if random.randint(0,1) == 0:
                                ans = 'n'
                            else:
                                ans = 'y'
                        else:
                            ans = config.configdict["choose"]
                    # did they already choose the car?
                    if choice == car_door:
                        # Monty randomly selects one of the goat doors
                        montys_choice = random.randint(1,numdoors)
                        while (montys_choice == car_door):
                            # repeat until door selected is not the car door
                            montys_choice = random.randint(1,numdoors)
                        if config.configdict["verbose"]: 
                            print(f"Monty's choice is {montys_choice}")
                        # show what's behind all doors apart from chosen one (which is the car door)
                        # and Monty's selected door
                        i = 0
                        while i < numdoors:
                            if (i != car_door-1) and (i != montys_choice-1):
                                all_doors[i] = 'G'
                            i += 1                                
                        if not config.configdict["auto"]:
                            print_doors(all_doors, DOORSPERLINE)
                            ans = input(f"Do you want to choose door {montys_choice} instead? (y/n)")
                        if ans == 'y':
                            choice = montys_choice
                    else:
                        # have already chosen one of the goat doors so Monty must choose 
                        # another goat door at random
                        montys_choice = random.randint(1,numdoors)
                        while (montys_choice == choice) or (montys_choice == car_door):
                            # repeat until Montys choice is not the one chosen or the car door
                            montys_choice = random.randint(1,numdoors)
                        if config.configdict["verbose"]: 
                            print(f"Monty's choice is {montys_choice}")   
                        # show what's behind all doors apart from the car door and the chosen door
                        i = 0
                        while i < numdoors:
                            all_doors[i] = 'G'
                            i += 1
                        # now hide the car door and one currently chosen
                        all_doors[car_door-1] = '?'
                        all_doors[choice-1] = '?'        
                        if not config.configdict["auto"]:
                            print_doors(all_doors, DOORSPERLINE)
                            ans = input(f"Do you want to choose door {car_door} instead? (y/n)")
                        if ans == 'y':
                            choice = car_door
                # check if they chose well, only print results if not in AUTO mode
                i = 0
                while i < numdoors:
                    all_doors[i] = 'G'
                    i += 1
                all_doors[car_door-1] = 'C'
                if choice == car_door:
                    if not config.configdict["auto"]:
                        print_doors(all_doors, DOORSPERLINE)
                        print("Congratulations, you got the car.")
                    results[0] = results[0] + 1
                else:
                    if not config.configdict["auto"]:
                        print_doors(all_doors, DOORSPERLINE)
                        print("Bad luck, you got a goat.")
                    results[1] = results[1] + 1
            else:
                print(f"Invalid choice: {choice}.")
    print(f"You guessed correctly {results[0]:,d} out of {results[0]+results[1]:,d} times.")
    if config.configdict["auto"] and config.configdict["timer"]:
        print(f"Elapsed time {timer()-start_time} seconds.")

############################
# Main program starts here #
############################
if __name__ == "__main__":
    print("Monty Hall Simulator")
    print("by Peter Cripps")
    print("Version 2.0")
    # read the command line arguments
    read_args(sys.argv)
    if config.configdict["verbose"]:
        print(config.configdict)
    # run the main program
    run_mh_simulator()