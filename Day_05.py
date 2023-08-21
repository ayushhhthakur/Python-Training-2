# def printPattern(n):
#     for i in range (n):
#         for j in range(n):
#             if i == j or i+j == n-1:
#                 print(i + 1,end=' ')
#             else:
#                 print(" ",end=' ')
#             print()

# printPattern(5)


# insertion sort
# Python program for implementation of Insertion Sort

# Function to do insertion sort
# def insertionSort(arr):

#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#         key = arr[i]
#         print(i)

#       # Move elements of arr[0..i-1], that are
#       # greater than key, to one position ahead
#       # of their current position
#     j = i-1
#     while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#     arr[j + 1] = key


# # Driver code to test above
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# for i in range(len(arr)):
#     print("% d" % arr[i])


# selection sort
# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
# for i in range(len(A)):
	
# 	# Find the minimum element in remaining
# 	# unsorted array
# 	min_idx = i
# 	for j in range(i+1, len(A)):
# 		if A[min_idx] > A[j]:
# 			min_idx = j
			
# 	# Swap the found minimum element with
# 	# the first element	
# 	A[i], A[min_idx] = A[min_idx], A[i]

# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
# 	print("%d" %A[i],end=" , ")

# quick sort
# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1


# Function to perform quicksort
print("This is quick sort")
def quicksort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quicksort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
	array = [10, 7, 8, 9, 1, 5]
	print("Input array: ", array)
	N = len(array)

	# Function call
	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=' ')

# This code is contributed by Adnan Aliakbar
