def remove_duplicates(arr):
    if not arr:
        return []
    
    unique_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])
    
    return unique_arr

arr = sorted(map(int, input("Enter sorted array elements separated by space: ").split()))
unique_array = remove_duplicates(arr)
print("Sorted array with duplicates removed:", unique_array)
