# my naive approach on insertion sort
def insertion_sort_1(arr):
	for index in range(1,len(arr)):                                   #in place sorting , but can be complex if the smaller
		current_element = arr[index]                                  # elements are present to the extreme ends 
		while arr[index-1] > current_element and index >0:
			arr[index]= arr[index-1]
			index = index -1 
		arr[index] = current_element

	print(arr)
 

def insertion_sort_2(arr):
	count = 0
	for i in range(1,len(arr)):
		value_to_sort = arr[i]

		while arr[i-1] > value_to_sort and i>0:                        # make sure to add index > 0 as it might result in 
                                                                       # index out of range error
			print("Before",arr)                                     
			arr[i-1],arr[i] = arr[i],arr[i-1]                          # this logic is more easy to grasp
			count += 1
			i = i-1
			print("After ",arr)
			print("\n")
			


	print(arr)
	print(count)

arr = [4,9,2,5,7,8,9,2,3,4,5,6,7,8,1,0,3,4,56,7,8,9,0,4]
apr = [3,2,5,7,4]
axr = [3,2,6,7,4,1]

insertion_sort_1(axr)
