import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='analyse')
sql = conn.cursor()

var1 = input("Voer uw naam in: ")
var2 = input("Voer uw email in: ")
var3 = int(input("Voer uw telefoonnummer in: "))
var4 = input("Voer uw adres in: ")
var5 = input("Voer uw woonplaats in: ")
var6 = input("Voer uw postcode in: ")

variable = {
    'KL_naam': var1,
    'KL_email': var2,
    'KL_telefoonnr': var3,
    'KL_adres': var4,
    'KL_woonplaats': var5,
    'KL_postcode': var6
}
sql = conn.cursor()
sql.execute ("""
            INSERT INTO klant (KL_naam, KL_email, KL_telefoonnr, KL_adres, KL_woonplaats, KL_postcode)
            VALUES
                (%(KL_naam)s, %(KL_email)s, %(KL_telefoonnr)s, %(KL_adres)s, %(KL_woonplaats)s, %(KL_postcode)s)
        """, variable)
conn.commit()
sql.execute("SELECT * FROM klant WHERE KL_idKlant = 4")
print(sql.fetchall())
