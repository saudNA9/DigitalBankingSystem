# DigitalBankingSystem

## Overview

The Bank Account Management System is a Python-based application designed to manage bank accounts. It allows users to deposit and withdraw money, apply interest, manage transaction history, schedule automatic payments, and view account information through both command-line logging and a graphical user interface (GUI).

## Features

- **Deposit Money:** Add funds to the bank account.
- **Withdraw Money:** Withdraw funds from the account with a maximum limit and low-balance alert.
- **Apply Interest:** Apply interest to the account balance.
- **View Balance:** Check the current balance of the account.
- **Transaction History:** Record and view the transaction history.
- **Scheduled Payments:** Schedule recurring payments to be processed automatically.
- **Monthly Summary:** Generate a monthly summary report of transactions.
- **Export to CSV:** Export the transaction history to a CSV file.
- **GUI Interface:** Manage the account through an easy-to-use graphical interface.

## Classes

### 1. BankAccount

- **Fields:** 
  - `owner_name`: Name of the account owner.
  - `__balance`: Private field for the account balance.
  - `__password`: Private field for account authentication.
  - `currency`: The currency of the account (default is SAR).
  - `__transaction_history`: Private list to store the transaction history.
  - `__scheduled_payments`: Private list to store scheduled payments.

- **Methods:** 
  - `deposit()`: Deposit funds into the account.
  - `withdraw()`: Withdraw funds from the account with validation.
  - `get_balance()`: Retrieve the current account balance.
  - `authenticate()`: Verify the user’s password.
  - `apply_interest()`: Apply interest to the account.
  - `schedule_payment()`: Schedule automatic payments.
  - `process_scheduled_payments()`: Process scheduled payments.
  - `generate_monthly_summary()`: Generate a monthly summary report.
  - `export_to_csv()`: Export transaction history to a CSV file.
  - `show_gui()`: Display the GUI for the bank account.
  - `_alert_low_balance()`: Alert the user when the balance is low.
  - `send_notification()`: Placeholder for sending notifications.

### 2. BankAccountGUI

- **Fields:** 
  - `root`: The main Tkinter window.
  - `bank_account`: Instance of the BankAccount class.

- **Methods:**
  - `deposit_money()`: Handle the deposit operation via GUI.
  - `withdraw_money()`: Handle the withdrawal operation via GUI.
  - `apply_interest()`: Handle interest application via GUI.
  - `check_balance()`: Display the current balance via GUI.
  - `show_transaction_history()`: Display transaction history via GUI.

## Usage

### Clone the repository:

```bash
git clone <repository-url>