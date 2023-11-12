import tkinter as tk
from tkinter import ttk
import calendar

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()
        self.monthly_budget = 0
        self.balance = 0

    def add_expense(self, name, category, date, amount):
        expense = {
            "name": name,
            "category": category,
            "date": date,
            "amount": amount,
        }
        self.expenses.append(expense)
        self.categories.add(category)
        self.update_balance(-amount)  

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Name: {expense['name']}, Category: {expense['category']}, Date: {expense['date']}, Amount: ₱{expense['amount']:.2f}")

    def view_expenses_by_category(self, category):
        for expense in self.expenses:
            if expense['category'] == category:
                print(f"Name: {expense['name']}, Date: {expense['date']}, Amount: ₱{expense['amount']:.2f}")

    def view_expenses_by_date(self):
        sorted_expenses = sorted(self.expenses, key=lambda x: x['date'])
        for expense in sorted_expenses:
            print(f"Name: {expense['name']}, Category: {expense['category']}, Date: {expense['date']}, Amount: ₱{expense['amount']:.2f}")

    def set_budget(self, budget):
        self.monthly_budget = budget

    def view_budget(self):
        print(f"Monthly Budget: ₱{self.monthly_budget:.2f}")

    def update_balance(self, amount):
        self.balance += amount

    def edit_expense(self, name, new_name, new_category, new_date, new_amount):
        for expense in self.expenses:
            if expense['name'] == name:
                self.update_balance(expense['amount'] - new_amount)  
                expense['name'] = new_name
                expense['category'] = new_category
                expense['date'] = new_date
                expense['amount'] = new_amount

    def delete_expense(self, name):
        for expense in self.expenses:
            if expense['name'] == name:
                self.update_balance(expense['amount'])  
        self.expenses = [expense for expense in self.expenses if expense['name'] != name]

def display_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

def view_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal = display_calendar(year, month)
    calendar_text.config(state=tk.NORMAL)
    calendar_text.delete(1.0, tk.END)
    calendar_text.insert(tk.END, cal)
    calendar_text.config(state=tk.DISABLED)

def add_expense():
    name = name_entry.get()
    category = category_entry.get()
    date = date_entry.get()
    amount = amount_entry.get()
    
    if name and category and date and amount:
        try:
            amount = float(amount)
            tracker.add_expense(name, category, date, amount)
            clear_input_fields()  
            update_expenses()
            update_balance_label()
        except ValueError:
            
            error_label.config(text="Invalid amount")
    else:
        
        error_label.config(text="Please fill in all fields")

def set_balance():
    new_balance = balance_entry.get()
    
    if new_balance:
        try:
            new_balance = float(new_balance)
            tracker.balance = new_balance
            clear_input_fields()  
            update_balance_label()
        except ValueError:
            
            error_label.config(text="Invalid balance")
    else:
       
        error_label.config(text="Please enter a balance")

def update_expenses():
    expenses_text.config(state=tk.NORMAL)
    expenses_text.delete(1.0, tk.END)
    for expense in tracker.expenses:
        expenses_text.insert(tk.END, f"Name: {expense['name']}, Category: {expense['category']}, Date: {expense['date']}, Amount: ₱{expense['amount']:.2f}\n")
    expenses_text.config(state=tk.DISABLED)

def update_balance_label():
    balance_label.config(text=f"Remaining Balance: ₱{tracker.balance:.2f}")

def clear_input_fields():
    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)
    error_label.config(text="")


root = tk.Tk()
root.title("Expense Tracker")


tracker = ExpenseTracker()


root.geometry("800x600")  
root.configure(bg='white')  


font = ('Helvetica', 12)


text_color = 'black'


style = ttk.Style()
style.configure("TButton", padding=10, font=font, foreground='black', background='light blue', bordercolor='light blue')

name_label = ttk.Label(root, text="Name:", font=font, background='white', foreground=text_color)
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")


name_entry = ttk.Entry(root, font=font)
name_entry.grid(row=0, column=1, padx=10, pady=10)

category_label = ttk.Label(root, text="Category:", font=font, background='white', foreground=text_color)
category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")


category_entry = ttk.Entry(root, font=font)
category_entry.grid(row=1, column=1, padx=10, pady=10)

date_label = ttk.Label(root, text="Date (MM/DD/YYYY):", font=font, background='white', foreground=text_color)
date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")


date_entry = ttk.Entry(root, font=font)
date_entry.grid(row=2, column=1, padx=10, pady=10)

amount_label = ttk.Label(root, text="Amount:", font=font, background='white', foreground=text_color)
amount_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")


amount_entry = ttk.Entry(root, font=font)
amount_entry.grid(row=3, column=1, padx=10, pady=10)

add_expense_button = ttk.Button(root, text="Add Expense (₱)", command=add_expense, style="TButton")
add_expense_button.grid(row=4, column=0, columnspan=2, pady=10)

balance_label = ttk.Label(root, text="Remaining Balance: ₱0.00", font=font, background='white', foreground=text_color)
balance_label.grid(row=5, column=0, columnspan=2, pady=10)

set_balance_label = ttk.Label(root, text="Set Balance:", font=font, background='white', foreground=text_color)
set_balance_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")


balance_entry = ttk.Entry(root, font=font)
balance_entry.grid(row=6, column=1, padx=10, pady=10)

set_balance_button = ttk.Button(root, text="Set Balance", command=set_balance, style="TButton")
set_balance_button.grid(row=7, column=0, columnspan=2, pady=10)

expenses_label = ttk.Label(root, text="Expenses:", font=font, background='white', foreground=text_color)
expenses_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

expenses_text = tk.Text(root, height=10, width=60, font=font, background='white', foreground=text_color)
expenses_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="w")
expenses_text.config(state=tk.DISABLED)

error_label = ttk.Label(root, text="", font=font, background='white', foreground='red')
error_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()  




