from pathlib import Path
 
# Initialising the text file path
file_path = Path(__file__).parent/"app.txt"
tasks = []

# Copying the existing tasks from the text file
if file_path.exists:
    tasks = file_path.read_text().splitlines()

# Function to save the changes in the text file
def save_tasks ():
    file_path.write_text("\n".join(tasks))

#Menu for the user
print("-----------------TO DO LIST-------------------\n")
print('1. "add" to add a task.\n')
print('2. "update" to update a task.\n')
print('3. "display" to display all the tasks.\n')
print('4. "delete" to delete a task.\n')
print('5. "exit" to exit from the app.\n')

#interface
while True:
    print("\nEnter your choice:")
    user_input = input();

    # Adding the task
    if user_input == "add":
        print("Enter task to add:")
        task = input()
        tasks.append(task)
        save_tasks()
        print("Task added successfully!\n")

    # Updating the task
    elif user_input == "update":
        print("Which task to update?\n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\n")
        try:
            update = int(input())
        except ValueError :
            print("Invalid Input")
        print("Enter new task:")
        try:
            new_task = input()
        except ValueError:
            print("Invalid Input")
        tasks[update-1] = new_task
        save_tasks()
        print("Task updated successfully!\n")
        
    # Displaying all the tasks
    elif user_input == "display":
        if not tasks:
            print("No tasks available!")
        else:
            print ("-----------Your Tasks-------------\n")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Deleting task
    elif user_input == "delete":
        print("Which task to delete?")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        del_index = int(input())
        removed_task = tasks.pop(del_index-1)  #returns the item and then removees it
        save_tasks()
        print(removed_task + ' deleted successfully!')

    # Exiting from the app
    elif user_input == "exit":
        print("GoodBye! :)\n")
        break;
    # Handling edge cases
    else:
        print("Invalid input! Try again\n")

 
