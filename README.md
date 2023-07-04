# pythonStarterPack:

## 1. Interaktywny Kalkulator w Pythonie
Ten projekt to prosty interaktywny kalkulator napisany w Pythonie. Dzięki niemu możesz wykonywać podstawowe operacje matematyczne, takie jak dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie i pierwiastkowanie. Kalkulator został zaprojektowany tak, aby być jak najbardziej przyjaznym dla użytkownika, z interfejsem konsolowym, który prowadzi przez cały proces obliczeń.

### Struktura projektu
Projekt składa się z trzech głównych plików:

- main.py - Główny plik, który uruchamia interfejs użytkownika kalkulatora. Jest to nieskończona pętla, która ciągle pyta użytkownika o wprowadzenie danych i wykonywanie obliczeń.

- logic.py - Plik ten zawiera klasę Logic, która kontroluje przepływ danych między użytkownikiem a kalkulatorem. Ta klasa pobiera dane od użytkownika, przekazuje je do odpowiedniej metody w klasie Operations i zwraca wyniki do użytkownika.

- operations.py - Ten plik zawiera klasę Operations, która zawiera metody do wykonywania operacji matematycznych. Każda metoda przyjmuje dwa argumenty (liczby) i zwraca wynik danej operacji.

### Jak korzystać z kalkulatora
1. Sklonuj repozytorium na swój komputer.
2. Upewnij się, że masz zainstalowaną odpowiednią wersję Pythona (3.6 lub nowszą).
3. Otwórz terminal i przejdź do folderu projektu.
4. Uruchom plik main.py wpisując w terminalu: python main.py
5. Postępuj zgodnie z instrukcjami na ekranie.