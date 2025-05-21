binary_Number = int (input("Enter binary number (e.g 1101):"))
 
product = 0
decimal= 0

while (binary_Number is > 0) :
	digit = binary_Number % 10
	decimal += (int) (digit * Math.pow(2,product))
	binary_Number = binary_Number / 10
	product++

	print(f"{decimal} equivalent is:decimal")	

	


