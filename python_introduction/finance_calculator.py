income = int(input("Enter your monthly inome:"))
expenses = int(input("Enter your totalmontly expenses:"))
savings = income - expenses
anualsaving = savings * 12 + (savings * 12 * 0.05)
print(f"Your monthly savigns are ${savings}")
print(f"Projected savings after one year, with interest, is: ${anualsaving}")
