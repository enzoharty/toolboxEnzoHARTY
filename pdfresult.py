import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_to_pdf(input_file, output_file):
    # Crée un canvas PDF
    c = canvas.Canvas(output_file, pagesize=letter)

    # Lecture du contenu du fichier texte
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Hauteur de la page
    page_width, page_height = letter

    # Position initiale
    x = 50  # Marge gauche
    y = page_height - 100  # Marge supérieure

    # Écriture des lignes dans le PDF
    for line in lines:
        # Si la ligne commence par '@@', considérez-la comme un titre centré
        if line.startswith('@@'):
            title = line.strip('@').strip()  # Récupère le titre sans '@@'
            title_width = c.stringWidth(title)
            # Calcule la position x pour centrer le titre
            title_x = (page_width - title_width) / 2
            c.drawString(title_x, y, title)
            # Dessine un rectangle autour du titre
            c.rect(title_x - 5, y - 10, title_width + 10, 30, stroke=1, fill=0)
            # Descend d'une ligne après le titre
            y -= 40
        # Si la ligne commence par '##', considérez-la comme un titre de niveau 2
        elif line.startswith('##'):
            title = line.strip('#').strip()  # Récupère le titre sans '##'
            title_width = c.stringWidth(title)
            # Calcule la position x pour centrer le titre
            title_x = (page_width - title_width) / 2
            # Dessine un trait sous le titre pour le souligner
            c.line(title_x, y - 2, title_x + title_width, y - 2)
            # Écrit le titre en gras
            c.setFont("Helvetica", 12)
            c.drawString(title_x, y, title)
            # Descend d'une ligne après le titre
            y -= 40
        else:
            # Découpe la ligne en mots
            words = line.strip().split()
            # Texte à écrire sur la ligne actuelle
            text = ''
            # Parcours de chaque mot
            for word in words:
                # Obtient la largeur du texte
                text_width = c.stringWidth(text + word)
                # Si le mot dépasse la largeur de la page
                if text_width > (page_width - 2 * x):  # 2*x pour prendre en compte les marges des deux côtés
                    # Écrit le texte actuel à la position actuelle
                    c.drawString(x, y, text.strip())
                    # Passe à la ligne suivante
                    y -= 12
                    # Vérifie si nous sommes à la fin de la page
                    if y < 50:
                        # Ajoute une nouvelle page
                        c.showPage()
                        # Réinitialise la position pour la nouvelle page
                        y = page_height - 50
                    # Réinitialise le texte pour la nouvelle ligne
                    text = ''
                # Ajoute le mot au texte actuel
                text += word + ' '
            # Écrit le reste du texte de la ligne sur la dernière ligne
            c.drawString(x, y, text.strip())
            # Passe à la ligne suivante
            y -= 12
            # Vérifie si nous sommes à la fin de la page
            if y < 50:
                # Ajoute une nouvelle page
                c.showPage()
                # Réinitialise la position pour la nouvelle page
                y = page_height - 50

    c.save()  # Enregistre le PDF


def convert_text_to_pdf(input_folder, input_file_name):
    # Chemin d'accès complet au fichier texte
    input_file_path = os.path.join(input_folder, input_file_name)

    # Vérifie si le fichier texte existe
    if os.path.exists(input_file_path):
        # Nom du fichier PDF de sortie
        output_file_path = os.path.join(input_folder, "resultat-complet.pdf")
        convert_to_pdf(input_file_path, output_file_path)
        print(f"Le fichier PDF a été créé : {output_file_path}")
    else:
        print(f"Le fichier '{input_file_name}' n'existe pas dans le dossier '{input_folder}'.")


# Appel de la fonction pour convertir le fichier texte en PDF
input_folder = "final-rapport"
input_file_name = "merged_content.txt"
convert_text_to_pdf(input_folder, input_file_name)
