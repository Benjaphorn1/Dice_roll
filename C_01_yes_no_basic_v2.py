
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

# main routine starts here

want_instructions = yes_no("Do you want to see instructions? ").lower()
want_coffee = yes_no("Do you want coffee? ")
print("We done")