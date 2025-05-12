customer_total_spending = int (input("Enter the given amount:"))
if customer_total_spending < 1000:
	print("invalid amount ")

purchase_between1000_10000 = float(0.05) * customer_total_spending
new_customer_amount = customer_total_spending - purchase_between1000_10000

purchase_between_10000_50000 = int(0.1) * customer_total_spending
new_customer_amount = customer_total_spending - purchase_between_10000_50000

purchase_between_50000 = float(0.2) * customer_total_spending
new_customer_amount = customer_total_spending - purchase_between_50000   
		
if customer_total_spending >= 1000 and customer_total_spending < 10000:
	print(f"the discounts between 1000 & 10000 is: {purchase_between1000_10000}")
	print("the new amount the customer will pay is:",new_customer_amount)

elif customer_total_spending >= 10000 and customer_total_spending <= 50000:
	print(f"the discounts receive between 10000 & 50000 is: {purchase_between_10000_50000}")
	print("the new amount the customer will pay is:",new_customer_amount)

elif customer_total_spending >= 50000:
	print(f"the discount recieve for 50000 is:{purchase_between_50000}")
	print("the new amount the customer will pay is:",new_customer_amount)

	
	




