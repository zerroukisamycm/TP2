"""
    Votre description du programme
    @auteur(e)s     Samy Zerrouki et Samy Sabri
    @matricules     e2365457 et eYYYYYY
    @date              20-05-2024
"""
import csv
import json
"2.2. La classe DonneesGeo"
class DonneesGeo:
    def __init__(self,ville,pays,latitude,longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"DonneesGeo: ville={self.ville} pays={self.pays} latitude={self.latitude} longitude={self.longitude}"

def lireDonneesCsv(nomFichier):
    donnees_geo = []
    with open(nomFichier,mode="r",newline='',encoding='utf-8') as DonneesCsv:
        reader = csv.reader(DonneesCsv,delimiter=',')
        next(reader)

        for ligne in reader:
            ville, pays, latitude, longitude = ligne
            donnees = DonneesGeo(ville, pays,float(latitude), float(longitude))
            donnees_geo.append(donnees)


    return donnees_geogit