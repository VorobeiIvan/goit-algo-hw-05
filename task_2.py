def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    return iterations, upper_bound


sorted_arr = [1.1, 2.5, 3.3, 4.8, 6.2, 7.7, 9.0]
print(binary_search(sorted_arr, 4.8))  
print(binary_search(sorted_arr, 5.0))  

