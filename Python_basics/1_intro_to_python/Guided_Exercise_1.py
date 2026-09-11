print("\n Welcome to the Gamer Ranker, we are going to ask you some information to calculate your gamer level \n")
username = (input("Question 1: What's your username? \n"))
game_hours = int(input("\nQ2: \nHow much hours had you been playing?"))
play_ranks = (input("\nQ3: \nDo you play ranked matches?"))

print("\nThe result is:")
if game_hours < 10:
    print("You are a Noob")
elif game_hours < 50:
    print("You are a Casual Gamer")
elif game_hours < 200:
    print("You are a Active Gamer")
elif play_ranks == "yes":
    print("You are a Pro")
else:
    print("You are a Active Gamer")
print(f" \n{username}")