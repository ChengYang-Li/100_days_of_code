from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

nobody = False
bidder_dict = {}

while not nobody:
  name = input("What is your name?: ")
  money = int(input("What is your bid?: $"))

  bidder_dict[money] = name

  another = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if another == "yes":
    clear()
  elif another == 'no':
    nobody = True
    winner = bidder_dict[max(bidder_dict)]
    print(bidder_dict)
    print(f"The winner is {winner} with a bid of ${max(bidder_dict)}")

