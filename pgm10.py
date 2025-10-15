color_list1 = input("Enter first color list(separete by space) :").split()
color_list2 = input("Enter second color list(separete by space) :").split()

unique_colors = [color for color in color_list1 if color not in color_list2]

print("Color in list1 not in list2 :",unique_colors)

