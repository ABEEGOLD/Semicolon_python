number = int(input("Enter number: "))

fact = 1
num = 0
one_fact = 0
two_fact = 0
third_fact = 0
fourth_fact = 0
fifth_fact = 0
sixth_fact = 0
seventh_fact = 0
eighth_fact = 0
ninth_fact = 0
tenth_fact = 0
for num in range(2, 0, -1):
	fact *= num
	two_fact = fact

for num in range(3, 0, -1):
	fact *= num
	third_fact = fact

for num in range(3, 0, -1):
	fact *= num
	third_fact = fact

for num in range(3, 0, -1):
	fact *= num
	third_fact = fact

for num in range(5, 0, -1):
	fact *= num
	fifth_fact = fact

for num in range(6, 0, -1):
	fact *= num
	sixth_fact = fact

for num in range(7, 0, -1):
	fact *= num
	seventh_fact = fact

for num in range(8, 0, -1):
	fact *= num
	eighth_fact = fact

for num in range(9, 0, -1):
	fact *= num
	ninth_fact = fact

for num in range(10, 0, -1):
	fact *= num
	tenth_fact = fact


e = 1 + (1/1) + (1 / two_fact) + (1 /third_fact) + (1/fourth_fact) + (1/fifth_fact) + (1/sixth_fact) + (1/seventh_fact) + (1/eighth_fact) + (1/ninth_fact) + (1/tenth_fact)  

print(e)




	


	
	

