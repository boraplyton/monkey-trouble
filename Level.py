import numpy as np
import random

bloc = [
    [],
    [(0, 0), (0, 1), (0, 3), (0, 5), (0, 7), (0, 8),
     (1, 0), (1, 1), (1, 7), (1, 8),
     (5, 0), (5, 1), (5, 7), (5, 8),
     (6, 0), (6, 1), (6, 7), (6, 8),
     (7, 0), (7, 1), (7, 2), (7, 3), (7, 6), (7, 7), (7, 8)],
    [(0, 0), (0, 1), (0, 2), (0, 6), (0, 7), (0, 8),
     (1, 0), (1, 1), (1, 7), (1, 8),
     (2, 0), (2, 8),
     (6, 0), (6, 8),
     (7, 0), (7, 1), (7, 7), (7, 8),
     (8, 0), (8, 1), (8, 2), (8, 6), (8, 7), (8, 8)]
]
level_size = (
    (6, 9),
    (8, 9),
    (9, 9)
)


class Level:
    __levels_size = []

    def __init__(self, level_number):
        self.__matrix = None
        self.__levels_number = level_number
        self.__dim = level_size[level_number]
        self.__levels_size.append(self.__dim)
        self.__bloc = bloc[level_number]
        self.__create_level()

    def __create_level(self):
        self.__matrix = self.__rand_append_matrix()
        count = 0
        while self.__check_match():
            count += 1
            self.__matrix = self.__rand_append_matrix()
            print(count)

    def __rand_append_matrix(self):
        result = np.zeros(self.__dim)
        for i in range(self.__dim[0]):
            for j in range(self.__dim[1]):
                if (i, j) not in self.__bloc:
                    result[i][j] = random.randint(1, 5)
        return result

    def __check_match(self):
        # Check row
        for i in range(self.__dim[0]):
            streak = 1
            for j in range(1, self.__dim[1]):
                if self.__matrix[i][j] == self.__matrix[i][j - 1] and self.__matrix[i][j] != 0:
                    streak += 1
                    if streak >= 3:
                        return True
                else:
                    streak = 1

        # Check column
        for i in range(self.__dim[1]):
            streak = 1
            for j in range(1, self.__dim[0]):
                if self.__matrix[j][i] == self.__matrix[j - 1][i] and self.__matrix[j][i] != 0:
                    streak += 1
                    if streak >= 3:
                        return True
                else:
                    streak = 1
        return False

    def move_col(self, index, delta):
        matrix_copy = self.__matrix.copy()
        if delta < 0:
            orientation = 'up'
        else:
            orientation = 'down'
        for i in range(abs(delta)):
            self.move_column_single(index, orientation)
        if self.__check_match():
            self.delete_duplicates()
            return 100
        else:
            self.__matrix = matrix_copy
            return 0

    def move_row(self, index, delta):
        matrix_copy = self.__matrix.copy()
        if delta < 0:
            orientation = 'left'
        else:
            orientation = 'right'
        for i in range(abs(delta)):
            self.move_row_single(index, orientation)
        if self.__check_match():
            self.delete_duplicates()
            return 100
        else:
            self.__matrix = matrix_copy
            return 0

    def move_column_single(self, index, orientation):
        """
        :param index:
        :param orientation: "up", "down"
        Перемещение столбца вверх или вниз на одну позицию
        """

        column = list(self.__matrix.T[index])

        number_of_zeros_in_front, number_of_zeros_in_back = self.number_of_zeros(column)

        if orientation == "up":
            remade_column = [0 for _ in range(number_of_zeros_in_front)]
            if number_of_zeros_in_back != 0:
                remade_column += column[number_of_zeros_in_front + 1:-number_of_zeros_in_back]
            else:
                remade_column += column[number_of_zeros_in_front + 1:]
            remade_column += [column[0 + number_of_zeros_in_front]]
            remade_column += [0 for _ in range(number_of_zeros_in_back)]
        else:
            remade_column = column[-1 - number_of_zeros_in_back]
            remade_column = np.append(remade_column, column[:-1 + number_of_zeros_in_back])
        self.__matrix = self.__matrix.T
        self.__matrix[index] = remade_column
        self.__matrix = self.__matrix.T

    def move_row_single(self, index, orientation):
        """
        :param index:
        :param orientation: "left", "right"
        Перемещение строки вправо или влево
        """
        if self.__levels_number == 2 and index == 0:
            return

        column = self.__matrix[index]

        number_of_zeros_in_front, number_of_zeros_in_back = self.number_of_zeros(column)

        if orientation == "left":
            remade_column = column[1 + number_of_zeros_in_front:]
            remade_column = np.append(remade_column, column[number_of_zeros_in_front])
        else:
            remade_column = column[-1 - number_of_zeros_in_back]
            remade_column = np.append(remade_column, column[:-1 - number_of_zeros_in_back])
        self.__matrix[index] = remade_column

    @staticmethod
    def number_of_zeros(arr):
        number_of_zeros_in_front = 0
        number_of_zeros_in_back = 0
        for i in arr:
            if i == 0:
                number_of_zeros_in_front += 1
            else:
                break
        for i in np.flip(arr):
            if i == 0:
                number_of_zeros_in_back += 1
            else:
                break
        return number_of_zeros_in_front, number_of_zeros_in_back
        pass

    @property
    def size(self):
        return self.__dim

    @property
    def matrix(self):
        return self.__matrix

    def delete_duplicates(self):
        while self.__check_match():
            self.delite()

    def delite(self):
        matrix = self.__matrix
        # находим последовательности трех и более одинаковых элементов
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1] - 2):
                if matrix[i, j] == matrix[i, j + 1] == matrix[i, j + 2]:
                    matrix[i, j:j + 3] = np.nan
                elif j < matrix.shape[1] - 3 and matrix[i, j] == matrix[i, j + 1] == matrix[i, j + 2] == matrix[
                    i, j + 3]:
                    matrix[i, j:j + 4] = np.nan

        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0] - 2):
                if matrix[j, i] == matrix[j + 1, i] == matrix[j + 2, i]:
                    matrix[j:j + 3, i] = np.nan
                elif j < matrix.shape[0] - 3 and matrix[j, i] == matrix[j + 1, i] == matrix[j + 2, i] == matrix[
                    j + 3, i]:
                    matrix[j:j + 4, i] = np.nan

        # заполняем пустые места рандомными значениями
        matrix[np.isnan(matrix)] = np.random.randint(1, 5, size=np.sum(np.isnan(matrix)))
        self.__matrix = matrix
