'''
Concepts: Lists, dictionaries, loops, functions, *args, try/except.

Requirements:
    1. Store expenses with descriptions and amounts.
    2. Display all expenses.
    3. Calculate the total expenses.
    4. Find the highest expense.
    5. Add a new expense.
    6. Search expenses by description.
    7. Create a function using *args to calculate the total of multiple amounts.
    8. Handle invalid user input.
'''

expenses = {
    "Food" : 10000,
    "Medical": 8500,
    "Travel" : 5030,
    "Rental" : 35000,
    "Extra" : 5550
}

print(expenses);

# Total Expenses
total_expenses = 0;
for expense in expenses.values():
    total_expenses = total_expenses + expense;

print("Total Expense: ", total_expenses);

higest_value_dic = {};
highest_amount = 0;
highest_expence_value = "";

# Highest Expense
for key, value in expenses.items():
    if highest_amount <= value:
        highest_amount = value;
        highest_expence_value = key;

higest_value_dic.update({highest_expence_value : highest_amount});

print("Higest Expences: ", higest_value_dic);

# 5. Add a new expense.
expenses["New"] = 8400;
print(expenses.items());

# 6. Search expenses by description.
search_expence = input("Search Expence: ");

for key, value in expenses.items():
    if search_expence == key:
        print(f"Expence: {key} , Amount: {value}");

# 7. Create a function using *args to calculate the total of multiple amounts.
def total_amount(*args):
    total = 0;
    for arg in args:
        total = total + arg;
    return total

total_amount_of_expences = total_amount(10000,2000,1000,2020);
print("Total Amounts: ", total_amount_of_expences);

