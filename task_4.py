import numpy as np
import timeit


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for i in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det += (-1) ** i * matrix[0][i] * determinant(minor)
        return det


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        print("Матрица не обратима")
        return None
    else:
        n = len(matrix)
        adjoint = []
        for i in range(n):
            adjoint_row = []
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]
                adjoint_row.append((-1) ** (i + j) * determinant(minor))
            adjoint.append(adjoint_row)
        adjoint = transpose(adjoint)
        inverse = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]
        return inverse


def inverse_numpy(matrix):
    try:
        return np.linalg.inv(np.array(matrix))
    except np.linalg.LinAlgError:
        print("Матрица не обратима")


def input_matrix():
    """
    Функция для ввода матрицы с клавиатуры.
    """
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = []
    print("Введите элементы матрицы:")

    for i in range(rows):
        row = list(map(float, input().split(" ")))
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    """
    Функция для вывода матрицы на экран.
    """

    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    print("Введите первую матрицу:")
    matrix1 = input_matrix()

    print("\nВозведение первой матрицы в степень -1:")
    print_matrix(inverse(matrix1))

    print("\nВзведение первой матрицы в степень -1 используя numpy:")
    print_matrix(inverse_numpy(matrix1))
