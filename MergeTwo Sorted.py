# merging two sorted arrays


def mergeTwo(left_half,right_half):

	final = [None] * (len(left_half)+len(right_half))
	i = 0
	j = 0
	k = 0

	while i < len(left_half) and j < len(right_half):

		if left_half[i] < right_half[j]:
			final[k] = left_half[i]			
			k += 1
			i += 1
		else:
			final[k] = right_half[j]
			k += 1
			j += 1

	while i < len(left_half):
		final[k] = left_half[i]
		i += 1
		k += 1

	while j < len(right_half):
		final[k] = right_half[j]
		j += 1
		k += 1
	print(final)
 
l = [1,4,7,9]
r = [4,8,13]
mergeTwo(l,r)


