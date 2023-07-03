import math


class Operations:

    def dodawanie(self, liczba1, liczba2):
        wynik = liczba1 + liczba2
        return wynik

    def odejmowanie(self, liczba1, liczba2):
        wynik = liczba1 - liczba2
        return wynik
    def mnozenie(self, liczba1, liczba2):
        wynik = liczba1 * liczba2
        return wynik

    def dzielenie(self, liczba1, liczba2):
        try:
            if liczba1 % liczba2 != 0:
                wynik = str(liczba1 / liczba2) + ", lub " + str(math.floor(liczba1 / liczba2)) + " oraz " + str(liczba1 % liczba2) + " reszty."
                return wynik
            else:
                wynik = str(liczba1 / liczba2)
                return wynik
        except ZeroDivisionError:
            exit("Nie dzielimy przez 0")

    def potegowanie(self, liczba1, liczba2):
        wynik = liczba1 ** liczba2
        return wynik

    def pierwiastkowanie(self, liczba1, liczba2):
        try:
            wynik = math.sqrt(liczba1 - liczba2)
            return wynik

        except ValueError:
            exit("Nieprawidłowa wartość do obliczenia pierwiastka.")