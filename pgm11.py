
colors = input("Enter color names separeted by commas :")

color_list = colors.split(",")
color_list = [color.strip() for color in color_list]
print("First color :",color_list[0])
print("Second color :",color_list[-1])

