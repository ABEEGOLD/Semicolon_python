principal = float(input("Enter the principal:"))
annualRate  = float(input("Enter the annual rate:"))
numberOfYears  = float(input("Enter the number of years:"))

a = 9
principal = 1000
n = (10,20,30)
number_10 = 10
number_20 = 20
number_30 = 30

annualRate = (7 / 100) / 1

amount_after_10_years = principal * pow((1 + annualRate), number_10)
amount_after_20_years = principal * pow((1 + annualRate), number_20)
amount_after_30_years = principal * pow((1 + annualRate), number_30)


print(f"the amounts after 10 years is: ", round(amount_after_10_years, 2))
print(f"the amounts after 20 years is: ", round(amount_after_20_years, 2))
print(f"the amounts after 30 years is: ", round(amount_after_30_years, 2))


 