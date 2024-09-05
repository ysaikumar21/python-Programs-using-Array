def find_smallest_num_in_array(num):
    if not num:
        raise ValueError("Array cannot be empty")
    smallest=num[0]
    for arr in num[1:]:
        if arr < smallest:
            smallest=arr
    return smallest
num=[2,3,5,8,9,5,1]
result=find_smallest_num_in_array(num)
print(result)