from Pracownik import Person


class Analyzer(Person):
    def __init__(self, id: int, wiek: int, stanowisko: str, imie: str, nazwisko: str):
        super().__init__(id, wiek, stanowisko, imie, nazwisko)