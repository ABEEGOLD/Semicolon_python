maximum = 0
value = 0

for number in range(1,11):
	if number > maximum:
		maximum = number
	value = maximum * number
print(value)