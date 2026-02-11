# SQLite + Tkinter (harjutused)

See repo sisaldab SQLite harjutusi (SQL skriptid ja näidisandmebaasid) ning Tkinteri näiterakendusi, mis kasutavad SQLite andmebaase.

### SQLite
- Windowsi jaoks on `sqlite3.exe` juba kaasas kaustas `SQLite/`.
- Soovi korral võid kasutada ka enda paigaldatud SQLite CLI-d.

## Kiirkäivitus: SQLite harjutused

SQL failid on jaotatud kaustadesse `SQLite/H12` … `SQLite/H18`.
Enamik `sql.txt` skripte sisaldab juba `.open ...` käsku, mis avab õige andmebaasi.

### 1) Käivita SQLite CLI
PowerShellis projekti juurest:

```powershell
cd .\SQLite
.\sqlite3.exe
```

### 2) Käivita konkreetse harjutuse skript
SQLite promptis:

```sql
.read H12/sql.txt
```

Sama loogika töötab ka teistega:

```sql
.read H13/sql.txt
.read H14/sql.txt
.read H15/sql.txt
.read H16/sql.txt
.read H17/sql.txt
```

Kui tahad käsitsi avada andmebaasi, siis näiteks:

```sql
.open H12/kplaas.db
```