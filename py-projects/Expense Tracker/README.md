# 💰 Personal Expense Tracker

A lightweight, terminal-based **Personal Expense Tracker** designed for simplicity and efficiency. This Python application helps you maintain control over your finances by logging your daily spending and income directly into local CSV files.

---

## 🚀 Key Features

* **Persistent Data:** Automatically saves your records to `log.csv` and `money.csv`.
* **Full CRUD Functionality:** Easily **C**reate, **R**ead, **U**pdate, and **D**elete expense records.
* **Financial Insights:** Instantly calculate your total expenditures and see exactly how much of your hard-earned money remains.
* **Intuitive CLI:** A clean, menu-driven interface that requires no setup or database configuration.

---

## 🛠 How It Works

This application utilizes Python’s `csv` module and `pathlib` for file management. Every time you log an expense, the app appends the data to a structured CSV file, ensuring your data is always safe and readable by spreadsheet software.

### Quick Command Reference

| Command | Description |
| :--- | :--- |
| **`add`** | Log a new transaction (Date, Category, Amount, Description). |
| **`update`** | Modify details for a previous entry by its S.No. |
| **`check exp`** | View a neatly formatted table of all your spending. |
| **`enter income`** | Update your total financial pool. |
| **`check income`** | View your total financial. |
| **`saving`** | Get an instant "Remaining Balance" report. |
| **`expense`** | View total money spent. |
| **`delete`** | Remove an expense record. |
| **`exit`** | Close the application. |

---

## 📋 Getting Started

### Prerequisites
* Ensure you have **Python 3.6 or higher** installed on your machine.

### Installation & Execution
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ayus28ayushi-ai/python-projects-abode.git](https://github.com/ayus28ayushi-ai/python-projects-abode.git)
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd python-projects-abode/py-projects/Expense\ Tracker/
    ```
3.  **Run the script:**
    ```bash
    python tracker.py
    ```

---

## 📊 Data Management
The application manages two files in your local directory:

* **`log.csv`**: This file tracks and saves all your individual expense records.
* **`money.csv`**: The accumulation log of your income.

> **Pro Tip:** Because these files are standard CSVs, you can open them in **Microsoft Excel** or **Google Sheets** at any time to create your own custom charts and visual reports.

---
***Author*** - Ayushi Singh
***GitHub Profile*** - https://github.com/ayus28ayushi-ai

*Built with simplicity in mind. Happy Tracking!*