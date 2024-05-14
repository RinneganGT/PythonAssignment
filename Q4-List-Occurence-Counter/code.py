
# Exercise Name:
# 	04-List-Occurence-Counter
# Description:
# 	Display all duplicate items from a list
# Given:
# 	sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Return:
# 	[20, 60, 30]
# Hint: 
# 	Count occurence of each item in the list and print items occuring more than once.


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicate_list = []

for index in range(len(sample_list)):
    flag=0
    for check in range(index+1,len(sample_list),1):
        if(sample_list[check]==sample_list[index]):
            flag=1
            break
    if flag==1:
        duplicate_list.append(sample_list[index])

print(duplicate_list)

