import csv
from pathlib import Path

PARENT_DIR  = Path(__file__).resolve().parent

# forcing the files to be in the same folder as this script
file_path = PARENT_DIR / "log.csv"
money_file_path = PARENT_DIR / "money.csv"
 
 

     
# Initialising the dictionary
keys = [ "Date", "Category", "Amount", "Description"]
expense_dict = dict.fromkeys(keys)


#User menu
print("==========================================================================")
print("======================PERSONAL EXPENSE TRACKER============================")
print("==========================================================================\n")

print('1. "add" to add expense\n')
print('2. "update" to update expense\n')
print('3. "check exp" to check all expenses\n')
print('4. "enter income" to enter the money you have.\n')
print('5. "check income" to check the money you entered.\n')
print('6. "saving" to to check the money left.\n')
print('7. "expense" to check the total money spent\n')
print('8. "delete" to delete expense\n')
print('9. "exit" to close the application\n')


# function to add expenses
def add_expense():
    #inputting expense details
    for key in keys:
        expense_dict[key] = input(f"Enter {key}:")
    file_existence = file_path.exists() and file_path.stat().st_size > 0

    # appending to the file
    with open(file_path, "a") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writerow(expense_dict)
        if not file_existence:
            writer.writeheader()
        print("Expense saved successfully.\n")

# updating the expense 
def update_expense():
    check_all_expenses()
    print("Which expense to update?(Mention S.No)")
    update_index = int(input())-1

    temp_expense = []
    with open (file_path, "r") as f:
        reader = csv.DictReader(f, fieldnames=keys)
        temp_expense = list(reader)

    if (update_index < len(temp_expense)) and (update_index >= 0):
        row_to_update = temp_expense[update_index]
        print("Which headings do you wish to update?(date, amount, category, description)")
        heading  = input().split(" ") 
        for i in range(len(heading)):
            temp = heading[i].title()
            if temp in row_to_update:
                row_to_update[temp] = input(f"Enter new {heading[i]}:")
                print(f"{temp} updated successfully!")
            else:
                print(f"{heading[i]} is an invalid heading!\n")


        with open(file_path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=keys)    
            writer.writerows(temp_expense)      
            print("Expense updated successfully for valid headings!") 

    else:
        print("Invalid S.No. Try again!\n")   


# function to delete expense
def delete_expense():
    check_all_expenses()

    with open (file_path, "r") as f:
            reader = csv.DictReader(f, fieldnames=keys)
            data = list(reader)

    print("Which expense to delete?(Mention S.No)")
    try:
        del_index = int(input())-1
        if (del_index >= 0) and (del_index < len(data)):
            data.pop(del_index)         
                
            with open(file_path, "w") as f:
                writer = csv.DictWriter(f, fieldnames=keys)     
                writer.writerows(data)      
                print("Expense deleted successfully!")  

        else :
            print("Invalid S.No\n") 
    except ValueError:
        print("Invalid S.no!\n")

#total expense calculator
def expense_calc():
    total = 0
    with open (file_path, "r") as f:
        reader = csv.DictReader(f, fieldnames=keys)
        for index in reader:
            total += int(index["Amount"])

    return total



#display all the expenses
def check_all_expenses():
     with open (file_path, "r") as f:
        reader = csv.DictReader(f, fieldnames=keys)  # we dont need fieldnames. csv file will automatically take the first row as the keys

        print ("-"*70 )
        print(f'{"S.No":<12} | {"Date":<12} | {"Category":<18} | {"Amount":<8} | {"Description"}')
        print ("-"*70 + "\n")
        for i, index in enumerate(reader, 1):
             print(f"{i:<12} | {index.get('Date', 'None'):<12} | {index.get('Category', 'None'):<18} | {index.get('Amount', 'None'):>8} | {index.get('Description', 'None')}")
        print("\n")

# adding income to the system
def put_money():
    print("Enter the amount in the system:")
    money = int(input())
    try:
        with open (money_file_path, "a") as f:
            f.write(f"{str(money)}\n")
        print("Income recorded!\n")
    except FileNotFoundError:
        print("Error!\n")

# getting total income from the system
def get_money():
    total = 0
    try:
        with open (money_file_path, "r") as f:
            reader = csv.reader(f)
            for entry in reader:
                if entry:
                    total += int(entry[0])
    except FileNotFoundError:
        print("Error!\n")
    return total





            
                
while True:
    print("Enter your choice:")
    choice = input().strip().lower()

    match choice:
        case "add":
            add_expense()
        case "update":
            update_expense()
        case "check exp":
            check_all_expenses()
        case "enter income":
            put_money()
        case "check income":
            print(f" Your income is {get_money()} Rupees\n")
        case "saving":
            if get_money() == 0:
                print("Add the income you have first!\n")
            else:
                saving = get_money() - expense_calc() 
                if(saving>=0):
                    print(f"You have {saving} Rupees left!\n" )
                else:
                    print("You don't have any savings left.\nYou overspent "+str(abs(saving)) + " Rupees\n")
        case "expense":
            total = expense_calc()
            print("Total expenditure : "+str(total))
        case "delete":
            delete_expense();
        case "exit":
            print("GoodBye! Logging out!")
            break
        case _:
            print("Invalid Input! Try again!\n")
        






