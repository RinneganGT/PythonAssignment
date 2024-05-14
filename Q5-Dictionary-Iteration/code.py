
# Exercise Name:
# 	05-Dictionary-Iteration
# Description:
# 	Reverse Dictionary mapping
# Given:
# 	ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Return:
# 	{65: 'A', 66: 'B', 67: 'C', 68: 'D'}


ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key_value_rev = {}

for key,value in ascii_dict.items():
    key_value_rev[value]=key
print(key_value_rev)