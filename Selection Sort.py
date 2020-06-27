# my naive approach ,will go to build optimal solution

def selection_sort(arr): 
	count = 0                           
	n = len(arr)
	for i in range(n):
		min_value = i                                            # Here in selection sort,we use a variable min_value 
		for j in range(i+1,n):
			if arr[j] < arr[min_value]:                            
				min_value = j

		if min_value != i:                                      # we check wether min_value which is set to i is same
																#the only way it will change is if we encounter a smaller number

			print("before",arr)                                 # this approaches significiantly reduces the number of swaps compared to
			          											# bubble sort
			arr[i],arr[min_value] = arr[min_value],arr[i]
			print("After",arr)
			print("\n")
			count += 1

	print(arr)
	print(count)
arr = [4,9,2,5,7,8,9,2,3,4,5,6,7,8,1,0,3,4,56,7,8,9,0,4]
apr = [3,2,5,7,4]
selection_sort(apr)