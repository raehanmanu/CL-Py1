
# 15
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Balance: {self.balance}")


# 16
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed: {title}")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"You returned: {title}")
                return
        print("Book not found.")


# 17
class Employee:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_by_department(self, dept):
        for emp in self.employees:
            if emp.dept == dept:
                print(emp.name)
