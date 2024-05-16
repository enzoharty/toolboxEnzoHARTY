import os
import json
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extract_credentials(file_path):
    credentials = ""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            credentials_data = json.load(file)
            credentials += json.dumps(credentials_data, indent=4)
    return credentials.strip()

def count_cves_by_port(file_path):
    cve_counts = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_host = None
    current_port = None

    for line in lines:
        if 'Nmap scan report for' in line:
            current_host = line.split()[-1]
        elif '/tcp' in line or '/udp' in line:
            port_info = re.findall(r'\d+', line)
            current_port = port_info[0]
            cve_counts[current_host + ':' + current_port] = 0
        elif 'https://vulners.com/' in line and current_host and current_port:
            cve_counts[current_host + ':' + current_port] += 1

    return cve_counts

def count_directories(file_path):
    directories = 0
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('+ http'):
                    directories += 1
    return directories

def generer_pdf(credentials, cve_counts, directories, nom_fichier):
    # Créer un canvas PDF
    c = canvas.Canvas("final-rapport/" + nom_fichier, pagesize=letter)
    # Titre centré et encadré
    title = "Résumé du scan d'ip privé"
    title_width = c.stringWidth(title)
    title_x = (letter[0] - title_width) / 2
    c.rect(title_x - 5, 750, title_width + 10, 20, stroke=1, fill=0)
    c.drawString(title_x, 760, title)
    # Coordonnées de départ pour écrire ligne par ligne
    y = 720
    # Écrire les résultats de DirBuster
    c.drawString(100, y, f"Nous avons trouvé {directories} répertoire(s) sur le serveur web")
    y -= 20  # Décalage vertical pour la prochaine ligne
    
    # Ajout d'un espace entre les sections
    y -= 20
    
    # Écrire les crédentials s'ils existent
    if credentials:
        c.drawString(100, y, "Voici les credentials trouvés :")
        y -= 20  # Décalage vertical pour la prochaine ligne
        for line in credentials.split('\n'):
            c.drawString(100, y, line)
            y -= 20  # Décalage vertical pour la prochaine ligne
    
    # Ajout d'un espace entre les sections
    y -= 20
    
    # Écrire le texte "Nombre de CVE par port"
    c.drawString(100, y, "Nombre de CVE par port :")
    y -= 20  # Décalage vertical pour la prochaine ligne
    
    # Écrire le texte des ports et des CVEs
    for port, count in cve_counts.items():
        c.drawString(100, y, f"Port : {port} il y a  {count} CVE(s)")
        y -= 20  # Décalage vertical pour la prochaine ligne
        # Si la position verticale atteint le bas de la page, ajouter une nouvelle page
        if y <= 50:
            c.showPage()
            c.drawString(100, 750, title)
            y = 720
    # Sauvegarder le PDF
    c.save()

# Chemin d'accès au fichier contenant le rapport de scan
folder_path = "final-rapport"
file_name = "merged_content.txt"
file_path = os.path.join(folder_path, file_name)

# Chemin d'accès au fichier contenant les credentials SSH
credentials_path = "tmp-result/credentialsSSH.json"

# Chemin d'accès au fichier contenant les résultats de DirBuster
dirbust_path = "tmp-result/resultats_dirbust.txt"

# Extraction des credentials SSH
credentials = extract_credentials(credentials_path)

# Compter les répertoires trouvés
directories = count_directories(dirbust_path)

# Exécute la fonction pour compter les CVE par port
cve_counts = count_cves_by_port(file_path)

# Appeler la fonction pour générer le PDF
generer_pdf(credentials, cve_counts, directories, "resultat-résumé-privé.pdf")

print("Le PDF a été généré avec succès dans le dossier 'final-rapport' sous le nom 'resultat-résumé-privé.pdf'.")
