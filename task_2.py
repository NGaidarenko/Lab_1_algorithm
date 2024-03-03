def transpose_matrix(matrix):
    """
    Функция для транспонирования матрицы.
    """

    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for i in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def multiply_matrix(matrix1, matrix2):
    """
    Функция для умножения матриц.
    """

    # Проверка на возможность перемножения
    if len(matrix1[0]) != len(matrix2):
        print("Невозможно умножить матрицы: неподходящий размер")
    result = [[0 for i in range(len(matrix2[0]))] for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def rank_of_matrix(matrix):
    """
    Функция для определения ранга матрицы.
    """

    rows = len(matrix)
    cols = len(matrix[0])
    rank = min(rows, cols)

    # Приводим матрицу к ступенчатому виду методом Гаусса
    for row in range(rank):
        if matrix[row][row] != 0:
            for col in range(row + 1, rows):
                ratio = matrix[col][row] / matrix[row][row]
                for i in range(rank):
                    matrix[col][i] -= ratio * matrix[row][i]
        else:
            reduce_rank = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    reduce_rank = False
                    break
            if reduce_rank:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]

    return rank


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
    print("\nВведите вторую матрицу:")
    matrix2 = input_matrix()

    print("\nТранспонированная первой матрицы:")
    print_matrix(transpose_matrix(matrix1))
    print("\nТранспонированная второй матрицы:")
    print_matrix(transpose_matrix(matrix2))

    print("\nРезультат умножения матриц:")
    print_matrix(multiply_matrix(matrix1, matrix2))

    print("\nРанг первой матрицы:", rank_of_matrix(matrix1))
    print("Ранг второй матрицы:", rank_of_matrix(matrix2))


"""
Пример ввода:
Введите количество строк матрицы: 2
Введите количество столбцов матрицы: 2
Введите элементы матрицы:
2 2
1 1

Введите вторую матрицу:
Введите количество строк матрицы: 2
Введите количество столбцов матрицы: 2
Введите элементы матрицы:
1 1
2 2
"""

main()
