expenses = [1200,1300,1500,1700]
total_expense = 0
for i in range(len(expenses)):
    expense = expenses[i]
    print(f"month{i+1}, Expense: {expense}")
    total_expense = expense + total_expense

print(f"total:",total_expense)
