from entities.position import Position


class Move:
    def __init__(self, origin: Position, destiny: Position) -> None:
        self.__origin = origin
        self.__destiny = destiny

    @property
    def origin(self) -> Position:
        return self.__origin

    @property
    def destiny(self) -> Position:
        return self.__destiny

    @origin.setter
    def origin(self, value: Position) -> None:
        if isinstance(value, Position):
            self.__origin = value

    @destiny.setter
    def destiny(self, value: Position) -> None:
        if isinstance(value, Position):
            self.__destiny = value
