# montyhall
Python program for investigating the Monty Hall problem

The [Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem) problem is stated thus:

_Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?_

This program allows you to investigate the Monty Hall program in the following ways.

- You can play against the program, it randomly places a car and two goats behind doors and you select which one you think is the car. You can choose whether Monty gives you the choice of picking another door or not. The program keeps track of your selections and gives you a score at the end.
- You can also choose to run the program in auto mode for up to a maximum number of runs. Again, you can choose whether Monty allows the choice of picking another door or not. You can also auto select whether you choose to, you can always choose, never choose or choose at random.

How you play is set via adjusting these constants for a given set of runs. Defaults are in brackets.
- MONTY (False). Set to True for Monty to tell you one of the False options and give you the option to change.
- ALWAYSCHOOSE ('n'). Set to 'y' if you always want to choose Monty's choice when in AUTO mode. Set to 'r' if the choice is to be random.
- AUTO (False). Set to True for the computer to decide.
- AUTOLIMIT (10). Max number of guesses if in auto mode.
- VERBOSE (False). If True print additional info on how the programme is running.

These can be set by adjusting in the program before a run.

To run the program type:

`python3 montyhall.py`

at a Python prompt.

Here are some typical results running this program one million times for each of the ALWAYSCHOOSE options 'y', 'n' and 'r'.

ALWAYSCHOOSE = 'y'            
_You guessed correctly 666829 out of 1000000 times._
ALWAYSCHOOSE = 'n'
_You guessed correctly 332883 out of 1000000 times._
ALWAYSCHOOSE = 'r'
_You guessed correctly 499910 out of 1000000 times._