from entities.board.coordenate import Coordenate


class Position:
    def __init__(self, value: int, coordenate: Coordenate):
        self.__value = value
        self.__coordenate = coordenate

    @property
    def value(self):
        return self.__value

    @property
    def coordenate(self):
        return self.__coordenate
