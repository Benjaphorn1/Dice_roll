
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below for testing puporses


while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break


    user_points = int(input("User points? "))
    comp_points = int(input("computer points? "))
    winner = input("who won? ")
    user_score = int(input("User Score: "))
    comp_score = int(input("Computer score? "))

    game_results = (f"Round 1: {rounds_played} User points: {user_points} | "
                    f"Computer points: {comp_points}, {winner} wins "
                    f"({user_score}|{comp_score})")

    game_history.append(game_results)

print("Game history")
for item in game_history:
    print(item)