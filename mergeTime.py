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

#merge sort function definition based on psuedocode in chapter two and 
#Stack Overflow discussion: 
# https://stackoverflow.com/questions/18761766/mergesort-with-python
def mergesort(array):
    #array length is greater than one, so the array contents will be sorted
    if len(array) > 1:
        #split the array into a left and right array
        middle = len(array)//2 
        left = array[:middle]
        right = array[middle:]

        #recursively call merge sort to split the list down to single elements
        mergesort(left)
        mergesort(right)

        #set all indexes for the arrays equal to 0
        l = r = key = 0
        
        #go through the length of each array, compare the values at the counter
        #position and place the lowest of the two in the array
        while l < len(left) and r < len(right):
            if int(left[l]) < int(right[r]):
                array[key] = left[l]
                l += 1
            else:
                array[key] = right[r]
                r += 1
            key += 1

        #copy any remaining elements of each split array if there are any
        while l < len(left):
            array[key] = left[l]
            l += 1
            key += 1
        while r < len(right):
            array[key] = right[r]
            r += 1
            key += 1

    #if there is only one number, then no sort is necessary   
    else:
        return "The list is sorted and singular in length."


#variable for array size
n = 500

#declare array
array = []

#fill array with n random integers between 0-10,0000
for i in range(n):
    array.append(random.randrange(0,10000))

#start running clock prior to insertion sort
start = time.time()

#merge sort sorts n numbers in the array
mergesort(array)

#stop the running clock for sorting the array
stop = time.time()

#calculate the running time
running_time = stop - start

#display results to screen
print(f"Array size, n: {n}\nRunning time: {running_time}")