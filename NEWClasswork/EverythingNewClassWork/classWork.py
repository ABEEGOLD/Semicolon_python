


def access_the_third_element(nums):
    return nums[2]

def change_the_last_item_in_the_color(colors):
    colors = ['red','green','blue']
    colors.pop(2)
    return colors.append('yellow')
    #return (colors)

def append_color():
    colors = ['red', 'green', 'blue']
    colors.append('purple')
    return colors

def remove_element_three_from_first(nums):
    nums.remove(3)
    return nums

def return_a_list_of_the_length_of_each_name_in_the_list():
    names = ['Alice', 'Bob', 'Charlie']
    for name in names:
        return len (name)

def sort_the_list_nums_in_ascending_order():
    my_list = [4,1,3,9,2]
    my_list.sort()
    return my_list

def my_function_return_list_of_even_numbers():
    my_list = [4,1,3,9,2,7,8,4,8,10]
    my_list_2 = []
    for num in my_list:
        if num % 2 == 0:
            my_list_2.append(num)
    return my_list_2

def two_list_of_numbers():
    my_list1 = [4,1,3,9,2,]
    my_list2 = [7,8,4,8,10]
    total_Of_list: list(int) == my_list1 + my_list2
    return total_Of_list

def letters_in_list_more_than_three():
    letters = ['lamb', 'kit', 'yam','dogs','man']
    for letter in letters:
        if letters.count(letter) >= 3:
            return letter












# access_the_third_element()
#change_The_Last_Item_In_The_Color()
#append_color()
#remove_element_three_from_first()
#return_a_list_of_the_length_of_each_name_in_the_list()
#sort_the_list_nums_in_accending_order()
#my_function_return_list_of_numbers()
#sort_the_list_nums_in_ascending_order()
#my_function_return_list_of_even_numbers()
#two_list_of_numbers()
#letters_in_list_more_than_three()