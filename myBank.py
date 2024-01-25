
#########################
# An example of a class #
#########################
import random

class yourBank(object):
  '''A demonstration of a class'''

  # an attribute to keep track of total number of accounts
  numb_accounts=0

  def __init__(self,name,balance):
    '''Class initialiser'''
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1

  # methods
  def deposit(self,amt):
    '''Adds an amount of money'''
    self.balance=self.balance+amt

  def withdraw(self,amt):
    '''Removes an amount of money'''
    self.balance=self.balance-amt

  def inquiry(self):
    '''Returns the current balance'''
    return self.balance
  
  def depoit_1000(self):
    self.balance=self.balance+1000

class evil(yourBank):

  def inquiry(self):
    num=random.randint(0,1)
    if num == 0:
      print(self.balance*1.2)
    else:
      print(self.balance)

# create insatace of a class
account1=yourBank('jiangjiang', 500)

# call a methoid within that class
account1.inquiry()


account2=evil('jiangjiang', 500)
account2.inquiry()