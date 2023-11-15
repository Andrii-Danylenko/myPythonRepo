class Score:
    __current = 0

    def __init__(self):
        self.__current = 0

    def getCurrent(self) -> int:
        return self.__current

    def incrementAndGet(self) -> int:
        self.__current += 1
        return self.__current

    def __str__(self):
        return f'Points: {self.__current}'
