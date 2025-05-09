

while True:
	number = int (input("Enter a number: "))
	if number < 0:
		print("Enter a positive number")
	for numbers in range(number, 0, -1):
		print(numbers)
	print("Blast off")
	if number > 0:
		break
