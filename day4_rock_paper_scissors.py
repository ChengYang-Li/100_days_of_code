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
pool = [rock, paper, scissors]

choose = int(input("What di you chooese? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)

if choose == computer:
  print(f"{pool[choose]}\nComputer chose:\n{pool[computer]}\nIt's a draw")
elif choose - computer == 1 or choose - computer == -2:
  print(f"{pool[choose]}\nComputer chose:\n{pool[computer]}\nYou win")
else:
  print(f"{pool[choose]}\nComputer chose:\n{pool[computer]}\nYou lose")