principal_amount = int(input("Enter the investment amount:"))
number_Of_Year = int(input("Enter the number of years:"))
interest_Rate = float(input("Enter the interest_Rate:"))

actual_interest = interest_Rate /100
year = year
number_Of_year_1 = 1
number_Of_year_2 = 2
number_Of_year_3 = 3
number_Of_year_4 = 4
number_Of_year_5 = 5

return_On_interest = principal_amount *(1 + actual_interest)**(number_Of_Year+1) 
print(f"the number for one {year} is:",{return_On_interest})

return_On_interest = principal_amount *(1 + actual_interest)**(number_Of_Year+2) 
print(f"the number for two {year} is:",{return_On_interest})

return_On_interest = principal_amount *(1 + actual_interest)**(number_Of_Year+3) 
print(f"the number for three {year} is:",{return_On_interest})

return_On_interest = principal_amount *(1 + actual_interest)**(number_Of_Year+4) 
print(f"the number for four {year} is:",{return_On_interest})

return_On_interest = principal_amount *(1 + actual_interest)**(number_Of_Year+5) 
print(f"the number for five {year} is:",{return_On_interest}) 

