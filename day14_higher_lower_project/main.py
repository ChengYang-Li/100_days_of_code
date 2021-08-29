from art import logo, vs
from game_data import data
from replit import clear
import random


def compare(num1, num2):
  if num1 > num2:
    return 'A'
  else:
    return 'B'

def question():
  return random.choice(data)

score = 0
choose1 = question()

while True:
  clear()
  
  choose2 =  question()
  while choose2 == choose1:
    choose2 = question()
  
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}.")
  print(f"Compare A: {choose1['name']}, a {choose1['description']}, from {choose1['country']}.")
  print(vs)
  print(f"Against B: {choose2['name']}, a {choose2['description']}, from {choose2['country']}.")

  result = compare(choose1['follower_count'], choose2['follower_count'])
  # print("Pssssst: ", result)
  choose = input("Who has more followers? Type 'A' or 'B': ")

  if choose == result:
    score += 1
    choose1 = choose2
  else:
    break

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")