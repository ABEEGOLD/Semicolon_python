number = int(input("Enter number: "))
fact = 1
sum = 0

for num in range(number, 0, -1):
	fact *= num
	print("The factorial:",num,"is", fact)
print(f"The factorial is: {fact}")
	


	
	