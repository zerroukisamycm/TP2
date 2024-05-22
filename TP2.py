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
def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    # Créer liste dictionnaires à partir des objets DonneesGeo
    liste_dict = []
    for obj in listeObjDonneesGeo:
        # Convertir objet en dictionnaire
        obj_dict = {
            'ville': obj.ville,
            'pays': obj.pays,
            'latitude': obj.latitude,
            'longitude': obj.longitude
        }
        liste_dict.append(obj_dict)

    # Ouvrir fichier en mode écriture et sauvegarder la liste de dictionnaires en JSON
    with open(nomFichier, 'w') as jsonfile:
        json.dump(liste_dict, jsonfile, indent=4)


"2.5. Fonction trouverDistanceMin(nomFichier)"
def haversine(lat1, lon1, lat2, lon2):
    # Rayon de la Terre en km
    R = 6371

    # Convertion des latitudes et longitudes de degrés en radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Formule Haversine
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def trouverDistanceMin(nomFichier):
    with open(nomFichier, 'r') as jsonfile:
        liste_donnees = json.load(jsonfile)
        min_distance = float('inf')
        ville1, ville2 = None, None
        for i in range(len(liste_donnees)):
            for j in range(i + 1, len(liste_donnees)):
                villeA = liste_donnees[i]
                villeB = liste_donnees[j]
                distance = haversine(villeA['latitude'], villeA['longitude'], villeB['latitude'], villeB['longitude'])
                if distance < min_distance:
                    min_distance = distance
                    ville1, ville2 = villeA, villeB

        if ville1 and ville2:
            print(f"Distance minimale en kilomètres entre 2 villes : "
                  f"Ville 1 : {ville1['ville']} {ville1['pays']} {ville1['latitude']} {ville1['longitude']} et "
                  f"Ville 2 : {ville2['ville']} {ville2['pays']} {ville2['latitude']} {ville2['longitude']} "
                  f"Distance en kilomètres : {min_distance}")

            with open('distances.csv', 'w', newline='') as csvfile:
                csvfile.write(f"{ville1['ville']}, {ville2['ville']}, {min_distance}\n")

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
