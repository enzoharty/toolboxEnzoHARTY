import os
import json
from datetime import datetime

# Dossier contenant les fichiers JSON et TXT
folder_path = "tmp-result"

# Liste pour stocker le contenu de tous les fichiers
all_content = []

# Parcourir les fichiers dans le dossier
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    # Lire le contenu des fichiers JSON et TXT
    if file_name.endswith('.json'):
        with open(file_path, 'r') as file:
            file_content = file.read()
            if file_name.startswith('resultatscanPUB'):
                # Ajouter un titre pour les fichiers de résultat de scan
                file_data = json.loads(file_content)
                ip = file_data[0]['IP']
                title = f"##Voici le résultat du scan pour l'adresse IP {ip} et les CVEs associées aux ports:\n"
                all_content.append(title)
                for entry in file_data:
                    port_info = f"Port: {entry['Port']}\nProduct: {entry['Product']}\nVersion: {entry['Version']}\n"
                    cve_info = "\n".join([f"CVE: {cve['CVE']}\nSummary: {cve['Summary']}\n" for cve in entry['CVEs']])
                    all_content.append(port_info + cve_info)
            elif file_name.startswith('credentials'):
                # Ajouter un titre pour les fichiers de credentials
                credentials_data = json.loads(file_content)
                # Récupérer les informations des credentials
                credentials_text = f"Nom d'utilisateur : {credentials_data['username']}\n" \
                                   f"Mot de passe : {credentials_data['password']}\n" \
                                   f"Adresse IP : {credentials_data['hostname']}\n" \
                                   f"Force du mot de passe : {credentials_data['password_strength']}\n"
                all_content.append("##Voici les credentials trouvés grâce au brute force en SSH :\n")
                all_content.append(credentials_text)
            else:
                all_content.append(file_content)
    elif file_name.endswith('.txt'):
        with open(file_path, 'r') as file:
            file_content = file.read()
            if file_name == 'extraction.txt':
                # Ajouter un titre pour le fichier d'extraction SSH
                all_content.append("##Voici les informations que nous avons récupérées grâce à la connexion SSH :\n")
                all_content.append(file_content)
            elif file_name.startswith("resultats_dir"):
                # Ajouter un titre si le fichier commence par "resultats_dir"
                title = "##Résultats du DirBust :\n"
                all_content.append(title)
                lines = file_content.split('\n')  # Séparer les lignes du contenu
                for line in lines:
                    if line.strip():  # Vérifier si la ligne n'est pas vide
                        # Vérifier si la ligne commence par un "+"
                        if line.strip().startswith("+"):
                            # Retirer le "+" et ajouter la ligne sans les espaces inutiles
                            all_content.append(line.strip()[1:])
                        else:
                            all_content.append(line.strip())  # Ajouter la ligne sans les espaces inutiles
            elif file_name.startswith('resultatscanPRI'):
                # Ajouter un titre pour le fichier resultatscanPRI
                all_content.append("##Voici les résultats du scan de l'IP privée et les CVEs associées aux ports:\n")
                all_content.append(file_content)

# Créer le dossier "final-rapport" s'il n'existe pas
output_folder_path = "final-rapport"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Enregistrer le contenu de tous les fichiers dans un fichier texte
output_file_path = os.path.join(output_folder_path, "merged_content.txt")
with open(output_file_path, 'w') as output_file:
    # Ajouter un titre avec la date et l'heure du rapport
    title = f"@@Voici le rapport final fait le {datetime.now().strftime('%d %B %Y à %H:%M:%S')}\n"
    output_file.write(title)
    output_file.write('\n')  # Ajouter une ligne vide après le titre
    for content in all_content:
        output_file.write(content)
        output_file.write('\n\n')  # Ajouter une ligne vide entre chaque contenu

print(f"Le contenu de tous les fichiers a été fusionné et enregistré dans '{output_file_path}'.")
os.system("python affichagerapport.py")
