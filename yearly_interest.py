# Invest term length in years

print('How many years will you be saving')
years = int(input('Enter years: '))

# Amount of current principal available

print('How much money is currently in your account?')
principal = float(input('Enter the current amount in your account: '))

# Planned monthly investment amount

print('How much money do you plan to invest each month?')
monthly_invest = float(input('Enter amount: '))

# Estimated yearly interest to gain

print('What is the estimated yearly interest for this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1): '))

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

        final_amount = (final_amount + monthly_invest) * (1 + interest)

print('This is the amount of money you will have in your account after {} years: ')
