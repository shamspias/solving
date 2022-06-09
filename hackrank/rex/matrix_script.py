#!/bin/python3

import math
import os
import random
import re
import sys



def list_to_string(s):
    """Convert List to string"""
    
    str1 =""
    return (str1.join(s))


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

my_string = ""
final_list = []
count_matrix = 0
for i in range(m):
    final_list.append([])
    
for i in matrix:
    for j in range(m):
        final_list[j].append(matrix[count_matrix][j])
    count_matrix += 1
for i in final_list:
    my_string += list_to_string(i)
rex = r"(?<=\w)([^\w\d]+)(?=\w)"
my_string = re.sub(rex,' ', my_string)
print(my_string)
