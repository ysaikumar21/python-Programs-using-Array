def find_second_largest_second_smallest(arr):
    if len(arr)<2:
        raise ValueError("Array must have atleast 2 element")
    smallest=arr[0]
    largest=arr[0]
    second_smallest=float('inf')
    second_largest=float('-inf')
    for num in arr[1:]:
        if num < smallest:
            second_smallest=smallest
            smallest=num
        elif num < second_smallest:
            second_smallest=num
        if num > largest:
            second_largest=largest
            largest=num
        elif num > second_largest:
            second_largest=num
    return second_smallest,second_largest
arr=[1,2,3,9,8,7]
second_smallest,second_largest = find_second_largest_second_smallest(arr)
print(f'Second_smallest : {second_smallest}')
print(f'Second_largest : {second_largest}')

            