"""
Tkinteri rakendus õpilaste haldamiseks (kool.db).

Funktsionaalsus:
- Kuvab kõik õpilased tabelis (Treeview)
- Otsib õpilasi eesnime järgi
- Lisab uue õpilase (adduser.py kaudu)
- Uuendab valitud õpilase andmeid
- Kustutab valitud õpilase

Keimo Plaas
11/2/2026
"""

import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess
from tkinter import messagebox

# --- OTSING / ANDMETE LAADIMINE ---
def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)
    
def load_data_from_db(tree, search_query=None):
    # Tühjenda Treeview
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect('kool.db')
    cursor = conn.cursor()

    if search_query:
        cursor.execute(
            "SELECT first_name, last_name, email, phone, sugu FROM users WHERE first_name LIKE ?",
            (f"%{search_query}%",)
        )
    else:
        cursor.execute(
            "SELECT first_name, last_name, email, phone, sugu FROM users"
        )
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", iid=row[0], values=row)  # iid seadmiseks võime kasutada eesnime (või ID, kui on)

    conn.close()

# --- KASUTAJA LISAMINE ---
def lisa_kasutaja():
    subprocess.run(["python", "adduser.py"])

# --- KASUTAJA ANDMETE UUENDAMINE ---
def update_record(record_id, entries, window):
    # Kogume andmed sisestusväljadest
    first_name = entries["Eesnimi"].get()
    last_name = entries["Perenimi"].get()
    email = entries["Email"].get()
    phone = entries["Phone"].get()
    sugu = entries["Sugu"].get()

    # Andmete uuendamine SQLite-is
    conn = sqlite3.connect('kool.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
        SET first_name=?, last_name=?, email=?, phone=?, sugu=?
        WHERE first_name=?  -- siin eeldame iid=row[0] ehk first_name
    """, (first_name, last_name, email, phone, sugu, record_id))
    conn.commit()
    conn.close()

    # Värskenda Treeview tabelit
    load_data_from_db(tree)

    # Sulge sisestusaken
    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")

def on_update():
    selected_item = tree.selection()
    if selected_item:
        record_id = selected_item[0]  # iid (kasutame first_name või ID)
        # Avame lihtsa aken, kus saab muuta andmeid
        edit_window = tk.Toplevel(root)
        edit_window.title("Uuenda kasutajat")

        # Loome sildid ja Entry väljad
        labels = ["Eesnimi", "Perenimi", "Email", "Phone", "Sugu"]
        entries = {}
        values = tree.item(selected_item)["values"]

        for i, label in enumerate(labels):
            tk.Label(edit_window, text=label).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(edit_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, values[i])
            entries[label] = entry

        # Salvesta nupp
        tk.Button(
            edit_window, 
            text="Salvesta", 
            command=lambda: update_record(record_id, entries, edit_window)
        ).grid(row=len(labels), column=0, columnspan=2, pady=10)
    else:
        messagebox.showwarning("Hoiatus", "Vali kõigepealt rida!")

# --- GUI ---
root = tk.Tk()
root.title("Kooli Õpilased")
root.geometry("1000x600")

# Loo ülemine raam, mis sisaldab otsingut ja nuppe
top_frame = tk.Frame(root)
top_frame.pack(pady=10, fill=tk.X, padx=10)

search_frame = tk.Frame(top_frame)
search_frame.pack(side=tk.LEFT, anchor="w")

search_label = tk.Label(search_frame, text="Otsi kasutaja Eesnime järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

buttons_frame = tk.Frame(top_frame)
buttons_frame.pack(side=tk.RIGHT, anchor="e")

open_button = tk.Button(root, text="Lisa õpilane", command=lisa_kasutaja)
open_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(root, text="Uuenda", command=on_update)
update_button.pack(side=tk.LEFT, padx=5)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(
    frame,
    yscrollcommand=scrollbar.set,
    columns=("first_name", "last_name", "email", "phone", "sugu"),
    show="headings"
)
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

# Veerud
tree.heading("first_name", text="Eesnimi")
tree.heading("last_name", text="Perenimi")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.heading("sugu", text="Sugu")

tree.column("first_name", width=100)
tree.column("last_name", width=100)
tree.column("email", width=200)
tree.column("phone", width=150)
tree.column("sugu", width=60)

# Alglaadimisel kõik kasutajad
load_data_from_db(tree)

root.mainloop()
