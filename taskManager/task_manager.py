from taskManager.task import Task
import pickle


class Task_manager:

    def stworzZadanie(self, nazwa, opis, status):
        nowe_zadanie = Task(nazwa, opis, status)

        with open("zadania.pickle", "wb") as file:
            pickle.dump(nowe_zadanie, file)

    def wyswietlZadanie(self, Task):

        with open("zadania.pickle", "rb") as file:

    # TU SKOŃCZYŁEŚ

    def edytujZadanie(self, Task, nazwa, opis, status):
        Task.nazwa = nazwa
        Task.opis = opis
        Task.status = status

    # def usunZadanie(self, Task):
    #