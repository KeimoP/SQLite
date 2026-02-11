"""
Kasutaja sisestab eesnime, perenime, emaili, telefoni ja soo.
Andmed valideeritakse ning salvestatakse tabelisse 'users'.

Keimo Plaas
11/2/2026
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Õpilaste lisamine")

labels = ["Eesnimi", "Perenimi", "Email", "Telefon", "Sugu"]
entries = {}

# Loome sisestusväljad
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry


def validate_data():
    """Kontrollib, et kõik väljad on täidetud ja telefon sisaldab ainult numbreid."""
    if not entries["Eesnimi"].get():
        messagebox.showerror("Viga", "Eesnime ei sisestatud!")
        return False
    if not entries["Perenimi"].get():
        messagebox.showerror("Viga", "Perekonnanime ei sisestatud!")
        return False
    if not entries["Email"].get():
        messagebox.showerror("Viga", "Emaili ei sisestatud!")
        return False
    if not entries["Telefon"].get().isdigit():
        messagebox.showerror("Viga", "Telefon peab sisaldama ainult numbreid!")
        return False
    if not entries["Sugu"].get():
        messagebox.showerror("Viga", "Sugu ei sisestatud!")
        return False
    return True


def insert_data():
    """Salvestab valideeritud andmed andmebaasi."""
    if validate_data():
        connection = sqlite3.connect("kool.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, phone, sugu)
            VALUES (?, ?, ?, ?, ?)
        """, (
            entries["Eesnimi"].get(),
            entries["Perenimi"].get(),
            entries["Email"].get(),
            entries["Telefon"].get(),
            entries["Sugu"].get()
        ))

        connection.commit()
        connection.close()
        messagebox.showinfo("Edu", "Andmed salvestati!")


submit_button = tk.Button(root, text="Sisesta õpilane", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

root.mainloop()
