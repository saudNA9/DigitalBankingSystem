from datetime import datetime, timedelta
import uuid
import csv
import logging
import sys
import tkinter as tk
from tkinter import messagebox

# Set up logging to stdout instead of stderr
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    MAX_WITHDRAWAL_LIMIT = 5000  # Maximum withdrawal limit per transaction
    LOW_BALANCE_THRESHOLD = 100  # Threshold for low balance alerts

    def __init__(self, owner_name, password, currency="SAR"):
        self.owner_name = owner_name
        self.__balance = 0.0
        self.__password = password
        self.currency = currency
        self.__transaction_history = []
        self.__scheduled_payments = []

    def deposit(self, amount):
        """Deposit money into the account."""
        try:
            if amount <= 0:
                raise ValueError("The amount must be greater than zero.")
            self.__balance += amount
            self.__record_transaction("deposit", amount)
            logging.info(f"{amount} {self.currency} deposited successfully.")
        except ValueError as e:
            logging.error(e)

    def withdraw(self, amount):
        """Withdraw money from the account."""
        try:
            if amount <= 0:
                raise ValueError("The amount must be greater than zero.")
            if amount > self.MAX_WITHDRAWAL_LIMIT:
                raise ValueError(f"Cannot withdraw more than {self.MAX_WITHDRAWAL_LIMIT} {self.currency} at a time.")
            if self.__balance >= amount:
                self.__balance -= amount
                self.__record_transaction("withdraw", amount)
                logging.info(f"{amount} {self.currency} withdrawn successfully.")
                self._alert_low_balance()
            else:
                raise ValueError("Insufficient balance for this transaction.")
        except ValueError as e:
            logging.error(e)
            self._alert_low_balance()

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

def authenticate(self, password):
    """Authenticate user by matching the password."""
    return self.__password == password

def __record_transaction(self, transaction_type, amount):
    """Record transactions in the account's history."""
    now = datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y, at %I:%M%p")
    transaction_id = str(uuid.uuid4())
    transaction = {
        'id': transaction_id,
        'type': transaction_type,
        'amount': amount,
        'date': formatted_date
    }
    self.__transaction_history.append(transaction)
    logging.info(f"{transaction_type.capitalize()} of {amount} {self.currency} recorded on {formatted_date}.")

def print_transaction_history(self):
    """Print the transaction history."""
    if not self.__transaction_history:
        logging.info("No transactions found.")
        return
    for transaction in self.__transaction_history:
        print(f"ID: {transaction['id']} | {transaction['type'].capitalize()} of {transaction['amount']} {self.currency} on {transaction['date']}.")

def get_transaction_history(self):
    """Return the transaction history."""
    return self.__transaction_history
