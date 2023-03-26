import random

money = 80
meth = 2
bullets = 6
health = 100
medicine = 1
acetone = 0
phosphorous = 0

print("You sure have fucked up now. Gustavo needs his money.")
print("Because of you, he's out $11,575.")
print("You better get selling, and quick.")
print()
print("Press any key to continue...")
input()

def purchase (item, price):
  global money, medicine
  amount = int(input(f"How many {item}s would you like to buy? >"))
  cost = amount * price
  if money >= cost
      money -= cost
      if item == "bullets"
        bullets += amount
      elif item == "medicine"
        medicine += amount
      elif item == "acetone"
        acetone += amount
      elif item == "phophorous"
        phosphorous += amount
      print(f"You bought {amount} {item}s.")
    else:
      print("You need more money to purchase that many {item}s. One {item} costs ${price}.")

