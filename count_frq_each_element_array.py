def Count_frequence_of_element_array(arr):
    frequencies={}
    for num in arr:
        if num in frequencies:
            frequencies[num]+=1
        else:
            frequencies[num]=1
    return frequencies
arr=[1,2,3,4,3,2,7,8,9,7] 
Count_elements=Count_frequence_of_element_array(arr)
print(Count_elements)  