#lab 4
def interchange_diagonals(matrix):
    n = len(matrix)

    for i in range(n):
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

interchange_diagonals(matrix)

print("\nMatrix after Diagonal Interchange:")
for row in matrix:
    print(row)





#lab 4
def find_indices(arr, target):
    indices = []

    for i, num in enumerate(arr):
        if num == target:
            indices.append(i)

    return indices

input_array = [4, 2, 7, 1, 4, 9, 4, 5]
target_number = 4

result_indices = find_indices(input_array, target_number)

if result_indices:
    print(f"The target number {target_number} is found at indices: {result_indices}")
else:
    print(f"The target number {target_number} is not present in the array.")



