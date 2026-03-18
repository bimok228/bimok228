import sqlite3

con = sqlite3.connect("school.sqlite")

cur = con.cursor()

que_create = """
CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    mark INTEGER
)
"""

cur.execute(que_create)

que_insert = """
INSERT INTO class (name, surname, mark) VALUES
    ("Василий", "Пупкин", 3),
    ("Денис", "Синицын", 4),
    ("Ангелина", "Соколова", 5),
    ("Саша", "Петров", 2)
"""
#cur.execute(que_insert)
que_select = """
SELECT * FROM class
"""

result = cur.execute(que_select)
data = result.fetchall()
for line in data:
    print(line)

con.commit()

con.close()
