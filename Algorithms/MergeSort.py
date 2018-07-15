# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    indexL = 0
    indexR = 0
    tempArr = []

    while indexL < (m-l) and indexR < (r-m):
        if arr[indexL] < arr[indexR]:
            tempArr.append(arr[indexL])
            indexL = indexL + 1
        else:
            tempArr.append(arr[indexR])
            indexR = indexR + 1
    if indexL == m-l:
        for i in range(indexR,r-m):
            tempArr.append(arr[i])
    else:
        for i in range(indexL,m-l):
            tempArr.append(arr[i])
    arr = tempArr



# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int((l + r) / 2)
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def sort(arr):
    mergeSort(arr,0,len(arr)-1)