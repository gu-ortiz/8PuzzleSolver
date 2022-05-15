from entities.board.coordenate import Coordenate


class Move:
    def __init__(self, origin: Coordenate, destiny: Coordenate):
        self.__origin = origin
        self.__destiny = destiny

    @property
    def origin(self):
        return self.__origin

    @property
    def destiny(self):
        return self.__destiny
