print("Welcome To ABEE Bank!!!!")
print("""Atm_Lists 

   What can we help you with today!!!

	1.Atm transactions
	2.Account logs
	3.Exit
    """)



account_Balance = float(input("Enter account balance:"))
print(f'account Balance is: {account_Balance}')

 
withdrawal_amount = float(input("Enter withdrawal Amount must be multiples of $500 or $1000:"))
print("Transaction successful!")

if withdrawal_amount % 500 == 0 and withdrawal_amount % 1000 == 0:
	

	withdrawal_fee = 100
	reduction_Balance = account_Balance - withdrawal_amount - withdrawal_fee

	print(f'The withdrawal_amount is {withdrawal_amount}')
	print(f'The withdrawal_fee is {'$'}{100}')
	print(f'Remaining balance is {reduction_Balance}')

	

if withdrawal_amount < 0.9  :
	print('You cannot withdraw that amount')
if withdrawal_amount > account_Balance:
	print("Invalid input")
	print("Enter a valid Amount:") 

	print(f"account details:",{account_amount},{withdrawal_amount},{withdrawal_fee},{reduction_Balance})


		

	
	
			