#lab 5
def find_row_with_most_ones(matrix):
    max_ones_count = -1
    row_with_most_ones = -1

    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            row_with_most_ones = i

    return row_with_most_ones

num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

matrix = []
for _ in range(num_rows):
    row = list(map(int, input(f"Enter row (space-separated) {_ + 1}: ").split()))
    matrix.append(row)

result_row = find_row_with_most_ones(matrix)

if result_row != -1:
    print(f"The row with the most ones is row {result_row + 1}.")
else:
    print("The matrix does not contain any ones.")




# lab 5
def sum_middle_row_and_column(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if num_rows > 0 else 0

    if num_rows % 2 == 1 and num_columns % 2 == 1:
        middle_row = matrix[num_rows // 2]
        middle_column = [matrix[i][num_columns // 2] for i in range(num_rows)]

        sum_middle_row = sum(middle_row)
        sum_middle_column = sum(middle_column)

        return sum_middle_row, sum_middle_column
    else:
        return None  
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_middle_row_and_column(matrix)

if result is not None:
    sum_middle_row, sum_middle_column = result
    print(f"Sum of the middle row: {sum_middle_row}")
    print(f"Sum of the middle column: {sum_middle_column}")
else:
    print("The matrix does not have a middle row and middle column.")

    