
# Demonstruje użycie klasy w programie wykorzystującym Tkinter

from tkinter import *

class Application(Frame):
    """ Aplikacja oparta na GUI z trzema przyciskami. """

    #zdefiniowanie konstrukrora:
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Tworzenie trzech przycisków, które nie mają obsługi zdarzeń. """
        # utwórz pierwszy przycisk
        self.bttn1 = Button(self, text = "Brak zdarzenia1!")
        self.bttn1.grid()

        # utwórz drugi przycisk
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Brak zdarzenia2!")

        # utwórz trzeci przycisk
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "To samo Brak zdarzenia3!"

# część główna
root = Tk()
root.title("Przyciski v2")
root.geometry("300x100")
app = Application(root)
root.mainloop()
