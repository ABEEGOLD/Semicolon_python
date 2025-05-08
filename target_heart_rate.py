users_Age = int (input("Enter users age:"))

beats_per_minutes = 220
target_Heart_Rate_Max = 85/100 
target_Heart_Rate_Min = 50/100


maximum_Heart_Rate = beats_per_minutes - users_Age
users_target_Heart_Rate_Max = (85/100) * maximum_Heart_Rate 
users_target_Heart_Rate_Min = (50/100) * maximum_Heart_Rate 

print(f"The maximum heart rate = ",maximum_Heart_Rate)
print("The target heart rate is between {} and {} ".format(users_target_Heart_Rate_Min,users_target_Heart_Rate_Max)) 
