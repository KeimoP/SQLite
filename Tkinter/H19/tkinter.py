import tkinter as tk

root = tk.Tik()
root.title("Filmi andmete sisestamine")

# Loo sildid ja sisestusväljad
labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta andmed")
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

def validate_data():
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        tk.messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return
    if not release_year.isdigit():
        tk.messagebox.showerror("Viga", "Aasta peab olema arv!")
        return
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        tk.messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return

    tk.messagebox.showinfo("Edu", "Andmed on kehtivad!")

# Näita Tkinteri akent
root.mainloop()