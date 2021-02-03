class usuario:
    def __init__(self, username, email, account_number):
        self.name = username
        self.email = email 
        self.bank_account = BankAccount(account_number,0,0.01)    #instancia de Bankaccount


class BankAccount:
	def __init__(self, account_number, balance, tasa_interes):
            self.account_number = account_number
            self.balance = balance
            self.tasa_interes = tasa_interes

	def deposit(self, amount):
            self.balance+= amount
            return self
	def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Saldo Insuficiente: se cobra una tarifa de $5")
                self.balance -= 5
            return self
		
	def display_account_info(self):
            print("cuenta: ", self.account_number, ", ", "Saldo: ", self.balance)
            return self
		
	def yield_interest(self):
            if self.balance>0:
                self.balance += self.balance * self.tasa_interes
            else:
                self.balance = self.balance
            return self.balance
		
monty = usuario("Monty Damon","MontyDa@gmail.com",1)
carlos = usuario("carlos","C@gmail.com",2)


monty.bank_account.deposit(200).display_account_info()



