def unpack_collection(collection):
    result = [0,0,0,0]
    for index in range(4):
        result[index]  = collection[index]
    return result



my_list = [33,22,8,9,6,2,7]
#print(unpack_collection(my_list))


def unpacking_collection(numbers):
        first_number, second_number,third_number, *other = numbers
        return first_number, second_number, third_number, *other


#print(unpacking_collection(my_list))


def slice_collection(numbers):
    return numbers[::]


#print(slice_collection(my_list))

def sort_collection(numbers):
   numbers.sort(reverse = True)
   return numbers



#print(sort_collection(my_list))



def is_Odd(number):
    return number % 2 == 1

def filter_collection(collection):
    return list(filter(is_Odd, collection))

#print(filter_collection(my_list))


def filter_with_lambda(collection):
    return list(filter(lambda number : number% 2 == 1, collection))

print(filter_with_lambda(my_list))


def sum_collection(collection):
    sum_all_numbers = sum(map(lambda number: number, collection))
    return sum_all_numbers


print(sum_collection([2,3,4]))
