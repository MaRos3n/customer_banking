# Module 3 Challenge: Savings and CD Account Management System

### This project is a Python program that simulates a savings and CD (Certificate of Deposit) account management system. It allows users to create and manage both savings and CD accounts, calculate interest earned, and update account balances.


## Instructions:

**Instructions taken from the UNC bootcampspot website:**

**<ins>Background<ins>:**

You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.


**<ins>Challenge Instructions:<ins>**

- The starter files consist of the following files: Accounts.py, savings_account.py, cd_account.py, and customer_banking.py. 
    - The Accounts.py file contains the Account class with methods to set the balance and interest.

- In the savings_account.py file, you will import the Account class and create a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

- In the cd_account.py file, you will import the Account class and create a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

- In the customer_banking.py file, you will import the create_savings_account and create_cd_account functions, then create a main function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

1. Create the Savings Account Function

2. Open the savings_account.py file, and do the following:

    - Imports the Account class from the Accounts.py file.

    - In the create_savings_account function do the following:

    - Create an instance of the Account class and pass in the balance and interest parameters.

    - Calculate interest earned.

    - Update the savings account balance by adding the interest earned.

    - Pass the updated balance to the set balance method using the instance of the Account class.

    - Pass the interest earned to the set interest method using the instance of the Account class.

    - Return the updated balance and interest earned.

* Create the CD Account Function

* Open the cd_account.py file, and do the following:

    - Import the Account class from the Accounts.py file.

    - In the create_cd_account function, do the following:

    - Create an instance of the Account class and pass in the parameters.

    - Calculate interest earned.

    - Update the savings account balance by adding the interest earned.   

    - Pass the updated balance to the set balance method using the instance of the Account class.

    - Pass the interest earned to the set interest method using the instance of the Account class.

    - Return the updated balance and interest earned.

    - Create the Main Function

* Open the customer_banking.py file, and do the following:

    - Import the create_cd_account and create_savings_account functions from the appropriate files.

* In the main function, do the following:

    - Prompt the user to set the savings balance, interest rate, and months for the savings account.

    - Call the create_savings_account function and pass in the variables from the user.

    - Print out the interest earned and updated savings account balance with interest earned for the given months.

    - Prompt the user to set the CD balance, interest rate, and months for the CD account.

    - Call the create_cd_account function and pass the variables to the function used to prompt the user from the user.

    - Print out the interest earned and updated CD account balance with interest earned for the given months.

    - Call the main function.


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


## References: 

- ChatGPT. OpenAI, 2024. (https://chat.openai.com/).
- Class information: Ryan Norman (Instructor).
- "Markdown Syntax." Stack Overflow, https://stackoverflow.com/questions/3003476/get-underlined-text-with-markdown.
- Python Documentation. Python Software Foundation, 2022. https://docs.python.org/3/.