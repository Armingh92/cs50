import random
from random import choice
names_list = ["a l b o r z", "b a r a n", "a r m i n", "a r s a l a n", "s a i n a"]
print(names_list)
name = choice(names_list)
alp = name.split()
creact_guess = []
wrong_guess = []
while True:
    for i in creact_guess:
        print(f"{i} is right")
    for i in wrong_guess:
        print(f"{i} is wrong")

    user_input = input("Enter your guess: ")
    if user_input in alp:
        creact_guess.append(user_input)
        continue
    elif user_input == name:
        print(f"congrats {user_input} is right!")
        break
    else:
        print("wrong")
        wrong_guess.append(user_input)
        continue