from heapq import heappush, heappop

def merge_k_sorted_arrays(arrs):
    min_heap = []
    result = []  
    for i, arr in enumerate(arrs):
        if arr:
            heappush(min_heap, (arr[0], i, 0))
    while min_heap:
        val, arr_idx, idx = heappop(min_heap)
        result.append(val)    
        idx += 1
        if idx < len(arrs[arr_idx]):
            heappush(min_heap, (arrs[arr_idx][idx], arr_idx, idx))
    return result

num_arrays = int(input("Enter the number of arrays (K): "))
array_size = int(input("Enter the size of each array (N): "))

arrays = []
for i in range(num_arrays):
    array = list(map(int, input(f"Enter elements of array {i+1}: ").split()))
    array.sort()  
    arrays.append(array)

merged_result = merge_k_sorted_arrays(arrays)
print("Merged sorted array:", merged_result)
