Mini ATM Interface

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

A simple, command-line-based ATM (Automated Teller Machine) simulation built with Python. This project demonstrates core Python concepts including loops, conditionals, functions, file handling for data persistence, and secure password input.

The application allows a user to perform basic ATM transactions, and it saves their account information (PIN and balance) to a local file, making the data persistent between sessions.

## ✨ Features

* **Secure PIN Protection:** Uses the `getpass` library to hide PIN input, preventing it from being shown on the screen as the user types.
* **First-Time Setup:** Automatically detects if it's the first time the program is run and guides the user through creating a 4-digit PIN and making an initial deposit.
* **Data Persistence:** Saves the user's PIN and current balance to a local `account.txt` file.
* **Core ATM Functions:**
    * Check Balance
    * Deposit Funds
    * Withdraw Funds (with checks for insufficient balance)
    * Exit

## 📋 Requirements

This project uses only built-in Python standard libraries. No external packages are needed.
* Python 3.x

## 🚀 How to Run

1.  **Clone the repository (or download the files):**
    ```bash
    # Replace with your repository's URL
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Run the Python script:**
    ```bash
    # On Windows
    python atm_interface.py
    
    # On macOS / Linux
    python3 atm_interface.py
    ```

3.  **First-Time Use:**
    The first time you run the script, it will guide you through setting up a 4-digit PIN and making an initial deposit.

4.  **Returning Use:**
    On all subsequent runs, it will ask for the PIN you created to log you in.

## 🔧 How It Works: Data Storage

The application's state is maintained by a simple text file named `account.txt` that is created in the same directory as the script.

* **Line 1:** Stores the 4-digit user PIN.
* **Line 2:** Stores the current account balance.

> **Warning:** This file stores the PIN in plain text. This method is suitable for a simple educational project to demonstrate file handling but is **not secure** for any real-world application.

If you want to reset the account, simply delete the `account.txt` file and run the program again.
