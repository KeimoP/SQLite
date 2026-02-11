import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess

def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)
    
def load_data_from_db(tree, search_query=None):
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
    subprocess.run(["python", "adduser.py"])

root = tk.Tk()
root.title("Kooli Õpilased")

open_button = tk.Button(root, text="Lisa õpilane", command=lisa_kasutaja)
open_button.pack(pady=20)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Otsi kasutaja Eesnime järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Loo tabel (Treeview) andmete kuvamiseks
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("first_name", "last_name", "email", "phone", "sugu"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)

# Seosta kerimisriba tabeliga
scrollbar.config(command=tree.yview)

# Määra veergude pealkirjad ja laius
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

# Lisa andmed tabelisse
load_data_from_db(tree)



root.mainloop()