import subprocess
import os

def dirbust(ip_address):
    print("Lancement de DirBuster...")
    try:
        # Créer le dossier pour stocker les résultats
        os.makedirs("tmp-result", exist_ok=True)
        
        # Chemin complet du fichier de résultats
        result_file = os.path.join("tmp-result", "resultats_dirbust.txt")
        
        # Exécuter DirBuster avec l'adresse IP fournie et rediriger la sortie vers un fichier dans le dossier "tmp-result"
        with open(result_file, "w") as f:
            process = subprocess.run(["dirb", "http://" + ip_address], capture_output=True, text=True)
            for line in process.stdout.splitlines():
                if line.startswith("+"):
                    f.write(line + "\n")
        print(f"Résultats enregistrés dans '{result_file}'.")
    except FileNotFoundError:
        print("Erreur: DirBuster n'est pas installé ou n'est pas dans le PATH.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    os.system("python main.py")
    

def main():
    ip_address = input("Entrez l'adresse IP cible : ")
    dirbust(ip_address)

if __name__ == "__main__":
    main()
