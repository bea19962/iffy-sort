#finds the biggest number
def largest(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def silly_sort(arr):
    if not arr:
        return []
    else:
        max_val = largest(arr)
        sorted_array = []  # Define sorted_array inside the function
        for i in range(1, max_val + 1):
            if i in arr:
                sorted_array.append(i)
        return sorted_array

# Define the array
arr = [1, 4, 8, 3,12,2,6,22,13]

# Print the result
print(silly_sort(arr))
