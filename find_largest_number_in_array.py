
def find_largest_num_in_array(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    largest=arr[0]
    for num in arr[1:]:
        if num > largest:
            largest=num
    return largest
arr=[9,4,6,7,8,5,3]
result=find_largest_num_in_array(arr)
print(result)

