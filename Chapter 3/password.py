password = input("Enter a password:")
count =0


for number in password:
	if number != '':
		count+= 1
standard_password = 16 
min_lenght = 8

if count < min_lenght:
	print("very weak")

if count == min_lenght:
	print("weak")

elif count > min_lenght and count <= standard_password:
	print("strong")

elif count >= standard_password:
	print("very strong")
print(count)

