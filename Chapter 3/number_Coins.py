purchase_price = int(input("Enter the purchase price(up to $1.00):"))

if purchase_price < 0 or purchase_price > 1.00:
	print("invalid input.price has to between 0.00 and $1.00:")
else:
	change = round((10 - purchase_price) * 100) 
	print(f"\nchange to be given:{change}cents")
		
	quarters = 25
	dimes = 10
	pennies = 0
	nickels = 5

	quarters = change // 25
	change % 25
			
	dimes = change // 10
	change % 10

	nickels = change // 5
	change % 5

	print(f"\nchange using the fewest number of coins:")
	print("quarters:", quarters)
	print("dimess:", dimes)
	print("nickels:", nickels)
	print("pennies:", pennies)

