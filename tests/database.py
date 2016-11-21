import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='python')
sql = conn.cursor()

var1 = input("Voer uw naam in: ")
var2 = input("Voer uw email in: ")
var3 = int(input("Voer uw Telefoonnummer in: "))
variable = {
    'naam': var1,
    'email': var2,
    'tel': var3
}
sql = conn.cursor()
sql.execute ("""
            INSERT INTO test (Naam, Email, Telefoonnummer)
            VALUES
                (%(naam)s, %(email)s, %(tel)s)
        """, variable)
conn.commit()
sql.execute("SELECT * FROM test")
print(sql.fetchall())
