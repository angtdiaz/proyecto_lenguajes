import tkinter as tk
from AnalizadorSintactico import aSintactico
from AnalizadorLexico import aLexico
from tkinter import ttk

class Ventana:

    # Le pasamos el componente raíz al constructor
    def __init__(self, root):

        # Establecemos el tamaño de la raíz
        root.geometry("900x700")
        root.configure(background='#0B0B0B')
        # Añadimos titulo
        self.titulo = tk.Label(
            root, text="Analizador Léxico y Sintáctico de Lenguaje de Programación: Ruby")
        self.titulo.place(x=100, y=20)
        self.titulo.config(fg="black",
                           font=("Arial", 22))
        # Añadimos entrada
        self.Labelentrada = tk.Label(root, text="Ingrese su expresion:  ")
        self.Labelentrada.place(x=10, y=70)
        self.Labelentrada.config(fg="black",
                                 font=("Arial", 12))
        self.txt = tk.Text(root, width=70)
        self.txt.place(x=180, y=70)
        self.txt.focus()
        # Añadimos botones
        self.buttonLexico = tk.Button(
            root, text="Analizar Léxico", command=self.aLexico)
        self.buttonLexico.place(x=100, y=530)
        self.buttonLexico.config(fg="white",  # Foreground
                                 bg="gray",  # Background
                                 font=("Verdana", 18))
        self.buttonSintactico = tk.Button(
            root, text="Analizar Sintáctico", command=self.aSintactico)
        self.buttonSintactico.place(x=300, y=530)
        self.buttonSintactico.config(fg="white",  # Foreground
                                     bg="gray",  # Background
                                     font=("Verdana", 18))

        self.buttonLimpiar = tk.Button(
            root, text="Limpiar", command=self.limpiar, )
        self.buttonLimpiar.place(x=100, y=600)
        self.buttonLimpiar.config(fg="black",  # Foreground
                                  bg="white",  # Background
                                  font=("Verdana", 18))

    # definicion de funciones

    def aLexico(self):
        entrada = self.txt.get("1.0","end-1c")
        resultados = aLexico(entrada)
        if resultados == "":
            ventanaNueva("Error, no se reconocio ningun token")

        else:
            ventanaNueva(resultados)

    def aSintactico(self):
        print("Se realizara un analizador sintáctico!")
        entrada = self.txt.get("1.0","end-1c")
        print(entrada)
        resultados= aSintactico(entrada)
        if not resultados:
            ventanaNueva(["NO HAY ERRORES"])
        else:
            ventanaNueva(resultados)

    def limpiar(self):
        self.txt.delete("1.0", "end-1c")

# Metodo de Nueva ventana para mostrar si lo ingresado e correcto o no


def ventanaNueva(resultados):
    toplevel = tk.Toplevel(width=100)
    container = tk.Frame(toplevel)
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(
        container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    labelresult = tk.Label(scrollable_frame, text=resultados, justify=tk.LEFT)
    labelresult.pack()
    labelresult.config(fg="blue",
                       bg="white",
                       font=("Arial", 12)
                       )

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
window = Ventana(win)
win.mainloop()