# check is user says yes / no
while True:

    want_instructions = input("Do you want to see instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes.")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no.")
        break
    else:
        print("please enter yes or no")
        continue

print("We done.")