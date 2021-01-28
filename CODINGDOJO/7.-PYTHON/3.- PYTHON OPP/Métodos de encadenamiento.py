class usuario:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0
        

    def make_deposit(self,amount):
        self.account_balance+=amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def transfer_money (self, otro_usuario, amount):
        self.account_balance -= amount
        otro_usuario.account_balance += amount
        return self

    def display_user_balance(self):
        print("User: ", self.name, ", ", "Total cuenta: ", self.account_balance)

        
        



monty = usuario("Monty Damon","MontyDa@gmail.com")
carlos = usuario("Carlos Orellana","CarlosO@gmail.com")
rodrigo = usuario("Rodrigo Riquelme", "rodri@gmail.com")

monty.make_deposit(200).make_deposit(200).make_deposit(50).make_deposit(200).display_user_balance()


carlos.make_deposit(300).make_deposit(500).make_withdrawal(50).make_withdrawal(50).display_user_balance()

rodrigo.make_deposit(1000).make_withdrawal(150).make_withdrawal(150).make_withdrawal(100).display_user_balance()


monty.transfer_money(rodrigo,200).display_user_balance()

rodrigo.display_user_balance()