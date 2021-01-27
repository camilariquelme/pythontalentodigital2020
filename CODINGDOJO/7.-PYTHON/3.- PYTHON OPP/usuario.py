class usuario:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0
        

    def make_deposit(self,amount):
        self.account_balance+=amount

    def make_withdrawal(self,cantidad):
        self.account_balance -= cantidad

    def transfer_money (self, otro_usuario, cantidad):
        self.account_balance -= cantidad

    def display_user_balance(self):
        
        
        


guido =usuario("Guido Rojas", "guidor@gmail.com")
monty= usuario("Monty Damon","MontyDa@gmail.com")
carlos = usuario("Carlos Orellana","CarlosO@gmail.com")

guido.make_deposit(100)
guido.make_deposit(200)
carlos.make_deposit(1000)
monty.make_deposit(50)
carlos.transfer_money(monty,500)
print('saldo', carlos.account_balance)
print('saldo', monty.account_balance)
