
#lab 1
def find_leaders(arr):
    n = len(arr)
    leaders = []

    
    max_right = arr[n - 1]
    leaders.append(max_right)

  
    for i in range(n - 2, -1, -1):
        
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

   
    leaders.reverse()

    return leaders
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders(arr)
print("Leaders in the array:", result)





#lab 1
def alternate_sort(arr):
    
    arr.sort()

    left, right = 0, len(arr) - 1

    result = []

    while left <= right:
        result.append(arr[right])
        right -= 1

        if left <= right:
            result.append(arr[left])
            left += 1

    return result

input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
output_sequence = alternate_sort(input_array)
print("Input array:", input_array)
print("Alternately sorted sequence:", output_sequence)