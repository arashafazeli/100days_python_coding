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

#Write your code below this line 👇
position_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice == 0:
  user_choice = position_list[0]
elif user_choice == 1 :
  user_choice = position_list[1]
elif user_choice == 2 :
  user_choice = position_list[2]
else:
  print("your typed an invalid number. ")

computer_choice = random.choice(position_list)
print(f"Your choice is {user_choice} and copmputer choice is{computer_choice}")
if user_choice == computer_choice :
  print("no winner, draw")
elif user_choice == rock and computer_choice == paper :
  print("computer is a winner")
elif user_choice == rock and computer_choice == scissors :
  print("you are a winner") 
elif user_choice == paper and computer_choice == rock :
  print("you are a winner")
elif user_choice == paper and computer_choice == scissors :
  print("computer is a winner")
elif user_choice == scissors and computer_choice == rock :
  print("computer is a winner")
elif user_choice == scissors and computer_choice == paper :
  print("you are a winner")

