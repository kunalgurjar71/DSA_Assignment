import random

dataset_type = int(input("Enter the dataset type(random = 1, sorted = 2, reverse = 3): "))

while dataset_type not in [1, 2, 3]:
    print("Enter correct input (1, 2, or 3)")
    dataset_type = int(input("Enter the dataset type(random = 1, sorted = 2, reverse = 3): "))

input2 = int(input("Enter the sorting algorithm(insertion = 1, quick = 2, merge = 3): "))

while input2 not in [1, 2, 3]:
    print("Enter correct input (1, 2, or 3)")
    input2 = int(input("Enter the sorting algorithm(insertion = 1, quick = 2, merge = 3): "))


arr1 = []
for i in range(0, 20):
    arr1.append(random.randint(1, 1000))

arr2 = []
for i in range(0, 20):
    arr2.append(i)

arr3 = []
for i in range(20, 0, -1):
    arr3.append(i)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if dataset_type == 1:
    if input2 == 1:
        insertionSort(arr1)
        printArray(arr1)
    elif input2 == 2:
        quickSort(arr1, 0, len(arr1) - 1)
        printArray(arr1)
    elif input2 == 3:
        mergeSort(arr1, 0, len(arr1) - 1)
        printArray(arr1)

if dataset_type == 2:
    if input2 == 1:
        insertionSort(arr2)
        printArray(arr2)
    elif input2 == 2:
        quickSort(arr2, 0, len(arr2) - 1)
        printArray(arr2)
    elif input2 == 3:
        mergeSort(arr2, 0, len(arr2) - 1)
        printArray(arr2)

if dataset_type == 3:
    if input2 == 1:
        insertionSort(arr3)
        printArray(arr3)
    elif input2 == 2:
        quickSort(arr3, 0, len(arr3) - 1)
        printArray(arr3)
    elif input2 == 3:
        mergeSort(arr3, 0, len(arr3) - 1)
        printArray(arr3)