principal_Amount = int(input("The pincipal  is:"))
interest_rate = float(input("The interest is:"))
numbers_Of_Years = int(input("The numbers of years is:"))

actual_rate = interest_rate /100  
 
for years in range(1, numbers_Of_Years+1):
	return_On_investment = principal_Amount * ((1 + actual_rate)**(years))
	print(f" the number of {years} is {return_On_investment:.2f}")


 		






