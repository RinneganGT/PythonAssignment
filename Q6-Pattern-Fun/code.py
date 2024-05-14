
# Exercise Name:
# 	06-Pattern-Fun
# Description:
# 	Prompt for row count and print a number pattern using that value
# Given:
# 	row_count = 5
# Return:
# 	1 1 1 1 1 
# 	2 2 2 2 
# 	3 3 3 
# 	4 4 
# 	5

# print("Enter the row number for pattern :")

row_number = int(input("Enter the number of rows for pattern :"))

for i in range(1,row_number+1):
    for j in range(row_number+1-i):
        print(i,end=" ")  
    print()
    


