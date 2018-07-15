import random
import time

import Algorithms.QuickSort as qs
import Algorithms.MergeSort as ms
import Algorithms.HeapSort as hs

def makeArr(size,low,high):
    arr = []
    for i in range(size):
        arr.append(random.randint(low,high))
    return arr


def runAlgorithm(testArr,algName):
    startTime = time.time()
    algName.sort(testArr)
    endTime = time.time()
    return endTime - startTime

size = 1000000
low = 1
high = 1000000
testArr = makeArr(size,low,high)
print("Quick Sort: " + str(runAlgorithm(testArr,qs)))
print("Merge Sort: " + str(runAlgorithm(testArr,ms)))
print("Heap Sort: " + str(runAlgorithm(testArr,hs)))