import random
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) 
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
# print(type(user_choose))
computer_choose = random.randint(0, 2)
if computer_choose == 0:
  final_computer_choose = rock
elif computer_choose == 1:
  final_computer_choose = paper
elif computer_choose == 2:
  final_computer_choose = scissors

if user_choose == 0:
  final_user_choose = rock
  if final_computer_choose == paper:
    result = "You lose"
  elif final_computer_choose == scissors:
    result = "You Win"
  else:
    result = "Draw" 
elif user_choose == 1:
  final_user_choose = paper
  if final_computer_choose == paper:
    result = "Draw"
  elif final_computer_choose == scissors:
    result = "You lose"
  else:
    result = "You Win"
elif user_choose == 2:
  final_user_choose = scissors
  if final_computer_choose == paper:
    result = "You Win"
  elif final_computer_choose == scissors:
    result = "Draw"
  else:
    result = "You lose"
else:
  print("Wrong number!!!")


print(final_user_choose)
print("Computer chose:")
print(final_computer_choose)
print(result)      