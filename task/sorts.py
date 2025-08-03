def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr1 = [6, 3, 1, 6, 2, 8]
arr2 = [5, 1, 2, 3, 8, 4]
arr3 = [7, 2, 1, 8, 6, 3]

print("Using Bubble Sort:")
bubbleSort(arr1)
print(arr1)

print("Using Selection Sort:")
selectionSort(arr2)
print(arr2)

print("Using Insertion Sort:")
insertionSort(arr3)
print(arr3)
