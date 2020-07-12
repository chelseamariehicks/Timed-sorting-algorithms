#############################################################################
# Author: Chelsea Marie Hicks
# OSU Email: hicksche@oregonstate.edu
# Course number/section: CS 325-401
# Assignment: Homework 1            Due Date: April 5, 2020 by 11:59 PM
#
# Description: Program generates arrays of size n containing random integers
#       from 0 to 10,0000 to be sorted. Program sorts the array contents
#       and uses the system clock to record the running time for sorting
#       different size n arrays. The program outputs the array size n 
#       and the running time to the terminal.
#############################################################################

import time
import random

#variable for array size
n = 500

#declare array
array = []

#fill array with n random integers between 0-10,0000
for i in range(n):
    array.append(random.randrange(0,10000))

#start running clock prior to insertion sort
start = time.time()

#insertion sort sorts n numbers in the array
for i in range(0, n):
    key = array[i]
    j = i - 1

    while j >= 1 and int(key) < int(array[j]):
        array[j+1] = array[j]
        j = j - 1
    array[j+1] = key 

#stop the running clock for sorting the array
stop = time.time()

#calculate the running time
running_time = stop - start

#display results to screen
print(f"Array size, n: {n}\nRunning time: {running_time}")