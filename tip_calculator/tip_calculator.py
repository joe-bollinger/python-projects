print('Tip Calculator')
print()

# TODO: Get the cost of the meal and print the results
get_cost = input('How much did your meal cost? (i.e. 45.67) ')
# Convert the input string to a float
get_cost = float(get_cost)
print(f"Food Cost: ${format(get_cost, '.2f')}")


# TODO: Calculate 10% sales tax for the bill and print the results.


def calc_tax():
    return round(get_cost * 1.10, 2)


print(f"Your bill after tax: ${format(calc_tax(), '.2f')}")
print()


# TODO: Get the amount the customer would like to pay for a tip and print the results.
get_tip = input(
    'What percentage of the bill would you like to pay as a tip? Please type in a number (i.e. 15) ')
# Convert the input string to a float.
get_tip = float(get_tip)
print(f'Customer wants to tip: {get_tip}%')


# TODO: Calculate the tip amount and print the results.


def calc_tip(tip):
    if tip <= 0:
        tip = 0
        return round(get_cost * ((tip / 100)), 2)
    else:
        return round(get_cost * ((tip / 100)), 2)


print(f'Tip amount: ${calc_tip(get_tip)}')


def total_amount():
    return calc_tip(get_tip) + calc_tax()


print(f'Total cost after tax and tip: ${total_amount()}')

print()

# TODO: Get number of people splitting the bill
get_diners = input('How many people will be splitting the bill? (i.e. 4) ')
# Convert the input string to a integer
get_diners = int(get_diners)
print('Diners:', get_diners)

# TODO: Calculate how much each person should pay (you can assume all people will split the bill evenly)


def split_amount(amount):
    if amount <= 0:
        amount = 1
    return round(total_amount() / amount, 2)


print()
print(f"Each person should pay: ${format(split_amount(get_diners), '.2f')}")
