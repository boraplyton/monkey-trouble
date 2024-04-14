import numpy as np
import random


class Level:
    __levels_size = []

    def __init__(self, level_number, level_size, bloc=None):
        if bloc is None:
            bloc = []
        self.__matrix = None
        self.__levels_number = level_number
        self.__dim = level_size
        self.__levels_size.append(level_size)
        self.__bloc = bloc

    def create_level(self):
        self.__matrix = self.__rand_append_matrix()
        while self.__check_match():
            self.__matrix = self.__rand_append_matrix()

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

        # Check column
        for i in range(self.__dim[1]):
            streak = 1
            for j in range(1, self.__dim[0]):
                if self.__matrix[j][i] == self.__matrix[j - 1][i] and self.__matrix[j][i] != 0:
                    streak += 1
            if streak >= 3:
                return True
        return False

    def get_matrix(self):
        return self.__matrix

