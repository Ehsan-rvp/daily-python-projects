import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[your_choice])
print(f"Computer chose:\n{game_image[computer_choice]}")
# orders
if your_choice == 0 and computer_choice == 0:
    print("Draw!")
elif your_choice == 0 and computer_choice == 1:
    print("You lose!")
elif your_choice == 0 and computer_choice == 2:
    print("You won!")
elif your_choice == 1 and computer_choice == 0:
    print("You won!")
elif your_choice == 1 and computer_choice == 1:
    print("Draw!")
elif your_choice == 1 and computer_choice == 2:
    print("You lose!")
elif your_choice == 2 and computer_choice == 0:
    print("You lose!")
elif your_choice == 2 and computer_choice == 1:
    print("You won!")
elif your_choice == 2 and computer_choice == 2:
    print("Draw!")
