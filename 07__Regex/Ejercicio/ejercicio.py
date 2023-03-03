from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
import re


def crear_db():
    con = sqlite3.connect("mi_db7.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = (
        "CREATE TABLE IF NOT EXISTS mi_tabla("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "producto TEXT, "
        "descripcion TEXT)"
    )
    cursor.execute(sql)
    con.commit()


def consulta_tabla(con):
    cursor = con.cursor()
    sql = "SELECT * FROM mi_tabla;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


con = crear_db()
crear_tabla(con)
tabla_inicial = consulta_tabla(con)

root = Tk()

root.title("App Unidad 7")
root.geometry("800x400")

label_producto = Label(root, text="Producto: ")
label_producto.pack()

var_producto = StringVar()

entry_producto = Entry(root, textvariable=var_producto)
entry_producto.pack()

label_descripcion = Label(root, text="Descripcion: ")
label_descripcion.pack()

var_descripcion = StringVar()

entry_producto = Entry(root, textvariable=var_descripcion)
entry_producto.pack()


def alta():
    cursor = con.cursor()

    producto = var_producto.get()
    descripcion = var_descripcion.get()

    patron_alfanumerico = re.compile("[a-zA-Z0-9áéíóúÁÉÍÓÚ]*$")

    if re.match(patron_alfanumerico, producto):

        data = (producto, descripcion)

        sql = "INSERT INTO mi_tabla(" "producto, descripcion) " "VALUES(?, ?);"

        cursor.execute(sql, data)
        con.commit()

        sql = "SELECT last_insert_rowid();"
        cursor.execute(sql)
        ultimo_id = cursor.fetchone()

        sql = "SELECT * FROM mi_tabla WHERE id =?;"
        cursor.execute(sql, ultimo_id)
        row = cursor.fetchone()

        values = (
            row[1],
            row[2],
        )

        tree_db.insert("", "end", text=str(row[0]), values=values)

    else:

        showerror(
            "Error", "El campo producto solo puede contener caracteres alfanumericos."
        )


button_alta = Button(root, text="Alta", command=alta)
button_alta.pack()

tree_db = ttk.Treeview(root)

tree_db["columns"] = (
    "producto",
    "descripcion",
)

tree_db.heading("#0", text="ID")
tree_db.heading("producto", text="Producto")
tree_db.heading("descripcion", text="Descripcion")

tree_db.pack(fill=X)

for row in tabla_inicial:
    values = (
        row[1],
        row[2],
    )
    tree_db.insert("", "end", text=str(row[0]), values=values)

root.mainloop()
