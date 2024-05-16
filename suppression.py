import os

def list_files(folder_path):
    # Liste tous les fichiers dans le dossier spécifié
    files = os.listdir(folder_path)
    return files

def display_menu(options):
    # Affiche le menu à l'utilisateur et retourne son choix
    print("=== Menu ===")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    print("============")
    choice = input("Choisissez une option : ")
    return choice

def delete_file(file_path):
    # Supprime le fichier spécifié
    try:
        os.remove(file_path)
        print(f"Le fichier {file_path} a été supprimé avec succès.")
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression du fichier : {e}")

def delete_all_files(folder_path):
    # Supprime tous les fichiers dans le dossier spécifié
    files = list_files(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        delete_file(file_path)

if __name__ == "__main__":
    folder_path = "tmp-result/"
    files = list_files(folder_path)

    if not files:
        print("Aucun fichier trouvé dans le dossier.")
    else:
        print("Fichiers dans le dossier :")
        for index, file_name in enumerate(files, start=1):
            print(f"{index}. {file_name}")

        while True:
            choice = display_menu(["Supprimer un fichier", "Tout supprimer", "Retour au menu"])

            if choice == "1":
                file_index = int(input("Entrez le numéro du fichier à supprimer : ")) - 1
                if 0 <= file_index < len(files):
                    file_to_delete = files[file_index]
                    file_path = os.path.join(folder_path, file_to_delete)
                    delete_confirmation = input(f"Voulez-vous vraiment supprimer le fichier {file_to_delete}? (O/N) : ").strip().upper()
                    if delete_confirmation == "O":
                        delete_file(file_path)
                        # Actualise la liste des fichiers après la suppression
                        files = list_files(folder_path)
                    else:
                        print("Suppression annulée.")
                else:
                    print("Numéro de fichier invalide.")
            elif choice == "2":
                delete_all_confirmation = input("Voulez-vous vraiment supprimer tous les fichiers? (O/N) : ").strip().upper()
                if delete_all_confirmation == "O":
                    delete_all_files(folder_path)
                    # Actualise la liste des fichiers après la suppression
                    files = list_files(folder_path)
                else:
                    print("Suppression annulée.")
            elif choice == "3":
                print("Retour au menu")
                os.system("python main.py")
                break
            else:
                print("Choix invalide.")
                os.system("python main.py")
