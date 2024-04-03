"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

from Account import Account

# print("1")

"""Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """


# Define a function for the Savings Account


def create_savings_account(balance, interest_rate, months):
   balance = float(balance)
   interest_rate = float(interest_rate)
   apr = interest_rate * months/12
   interest_earned = balance * apr/100
   savings_account = Account(balance, interest_earned)

   return savings_account, interest_earned

# print("2")

# Create an instance of the `Account` class and pass in the balance and interest parameters.
#  Hint: You need to add the interest as a value, i.e, 0.
# ADD YOUR CODE HERE

balance = float(0)
apr = float(0)
months = int(12)

account_instance = Account(balance, apr)

# print("3")

    #(NOTE:
    #pass in 0 for the initial balance, 0 for the interest rate, 
    #and 0 for the number of months, assuming you want to start with zero balance 
    #and zero interest.
   

# Calculate interest earned
# ADD YOUR CODE HERE

interest_earned = balance * (apr/100 * months/12)

    # NOTE:
    # print("Interest earned:", interest_earned)
    # print("4")

# # Update the savings account balance by adding the interest earned
# # ADD YOUR CODE HERE  

updated_savings_balance = balance + interest_earned

    # NOTE:
    # print("New balance:", updated_savings_balance)
    # print("5")

# # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
# # ADD YOUR CODE HERE

account_instance.set_balance(updated_savings_balance)

# print("6")

# # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
# # ADD YOUR CODE HERE

account_instance.set_interest(interest_earned)

# print("7")

# # Return the updated balance and interest earned.
# # ADD YOUR CODE HERE

print("Savings account balance: $", (updated_savings_balance))
print("Interest earned on savings account: $", (interest_earned))