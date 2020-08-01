def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        print(lefthalf,"---",righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i = i + 1
            else:
                A[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j = j + 1
            k = k + 1

A = [534, 246, 933, 3,543322,127, 277, 321, 3,3,3,3,3,3,454, 565, 220]
B= [34, 5, 44]
MergeSort(A)
print(A)