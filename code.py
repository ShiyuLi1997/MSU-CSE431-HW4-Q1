import random
from time import time
from matplotlib import pyplot as plt
import math
from statistics import mean 
"""
The merge sort implementation is taken from website:
URL: https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python
"""
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

"""
The insertion Sort algorithm is taken from website:
URL: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
"""
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def findFirst(l,text):
    for i in range(1,len(l)):
        if l[i] == text:
            return i

def findLast(l,text):
    for i in reversed(range(len(l))):
        if l[i] == text:
            return i

N = 200         # data input
k = 40          # each input run k times and take the average time cost

if __name__ == "__main__":
    mergeTime = []
    insertionTime = []
    inpSize = []
    winnerList = []
    for n in range(1,N):
        # append input size to 

        subMerge = []
        subInser = []
        for j in range(k):
            # Generate an array of `ARRAY_LENGTH` items consisting
            # of random integer values between 0 and 999
            #print("n: ",n)
            array = [random.randint(0, 1000) for i in range(n)]
            # copy array for merge sort and insertion sort
            a1 = array.copy()
            a2 = array.copy()
            # Call the function using the name of the sorting algorithm
            # and the array you just created
            t0 = time()
            merge_sort(a1)
            t1 = time()
            # call the insertionSort function using the input
            ta = time()
            insertionSort(a2)
            tb = time()
            # append time info in the list
            subMerge.append(t1-t0)
            subInser.append(tb-ta)
            #print(l)
            #print("Average time cost for merge_sort    for n={}: ".format(n),(t1-t0)/n)
            #print("Average time cost for insertionSort for n={}: ".format(n),(tb-ta)/n)
            
        inpSize.append(n)
        mergeTime    .append(mean(subMerge))
        insertionTime.append(mean(subInser))
        print("n: ",n,"  ",end="")
        winner = "Merge" if (t1-t0)/n <= (tb-ta)/n else "Insertion"
        if (t1-t0)/n <= (tb-ta)/n:
            winnerList.append("Merge")
        else:
            winnerList.append("Insertion")
        print("insertion:{}, merge:{},    {}  wins ".format((tb-ta)/n,(t1-t0)/n,winner))
        #
    # print out the range of n that function MergeSort is better than Insertion sort
    #           regarding the time complexity or time cost
    print("From range {} to {} that merge sort is quicker than insertion sort"
            .format(findFirst(winnerList,"Merge"),findLast(winnerList,"Insertion")))
    
    # plotting the graph
    plt.plot(inpSize, mergeTime, label='MergeSortTimeCost')
    plt.plot(inpSize, insertionTime, label='InsertionSortTimeCost')
    plt.xlabel("Input size (n)")
    plt.ylabel("Cost of time(s)")
    plt.legend()
    plt.show()
