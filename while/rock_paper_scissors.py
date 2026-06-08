import random
outcomes = ['rock','paper','scissors']
username = input('Enter your name: ')
while True:
    user_choice = input("Choose an option (rock, paper, or scissors): ")
    computer_choice = random.choice(outcomes)
    message = f"Computer choice: {computer_choice}"
    #rock
    if computer_choice == "rock":
        if user_choice == "paper":
            print(message)
            print(username, "Wins!")
            break
        elif user_choice == "scissors":
            print(message)
            print("computer Wins!")
            break

        elif user_choice == "rock":
            print(message)
            print("Draw! Try again...")
            continue
     #paper
    elif computer_choice == "paper":
        if user_choice == "rock":
            print(message)
            print("computer Wins!")
            break
        elif user_choice == "scissors":
            print(message)
            print(username, "Wins!")
            break
        elif user_choice == "paper":
            print(message)
            print("Draw! Try again...")
            continue
    #scissors
    elif computer_choice == "scissors":
        if user_choice == "paper":
            print(message)
            print("computer Wins!")
            break
        elif user_choice == "rock":
            print(message)
            print(username, "Wins!")
            break
        elif user_choice == "scissors":
            print(message)
            print("Draw! Try again...")
            continue