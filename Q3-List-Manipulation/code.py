
# Exercise Name:
# 	03-List-Manipulation
# Description:
# 	Remove items greater than 50 from a list while iterating but without creating a different copy of a list.
# Given:
# 	number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Return:
# 	[10, 20, 30, 40, 50]
# Note:
# 	ID of input and output list should match

# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# length = len(number_list)


# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

number_list = [100,90,80,70,50,40,20,10]

# Iterate over the list in reverse order
for index in range(len(number_list) - 1, -1, -1):
    if (number_list[index] > 50):
        del number_list[index]

print(number_list)
