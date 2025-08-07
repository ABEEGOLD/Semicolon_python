# list_natural_numbers = []
# def solution_that_returns_multiples_of_three_and_five():
# list_natural_numbers = []
# sum = 0
# for number in list_natural_numbers:
#     list_natural_numbers = list_natural_numbers + [number]
#     if number % 3 == 1 and number % 5 == 1:
#      sum = sum + number
# print(sum)

def solution(number):
    if number < 0:
        return 0

    for i in range(number):
        if(i % 3 == 0 or i % 5 == 0):
            return i

print(solution(5))



# def multiples_of_3_or_5(number):
#     if number < 0:
#         return 0
#
#
# number = multiples_of_3_or_5(10)
# result = sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
# print("Sum of multiples of 3 or 5 below", number, "is:", result)
