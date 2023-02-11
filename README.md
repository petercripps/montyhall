# montyhall
A Python program for investigating the Monty Hall problem.

The [Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem) problem is stated thus:

_Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?_

This program allows you to investigate the Monty Hall program in the following ways.

- You can play against the program, it randomly places a car and two goats behind doors and you select which one you think is the car. You can choose whether Monty gives you the choice of picking another door or not. The program keeps track of your selections and gives you a score at the end.
- You can also choose to run the program in auto mode for up to a maximum number of runs. Again, you can choose whether Monty allows the choice of picking another door or not. You can also auto select whether you choose to switch: you can always choose, never choose or choose at random.

How you play is decided by adjusting program variables set on the command line or via a YAML file called `config.yaml`.
- "monty" set to `True` for Monty to tell you one of the false options and give you option to change.
- "choose" set to `y` if you always want to choose Monty's choice when in auto mode. Set to `n` if you never want to select Monty's choice. Set to `r` if the choice is to be random.
- "auto" set to `True` for the computer to decide.
- "limit" the max number of guesses if in auto mode.
- "verbose" if `True` print additional info on how the programme is running.
- "timer" if `True` display the time if in `auto` mode for how long it takes to make number of guesses defined by `limit`.

To run the program type:

`python3 montyhall.py`

at a Python prompt. Change program variables via one of:
- -m set to `True` for Monty to give you a second guess, `False` otherwise.
- -c set to `y` if you want a second guess in auto mode, `r` to randomly guess or `n` for no second guess.
- -a set to `True` for auto mode, `False` otherwise.
- -l number defining the number of goes you can have.
- -v set to `True` for verbose mode, `False` otherwise.
- -t set to `True` to time number of runs, `False` otherwise.

Here are some typical results running this program one million times for each of the _choose_ options 'y', 'n' and 'r'.

`python3 montyhall.py -c 'y' -l 1000000`

`You guessed correctly 666,829 out of 1,000,000 times.`

`python3 montyhall.py -c 'n' -l 1000000`

`You guessed correctly 332,883 out of 1,000,000 times.`

`python3 montyhall.py -c 'r' -l 1000000`

`You guessed correctly 499,910 out of 1,000,000 times.`

So it would appear the strategy to win the car is always to change your guess when asked to do so. If you do the chance of winning is 2/3 as opposed to 1/3 if you don't. If you randomly change sometimes and not others odds are 1/2. Still don't believe this, see this video: https://www.youtube.com/watch?v=UgKrQ2ywVfs 