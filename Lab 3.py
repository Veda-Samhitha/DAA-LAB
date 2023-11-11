#lab 3
original_array = [0, 0, 1, 2, 0, 1, 2, 2, 1]

unique_set = set(original_array)

unique_list = list(unique_set)

print("Original array:", original_array)
print("Array with duplicates removed:", unique_list)




#lab 3
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False

    slow_pointer = head
    fast_pointer = head.next

    while slow_pointer != fast_pointer:
        if not fast_pointer or not fast_pointer.next:
            return False

        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  

result = has_cycle(node1)
print("Does the linked list have a loop?", result)




#lab 3
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

input_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(input_array)
print("Original array:", input_array)
print("Sorted array using merge sort:", sorted_array)




#lab 3
def max_subarray_sum(arr):
    if not arr:
        return 0

    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(input_array)
print("Maximum sum of subarray:", result)


