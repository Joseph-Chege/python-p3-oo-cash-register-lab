#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    #Setting instance variables to respective defaults
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quantity=1):
    #Adding the item to the list of items
    for _ in range(quantity):
      self.items.append(title)
    #Adding the price of the item to the total
    self.total += price * quantity
    self.last_transaction = price * quantity

  def apply_discount(self):
    #Checking if there is a discount
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      #Applying the discount to the total
      self.total -= int(self.total * self.discount / 100)
      print(f"After the discount, the total comes to ${self.total}.")
      
  def items(self):
    #Returning the list of items
    return self.items
  
  def void_last_transaction(self):
    #Subtracting the last item from the total
    self.total -= self.last_transaction
    self.items = self.items[:-1]

  
  


  pass
