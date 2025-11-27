# ===============================
# 1. Encapsulation
# ===============================

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1
print(f"account Balance: {account.balance}")


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
  # No setter property provided [Encapsulation]  
    def deposite(self , amount):
        if amount <= 0:
            raise ValueError("Deposited amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount >= 0:
            if amount >= self._balance:
                raise ValueError("Insuffiicient Balance")
            self._balance -= amount

account = BankAccount()

print(account.balance)
account.deposite(1.99)
print(account.balance)
account.withdraw(1.00)
print(account.balance)


# ===============================
# 2. Abstraction
# ===============================

class EmailService:

    def _connect(self):
        print(f"Connecting to email Server...")
    
    def _authenticate(self):
        print(f"Authenticating...........")
    
    def _disconnect(self):
        print(f"disconnecting...........")

    def send_email(self, content):
        self._connect()
        self._authenticate()
        print(f"Sending Email : {content} ")
        self._disconnect()

email = EmailService()
email.send_email(content= "jai ho bhaiya ji jai hooooo")

# CREATE A TABULAR VISUALISATION OF MAJOUR DIFFERANCES BETWEEN ENCAPSULATIION AND ABSTRACTION
# here....


# ===============================
# 3. Inheritance
# ===============================

class Vehical:
    def __init__(self,brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"************ Vehical Started **********")
    
    def stop(self):
        print(f"************ Vehical Stoped **********")

class Car(Vehical):
    def __init__(self, brand , model , year , number_of_doors, number_of_weels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_weels = number_of_weels

class Bike(Vehical):
    def __init__(self , brand, model, year, number_of_weels):
        super().__init__(brand, model, year)
        self.number_of_weels = number_of_weels


car1 = Car("Ford","Focue", 1979,8,8)
bike1 = Bike("honda" , "Xtream",2025,2)
print(car1.__dict__)