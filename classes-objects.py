# Problem 1: Creating a Simple Class for a Student

# Create a Student class with the following attributes:

#     name (string): stores the student's name.
#     age (int): stores the student's age.
#     grade (float): stores the student's grade.

# The class should have a method display_info that prints out all the student's information in a readable format.

# Expected Output:
# Name: Alice
# Age: 20
# Grade: 88.5


class Student():
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age 
		self.grade = grade

	def display_info(self):
		print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")


student1 = Student("Alice", 20 , 88.5)
student1.display_info()


# Problem 2: Bank Account Class
# Create a BankAccount class with:

#     Attributes account_holder (string), balance (float), and account_number (string).
#     A method deposit(amount) that adds money to the balance.
#     A method withdraw(amount) that deducts money from the balance if there are sufficient funds, otherwise prints "Insufficient funds".

class BankAccount():
	def __init__(self, account_holder, balance ,account_number):
		self.account_holder = account_holder
		self.balance = balance
		self.account_number = account_number

	def deposit(self):
		new_amount = int(input("Enter the amount you want to deposit: "))
		self.balance += new_amount 
		print(f"Balance after deposit: {self.balance}")

	def withdraw(self):
		amount = int(input("Enter the amount you want to withdraw: "))
		if amount > self.balance:
			print("Insufficient funds")
		else:
			self.balance -= amount
			print(f"Balance after withrawal: {self.balance}")


account1 = BankAccount("John Doe", 1000, "123456789")
account1.deposit()
account1.withdraw()		
