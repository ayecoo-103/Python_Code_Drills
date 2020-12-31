"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3278.42}
]

# Create the `login` function for the ATM application.
# The login function will take in a user PIN.
# The function should validate the PIN against this list of `accounts`.
# If the PIN is validated, the function should return the account's balance.



def login(user_pin):
    for account in accounts:
        if account["pin"] == user_pin:
            print(f"The account balance for PIN {account['pin']} is {account['balance']}.")
            return account["balance"]
    print("Wrong PIN number:")
    return False
# Create the `check_balance` function for the ATM application.
# WRITE YOUR LOGIC HERE!
# YOUR CODE HERE!
def login(user_pin):
    for account in accounts:
        if account ["pin"] == user_pin:
            


# Create the `make_deposit` function for the ATM application.
# WRITE YOUR LOGIC HERE!
# YOUR CODE HERE!




# Create the `make_withdrawal` function for the ATM application.
# WRITE YOUR LOGIC HERE!
# YOUR CODE HERE!
