def access_The_Third_Element(nums):
    nums = [10,20,30,40,50]
    print(nums[2])

def change_The_Last_Item_In_The_Color(colors):
    colors = ['red','green','blue']
    colors.pop(2)
    colors.append('yellow')
    print(colors)

    def append_color(color):
        colors.append('purple')
        print(colors)

    #access_The_Third_Element(10,20,30,40,50)