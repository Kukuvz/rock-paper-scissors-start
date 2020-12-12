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
import random
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) 
# print(type(user_choose))
computer_choise = random.randint(0, 2)
if computer_choise == 0:
  final_computer_choise = rock
elif computer_choise == 1:
  final_computer_choise = paper
elif computer_choise == 2:
  final_computer_choise = scissors

if user_choise == 0:
  final_user_choise = rock
  if final_computer_choise == paper:
    result = "You lose"
  elif final_computer_choise == scissors:
    result = "You Win"
  else:
    result = "Draw" 
elif user_choise == 1:
  final_user_choise = paper
  if final_computer_choise == paper:
    result = "Draw"
  elif final_computer_choise == scissors:
    result = "You lose"
  else:
    result = "You Win"
elif user_choise == 2:
  final_user_choise = scissors
  if final_computer_choise == paper:
    result = "You Win"
  elif final_computer_choise == scissors:
    result = "Draw"
  else:
    result = "You lose"
else:
  print("Wrong number!!!")


print(final_user_choise)
print("Computer chose:")
print(final_computer_choise)
print(result)      