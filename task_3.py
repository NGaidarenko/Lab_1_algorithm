import numpy


def transpose_matrix(matrix):
    """
    Функция для транспонирования матрицы
    """

    tr_matrix = numpy.transpose(matrix)
    print_matrix(tr_matrix)


def multiply_matrix(matrix1, matrix2):
    """
    Функция для умножения матриц.
    """
    if len(matrix1[0]) != len(matrix2):
        print("Невозможно умножить матрицы: неподходящий размер")
    else:
        result = numpy.matmul(matrix1, matrix2)
        print_matrix(result)


def rank_of_matrix(matrix):
    """
    Функция для определения ранга матрицы.
    """
    return numpy.linalg.matrix_rank(matrix)



def print_matrix(matrix):
    """
    Функция для вывода матрицы на экран.
    """

    for row in matrix:
        print(" ".join(map(str, row)))


def input_matrix():
    """
    Функция для ввода матриц с клавиатуры.
    """
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = []
    print("Введите элементы матрицы: ")
    for i in range(rows):
        row = list(map(float, input().split(" ")))
        matrix.append(row)

    return matrix


def main():
    print("Введите первую матрицу:")
    matrix1 = input_matrix()
    print("\nВведите вторую матрицу: ")
    matrix2 = input_matrix()

    print("\nТранспонирование первой матрицы")
    transpose_matrix(matrix1)
    print("\nТранспонирование второй матрицы")
    transpose_matrix(matrix2)

    print("\nРезультат умножения матриц:")
    multiply_matrix(matrix1, matrix2)

    print("\nРанг первой матрицы: ", rank_of_matrix(matrix1))
    print("\nРанг второй матрицы: ", rank_of_matrix(matrix2))