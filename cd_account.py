"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

from Account import Account

def create_cd_account(balance, interest_rate, months):
    balance = float(balance)
    interest_rate = float(interest_rate)
    apr = interest_rate * months/12
    interest_earned = balance * apr/100
    cd_account = Account(balance, interest_earned)

    return cd_account, interest_earned

# NOTE: The "print("num")" method that is commented out in this document is to
        # help debug different segements of the code when it run in the terminal.)"

# print("1")

"""Creates a CD account, calculates interest earned, and updates the account balance.

Args:
    balance (float): The initial CD account balance.
    interest_rate (float): The APR interest rate for the CD account.
     months (int): The length of months for the CD.

 Returns:
    float: The updated CD account balance after adding the interest earned.
    And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

balance = float(0)
apr = float(0)
months = int(12)

account_instance = Account(balance, apr)

    # print("2")

# Calculate interest earned
# ADD YOUR CODE HERE

interest_earned = balance * (apr/100 * months/12)

    # NOTE:
    #print("Interest earned:", interest_earned)
    # print("3")


    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

updated_cd_balance_with_interest = balance + interest_earned

    # NOTE: 
    # print("New balance:", updated_balance)
    # print("4")

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

account_instance.set_balance(updated_cd_balance_with_interest)

# print("5")

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

account_instance.set_interest(interest_earned)

# print("6")

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE

print("CD account balance: $", (updated_cd_balance_with_interest))
print("Interest earned on CD account: $", (interest_earned))

# print("7")
