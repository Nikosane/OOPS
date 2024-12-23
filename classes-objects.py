# Problem 1: Creating a Simple Class for a Student

# Create a Student class with the following attributes:

#     name (string): stores the student's name.
#     age (int): stores the student's age.
#     grade (float): stores the student's grade.

# The class should have a method display_info that prints out all the student's information in a readable format.

# Create a student object
# student1 = Student("Alice", 20, 88.5)
# student1.display_info()

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

# Create a bank account object
# account1 = BankAccount("John Doe", 1000, "123456789")
# account1.deposit(500)
# account1.withdraw(200)
# account1.withdraw(2000)

# Expected Output:
# Balance after deposit: 1500
# Balance after withdrawal: 1300
# Insufficient funds

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

# Problem 3: Rectangle Class with Area and Perimeter

# Create a Rectangle class with:

#     Attributes length and width.
#     Methods area() and perimeter() that calculate and return the area and perimeter of the rectangle, respectively.

class Rectangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		area = self.length * self.width
		print(f"Area: {area}")

	def perimeter(self):
		print(f"Perimeter: {2*(self.length + self.width)}")

rect1 = Rectangle(4,5)
rect1.area()
rect1.perimeter()

# Problem 4: Library and Book Classes

# Create a simple model for a library system using two classes: Library and Book.

#     Book: Each book should have:
#         Attributes title, author, isbn, and status (e.g., "available" or "borrowed").
#         A method display_details() to print out book information.
#         A method borrow() that sets the status to "borrowed" if the book is available, otherwise prints "Book is already borrowed."
#         A method return_book() that sets the status to "available".

#     Library: The library should manage a collection of books with:
#         An attribute books that holds a list of Book objects.
#         Methods add_book(book) to add a new book to the collection, remove_book(isbn) to remove a book by its ISBN, and display_books() to display details of all books.

book_list = [
    {"title": "1984", "author": "George Orwell", "isbn": "12345", "status": "available"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "67890", "status": "available"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "11223", "status": "available"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "33445", "status": "available"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "55667", "status": "available"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "77889", "status": "available"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "isbn": "99001", "status": "available"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "isbn": "22334", "status": "available"},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "isbn": "44556", "status": "available"},
    {"title": "Moby Dick", "author": "Herman Melville", "isbn": "66778", "status": "available"}
]

class Book:
	def __init__(self ,title, author, isbn=None, status="available"):
		self.title = title
		self.author = author
		self.isbn = isbn
		self.status = status

	def display_details(self):
		print(f"title: {self.title},author: {self.author},isbn: {self.isbn}")

	def borrow(self):
		if self.status == "available":
			self.status = "borrowed"
			print(f"{self.title} has been borrowed")


	def return_book(self):
		if self.status == "borrowed":
			self.status = "available"
			print(f"{self.title} has been returned")
		else:
			print(f"{self.title} is already available")	
			
			
class Library:
	def __init__(self):
		self.books = []

	def add_book(self, book):
		if book not in self.books:
			self.books.append(book)
			print(f"{book.title} has been added to Library")
		else:
			print(f"{book.title} is already there in Library")

	
	def remove_book(self, book):
		if book in self.books:
			self.books.remove(book)
			print(f"{book.title} has been removed from the Library")

	def display_books(self):
		if not self.books:
			print("no books in the library")
		else:
			for book in self.books:
				book.display_details()




book1 = Book("1984","George Orwell")
library = Library()
library.add_book(book1)

# Problem: Online Shopping Cart

# Create a basic online shopping cart system where users can add products, view their cart, and calculate the total price. There are three classes to implement:
# 1. Product class

#     Attributes:
#         name (str): The name of the product
#         price (float): The price of the product
#         quantity (int): The quantity of this product added to the cart

#     Methods:
#         display_product(): Prints the product's name, price, and quantity.

# 2. CartItem class

#     Attributes:
#         product (Product): A product instance associated with the cart item
#         quantity (int): Quantity of the product in the cart

#     Methods:
#         item_total(): Returns the total price for this item based on its price and quantity.

# 3. ShoppingCart class

#     Attributes:
#         items (list): A list of CartItem objects

#     Methods:
#         add_item(product, quantity): Adds a CartItem to the cart with the specified quantity.
#         view_cart(): Displays all items in the cart with their quantities and individual total prices.
#         calculate_total(): Calculates and returns the total price for all items in the cart.

# Example Usage

#     Create products with a name, price, and default quantity.
#     Add products to the shopping cart with specified quantities.
#     View all items in the cart and the total price.

# Sample Output

# plaintext

# # Example output of view_cart()
# Product: Apple, Price: $2.5, Quantity: 3, Item Total: $7.5
# Product: Banana, Price: $1.0, Quantity: 5, Item Total: $5.0

# # Example output of calculate_total()
# Total Cart Price: $12.5

class Product:
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def item_total(self):
        # Calculate total for this item
        return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = []  # Initialize an empty list of items

    def add_item(self, product, quantity):
        # Add a new CartItem to the shopping cart
        item = CartItem(product, quantity)
        self.items.append(item)
        print(f"Added {quantity} of {product.name} to the cart.")

    def view_cart(self):
        # Display all items in the cart
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                item_total = item.item_total()
                print(f"Product: {item.product.name}, Price: ${item.product.price}, Quantity: {item.quantity}, Item Total: ${item_total}")

    def calculate_total(self):
        # Calculate the total price for all items in the cart
        total = sum(item.item_total() for item in self.items)
        print(f"Total Cart Price: ${total}")

# Example usage
product1 = Product("Apple", 2.5, 50)
product2 = Product("Banana", 1.0, 100)

# Display products
product1.display_product()
product2.display_product()

# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item(product1, 3)  # 3 Apples
cart.add_item(product2, 5)  # 5 Bananas

# View cart and calculate total
cart.view_cart()
cart.calculate_total()

	
