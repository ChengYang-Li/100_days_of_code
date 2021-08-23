import art
from replit import clear

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

def calculator():
  print(art.logo)
  continue_flag = True

  num1 = float(input("what's the first number? "))
  for _ in operations:
    print(_)
  operator = input("Pick an operation from the line above: ")
  num2 = float(input("what's the second number? "))

  answer = operations[operator](num1, num2)
  print(f"{num1} {operator} {num2} = {answer}")

  while continue_flag:
    flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if flag == 'n':
      continue_flag = False
      clear()
      calculator()
    else:
      operator = input("Pick an operation: ")
      num2 = float(input("what's the next number: "))
      num1 = answer
      answer = operations[operator](num1, num2)
      print(f"{num1} {operator} {num2} = {answer}")

calculator()