principal = float(input('Enter the principal amount: '))
rate = float(input('Enter the annuel interest rate: '))
duration = float(input('Enter the duration in years: '))

n = duration

new_rate = (rate / 100) / 12
n = 10 * 12

numerator = ((1 + new_rate) ** n) - 1
denominator = new_rate * ((1 + new_rate) ** n)

mortgage = principal * (denominator / numerator)

print(ff"your monthly payment is: {mortgage:.2f}")

