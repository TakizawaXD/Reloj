import tkinter as tk
from time import strftime
from tkinter import ttk
def actualizar_reloj():
    tiempo_actual = strftime("%H:%M:%S")
    if etiqueta_hora.cget("text") != tiempo_actual:
        etiqueta_hora.after(200, animar_cambio, tiempo_actual, 0)  
    etiqueta_hora.after(1000, actualizar_reloj)
def animar_cambio(nuevo_texto, paso):
    actual_texto = etiqueta_hora.cget("text")
    if paso < len(nuevo_texto):
        etiqueta_hora.config(text=actual_texto[:paso] + nuevo_texto[paso:])
        etiqueta_hora.after(50, animar_cambio, nuevo_texto, paso + 1)
    else:
        etiqueta_hora.config(text=nuevo_texto)
        animar_color()
def animar_color():
    colores = ["#AEDFF7", "#A7D6A0", "#F7D8A7", "#F2A7A7"]
    color_actual = etiqueta_hora.cget("fg")
    indice = colores.index(color_actual) if color_actual in colores else 0
    etiqueta_hora.config(fg=colores[(indice + 1) % len(colores)])
ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("500x300")
ventana.resizable(False, False)
ventana.configure(bg="#2B2B2B")
etiqueta_hora = tk.Label(
    ventana,
    text="",
    font=("DS-Digital", 72),
    fg="#AEDFF7",
    bg="#2B2B2B"
)
etiqueta_hora.pack(expand=True)
estilo = ttk.Style()
estilo.theme_use("clam")
ventana.option_add("*Label.Font", "Helvetica 16")
ventana.option_add("*Label.Foreground", "#D9D9D9")
actualizar_reloj()
ventana.mainloop()