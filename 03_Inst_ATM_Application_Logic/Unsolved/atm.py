"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

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
    "balance": 3258.42}
]

def login(user_pin):
    for account in accounts:
        if account ["pin"] == user_pin:
            print ("")
            return account["balance"]
    print("Wrong PIN")
    return False 
# Create the `login` function for the ATM application.
