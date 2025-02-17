import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

'''cursor.execute("""
     CREATE TABLE funcionarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL
     )
""")'''

conn.commit()
conn.close()

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 2500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 3000)")

conn.commit()
conn.close()

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

for funcionario in funcionarios:
    print(funcionario)

conn.close()

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("UPDATE funcionarios SET salario = 3000.00 WHERE nome = 'Pedro Santos'")

conn.commit()
conn.close()

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM funcionarios WHERE nome = 'Mariana Costa'")

conn.commit()
conn.close()
