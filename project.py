import os
import sys
import time
import getpass

ACCOUNT_FILE = "account.txt"



def read_account():
    """Reads the PIN and balance from the account file."""
    if not os.path.exists(ACCOUNT_FILE):
        return None, None
    
    with open(ACCOUNT_FILE, "r") as f:
        pin = f.readline().strip()
        balance_str = f.readline().strip()
        
        if not pin or not balance_str:
            print("\n[!] Error: Account file is corrupt. Please delete 'account.txt' and restart.")
            sys.exit()
            
        balance = float(balance_str)
        return pin, balance

def write_account(pin, balance):
    """Writes the PIN and balance to the account file."""
    with open(ACCOUNT_FILE, "w") as f:
        f.write(f"{pin}\n")
        f.write(f"{balance:.2f}\n")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')



def first_time_setup():
    """Guides a new user through setting up their PIN and initial deposit."""
    clear_screen()
    print("~~~ Welcome to Mini ATM Setup ~~~")
    print("Since this is your first time, let's set up your account.")
    
    while True:
        try:
            pin = getpass.getpass("Please create a 4-digit PIN: ")
            if len(pin) == 4 and pin.isdigit():
                pin_confirm = getpass.getpass("Please confirm your PIN: ")
                if pin == pin_confirm:
                    break
                else:
                    print("[!] PINs do not match. Please try again.\n")
            else:
                print("[!] Invalid PIN. Must be exactly 4 digits.\n")
        except ValueError:
            print("[!] Invalid input.")

    while True:
        try:
            balance = float(input("Enter your initial deposit amount (e.g., 1000.00): "))
            if balance >= 0:
                break
            else:
                print("[!] Deposit cannot be negative.")
        except ValueError:
            print("[!] Invalid amount. Please enter a number.")
            
    write_account(pin, balance)
    print("\nAccount setup successful!")
    time.sleep(2)
    return pin, balance

def login():
    
    clear_screen()
    print("Welcome to Mini ATM ")
    stored_pin, balance = read_account()
    
    if stored_pin is None:
        print("[!] Account file not found. Critical error.")
        sys.exit()

    attempts = 3
    while attempts > 0:
        try:
            pin = getpass.getpass("Please enter your 4-digit PIN: ")
            if pin == stored_pin:
                print("\nLogin successful!")
                time.sleep(1)
                return stored_pin, balance
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"[!] Invalid PIN. You have {attempts} attempt(s) left.")
                else:
                    print("\n[!] Too many failed attempts. Exiting for security.")
                    time.sleep(2)
                    sys.exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit()

def check_balance(balance):
    """Displays the current account balance."""
    print(f"\nYour current account balance is: ${balance:.2f}")

def deposit(pin, balance):
    """Adds funds to the account."""
    try:
        amount = float(input("\nEnter amount to deposit: "))
        if amount <= 0:
            print("[!] Deposit amount must be positive.")
            return balance
        
        balance += amount
        write_account(pin, balance)
        print(f"\nDepositing ${amount:.2f}...")
        time.sleep(2)
        print("Deposit successful!")
        print(f"Your new balance is: ${balance:.2f}")
        return balance
        
    except ValueError:
        print("[!] Invalid amount. Please enter a number.")
        return balance

def withdraw(pin, balance):
    """Withdraws funds from the account, checking for sufficient balance."""
    try:
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("[!] Withdrawal amount must be positive.")
            return balance
            
        if amount > balance:
            print(f"\n[!] Insufficient funds. Your balance is ${balance:.2f}")
            return balance
        
        balance -= amount
        write_account(pin, balance)
        print(f"\nWithdrawing ${amount:.2f}...")
        time.sleep(2)
        print("Withdrawal successful!")
        print(f"Your new balance is: ${balance:.2f}")
        return balance

    except ValueError:
        print("[!] Invalid amount. Please enter a number.")
        return balance

# --- Main Execution ---

def main():
    """The main application loop."""
    
    # Check if account exists. If not, run setup.
    if not os.path.exists(ACCOUNT_FILE):
        pin, balance = first_time_setup()
    else:
        # If account exists, prompt for login
        pin, balance = login()


    while True:
        clear_screen()
        print("~~~ Mini ATM Main Menu ~~~")
        print("\nWhat would you like to do?")
        print("  1. Check Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(pin, balance)
        elif choice == '3':
            balance = withdraw(pin, balance)
        elif choice == '4':
            print("\nThank you for using Mini ATM. Goodbye!")
            time.sleep(2)
            sys.exit()
        else:
            print("\n[!] Invalid choice. Please select 1, 2, 3, or 4.")
            
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
