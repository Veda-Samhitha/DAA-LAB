
#lab 2
def find_triplets_with_sum(arr, target_sum):
    n = len(arr)
    triplets = []

    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

arr = [1, 4, 2, 8, 3, 9, 6]
target_sum = 15
result_triplets = find_triplets_with_sum(arr, target_sum)
print(f"Triplets with sum {target_sum}: {result_triplets}")




#lab 2
def counting_sort(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

input_array = [0, 0, 1, 2, 0, 1, 2, 2, 1]
sorted_array = counting_sort(input_array)
print("Input array:", input_array)
print("Sorted array using counting sort:", sorted_array)
