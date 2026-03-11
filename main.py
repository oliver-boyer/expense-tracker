from categorizer import categorize
expenses= []
print("welcome to your expense tracker ")

def save_expenses(expenses):
    with open ("expenses.txt", "w") as f:
        for expense in expenses:
          f.write(f"{expense['name']},{expense['amount']}\n")

while True:

  name = input("What did you spend your money on : ").strip()
  amount = float(input("how much money did it cost ?"))
  category = categorize(name)
  expenses.append({'name':name,'amount':amount,'category':category})
  print(expenses)

  another = input("add other ? yes/no :")
  if another == 'no':
     break
print("\n--- Your Expenses ---")
for expense in expenses:
  print(f"{expense['name']} - ${expense['amount']} - {expense['category']}")

total = sum(expense['amount'] for expense in expenses)
print(f"\nTotal spent : ${total}")
save_expenses(expenses)
print("Expenses saved")
