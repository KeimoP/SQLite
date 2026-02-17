# SQLite ülesanded - Koondkdokumentatsioon

Antud dokumentatsioon kirjeldab kõiki SQLite harjutusi (H12-H18) ja Tkinter rakendusi (H19-H22), mis kasutavad SQLite andmebaase.

## Sisukord
- [Kiirkäivitus](#kiirkäivitus)
- [H12: Tabeli loomine ja skeemi muutmine](#h12-tabeli-loomine-ja-skeemi-muutmine)
- [H13: Tabeli loomine + näidisandmete lisamine](#h13-tabeli-loomine--näidisandmete-lisamine)
- [H14: Päringud, sisestused ja tingimuslikud uuendused](#h14-päringud-sisestused-ja-tingimuslikud-uuendused)
- [H15: UPDATE/DELETE koos RETURNING ja valikupäringud](#h15-updatedelete-koos-returning-ja-valikupäringud)
- [H16: Spordiklubi andmemudel](#h16-spordiklubi-andmemudel)
- [H17: Koondpäringud treenerite ja osalejate kohta](#h17-koondpäringud-treenerite-ja-osalejate-kohta)
- [H18: Täiendav ülesanne](#h18-täiendav-ülesanne)
- [H19-H22: Tkinter rakendused](#h19-h22-tkinter-rakendused)

---

## Kiirkäivitus

### SQLite käsu rida avada

PowerShellis projekti juurest:

```powershell
cd .\SQLite
.\sqlite3.exe
```

### Konkreetse harjutuse skripti käivitamine

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

### Andmebaasi käsitsi avamine

```sql
.open H12/kplaas.db
```

**Märkus:** Windows jaoks on `sqlite3.exe` juba kaasas kaustas `SQLite/`. Soovi korral võid kasutada ka enda paigaldatud SQLite CLI-d.

---

## H12: Tabeli loomine ja skeemi muutmine

**Eesmärk:** Tabeli loomine, nimetamise muutmine ja veeru lisamine.

**Teemad:**
- `CREATE TABLE` - uue tabeli loomine
- `ALTER TABLE RENAME` - tabeli nimetamise muutmine
- `ALTER TABLE RENAME COLUMN` - veeru nimetamise muutmine
- `ALTER TABLE ADD COLUMN` - uue veeru lisamine

**Samm-sammult:**
1. Avatakse/luuakse andmebaasifail `H12/kplaas.db`
2. Luuakse tabel nimega `kasutajad` järgmiste veergudega:
   - `id` - INTEGER PRIMARY KEY AUTOINCREMENT (automaatselt kasvav ID)
   - `first_name` - TEXT NOT NULL (eesnimi)
   - `last_name` - TEXT NOT NULL (perekonnanimi)
   - `email` - TEXT NOT NULL (e-post)
   - `telefon` - REAL NOT NULL (telefon numbriline)

3. Tehakse skeemi muudatused:
   - Nimetatakse tabel ümber ingliskeelseks: `kasutajad` → `users`
   - Nimetatakse veerg ümber: `telefon` → `phone`
   - Lisatakse uus veerg `image` (profiilipildi link)

**Andmebaas:** `H12/kplaas.db`

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H12/sql.txt
```

---

## H13: Tabeli loomine + näidisandmete lisamine

**Eesmärk:** Tabeli loomine skeemi muudatustega ja näidisandmete sisestamine.

**Teemad:**
- Tabeli loomine (sama nagu H12)
- `INSERT INTO` - andmete sisestamine

**Samm-sammult:**
1. Avatakse/luuakse andmebaasifail `H13/kplaas.db`
2. Luuakse `users` tabel (nagu H12-s)
3. Lisatakse kaks näidiskasutajat:
   - Keimo Plaas (keimo.plaas22@gmail.com, 56192547, keimo.jpg)
   - Karin Eegrid (karineegrid@gmail.com, 688673, neegeros.jpg)

**Andmebaas:** `H13/kplaas.db`

**Näide - sisestamine:**
```sql
INSERT INTO users (first_name, last_name, email, phone, image)
VALUES ('Keimo','Plaas','keimo.plaas22@gmail.com','56192547','keimo.jpg');
```

**Täiendav ressurss:** Fail `H13/users.txt` sisaldab 100 katsetäpse näidiskasutaja INSERT käsku, mida saab kasutada testimiseks.

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H13/sql.txt
```

---

## H14: Päringud, sisestused ja tingimuslikud uuendused

**Eesmärk:** SELECT päringud, sisestused ja CASE loogikaga tingimustlikud uuendused.

**Teemad:**
- `SELECT` - andmete pärimine
- `ORDER BY` ja `LIMIT` - järjestamine ja piiramine
- `LIKE` - tekstitingimused
- `INSERT INTO` - andmete sisestamine
- `ALTER TABLE ADD COLUMN` - uue veeru lisamine
- `UPDATE` + `CASE` - tingimustlik veeru uuendamine

**Samm-sammult:**
1. Avatakse andmebaasifail `H14/kplaas.db`
2. Kuvatakse 3 esimest perekonnanime ID järgi järjestatult
3. Lisatakse kaks uut kasutajat (Gabriel ja Eestlane)
4. Filtreeritakse kasutajaid LIKE abil:
   - Eesnimi algab "g" JA e-post lõpeb ".com"
5. Lisatakse uued veerud:
   - `EESTI` - märgend riigikoodi (372) põhjal
   - `haridusasutus` - märgend e-posti domeeni ("gov" või "edu") põhjal
6. Täidetakse veerud CASE loogikaga

**Andmebaas:** `H14/kplaas.db`

**Näide - LIKE päring:**
```sql
SELECT * FROM users 
WHERE first_name LIKE 'g%' AND email LIKE '%.com';
```

**Näide - CASE tingimus UPDATE:**
```sql
UPDATE users
SET EESTI =
  CASE
    WHEN phone LIKE '372%' THEN 'EESTI'
    ELSE '---'
  END;
```

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H14/sql.txt
```

---

## H15: UPDATE/DELETE koos RETURNING ja valikupäringud

**Eesmärk:** Andmete uuendamine ja kustutamine RETURNING klaususiga, mis tagastab muudetud/kustutatud read kohe.

**Teemad:**
- `SELECT` + `ORDER BY` + `LIMIT`
- `UPDATE` + `RETURNING` - muudetud andmete tagastamine
- `DELETE` + `RETURNING` - kustutatud andmete tagastamine
- SQLite süntaksi erinevused (nt "SELECT TOP" ei toeta SQLite)

**Samm-sammult:**
1. Avatakse andmebaasifail `H15/kplaas.db`
2. Kuvatakse 3 esimest perekonnanime
3. Uuendatakse Keimo kasutajan e-post ja telefon, RETURNING näitab muudetud väljad
4. Kustutatakse kasutajad ID vahemikus 5-10, RETURNING näitab kustutatud read
5. Näide "SELECT TOP" süntaksist (see on SQL Serveri stiil, SQLite-s ei tööta)

**Andmebaas:** `H15/kplaas.db`

**Näide - UPDATE koos RETURNING:**
```sql
UPDATE users
SET email = 'muudetud@gmail.com', phone = 123
WHERE first_name = 'Keimo'
RETURNING email, phone;
```

**Näide - DELETE koos RETURNING:**
```sql
DELETE FROM users
WHERE id BETWEEN 5 AND 10
RETURNING *;
```

**Märkus SQLite süntaksist:**
- SQLite ei toeta "SELECT TOP 10" süntaksit (see on SQL Serveri stiil)
- SQLite-s kasutatakse selle asemel: `SELECT * FROM users LIMIT 10;`

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H15/sql.txt
```

---

## H16: Spordiklubi andmemudel

**Eesmärk:** Realistiku äri andmemudeli loomine (spordiklubi) mitme tabeliga, võõrvõtmed ja JOIN päringud.

**Teemad:**
- Mitme tabeli andmemudel
- `FOREIGN KEY` - andmete seosed
- `PRIMARY KEY` - unikaalne identifikaator ja liittekstid
- `JOIN` - tabelite ühendamine
- Näidispäringud

**Andmestruktuur - 4 tabelit:**

### 1. `users` tabel (kliendiid/liikmed)
| Veerg | Tüüp | Kirjeldus |
|-------|------|-----------|
| user_id | INTEGER PRIMARY KEY AUTOINCREMENT | Unikaalne ID |
| first_name | TEXT NOT NULL | Eesnimi |
| last_name | TEXT NOT NULL | Perekonnanimi |
| email | TEXT UNIQUE NOT NULL | E-post (unikaalne) |
| phone | TEXT | Telefon (tekstina paindlik) |
| profile_image | TEXT | Profiilipildi nimi/URL |

### 2. `trainers` tabel (treenerid)
| Veerg | Tüüp | Kirjeldus |
|-------|------|-----------|
| trainer_id | INTEGER PRIMARY KEY AUTOINCREMENT | Unikaalne ID |
| name | TEXT NOT NULL | Nimi |
| speciality | TEXT | Eriala/spetsialiseerumine |
| contact | TEXT | Kontaktinfo |

### 3. `sessions` tabel (treeningseansid)
| Veerg | Tüüp | Kirjeldus |
|-------|------|-----------|
| session_id | INTEGER PRIMARY KEY AUTOINCREMENT | Unikaalne ID |
| session_name | TEXT NOT NULL | Seansi nimi |
| trainer_id | INTEGER NOT NULL | Viide treenerile (FOREIGN KEY) |
| session_date | TEXT NOT NULL | Kuupäev (YYYY-MM-DD) |

### 4. `attendance` tabel (osalemised - mitme-mitme seos)
| Veerg | Tüüp | Kirjeldus |
|-------|------|-----------|
| user_id | INTEGER NOT NULL | Viide kasutajale (FOREIGN KEY) |
| session_id | INTEGER NOT NULL | Viide seansile (FOREIGN KEY) |
| status | TEXT CHECK IN ('kohal', 'puudus', 'hilines') NOT NULL | Osalemise staatus |
| PRIMARY KEY | (user_id, session_id) | Tagab unikaalsuse |

**Relatsioonimudelis:**
```
trainers (1) : (M) sessions (1) : (M) users
    ↓
Üks treener juhendab mitut seanssi
Üks seanss kuulub ühele treenerile
Üks kasutaja osaleb mitmel seansil
Üks seanss võib osaleda mitmel kasutajal
```

**Näidispäringud H16/sql.txt-s:**

1. **Kohal käinud kasutajad:**
```sql
SELECT u.first_name, u.last_name, a.session_id, a.status
FROM users u
JOIN attendance a ON u.user_id = a.user_id
WHERE a.status = 'kohal';
```

2. **Seansid treeneri nimega:**
```sql
SELECT s.session_name, s.session_date, t.name AS trainer_name
FROM sessions s
JOIN trainers t ON s.trainer_id = t.trainer_id;
```

3. **Kasutaja + seanss + kuupäev + staatus:**
```sql
SELECT u.first_name, u.last_name, s.session_name, s.session_date, a.status
FROM users u
JOIN attendance a ON u.user_id = a.user_id
JOIN sessions s ON a.session_id = s.session_id
ORDER BY u.last_name, s.session_date;
```

**Andmebaas:** `H16/Spordiklubi.db`

**Failid H16 kaustas:**
- `sql.txt` - kogu skript tabelite loomiseks ja näidispäringuteks
- `users.sql` - kasutajate tabeli loomine
- `trainers.sql` - treenerite tabeli loomine
- `sessions.sql` - treeningseansside tabeli loomine
- `attendance.sql` - osalemiste tabeli loomine

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H16/sql.txt
```

---

## H17: Koondpäringud treenerite ja osalejate kohta

**Eesmärk:** Koondamisinfoga (aggregate) päringud - võimaldavad grupeerida ja kokku võtta andmeid.

**Teemad:**
- `COUNT()` - kirjete arvu loendamine
- `GROUP BY` - andmete grupeerimine
- `SUM()` - summeerimine
- `CASE` - tingimustlik arvutamine
- `LEFT JOIN` - vasak kõikide osalisega
- Alampäringud (subqueries) ja `HAVING` klauzul
- `MAX()` - maksimaalse väärtuse leidmine

**Saadud teabe näited:**

### 1. Treenerid, kellel on kõige rohkem treeningseansse
```sql
SELECT t.trainer_id, t.name, COUNT(s.session_id) AS session_count
FROM trainers t
JOIN sessions s ON t.trainer_id = s.trainer_id
GROUP BY t.trainer_id
ORDER BY session_count DESC;
```

### 2. Treenerid, kellel on kõige rohkem osalejaid (kohal)
```sql
SELECT t.trainer_id, t.name, COUNT(a.user_id) AS total_participants
FROM trainers t
JOIN sessions s ON t.trainer_id = s.trainer_id
JOIN attendance a ON s.session_id = a.session_id
WHERE a.status = 'kohal'
GROUP BY t.trainer_id
ORDER BY total_participants DESC;
```

### 3. Seansside arv treeneri kohta
```sql
SELECT trainer_id, COUNT(*) AS session_count
FROM sessions
GROUP BY trainer_id;
```

### 4. Osalejate arv treeneri kohta (SUM + CASE)
```sql
SELECT t.trainer_id, t.name,
  SUM(CASE WHEN a.status = 'kohal' THEN 1 ELSE 0 END) AS participant_sum
FROM trainers t
JOIN sessions s ON t.trainer_id = s.trainer_id
LEFT JOIN attendance a ON s.session_id = a.session_id
GROUP BY t.trainer_id;
```

### 5. Treener, kellel on maksimaalne kohalolijate arv (alampäring)
```sql
SELECT t.trainer_id, t.name, COUNT(a.user_id) AS total_participants
FROM trainers t
JOIN sessions s ON t.trainer_id = s.trainer_id
JOIN attendance a ON s.session_id = a.session_id
WHERE a.status = 'kohal'
GROUP BY t.trainer_id
HAVING total_participants = (
    SELECT MAX(participant_count)
    FROM (
        SELECT COUNT(a2.user_id) AS participant_count
        FROM sessions s2
        JOIN attendance a2 ON s2.session_id = a2.session_id
        WHERE a2.status = 'kohal'
        GROUP BY s2.trainer_id
    )
);
```

**Andmebaas:** `H17/Spordiklubi.db` (sama andmetega nagu H16)

**Käivitus:**
```powershell
cd .\SQLite
.\sqlite3.exe
.read H17/sql.txt
```

---

## H18: Täiendav ülesanne

Kaust `H18` sisaldab täiendavat materjali. Praegu sisaldab see ainult pildifaili.

---

## H19-H22: Tkinter rakendused

Tk Süntaksi käigus pöördub ka SQLite andmebaaside juurde Python koodiga. Tkinter on Python graafiline kasutajaliidesestandardkirjastik.

### H19: Treenijate lisamine (db.py)

**Eesmärk:** Lihtne Tkinter rakendus treenijate lisamiseks andmebaasiga.

**Funktsioon:**
- Kasutaja sisestab: eesnimi, perekonnanimi, email, telefon, profiili lingi
- Andmed valideeritakse
- Andmed salvestatakse tabelisse `users` andmebaasi `database.db`

**Validatsioonid:**
- Eesnimi - kohustuslik
- Perekonnanimi - kohustuslik
- Email - kohustuslik
- Telefon - kohustuslik, ainult numbrid
- Profiili link - kohustuslik

**Käivitus:**
```powershell
python H19/db.py
```

---

### H20: Õpilaste haldamine

Kaks faili:
- **adduser.py** - õpilase lisamine
- **viewusers.py** - õpilaste vaatamine ja otsing

#### H20/adduser.py
Lihtne Tkinter rakendus õpilase lisamiseks andmebaasiga.

**Funktsioon:**
- Kasutaja sisestab: eesnimi, perekonnanimi, email, telefon, sugu
- Andmed valideeritakse
- Andmed salvestatakse tabelisse `users` andmebaasi `kool.db`

**Validatsioonid (nagu H19, lisaks sugu):**
- Eesnimi - kohustuslik
- Perekonnanimi - kohustuslik
- Email - kohustuslik
- Telefon - kohustuslik, ainult numbrid
- Sugu - kohustuslik

**Käivitus:**
```powershell
python H20/adduser.py
```

#### H20/viewusers.py
Tkinter rakendus õpilaste kuvamiseks andmebaasist.

**Funktsioon:**
- Kuvab kõik õpilased tabelis (Treeview komponendis)
- Võimaldab otsida õpilast eesnime järgi
- Avab `adduser.py` uue õpilase lisamiseks

**Komponendid:**
- Otsinguväli (Entry)
- Otsingu nuppu
- Tabel (Treeview) õpilaste kuvamiseks
- "Lisa õpilane" nupp

**Käivitus:**
```powershell
python H20/viewusers.py
```

---

### H21: Õpilaste haldamine (parendatud versioon)

**Struktuuri:** Sarnane H20-le, kuid võib sisaldada täiendavaid funktsioone.

- **adduser.py** - õpilase lisamine (täiendatud)
- **viewusers.py** - õpilaste vaatamine ja otsing (täiendatud)

**Käivitus:**
```powershell
python H21/viewusers.py
# või
python H21/adduser.py
```

---

### H22: Õpilaste haldamine (lõplik versioon)

**Struktuuri:** Sarnane H20/H21-le, kuid sisaldab potentsiaalselt kõige rohkem funktsioone.

- **adduser.py** - õpilase lisamine (lõplik versioon)
- **viewusers.py** - õpilaste vaatamine ja otsing (lõplik versioon)

**Käivitus:**
```powershell
python H22/viewusers.py
# või
python H22/adduser.py
```

---

## Kokkuvõte SQL käsudest

| Käsk | Kirjeldus | Näide |
|------|-----------|-------|
| `CREATE TABLE` | Uue tabeli loomine | `CREATE TABLE users (id INTEGER PRIMARY KEY);` |
| `ALTER TABLE RENAME` | Tabeli nimetamise muutmine | `ALTER TABLE kasutajad RENAME TO users;` |
| `ALTER TABLE ADD COLUMN` | Uue veeru lisamine | `ALTER TABLE users ADD COLUMN image TEXT;` |
| `INSERT INTO` | Andmete sisestamine | `INSERT INTO users (name) VALUES ('Keimo');` |
| `SELECT` | Andmete pärimine | `SELECT * FROM users;` |
| `WHERE` | Tingimuste määramine | `SELECT * FROM users WHERE id = 1;` |
| `ORDER BY` | Järjestamine | `SELECT * FROM users ORDER BY name;` |
| `LIMIT` | Maht piiritamine | `SELECT * FROM users LIMIT 10;` |
| `LIKE` | Tekstitingimused | `SELECT * FROM users WHERE name LIKE 'K%';` |
| `CASE` | Tingimustlik väärtus | `CASE WHEN age > 18 THEN 'täiskasvanu' ELSE 'alaealine' END` |
| `UPDATE` | Andmete uuendamine | `UPDATE users SET name = 'Uus' WHERE id = 1;` |
| `DELETE` | Andmete kustutamine | `DELETE FROM users WHERE id = 1;` |
| `RETURNING` | Tagastab muudetud/kustutatud read | `UPDATE users SET name = 'X' RETURNING *;` |
| `JOIN` | Tabelite ühendamine | `SELECT * FROM users JOIN orders ON users.id = orders.user_id;` |
| `LEFT JOIN` | Vasak kõikide osalisega | `SELECT * FROM users LEFT JOIN orders ON ...;` |
| `COUNT()` | Kirjete arvu loendamine | `SELECT COUNT(*) FROM users;` |
| `SUM()` | Summeerimine | `SELECT SUM(price) FROM orders;` |
| `GROUP BY` | Andmete grupeerimine | `SELECT name, COUNT(*) FROM users GROUP BY name;` |
| `HAVING` | Grupifilter | `GROUP BY name HAVING COUNT(*) > 1;` |
| `FOREIGN KEY` | Andmete seosed | `FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)` |
| `PRIMARY KEY` | Unikaalne identifikaator | `user_id INTEGER PRIMARY KEY AUTOINCREMENT` |

---

## SQLite vs SQL Server erinevused

| Funktsioon | SQLite | SQL Server |
|-----------|--------|-----------|
| TOP klausul | LIMIT | SELECT TOP 10 |
| Autoincrement | AUTOINCREMENT | IDENTITY, SERIAL |
| Vaikimisi süntaks | LIMIT | OFFSET FETCH |
| Nimeruumi muutmine | ALTER TABLE x RENAME TO y | sp_rename |

---

## Ressursid ja viited

- **SQLite dokumentatsioon:** [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
- **Tkinter dokumentatsioon:** [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- **Python sqlite3 moodul:** [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)

---

## Autorid

- Keimo Plaas
- Dokumentatsioon: Februar 2026

---

## Märkus

Kaikiddes harjutustes kasutatakse SQLite relatsioonilist andmebaasi. Praktiliste rakenduste jaoks (H19-H22) kasutatakse Python Tkinter graafilist kasutajaliidest.

Harjutused on järjestatud järk-järgult keerukuse suurenemisel:
- **H12-H15:** Põhilised SQL operatsioonid
- **H16-H17:** Keerulisemad andmemudelid ja päringud
- **H19-H22:** Praktilised rakendused Tkinter-iga
