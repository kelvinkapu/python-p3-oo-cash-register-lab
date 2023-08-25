#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total= 0, items=[]):
    self.total =total
    self.items = []
    self.discount =discount
  
  def add_item(self,title,price,quantity=1):
    self.title = title
    self.price = price
    self.quantity = quantity
    self.items.extend([self.title] * self.quantity) 
    self.total = (self.price * self.quantity) + self.total
    return self.total
  
  def apply_discount(self):
    # self.discount=20
    self.total= self.total-((self.total*self.discount)/100)
    if self.discount > 0:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    # __dir__(float)
    else:
      print("There is no discount to apply.")
    return self.total
  
  def void_last_transaction(self):
      # if self.items:pytest
          # last_item = self.items[-1]
          x = self.price * self.quantity
          self.total =  (self.total-x)
          return self.total
          
    



    

  
  # def items_list(self):
    # new_list=[]
    # for items in new_list:
    #   new_list.append(self.title)
    #   self.items=new_list
    # return self.items
  #   for item in self.items:
  #     x=self.items.insert(-1,self.title)
  #   return x



 