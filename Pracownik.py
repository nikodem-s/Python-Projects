class Person:

    # important methods
    def __init__(self, id: int, wiek: int, stanowisko: str, imie: str, nazwisko: str):
        self.__id = id
        self.__wiek = wiek
        self.__stanowisko = stanowisko
        self.__imie = imie
        self.__nazwisko = nazwisko

    def __repr__(self):
        return f"({self.__id}, '{self.__imie}', '{self.__nazwisko}', {self.__wiek}, '{self.__stanowisko}')"

    # getters of class, made them read-only / private
    @property
    def id(self):
        return self.__id

    @property
    def wiek(self):
        return self.__wiek

    @property
    def stanowisko(self):
        return self.__stanowisko

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko