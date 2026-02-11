import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Treenijate lisamine")

labels = ["Eesnimi", "Perenimi", "Email", "Telefon","Profiil"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

def validate_data():
    first_name = entries["Eesnimi"].get()
    last_name = entries["Perenimi"].get()
    email = entries["Email"].get()
    phone = entries["Telefon"].get()
    profilepic = entries["Profiil"].get()

    if not first_name:
        messagebox.showerror("Viga", "Eesnime ei sisestatud!")
        return False
    if not last_name:
        messagebox.showerror("Viga", "Perekonna nime ei sisestatud!")
        return False
    if not email:
        messagebox.showerror("Viga", "Emaili ei sisetatud!")
        return False
    if not phone.isdigit():
        messagebox.showerror("Viga", "Ei sisetatud numbrit!")
        return False
    if not profilepic:
        messagebox.showerror("Viga", "Profiilipildi linki ei sisetatud!")
        return False

    return True

def insert_data():
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
        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")

submit_button = tk.Button(root, text="Sisesta kasutaja", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

root.mainloop()
