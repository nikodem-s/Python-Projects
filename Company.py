import pprint

import psycopg2

from Analyzer import Analyzer
from Programmer import Programer


def connect_database():
    connection = psycopg2.connect("dbname=Firma user=postgres password=admin")
    return connection


def close_connection():
    connect_database().close()


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS pracownicy(
            id INT PRIMARY KEY,
            imie VARCHAR(25),
            nazwisko VARCHAR(25),
            wiek INT,
            stanowisko VARCHAR(25)
        )
        """
    )
    cur = connect_database().cursor()
    cur.execute(commands)
    cur.close()
    connect_database().commit()
    close_connection()


def insert_into_database(id, imie, nazwisko, wiek, pozycja):
    connection = psycopg2.connect("dbname=Firma user=postgres password=admin")
    sql = """INSERT INTO "Firma".public.pracownicy(id, imie, nazwisko, wiek, stanowisko) VALUES(%s,%s,
                %s,%s,%s) """
    cur = connection.cursor()

    record_to_insert = (int(id),
                        str(imie),
                        str(nazwisko),
                        int(wiek),
                        str(pozycja),
                        )
    cur.execute(sql, record_to_insert)
    cur.close()
    connection.commit()


def delete_from_database(id):
    connection = psycopg2.connect("dbname=Firma user=postgres password=admin")
    cur = connection.cursor()
    sql = """DELETE FROM "Firma".public.pracownicy WHERE id = %s"""
    cur.execute(sql, (id, ))
    cur.close()
    connection.commit()
    connection.close()


class Company:
    def __init__(self):
        self.lista = []

    def create_worker(self):
        mID = int(input('Podaj ID:'))
        Imie = str(input('Podaj imie:'))
        Nazwisko = str(input('Podaj nazwisko:'))
        Wiek = int(input('Podaj wiek:'))
        Stanowisko = str(input('Podaj stanowisko:'))
        if self.__check_existance(mID):
            if Stanowisko.lower() == "analityk":
                self.lista.append(Analyzer(mID, Wiek, Stanowisko, Imie, Nazwisko))
                insert_into_database(mID, Imie, Nazwisko, Wiek, Stanowisko)
            elif Stanowisko.lower() == "programista":
                self.lista.append(Programer(mID, Wiek, Stanowisko, Imie, Nazwisko))
                insert_into_database(mID, Imie, Nazwisko, Wiek, Stanowisko)
            else:
                print('Firma nie przyjmuje tego typu pracownikow!(Tylko Analitycy/Programisci)')
        else:
            print('Pracownik o podanym ID istnieje! ID jest cecha unikalną!')

    def __check_existance(self, ID):  # chce aby byla prywatna
        for instance in self.lista:
            if ID == instance.id:
                return True
        return False

    def read_database(self):
        connection = psycopg2.connect("dbname=Firma user=postgres password=admin")
        db_cursor = connection.cursor()
        sql_select = """SELECT * FROM "Firma".public.pracownicy"""
        db_cursor.execute(sql_select)
        self.lista = db_cursor.fetchall()

    # methods to sort

    def sort_by_id(self):
        if len(self.lista) > 0:
            self.lista = sorted(self.lista, key=lambda instance: instance.id)
        else:
            print('Lista jest pusta!')

    def sort_by_age(self):
        if len(self.lista) > 0:
            self.lista = sorted(self.lista, key=lambda instance: instance.wiek)
        else:
            print('Lista jest pusta!')

    def sort_by_surname(self):
        if len(self.lista) > 0:
            self.lista = sorted(self.lista, key=lambda instance: instance.nazwisko)
        else:
            print('Lista jest pusta!')

    def sort_by_position(self):
        if len(self.lista) > 0:
            self.lista = sorted(self.lista, key=lambda instance: instance.stanowisko)
        else:
            print('Lista jest pusta!')

    def fire_workers(self):
        mID = int(input('Podaj ID pracownika do zwolnienia: '))
        delete_from_database(mID)
        self.read_database() # aktualizuje liste
