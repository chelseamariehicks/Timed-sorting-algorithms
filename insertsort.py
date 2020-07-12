#############################################################################
# Author: Chelsea Marie Hicks
# OSU Email: hicksche@oregonstate.edu
# Course number/section: CS 325-401
# Assignment: Homework 1            Due Date: April 5, 2020 by 11:59 PM
#
# Description: Program reads inputs from a file named data.txt in which
#       the first value in the line is the number of integers to be sorted.
#       Program sorts the input using insertion sort and writes the output
#       to file named insertout.txt.
#############################################################################


#open data.txt file and read in each list of numbers
with open("data.txt", "r") as numLists:
    for row in numLists:
        #use the split function to create an array for reach line in data.txt
        row = row.split()

        #insertion sort based on psuedocode from chapter 2
        for i in range(2, len(row)):
            key = row[i]
            j = i -1 

            while j >= 1 and int(key) < int(row[j]):
                row[j+1] = row[j]
                j = j - 1
            row[j+1] = key

        #first integer in each row of program is a counter and must be removed
        row.remove(row[0])

        #write the sorted rows to a file named insertout.txt
        with open("insert.out", "a") as sortedNumLists:
            for num in range(len(row)):
                sortedNumLists.write(str(row[num]) + " ")
            sortedNumLists.write("\n")
        
        sortedNumLists.close()

numLists.close()