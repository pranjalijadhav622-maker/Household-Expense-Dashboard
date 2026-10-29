import matplotlib.pyplot as plt

# Household Expenses
categories = ["Food", "Travel", "Shopping", "Bills", "Education"]
amounts = [3000, 1000, 2000, 1500, 1000]

# Calculate total
total = sum(amounts)

print("HOUSEHOLD EXPENSE DASHBOARD")
print("---------------------------")

for i in range(len(categories)):
    print(categories[i], ":", amounts[i])

print("---------------------------")
print("Total Expenses: Rs.", total)

# Create 3 charts
plt.figure(figsize=(12, 4))

# Pie Chart
plt.subplot(1, 3, 1)
plt.pie(amounts, labels=categories, autopct="%1.1f%%")
plt.title("Expense Distribution")

# Bar Chart
plt.subplot(1, 3, 2)
plt.bar(categories, amounts)
plt.title("Category-wise Expenses")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=45)

# Line Chart
plt.subplot(1, 3, 3)
plt.plot(categories, amounts, marker="o")
plt.title("Expense Comparison")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
