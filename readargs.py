########################################################################
# readargs.py
# Read the arguments from the command line. Arguments not provided will
# be taken from the config file config.yaml.
# Note that this uses Python's new 'match' statement which has only been
# available from v3.10. Ensure you have that version or later installed.
########################################################################

import sys
import config

# Reads a list of arguments or, if none, a file in yaml format.
# Parameters:
#   args : List - The command line arguments 
# Returns:
#   None 
def read_args(args):
    if len(args) == 1:
        print("No arguments provided so using YAML file")
        return
    
    # start looking at parameters from first argument
    i = 1
    # read arguments
    try:
        while i < len(args):
            match args[i]:     
                case '-m':
                    val = args[i + 1].capitalize()
                    config.configdict["monty"] = (val == "True")
                    i += 1
                case '-a':
                    val = args[i + 1].capitalize()
                    config.configdict["auto"] = (val == "True")
                    i += 1
                case '-l':
                    config.configdict["limit"] = int(args[i + 1])
                    i += 1
                case '-v':
                    val = args[i + 1].capitalize()
                    config.configdict["verbose"] = (val == "True")
                    i += 1
                case '-c':
                    val = args[i + 1].lower()
                    if val == 'y' or val == 'n' or val == 'r':
                        config.configdict["choose"] = val
                    else:
                        print(f"ERROR Unknown parameter {args[i+1]} to argument {args[i]}")
                    i += 1    
                case _:
                    print(f"ERROR Unknown argument {args[i]}")
            i += 1    
    except IndexError:
        print("ERROR Invalid or missing argument")

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if True:
        read_args(sys.argv)
        print(config.configdict)