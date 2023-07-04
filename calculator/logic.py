import time
import operations

class Logic:

    def interview(self):

        operacje = operations.Operations()
        try:
            liczba1 = int(input("\nPodaj pierwszą liczbę:"))
            liczba2 = int(input("Podaj drugą liczbę:"))
            dzialanie = int(input("Co zamierzasz zrobić?:\n"
                                  "1. Dodawać\n"
                                  "2. Odejmować\n"
                                  "3. Mnożyć\n"
                                  "4. Dzielić\n"
                                  "5. Potęgować\n"
                                  "6. Pierwiastkować\n"))
        except ValueError:
            exit("Podaj liczbę całkowitą!")

        if int(dzialanie) == 1:
            self.pisanie(operacje.dodawanie(liczba1, liczba2))
        elif int(dzialanie) == 2:
            self.pisanie(operacje.odejmowanie(liczba1, liczba2))
        elif int(dzialanie) == 3:
            self.pisanie(operacje.mnozenie(liczba1, liczba2))
        elif int(dzialanie) == 4:
            self.pisanie(operacje.dzielenie(liczba1, liczba2))
        elif int(dzialanie) == 5:
            self.pisanie(operacje.potegowanie(liczba1, liczba2))
        elif int(dzialanie) == 6:
            self.pisanie(operacje.pierwiastkowanie(liczba1, liczba2))

    def pisanie(self, tekst):

        opisanie = "Wynik działania: " + str(tekst)

        for znak in opisanie:
            print(znak, end='', flush=True)
            time.sleep(0.1)
