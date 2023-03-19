import tkinter as tk
from tkinter import ttk, Menu, END, StringVar, IntVar, DoubleVar
import sqlite3

main = tk.Tk()

# ------------------
#       Colores
# ------------------

global count, id
count = 0

fondo0 = "#242424"
fondo1 = "#2b2b2b"
botones = "#1f6aa5"
fondo_campos = "#343638"

# ---------------------
#      Config App
# ---------------------

main.title("Programa ABMC")
main.geometry("800x600")
main.resizable(0, 0)
# main.iconbitmap('Nombre_del_archivo.ico') Ver imagen / En la mayoria de los casos .ico ---> .xbm

main.configure(background=fondo0)  # #2b2b2b "Nuestro drakmode"

# ---------------------
#     Menu Superior
# ---------------------

# Como no se puede cambiar el background en Windows almenos, no se lo coloca.

menubar = Menu(main)

file = Menu(menubar, tearoff=0)

file.add_command(label="Test")
file.add_separator()
file.add_command(label="Salir", command=main.quit)

menubar.add_cascade(label="Archivo", menu=file)

main.config(menu=menubar)

# ---------------------
#        TITULO
# ---------------------

titulo = ttk.Label(
    main,
    text="Programa ABMC",
    background=fondo0,
    foreground="white",
    font=("Arial", 18, "bold"),
)
titulo.grid(row=0, column=0, sticky="n", padx=50, pady=15)

segundo_fondo = tk.Frame(main, width=700, height=500, background=fondo1)
segundo_fondo.grid(row=1, column=0, sticky="n", padx=50)

# --------------------------------
#       Databases y Funciones
# --------------------------------

# Creacion de database o conectar a una
conn = sqlite3.connect("00__Mis_codigos/listado_productos.db")

c = conn.cursor()

# Creamos la tabla

c.execute(
    """CREATE TABLE if not exists productos (
        id INTEGER,
        marca TEXT,
        medida REAL,
        precio REAL,
        stock INTEGER,
        costo REAL,
        descripcion TEXT
        )"""
)

# Pasar cambios
conn.commit()

# Cerrar coneccion
conn.close()


# ---------------
#    Funciones
# ---------------


def submit():
    global count
    # Creacion de database o conectar a una
    conn = sqlite3.connect("00__Mis_codigos/listado_productos.db")

    c = conn.cursor()

    # Insertar en la tabla
    count += 1

    c.execute(
        "INSERT INTO productos VALUES(:id, :marca, :medida, :precio, :stock, :costo, :descripcion)",
        {
            "id": count,
            "marca": marca.get(),
            "medida": medida.get(),
            "precio": precio.get(),
            "stock": stock.get(),
            "costo": costo.get(),
            "descripcion": descripcion.get(),
        },
    )

    u = c.execute(
        "SELECT * FROM productos WHERE ROWID IN (SELECT max(ROWID) FROM productos)"
    )
    ultimo = u.fetchone()

    lista.insert(
        "",
        "end",
        values=(
            ultimo[0],
            ultimo[1],
            ultimo[2],
            ultimo[3],
            ultimo[4],
            ultimo[5],
            ultimo[6],
        ),
        tags=(""),
    )

    # Pasar cambios
    conn.commit()

    # Cerrar coneccion
    conn.close()

    # Limpiar los campos
    marca.delete(0, END)
    medida.delete(0, END)
    precio.delete(0, END)
    stock.delete(0, END)
    costo.delete(0, END)
    descripcion.delete(0, END)


def delete():

    item = lista.focus()
    lista_nueva = lista.item(item)

    print(lista_nueva)

    id = lista_nueva["text"]

    # Creacion de database o conectar a una
    conn = sqlite3.connect("00__Mis_codigos/listado_productos.db")

    c = conn.cursor()
    c.execute("DELETE FROM productos WHERE id = ?;", (id,))

    lista.delete(item)

    # Pasar cambios
    conn.commit()

    # Cerrar coneccion
    conn.close()


def select():
    global id

    item = lista.focus()
    lista_nueva = lista.item(item)
    lista_nueva_1 = lista_nueva["values"]
    id = lista_nueva_1[0]

    # Limpiar los campos
    marca.delete(0, END)
    medida.delete(0, END)
    precio.delete(0, END)
    stock.delete(0, END)
    costo.delete(0, END)
    descripcion.delete(0, END)

    # Llenar los campos
    marca.insert(0, lista_nueva_1[1])
    medida.insert(0, lista_nueva_1[2])
    precio.insert(0, lista_nueva_1[3])
    stock.insert(0, lista_nueva_1[4])
    costo.insert(0, lista_nueva_1[5])
    descripcion.insert(0, lista_nueva_1[6])
    return


def modify():
    global id

    # Creacion de database o conectar a una
    conn = sqlite3.connect("00__Mis_codigos/listado_productos.db")

    c = conn.cursor()

    c.execute(
        "UPDATE productos SET id=?, marca= ?, medida=?, precio=?, stock=?, costo=?, descripcion=? WHERE ID="
        + str(id),
        (
            id,
            marca.get(),
            medida.get(),
            precio.get(),
            stock.get(),
            costo.get(),
            descripcion.get(),
        ),
    )

    # Limpiar Treeview

    lista.delete(*lista.get_children())

    # Pasar la lista

    c.execute("SELECT * FROM productos")
    productos = c.fetchall()

    for producto in productos:
        lista.insert(
            "",
            "end",
            values=(
                producto[0],
                producto[1],
                producto[2],
                producto[3],
                producto[4],
                producto[5],
                producto[6],
            ),
            tags=(""),
        )

    # Pasar cambios
    conn.commit()

    # Cerrar coneccion
    conn.close()


