from entities.coordenate import Coordenate


class Position:
    def __init__(self, value: int, coordenate: Coordenate) -> None:
        self.__value = value
        self.__coordenate = coordenate

    @property
    def value(self) -> int:
        return self.__value

    @property
    def coordenate(self) -> Coordenate:
        return self.__coordenate

    @value.setter
    def value(self, value: int) -> None:
        if isinstance(value, int):
            self.__value = value

    @coordenate.setter
    def coordenate(self, value: Coordenate) -> None:
        if isinstance(value, Coordenate):
            self.__coordenate = value
