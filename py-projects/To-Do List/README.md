# 📝 CLI To-Do List

A simple, command-line interface (CLI) task management tool that helps you stay organized by saving your tasks to a local text file.

## 🚀 Features

* **Add:** Create new tasks and append them to your list.
* **Update:** Modify existing tasks in your list by selecting their index.
* **Display:** View a clear, numbered list of all your current tasks.
* **Delete:** Remove tasks once they are completed or no longer needed.
* **Data Persistence:** Your tasks are automatically saved to `app.txt` in real-time, ensuring your data is never lost when you exit the app.

## 🛠 How to Run

1. Ensure you have [Python](https://www.python.org/) installed on your system.
2. Clone this repository to your local machine.
3. Open your terminal and navigate to the `todo/` folder.
4. Run the application:

```bash
python main.py
```


## ⚙️How to Run
This application uses the pathlib library to manage file paths, ensuring the program reliably finds the app.txt file regardless of where it is executed from.

* ***Load:*** On startup, it reads existing tasks from the text file into a Python list.

* ***Modify:*** When you add, update, or delete, the changes are applied to the memory (the list).

* ***Save:*** The save_tasks() function triggers an immediate overwrite of the text file with the updated list, ensuring your data on the hard drive always matches your current session.


***_____________________________________________________________________________________________________________***

***Author:*** Ayushi Singh
***GitHub Profile:*** https://github.com/ayus28ayushi-ai

