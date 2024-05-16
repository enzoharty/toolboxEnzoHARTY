import os
import json

def list_open_ports():
    # Chemin vers le fichier JSON
    file_path_json = os.path.join("tmp-result", "resultatscanPUBLIC.json")
    # Liste pour stocker les ports ouverts du JSON
    open_ports_json = []

    # Lecture du contenu du fichier JSON
    if os.path.exists(file_path_json):
        with open(file_path_json, "r") as file:
            json_data = file.read()

        # Charger le JSON
        data = json.loads(json_data)

        # Parcourir les éléments du JSON et ajouter les ports ouverts à la liste
        for item in data:
            if "Port" in item:
                open_ports_json.append(item["Port"])
    
    # Afficher la liste des ports ouverts du JSON si elle n'est pas vide
    if open_ports_json:
        print("Ports ouverts (resultatscanPUBLIC.json) :", open_ports_json)

    # Chemin vers le fichier texte
    file_path_txt = os.path.join("tmp-result", "resultatscanPRIVE.txt")
    # Liste pour stocker les ports ouverts du texte
    open_ports_txt = []

    # Lire le contenu du fichier texte et extraire les ports ouverts
    if os.path.exists(file_path_txt):
        with open(file_path_txt, "r") as file_txt:
            lines = file_txt.readlines()
            for line in lines:
                if "/tcp" in line and "open" in line:
                    port = line.split("/")[0].strip()
                    open_ports_txt.append(port)

        # Afficher la liste des ports ouverts du texte si le fichier existe et contient des ports ouverts
        if open_ports_txt:
            print("Ports ouverts (resultatscanPRIVE.txt) :", open_ports_txt)

    # Si aucun des fichiers n'existe ou ne contient de ports ouverts, afficher "Aucun scan n'a été effectué"
    if not open_ports_json and not open_ports_txt:
        print("Aucun scan n'a été effectué")
    os.system("python main.py")

# Appeler la fonction
list_open_ports()
