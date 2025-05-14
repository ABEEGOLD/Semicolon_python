gallons_used = 0.0
miles_driven = 0.0
combined_miles_per_gallon = 0.00
counter = 0

while(True):
	gallons_used = float(input("Enter gallons used (or -1 to end): "))
	if gallons_used == -1:
		break
	miles_driven = float(input("Enter miles driven: "))

	miles_per_gallon = miles_driven / gallons_used
	counter += 1
	combined_miles_per_gallon += miles_per_gallon
	average_mile_per_gallon = combined_miles_per_gallon / counter

	print(f"The miles/gallon for this tank was {miles_per_gallon}")

print(f"The overall average miles/gallon was {average_mile_per_gallon}")

