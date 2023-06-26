# Напишите функцию для транспонирования матрицы


def transpose_(lst: list) -> list:
    res_list = []
    for i in range(len(lst[0])):
        temp_lst = []
        for j in range(len(lst)):
            temp_lst.append(lst[j][i])
        res_list.append(temp_lst)
    return res_list

def print_matrix(matrix: list):
    for i in matrix:
        print(' '.join(map(str, i)))


matrix = [[1, 2, 3, 20],
          [4, 5, 6, 21],
          [7, 8, 9, 22]]


new_matrix = transpose_(matrix)
print_matrix(matrix)
print()
print_matrix(new_matrix)

