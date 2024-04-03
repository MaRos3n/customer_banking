# Savings and CD Account Management System

This project is a Python program that simulates a savings and CD (Certificate of Deposit) account management system. It allows users to create and manage both savings and CD accounts, calculate interest earned, and update account balances.

## Features

- **Create Savings Account**: Allows users to create a savings account by specifying the initial balance, interest rate, and the length of time in months.
- **Calculate Interest Earned**: Calculates the interest earned on both savings and CD accounts based on the provided interest rate and time period.
- **Update Account Balances**: Updates the balances of savings and CD accounts by adding the interest earned to the initial balance.
- **Interactive User Interface**: Provides an interactive user interface for users to input account details and view the interest earned and updated balances.

## How to Use

1. **Run the Program**: Execute the main Python script `main.py`.
2. **Input Account Details**: Follow the prompts to enter the initial balance, interest rate, and months for both savings and CD accounts.
3. **View Results**: The program will display the interest earned and updated balances for both accounts.

## Components

The project consists of the following components:

- **Account Class**: Defines an `Account` class with methods for setting the balance and interest of an account.
- **Savings Account Function**: Defines a function `create_savings_account` to create a savings account, calculate interest earned, and update the balance.
- **CD Account Function**: Defines a function `create_cd_account` to create a CD account, calculate interest earned, and update the balance.
- **Main Function**: Executes the main functionality of the program, allowing users to interactively create and manage savings and CD accounts.

## File Structure

- `main.py`: Contains the main functionality of the program.
- `savings_account.py`: Defines functions related to the savings account.
- `cd_account.py`: Defines functions related to the CD account.
- `Account.py`: Contains the `Account` class definition.

## Usage

```bash
python main.py
