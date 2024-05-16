import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extract_credentials(file_path):
    credentials = ""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            credentials_data = json.load(file)
            credentials += json.dumps(credentials_data, indent=4)
    return credentials.strip()

def count_cves_by_port():
    # Dictionnaire pour stocker le nombre de CVE par port
    cve_counts = {}

    # Chemin d'accès au fichier contenant le rapport de scan
    folder_path = "final-rapport"
    file_name = "merged_content.txt"
    file_path = os.path.join(folder_path, file_name)

    # Vérifie si le fichier existe
    if os.path.exists(file_path):
        # Lecture du contenu du fichier texte
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Variables pour stocker les informations du rapport de scan
        current_port = None
        cve_count = 0

        # Analyse des lignes pour extraire les informations
        for line in lines:
            if line.startswith("Port: "):
                # Si nous rencontrons une nouvelle entrée de port, nous mettons à jour le port actuel et le nombre de CVE associé
                if current_port is not None:
                    cve_counts[current_port] = cve_count
                current_port = line.split(": ")[1].strip()
                cve_count = 0
            elif line.startswith("CVE: "):
                # Si nous trouvons une ligne CVE, nous incrémentons le nombre de CVE pour ce port
                cve_count += 1

        # Pour la dernière entrée de port
        if current_port is not None:
            cve_counts[current_port] = cve_count

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
    title = "Résumé scan public"
    title_width = c.stringWidth(title)
    title_x = (letter[0] - title_width) / 2
    c.rect(title_x - 5, 750, title_width + 10, 20, stroke=1, fill=0)
    c.drawString(title_x, 760, title)

    # Coordonnées de départ pour écrire ligne par ligne
    y = 720
    
    # Écrire le texte "Voici les credentials trouvés" s'ils existent
    if credentials:
        c.drawString(100, y, "Voici les credentials trouvés :")
        y -= 20  # Décalage vertical pour la prochaine ligne
        for line in credentials.split('\n'):
            c.drawString(100, y, line)
            y -= 20  # Décalage vertical pour la prochaine ligne
        y -= 20  # Espace supplémentaire après les crédentials
    
    # Écrire le texte "Nombre de CVE par port"
    c.drawString(100, y, "Nombre de CVE par port :")
    y -= 20  # Décalage vertical pour la prochaine ligne
    
    # Écrire le texte des ports et des CVEs
    for port, count in cve_counts.items():
        c.drawString(100, y, f"Port {port}: {count} CVE(s)")
        y -= 20  # Décalage vertical pour la prochaine ligne
    y -= 20  # Espace supplémentaire après les CVEs
    
    # Écrire le nombre de répertoires trouvés
    c.drawString(100, y, f"Nous avons trouvé {directories} répertoire(s) sur le serveur web")
    
    # Sauvegarder le PDF
    c.save()

# Appel de la fonction pour compter les CVE par port
cve_counts = count_cves_by_port()

# Chemin d'accès au fichier contenant les credentials
credentials_path = "tmp-result/credentialsSSH.json"

# Extraction des credentials
credentials = extract_credentials(credentials_path)

# Chemin d'accès au fichier contenant les résultats de DirBuster
dirbust_path = "tmp-result/resultats_dirbust.txt"

# Compter le nombre de répertoires trouvés
directories = count_directories(dirbust_path)

# Appel de la fonction pour générer le PDF
generer_pdf(credentials, cve_counts, directories, "resultat-résumé-public.pdf")

print("Le PDF a été généré avec succès dans le dossier 'final-rapport' sous le nom 'resultat-résumé-public.pdf'.")
