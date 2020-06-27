def bubble_sort(arr):                                  #my initial approach,will go on modifying this to optimal
	swaps = 0
	for j in range(len(arr)):                                       
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
				swaps += 1
	print(arr)
	print(swaps)
		


 
def bubble_sort_2(arr):                              # Proper bubble sort , we use a boolean sorted which helps to 
	count = 0
	sorted = False									 # break from the loop
	while sorted is False:							 # remove # to understand the working at each level
		sorted = True
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:                     # Time complexity = O(n*n). #Space O(1),as we r not using any
				print(arr,"before")				      # additional data structure
				arr[i],arr[i+1] = arr[i+1],arr[i]
				count += 1
				print(arr,"after")
				print("\n")

				sorted = False
	print(arr)
	print(count)

		
	

 


arr =[4,9,2,5,7,8,9,2,3,4,5,6,7,8,1,0,3,4,56,7,8,9,0,4]
apr = [3,2,5,7,4]
bubble_sort_2(arr)