from settings import BOARD_SIZE


class Coordenate:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_axis(self):
        return self.__x, self.__y

    def valid_coordenate(self):
        for axis in (self.__x, self.__y):
            if axis > (BOARD_SIZE - 1) or axis < 0:
                return False
        return True
