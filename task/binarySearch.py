def search_binary(arr, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return search_binary(arr, l, mid - 1, x)
        else:
            return search_binary(arr, mid + 1, r, x)
    else:
        return -1

x = int(input("Enter number you want to find: "))
arr = [10, 20, 30, 40, 50, 80]
result = search_binary(arr, 0, len(arr) - 1, x)
if result != -1:
    print("The element is at index:", result)
else:
    print("Element not found")


