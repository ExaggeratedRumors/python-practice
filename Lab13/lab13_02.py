from tkinter import *


# część główna
root = Tk()
#ustawienie tytułu okna głównego:
root.title("Interfejs GUI")
# rozmiar wyrażony w pikselach:
root.geometry("300x100")
# uruchamia pętlę zdarzeń obiektu root:

#-----------------
# utworzenie w oknie ramki jako pojemnik na inne widżety tzn. przechowuje inne elementy:
# za każdym razem, gdy tworzony jest nowy widżet należy przekazać do jego konstruktora obiekt nadrzędny - u nas root:
app = Frame(root)

#Metodę grid() posiadają wszystkie widżety.
# Jest ona związana z menedżerem układów (ang. layout manager), który umożliwia rozplanowanie położenia widżetów.
app.grid()

# utwórz w ramce etykietę:
lbl = Label(app, text = "Jestem etykietą!")
# przy przekazaniu obiektu app do konstruktora obiektu klasy Label powoduje to,
# że ramka, do której odwołuje się zmienna app, staje się obiektem nadrzędnym widżetu Label.


lbl.grid()      #To zapewnia widoczność etykiety.


root.mainloop()
