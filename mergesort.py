#############################################################################
# Author: Chelsea Marie Hicks
# OSU Email: hicksche@oregonstate.edu
# Course number/section: CS 325-401
# Assignment: Homework 1            Due Date: April 5, 2020 by 11:59 PM
#
# Description: Program reads inputs from a file named data.txt in which
#       the first value in the line is the number of integers to be sorted.
#       Program sorts the input using merge sort and writes the output
#       to file named mergeout.txt.
#############################################################################

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


#open data.txt file and read in each list of numbers
with open("data.txt", "r") as numLists:
    for row in numLists:
        #use the split function to create an array for reach line in data.txt
        row = row.split()

        #first integer in each row of program is a counter and must be removed
        row.remove(row[0])

        #call merge sort function
        mergesort(row)

        #write the sorted rows to a file named mergeout.txt
        with open("merge.out", "a") as sortedNumLists:
            for num in range(len(row)):
                sortedNumLists.write(str(row[num]) + " ")
            sortedNumLists.write("\n")
        
        sortedNumLists.close()

numLists.close()