from settings import BOARD_SIZE


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, value: int) -> None:
        self.__x = value

    @y.setter
    def y(self, value: int) -> None:
        self.__y = value

    def get_axis(self) -> tuple[int, int]:
        return self.__x, self.__y

    def valid_coordinate(self) -> bool:
        for axis in (self.__x, self.__y):
            if axis > (BOARD_SIZE - 1) or axis < 0:
                return False
        return True
