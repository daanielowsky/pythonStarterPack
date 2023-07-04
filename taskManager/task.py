import time


class Task:

    def __init__(self, nazwa, opis, status):
        self.nazwa = nazwa;
        self.opis = opis;
        self.data = str(time.localtime().tm_mday + "." + time.localtime().tm_mon + "." + time.localtime().tm_year)
        self.status = status
