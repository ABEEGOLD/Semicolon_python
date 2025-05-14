current_population = 8000500000
growth_rate = 0.0085

print(f"{'YEAR':<5}{'POPULATION':<20}{'ANNUAL INCREASE':<20}")

population = current_population
for year in range(1, 101):
	increase = population * growth_rate
	population = population + increase
	print(f"{year:<5}{population:<20}{increase:<20}")

	if population >= (current_population * 2):
		print(f"Population doubled in year {year}")
	if population >= (current_population * 4):
		print(f"Population quadripled in year {year}")

