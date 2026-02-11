"""
Kasutaja sisestab eesnime, perenime, emaili, telefoni ja profiilipildi lingi.
Andmed valideeritakse ning salvestatakse tabelisse 'users' (database.db).

Keimo Plaas
11/2/2026
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Treenijate lisamine")

labels = ["Eesnimi", "Perenimi", "Email", "Telefon", "Profiil"]
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
    if not entries["Profiil"].get():
        messagebox.showerror("Viga", "Profiilipildi link puudub!")
        return False
    return True


def insert_data():
    """Salvestab valideeritud andmed andmebaasi."""
    if validate_data():
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, phone, profile_image)
            VALUES (?, ?, ?, ?, ?)
        """, (
            entries["Eesnimi"].get(),
            entries["Perenimi"].get(),
            entries["Email"].get(),
            entries["Telefon"].get(),
            entries["Profiil"].get()
        ))

        connection.commit()
        connection.close()
        messagebox.showinfo("Edu", "Andmed salvestati!")


submit_button = tk.Button(root, text="Sisesta kasutaja", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

root.mainloop()
