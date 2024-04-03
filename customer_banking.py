# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = float(input("Please enter the savings account balance: "))
    savings_interest = float(input("Please enter the interest rate for the savings account: "))
    savings_maturity = int(input("Please enter the number of months for the savings account: "))

    # NOTE: print("1")

    # Call the create_savings_account function and pass the variables from the user.
    
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity)

    # NOTE: print("2")

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    updated_savings_balance = updated_savings_balance.balance + savings_interest_earned

    print(f"Interest earned on savings account: $ {savings_interest_earned:.2f}")
    print(f"Updated savings account balance: $ {updated_savings_balance:.2f}")

    # NOTE: print("3")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance = float(input("Please enter the CD account balance: "))
    cd_interest = float(input("Please enter the interest rate for the CD account: "))
    cd_maturity = int(input("Please enter the number of months for the CD account: "))

    # NOTE: print("4")

    # Call the create_cd_account function and pass the variables from the user.
   
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity)
    
    # NOTE: print("5")

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    
    updated_cd_balance_with_interest = updated_cd_balance.balance + cd_interest_earned
    
    print(f"Interest earned on CD account: $ {cd_interest_earned:.2f}")
    print(f"Updated CD account balance: $ {updated_cd_balance_with_interest:.2f}")

    # NOTE: print("6")

    # Call the main function.
if __name__ == "__main__":
    main()