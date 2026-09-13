#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = [] 
    self.previous_transactions = []


  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    # checks if the discount is and in and between 0 and 100 inclusive
    if isinstance(discount, int) and 0 <= discount <= 100:
      self._discount = discount
    else: 
      print("Not valid discount")

  def add_item(self, item, price, quantity=0):
    if quantity <= 0:
      self.total = self.total + price
      self.items.append(item)
    else:
      self.total = self.total + (price * quantity)
      # appends the items based on the quantity if it's greater than zero
      for _ in range(quantity):
        self.items.append(item)


    new_transaction = {
      "item": item, 
      "price": price, 
      "quantity": quantity
    }

    self.previous_transactions.append(new_transaction)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else: 
      # calculate discount
      self.total = self.total - (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
    if len(self.previous_transactions) == 0:
          print("There is no transaction to void.")
    else: 
      prev_trans = self.previous_transactions.pop() # store the popped transaction in a variable to update the total
      if prev_trans["quantity"] == 0:
        self.total = self.total - prev_trans["price"]
      else: 
        self.total = self.total - (prev_trans["price"] * prev_trans["quantity"])
