import random

def game_life(level):
  '''return game life'''
  if level == 'easy':
    life = 10
  elif level == 'hard':
    life = 5
  return life

def compare(guess, target):
  '''return str -> result'''
  if guess > target:
    return 'high'
  elif guess < target:
    return 'low'
  elif guess == target:
    return 'You got it! The answer was'

def main():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  target = random.randint(1, 100)
  life = game_life(level)
  print(f"You have {life} attempts remaining to guess the number.")

  while life:
    guess = int(input("Make a guess: "))
    result = compare(guess, target)
    if result == 'You got it! The answer was':
      print(f"{result} {guess}.")
      return
    else:
      life -= 1
      print("Too", result)
      if life:
        print("Guess again.")
        print(f"You have {life} attempts remaining to guess the number.")
      else:
        print("You've run out of guesses, you lose.")

if __name__ == '__main__':
  main()