def two_numbers_multiply(first_num, second_num):
	multiply = 0	

	for num in range(second_num):
		multiply += first_num
	return multiply	






first_num = int (input("Enter first number:"))
second_num = int (input("Enter second number:"))
print(two_numbers_multiply(first_num, second_num))
		