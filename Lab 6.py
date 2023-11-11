#lab 6
def sort_matrix_and_replace_diagonals(matrix):
    flattened_matrix = [element for row in matrix for element in row]

    flattened_matrix.sort()

    sorted_matrix = [flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(flattened_matrix), len(matrix[0]))]

    for i in range(len(matrix)):
        sorted_matrix[i][i] = 0

    for i in range(len(matrix)):
        sorted_matrix[i][len(matrix) - 1 - i] = 0

    return sorted_matrix

matrix = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

sorted_and_replaced_matrix = sort_matrix_and_replace_diagonals(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nSorted Matrix with Diagonal Replacement:")
for row in sorted_and_replaced_matrix:
    print(row)




#lab 6
def multiply(a, b):
    result = 0

    sign = 1
    if a < 0:
        a = -a
        sign = -sign
    if b < 0:
        b = -b
        sign = -sign

    for _ in range(b):
        result += a

    result *= sign

    return result


num1 = 5
num2 = 4
result = multiply(num1, num2)

print(f"The product of {num1} and {num2} is: {result}")
