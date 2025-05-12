print("\nProgram checks and sorts 3 numbers in ascending order")


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

value_1 = float(number_1)
value_2 = float(number_2)
value_3 = float(number_3)

largest = 0
smallest = 0
middle = 0


if value_1 > value_2 and value_1 > value_3:
	largest = value_1
elif value_1 < value_2 and value_1 < value_3:
	smallest = value_1
else: 
	middle = value_1

if value_2 > value_1 and value_2 > value_3:
	largest = value_2
elif value_2 < value_1 and value_2 < value_3:
	smallest = value_2
else: 
	middle = value_2

if value_3 > value_1 and value_3 > value_2:
	largest = value_3
elif value_3 < value_1 and value_3 < value_2:
	smallest = value_3
else: 
	middle = value_3

print(smallest, middle, largest)
