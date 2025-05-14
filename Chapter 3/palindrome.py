user_input = int(input("Enter a number:"))

first_Num = (user_input // 10000) % 10
second_Num = (user_input // 1000)  % 10		
third_Num = (user_input //100) % 10
fourth_Num =(user_input // 10) % 10
fifth_Num = (user_input // 1 % 10) 

print(first_Num)
print(second_Num)
print(third_Num)
print(fourth_Num)
print(fifth_Num)


if first_Num == fifth_Num and second_Num == fourth_Num:
	print('palindrome')
else:
	print('not palindrome')	 