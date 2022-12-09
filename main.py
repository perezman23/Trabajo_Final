from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------FUNCIONES------------------


def conexionBBDD():
    
    miConexion=sqlite3.connect("Usuario")
    miCursor=miConexion.cursor()
    
    try:
        
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ALTA_ALUMNO VARCHAR(50),
            LISTA_ALUMNO VARCHAR (20))''')
    
        messagebox.showinfo("BBDD", "BBDD creada con exito")            
    
    except:
        messagebox.showwarning("¡ATENCION!", "lA BBDD ya existe")    


def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Deseas salir de la Aplicación ?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    
    miId.set("")
    miAlta.set("")
    miLista.set("")
    textoComentario.delete(1.0, END)
    
def crear():
    miConexion=sqlite3.connect("Usuario")

    miCursor=miConexion.cursor()
    
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'" + miId.get() +
    "','" + miAlta.get() + 
    "','" + miLista.get() +
    "','" + textoComentario.get("1.0", END) + "')")
    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Registro insertado con exito")

root=Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=1000, height=400)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label= "BBDD",menu=bbddMenu)
barraMenu.add_cascade(label= "Borrar",menu=borrarMenu)
barraMenu.add_cascade(label= "Crud",menu=crudMenu)
barraMenu.add_cascade(label= "Ayuda",menu=ayudaMenu)



miFrame=Frame(root, bg= "blue")
miFrame.pack()

miId=StringVar()
miAlta=StringVar()
miLista=StringVar()





cuadroID= Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroAlta= Entry(miFrame, textvariable=miAlta)
cuadroAlta.grid(row=1, column=1, padx=10, pady=10)
cuadroAlta.config(fg="red", justify="right")

cuadroLista=Entry(miFrame, textvariable=miLista)
cuadroLista.grid(row=2, column=1, padx=10, pady=10)




textoComentario=Text(miFrame, width=26, height=5)
textoComentario.grid(row=2, column=1, padx=10, pady= 10)
scrollvert=Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=5 , column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)

#-------------------label-------------------------#

idLabel=Label(miFrame, text="Ingrese un Número:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

altalabel=Label(miFrame, text="Alta del Alumno:")
altalabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

listalabel=Label(miFrame, text="Lista de Alumnos:")
listalabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)



root.mainloop()