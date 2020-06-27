# Quick sort is one of the fastest sortting algorithim 

# complexity 
#. Most ain,verage    Time = O (n log n).    
# Worst case 
def Quick_sort(arr):                     

	length = len(arr)

	if length <= 1:
		return arr
	else:
		pivot = arr.pop()

	items_greater = []
	items_lesser = []

	for item in arr:

		if item > pivot:
			items_greater.append(item)
		else:
			items_lesser.append(item)

	return Quick_sort(items_lesser) + [pivot] + Quick_sort(items_greater)

# this is the second implemetaion , an in place implementation of  QuickSort


# lomouto partition

def partition(arr,low,high):                        # the basic 
	count = 0
	i = low -1
	pivot = arr[high]

	for j in range(low,high):

		if arr[j] <= pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
			count +=1

	arr[i+1],arr[high] = arr[high],arr[i+1]                    # swapping the i+1 index position with pivot
	return i+1   											   # pivot_index                                   


def quicksort_inplace(arr,low = 0,high = None):
	if high == None:
		high = len(arr) -1
	if low < high:
		pivot_index = partition(arr,low,high)
		quicksort_inplace(arr,low,pivot_index -1)        # sorting the left half
		quicksort_inplace(arr,pivot_index +1,high)       # sorting the right half

arr = [2, 46, 21, 11, 36, 43, 32, 15, 20, 26, 40, 11, 25, 39, 14, 15, 49, 8, 12, 21, 30, 12, 33, 39, 32]
print("Unsorted :",arr)
quicksort_inplace(arr)
print("Sorted   :",arr)




#print(Quick_sort(arr))