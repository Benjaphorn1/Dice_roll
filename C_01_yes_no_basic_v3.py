
# function starts here

def yes_no(question):

    """ checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")
            continue

def instructions():
    """prints instructions"""

    print(""""
 *** Instructions ***
 
 Roll the dice and try to win!   
    """)


# main routine starts here

# ask user if they want instructions
want_instructions = yes_no("Do you want to see instructions? ")

#if user says yes display instructions
if want_instructions == "yes":
    instructions()

print()
print("Program continues")



