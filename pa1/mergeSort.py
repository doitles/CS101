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
import scipy
import timeit
import numpy as np

T = [0] * 100
A = np.arange(100)
print("Best Case:")
print(A)
E = timeit.Timer(lambda: mergeSort(A, 0, 99))
print("Sorted Array:")
print(A)
T = E.repeat(repeat = 100, number = 1)
R = (scipy.mean(E.repeat(repeat = 100,number = 1)))
print("Times: ")
print("%s seconds " % T)
print("Average Time: ")
print( "%s seconds" % R)

T1 = [0] * 100
B = np.arange(100)
B1 = B[::2]
B2 = B[1::2]
B3 = np.concatenate((B1, B2), axis=1)
print("Worst Case:")
print(B3)
F = timeit.Timer(lambda: mergeSort(B3, 0, 99))
print("Sorted Array:")
print(B3)
T1 = F.repeat(repeat = 100, number = 1)
Q = (scipy.mean(F.repeat(repeat = 100,number = 1)))
print("Times: ")
print("%s seconds " % T1)
print("Average Time: ")
print( "%s seconds" % Q)

T2 = [0] * 100
C = np.array(np.random.random_integers(0, 100, 100))
print("Random Case:")
print(C)
G = timeit.Timer(lambda: mergeSort(C, 0, 99))
print("Sorted Array:")
print(C)
T2 = G.repeat(repeat = 100, number = 1)
S = (scipy.mean(G.repeat(repeat = 100,number = 1)))
print("Times: ")
print("%s seconds " % T2)
print("Average Time: ")
print( "%s seconds" % S)
