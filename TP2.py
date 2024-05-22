"""
    Votre description du programme
    @auteur(e)s     Samy Zerrouki et Samy Sabri
    @matricules     e2365457 et eYYYYYY
    @date              20-05-2024
"""
import csv
import json
import math
"2.2. La classe DonneesGeo"
class DonneesGeo:
    def __init__(self,ville,pays,latitude,longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"DonneesGeo: ville={self.ville} pays={self.pays} latitude={self.latitude} longitude={self.longitude}"
"2.3. La fonction lireDonneesCsv(nomFichier)"
def lireDonneesCsv(nomFichier):
    donnees_geo = []
    with open(nomFichier,mode="r",newline='',encoding='utf-8') as DonneesCsv:
        reader = csv.reader(DonneesCsv,delimiter=',')
        next(reader)

        for ligne in reader:
            ville, pays, latitude, longitude = ligne
            donnees = DonneesGeo(ville, pays,float(latitude), float(longitude))
            donnees_geo.append(donnees)


    return donnees_geo
"2.4. Fonction ecrireDonneesJson(nomFichier,listeObjDonneesGeo)"
def ecrireDonneesJson(nomFichier,listeObjDonneesGeo):
    pass

"2.5. Fonction trouverDistanceMin(nomFichier)"
def trouverDistanceMin(nomFichier):
    pass
"2.6. Menu"
def menu():
    while True:
        print("Menu :")
        print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
        print("2- Sauvegarder les données dans un fichier .json.")
        print("3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
        print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")
        option = input("->")

        if option == "1":
            donnees_geo = lireDonneesCsv("Donnees.csv")
        elif option == "2":
            if 'donnees_geo' not in locals():
                print("Veuillez d'abord faire l'option 1")
            else:
                ecrireDonneesJson("donnees.json", donnees_geo)
                print("Données sauvegardées dans donnees.json.")
        elif option == '3':
            if 'donnees_geo' not in locals():
                print("Veuillez d'abord lire les données du fichier CSV (option1).")
            else:
                trouverDistanceMin("donnees.json")
        elif option.lower() == 'q':
            print("Programme terminé")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide ou 'q' pour quitter.")

menu()