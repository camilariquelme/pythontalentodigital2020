
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
		

cuenta_uno = BankAccount(1234, 0, 0.01)  #crear instancia
cuenta_dos = BankAccount(5678, 0, 0.01)

cuenta_uno.deposit(200).deposit(50).deposit(100).withdraw(50).display_account_info().yield_interest()
cuenta_dos.deposit(200).deposit(200).withdraw(250).withdraw(100).withdraw(100).withdraw(50).display_account_info().yield_interest()