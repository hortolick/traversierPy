from tkinter import *
from tkinter import ttk

from vues.TransStLaurent import TransStLaurentVue


window = Tk()
window.title("Transport St-Laurent")
window.geometry("640x480")

# Création d'un controleur de tab
tabControl = TransStLaurentVue(window)
tabControl.pack(expand=1, fill="both")

window.mainloop()