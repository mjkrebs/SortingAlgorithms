def heapify(arr,n,index):
    largest = index

    l = 2*index + 1
    r = 2*index + 2

    if l < n and arr[index] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != index:
        arr[index],arr[largest] = arr[largest],arr[index]
        heapify(arr,n,largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range (n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

def sort(arr):
    heapSort(arr)
