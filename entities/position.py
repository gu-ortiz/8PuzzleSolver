from entities.coordinate import Coordinate


class Position:
    def __init__(self, value: int, coordinate: Coordinate) -> None:
        self.__value = value
        self.__coordinate = coordinate

    @property
    def value(self) -> int:
        return self.__value

    @property
    def coordinate(self) -> Coordinate:
        return self.__coordinate

    @value.setter
    def value(self, value: int) -> None:
        self.__value = value

    @coordinate.setter
    def coordinate(self, value: Coordinate) -> None:
        self.__coordinate = value
