print ("Welcome to the ATM 🏧")

class ATM:
  def __init__(self):
    self.pin = ""
    self.balance = 0 
    self.menu()
    
  def menu(self):
    user_input = input('''\n Hello, How would you like to proceed?
    Enter 1 to create a PIN.
    Enter 2 to deposit.
    Enter 3 to withdraw.
    Enter 4 to check balance
    Enter 5 to exit.
    
    Enter you step here: ''')
    if user_input == "1":
      self.create_pin()
    elif user_input == "2":
      self.deposit()
    elif user_input == "3":
      self.withdraw()
    elif user_input == "4":
      self.balance_check()
    elif user_input == "5":
      print("EXIT")
      return
      
    else:
      self.menu()
  
  def create_pin(self):
    self.pin = input("Create your PIN: ")
    print("PIN created ✅")
    self.menu()
    
  def deposit(self):
    pin_check = input("Enter yor PIN: ")
    if self.pin == pin_check:
      print("Correct PIN")
      amount = int(input("Enter the deposit amount: "))
      self.balance = self.balance + amount
      print ("Deposit Successful 💰")
      self.menu()
    else:
      print("Incorrect PIN")
    self.menu()
  
  def withdraw(self):
    pin_check = input("Enter yor PIN: ")
    if self.pin == pin_check:
      print("Correct PIN")
      amount = int(input("Enter the withdrawal amount: "))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print("Withdrwal Successful")
      else:
        print("Insufficient balance")
    else:
      print("Incorrect PIN")
    self.menu()
    
  def balance_check(self):
    pin_check = input("Enter yor PIN: ")
    if self.pin == pin_check:
      print("Correct PIN")
      print(f"Your current balance is ${self.balance}")
    else:
      ("Incorrect PIN")
    self.menu()
  

atm = ATM()
