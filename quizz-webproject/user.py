#creation d'une DataBase
import peewee as pw

# connection a la base de donnees
myDB = pw.MySQLDatabase("marattm_webproject_quizz",
    host="mysql2.paris1.alwaysdata.com",
    port=3306,
    user="marattm",
    passwd="Azer0123")
myDB.connect()

# Definition de la table 'HighScore'
class Quizz(pw.Model):
    class Meta:
        database = myDB
    # Definition de 3 colonnes
    name = pw.CharField()           #nom image
    img = pw.CharField()            #adresse une image
    label_name = pw.CharField()     #type de l'image
    label_nb = pw.BigIntegerField() #ordre
    # le champ id est automatiquement cree


if __name__ == "__main__":
    # si ce fichier est execute a la main, alors creation de la table
    myDB.create_tables([Quizz])
