def categorize_numbers(numbers,divisible_By = 5):
	
	
	values = 10
	values = 15
	values = 21
	values = 30	
 
	for nums in numbers:
		if nums // divisible_By:
			return nums
	else:
		return ("No divisible number found")
values = categorize_numbers((10,15,21,30),5)
print(values)
         