def InsertionSort(A):
	for j in range(1, len(A)):
		key = A[j]
		#insert A[j] into sorted sequence A[1...j - 1]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = key
import time
import numpy as np

T = [0] * 2
A = np.arange(10000)
start = time.time()
print("Best Case: ")
print(A)
InsertionSort(A)
print("Sorted List: ")
print(A)
end = time.time()
print("Time: ")
print("%s seconds " % (end - start))
T[0] = (end - start)

start1 = time.time()
A1 = np.array(np.random.random_integers(0, 100, 10000))
print("Worst Case: ")
print(A1)
InsertionSort(A1)
print("Sorted List: ")
print(A1)
end1 = time.time()
print("Time: ")
print("%s seconds " % (end1 - start1))
T[1] = (end1 - start1)
