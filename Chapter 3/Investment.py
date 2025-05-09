principal = float(input("Enter the principal:"))
annualRate  = float(input("Enter the annual rate:"))
numberOfYears  = int(input("Enter the number of years:"))

a = 9
principal = 1000
n = (10,20,30)
number_10 = 10
number_20 = 20
number_30 = 30

annualRate = (7 / 100) / 1

for year in range(numberOfYears):

	amount = round(principal * pow((1 + annualRate), year))

	print(f"the {principal} money earned after {year} is: ", amount)