def view():

    # Creacion de database o conectar a una
    conn = sqlite3.connect("00__Mis_codigos/listado_productos.db")

    c = conn.cursor()

    c.execute("SELECT * FROM productos")
    productos = c.fetchall()

    for producto in productos:
        lista.insert(
            "",
            "end",
            values=(
                producto[0],
                producto[1],
                producto[2],
                producto[3],
                producto[4],
                producto[5],
                producto[6],
            ),
            tags=(""),
        )

    # Pasar cambios
    conn.commit()

    # Cerrar coneccion
    conn.close()


# ---------------------
#  SeccionEntradaDatos
# ---------------------

nmarca = ttk.Label(
    main,
    text="Marca",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
nmarca.place(x=230, y=85)

marca = tk.Entry(
    bg=fondo_campos,
    borderwidth=2,
    fg="white",
    justify="center",
    textvariable=StringVar(),
)
marca.place(x=165, y=110, width=200, height=25)

ndescripcion = ttk.Label(
    main,
    text="Descripcion",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
ndescripcion.place(x=205, y=140)

descripcion = tk.Entry(
    bg=fondo_campos,
    borderwidth=2,
    fg="white",
    justify="center",
    textvariable=StringVar(),
)
descripcion.place(x=165, y=165, width=200, height=25)

nmedida = ttk.Label(
    main,
    text="Medida",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
nmedida.place(x=230, y=195)

medida = tk.Entry(
    bg=fondo_campos,
    borderwidth=2,
    fg="white",
    justify="center",
    textvariable=DoubleVar(),
)
medida.place(x=165, y=220, width=200, height=25)

nprecio = ttk.Label(
    main,
    text="Precio",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
nprecio.place(x=528, y=85)

precio = tk.Entry(
    bg=fondo_campos,
    borderwidth=2,
    fg="white",
    justify="center",
    textvariable=DoubleVar(),
)
precio.place(x=460, y=110, width=200, height=25)

nstock = ttk.Label(
    main,
    text="Stock",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
nstock.place(x=530, y=140)

stock = tk.Entry(
    bg=fondo_campos, borderwidth=2, fg="white", justify="center", textvariable=IntVar()
)
stock.place(x=460, y=165, width=200, height=25)

ncosto = ttk.Label(
    main,
    text="Costo",
    background=fondo1,
    foreground="white",
    font=("Arial", 14, "bold"),
)
ncosto.place(x=530, y=195)

costo = tk.Entry(
    bg=fondo_campos,
    borderwidth=2,
    fg="white",
    justify="center",
    textvariable=DoubleVar(),
)
costo.place(x=460, y=220, width=200, height=25)

# ---------------------
#       Botones
# ---------------------

boton_seleccionar = tk.Button(
    main, text="Seleccionar", background="#FFF0C9", bd=3, command=select
)
boton_seleccionar.place(x=80, y=280, width=125, height=30)


boton_modificar = tk.Button(
    main, text="Modificar", background=botones, bd=3, command=modify
)
boton_modificar.place(x=215, y=280, width=125, height=30)


boton_eliminar = tk.Button(
    main, text="Eliminar", background="#fc3434", bd=3, command=delete
)
boton_eliminar.place(x=465, y=280, width=125, height=30)


boton_aceptar = tk.Button(
    main, text="Aceptar", background="#24b44c", bd=3, command=submit
)
boton_aceptar.place(x=600, y=280, width=125, height=30)

# ---------------------
#         Lista
# ---------------------

lista = ttk.Treeview(
    main, columns=("Id", "Marca", "Medida", "Precio", "Stock", "Costo", "Descripcion")
)
lista.heading("#0")
lista.heading("Id", text="Id")
lista.heading("Marca", text="Marca")
lista.heading("Medida", text="Medida")
lista.heading("Precio", text="Precio")
lista.heading("Stock", text="Stock")
lista.heading("Costo", text="Costo")
lista.heading("Descripcion", text="Descripcion")

lista.column("#0", width=0, minwidth=0, anchor="center")
lista.column("Id", width=35, minwidth=35, anchor="center")
lista.column("Marca", width=100, minwidth=100, anchor="center")
lista.column("Medida", width=80, minwidth=80, anchor="center")
lista.column("Precio", width=90, minwidth=90, anchor="center")
lista.column("Stock", width=90, minwidth=90, anchor="center")
lista.column("Costo", width=80, minwidth=80, anchor="center")
lista.column("Descripcion", width=168, minwidth=168, anchor="center")

lista.place(x=80, y=325)

"""
self.scrollbar_vertical = ttk.Scrollbar(self.framebot, orient='vertical', command = self.tabla.yview)
    self.scrollbar_vertical.grid(row=1,column=5, sticky=N+S)
"""

view()


main.mainloop()
