import sqlite3

# Yangi database yaratish (yoki ulanish)
conn = sqlite3.connect("star_trek.db")
cursor = conn.cursor()

# 1. Jadval yaratish
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Ma'lumotlar kiritish
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)

# 3. Update qilish (Jadzia Dax → Ezri Dax)
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Bajoranlarni ko‘rsatish (Name va Age)
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
bajorans = cursor.fetchall()

print("Bajoranlar:")
for b in bajorans:
    print(f"Name: {b[0]}, Age: {b[1]}")

# O‘zgarishlarni saqlash va yopish
conn.commit()
conn.close()
