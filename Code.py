import random

def roll():
    min_v = 1
    max_v = 6
    roll = random.randint(min_v,max_v)

    return roll
while True:
    players = int(input("Enter the number of players (2-4): "))
    if 2 <= players <= 4:
        break
    else:
        print("Must be between 2-4.")

max_score = 50
player_scores = [ 0 for i in range(players)]

while max(player_scores) < max_score:

    for player_i in range(players):
        print("\nPlayer number",player_i + 1, "turn has started!")
        print("Your total score is :",player_scores[player_i],"\n")
        current_score = 0

        while True:
            should_roll = input("Would u like to roll (y)?\t")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            
            print("Your current score : ",current_score)

        player_scores[player_i] += current_score
        print("Your total score is :",player_scores[player_i])

max_score = max(player_scores)
winning_i = player_scores.index(max_score)
print(f"Player {winning_i + 1} is the winner! with the score of : {max_score}")
        
    
