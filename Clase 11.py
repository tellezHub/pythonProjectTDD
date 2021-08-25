from tkinter import *
from math import *

def Cilindro ():

    valor_Radio = float(dato1.get())
    valor_Altura = float(dato2.get())
    resultado = pi * (valor_Radio**2) * valor_Altura
    print("resultado del volumen del cilindro:", resultado)
    respuesta.config(text=resultado)
    dato_resultado.set(str(resultado))

# ----------Ventana------------
ven_ci = Tk()
ven_ci.title("Calcular volumen de un cilindro")
ven_ci.geometry("500x330")
# ----------etiqueta------------
titulo = Label(ven_ci, text="Calcular volumen de un Cilindro", fg="blue").place(x=30, y=10)
radio = Label(ven_ci, text="Ingrese el Radio:", fg="Red").place(x=80, y=80)
altura = Label(ven_ci, text="Ingrese la Altura:", fg="blue").place(x=80, y=120)
resul = Label(ven_ci, text="Resultado:", fg="blue").place(x=60, y=240)
respuesta = Label(ven_ci, text="")
respuesta.place(x=120, y=240)
# ----------Entry------------
dato1 = DoubleVar()
caja1 = Entry(ven_ci, textvariable=dato1, width=5)# el valor que ingresa radio
caja1.place(x=180, y=80)
dato2 = DoubleVar()
caja2 = Entry(ven_ci, textvariable=dato2, width=5)# el valor que ingresa Altura
caja2.place(x=180, y=120)
# ----------imagen------------
imagen_cilindro = PhotoImage(file="cilin.gif")
etiqueta_foto = Label(ven_ci, image=imagen_cilindro, width=200, height=250)
etiqueta_foto.image = imagen_cilindro
etiqueta_foto.place(x=280, y=50)
# ----------boton------------
botonC=Button(ven_ci,text="Calcular", command=Cilindro,width=10,height=2).place(x=60, y=180)

botonSalir=Button(ven_ci,text="Salir", command=quit,width=10,height=2).place(x=180, y=180)

# ----------Entry resultado------------
resul_entry = Label(ven_ci, text="Resultado:", fg="#9D671E").place(x=60, y=270)

dato_resultado = IntVar()
caja_resultado = Entry(ven_ci, textvariable=dato_resultado, width=20)
caja_resultado.place(x=140, y=270)

ven_ci.mainloop()
