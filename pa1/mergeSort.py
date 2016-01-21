def mergeSort(A, low, high):
	#intialize first
    i = 0
    j = 0
    #if array hasn't been touched yet sort starting at index 0
    if i < low and j < low:
        mergeSort( A, 0, len(A) - 1)
    #if first index is lower, keep on sorting
    if low < high:
    	#first block
        for i in range(low, high):
            curr = i
            #second block to compare
            for j in range( i + 1, high + 1):
                if A[j] < A[curr]:
                    curr = j
            if curr != i:
                A[i], A[curr] = A[curr], A[i]      #swap
    #splitting array           
    elif low < high:
        mid = (low + high)//2
        mergeSort(A, low, mid)
        mergeSort(A, mid+1, high)
        merge(A, low, mid, high)
        
def merge(A, low, mid, high):
    #intialize arrays and split them
    left = A[low:mid]
    right = A[mid:high + 1]
    #set the last index of the arrays to be infinity-ish
    left.append(999999999)
    right.append(999999999)
    #magic of merging
    for k in range (low, high + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
#test
import time
import numpy as np

T = [0] * 2
A = np.arange(10000)
start = time.time()
print("Best Case:")
print(A)
mergeSort(A, 0, 9999)
print("Sorted Array:")
print(A)
end = time.time()
print("Time: ")
print("%s seconds " % (end - start))
T[0] = (end - start)

start1 = time.time()
A1 = np.array(np.random.random_integers(0, 100, 10000))
print("Worst Case:")
print(A1)
mergeSort(A1, 0, 9999) 
print("Sorted List:")
print(A1)
end1 = time.time()
print("Time: ")
print("%s seconds " % (end1 - start1))
T[1] = (end1 - start1)
