from replit import clear
import random
import art


def init(cards):
  init_dict = {}
  init_dict["user_init"] = [random.choice(cards) for _ in range(2)]
  init_dict["dealer_init"] = [random.choice(cards) for _ in range(2)]
  if init_dict["user_init"] == [11, 11]:
    init_dict["user_init"] = [11, 1]
  if init_dict["dealer_init"] == [11, 11]:
    init_dict["dealer_init"] = [11, 1]
  init_dict["user_score"] = sum(init_dict["user_init"])
  init_dict["dealer_score"] = sum(init_dict["dealer_init"])
  print(f"Your cards: {init_dict['user_init']}, current score: {init_dict['user_score']}")
  print(f"Computer's first card: {init_dict['dealer_init'][0]}")
  return init_dict

def user_round(init_dict, cards):
  user_list = init_dict["user_init"]
  sum_score = random.choice(cards)
  if sum_score == 11:
    if sum(user_list) + sum_score > 21:
      sum_score = 1
  user_list.append(sum_score)
  init_dict["user_init"] = user_list
  init_dict['user_score'] = sum(user_list)
  print(f"Your cards: {init_dict['user_init']}, current score: {init_dict['user_score']}")
  print(f"Computer's first card: {init_dict['dealer_init'][0]}")
  return init_dict

def dealer_round(init_dict, cards):
  while sum(init_dict['dealer_init']) < 17:
    dealer_list = init_dict['dealer_init']
    sum_score = random.choice(cards)
    if sum_score == 11:
      if sum(dealer_list) + sum_score > 21:
        sum_score = 1
    dealer_list.append(sum_score)
    init_dict['dealer_init'] = dealer_list
    init_dict['dealer_score'] = sum(dealer_list)
  return init_dict

def result(init_dict):
  user_score = init_dict['user_score']
  dealer_score = init_dict['dealer_score']
  print(f"Your final hand: {init_dict['user_init']}, final score: {user_score}")
  print(f"Computer's final hand: {init_dict['dealer_init']}, final score: {dealer_score}")
  if len(init_dict['user_init']) == 2 and user_score == 21:
    if dealer_score == 21:
      print("Draw 🙃")
    else:
      print("Win with a Blackjack 😎")
  elif len(init_dict['dealer_init']) == 2 and dealer_score == 21:
    print("Lose, opponent has Blackjack 😱")
  else:
    if user_score <= 21:
      if dealer_score <= 21:
        if user_score > dealer_score:
          print("You win 😃")
        elif user_score < dealer_score:
          print("You lose 😤")
        elif user_score == dealer_score:
          print("Draw 🙃")
      elif dealer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > 21:
      if dealer_score <= 21:
        print("You went over. You lose 😭")
      elif dealer_score > 21:
        print("You went over. You lose 😤")
  
  main() 

def main():
  options = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if options == 'y':
    clear()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(art.logo)
    
    init_dict = init(cards)
    
    while sum(init_dict["user_init"]) < 21 and sum(init_dict["dealer_init"]) < 21:
      get_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if get_card == 'y':
        init_dict = user_round(init_dict, cards)
      else:
        break

    init_dict = dealer_round(init_dict, cards)    
    result(init_dict)
  else:
    print("really don't play?!")

if __name__ == "__main__":
  main()
