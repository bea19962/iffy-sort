#finds the biggest number
def largest(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
    
#finds the smallest number
def smallest(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

def silly_sort(arr):
    if not arr:
        return []
    else:
        max_val = largest(arr)
        min_val = smallest(arr)
        sorted_array = []
        #loops the biggest number of times and checks if the number exists in the array
        for i in range(min_val, max_val + 1):
            if i in arr:
                sorted_array.append(i)
        return sorted_array

# Define the array
arr = [-1, 4, -8, -3]

# Print the result
print(silly_sort(arr))
