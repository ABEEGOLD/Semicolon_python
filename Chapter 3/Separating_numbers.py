separated_Digit = int(input("Enter separated five digits:"))

first_Number = (separated_Digit // 10000)% 10 
second_Number = (separated_Digit // 1000)% 10 
third_Number = (separated_Digit // 100)% 10 
fourth_Number = (separated_Digit // 10)% 10 
fifth_Number = (separated_Digit // 1 % 10) 

for numbers in range(5):
         print(first_Number)
	 print(second_Number)
	 print(third_Number)
	 print(fourth_Number)
	 print(fifth_Number)
		
if first_Number // fifth_Number and second_Number % 			 fourth_Number:
	 printf("dispay each {digits}:", numbers)