"""
Tkinteri rakendus õpilaste kuvamiseks andmebaasist (kool.db).

Võimalused:
- Kuvab kõik õpilased tabelis (Treeview).
- Otsib õpilasi eesnime järgi.
- Avab eraldi faili (adduser.py) uue õpilase lisamiseks.
"""

import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess


def on_search():
    """Käivitab otsingu eesnime alusel."""
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)


def load_data_from_db(tree, search_query=None):
    """Laeb andmed andmebaasist ja kuvab need tabelis."""
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
        tree.insert("", "end", values=row)

    conn.close()


def lisa_kasutaja():
    """Avab uue akna õpilase lisamiseks."""
    subprocess.run(["python", "adduser.py"])


root = tk.Tk()
root.title("Kooli Õpilased")

open_button = tk.Button(root, text="Lisa õpilane", command=lisa_kasutaja)
open_button.pack(pady=20)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Otsi kasutaja eesnime järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Tabel andmete kuvamiseks
tree = ttk.Treeview(
    frame,
    yscrollcommand=scrollbar.set,
    columns=("first_name", "last_name", "email", "phone", "sugu"),
    show="headings"
)
tree.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=tree.yview)

# Veergude pealkirjad
tree.heading("first_name", text="Eesnimi")
tree.heading("last_name", text="Perenimi")
tree.heading("email", text="Email")
tree.heading("phone", text="Telefon")
tree.heading("sugu", text="Sugu")

# Veergude laiused
tree.column("first_name", width=100)
tree.column("last_name", width=100)
tree.column("email", width=200)
tree.column("phone", width=150)
tree.column("sugu", width=60)

# Lae algandmed
load_data_from_db(tree)

root.mainloop()
