class User:	
   bank_name = "First National Dojo"

   def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account_balance = 0

   # deposit
   def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
      self.account_balance += amount	# the specific user's account increases by the amount of the value received

   # withdrawal
   def make_withdrawal(self, amount):
      self.account_balance -= amount

   # display
   def display_user_balance(self):
      print(f"User: {self.name}, Balance {self.account_balance}")

   # transfer
   def transfer_money(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount
      print(f"{self.name} has transfered {amount} to {other_user.name}")
      print(f"{self.name} has a new balance of {self.account_balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
murphy = User("Murphy Merf", "murphy@merf.aol")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(25)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(25)
monty.display_user_balance()

murphy.make_deposit(1000)
murphy.make_withdrawal(100)
murphy.make_withdrawal(100)
murphy.make_withdrawal(40)
murphy.display_user_balance()

murphy.transfer_money(guido, 100)
