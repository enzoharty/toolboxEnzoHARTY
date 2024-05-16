import subprocess
import os
def open_script(script_path):
    subprocess.Popen(['python', script_path])

menu_options = {
    "1": "Résumé scan PRIVE",
    "2": "Résumé scan PUBLIC",
    "3": "Quitter"
}

while True:
    print("Menu:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    user_input = input("Entrez votre choix: ")

    if user_input == "1":
        print("Option 1 sélectionnée")
        subprocess.run(["python", "resumePRIVE.py"])
    elif user_input == "2":
        print("Option 1 sélectionnée")
        subprocess.run(["python", "resumePUB.py"])
    elif user_input == "3":
        print("Retour au menu")
        os.system("python main.py")
        
    else:
        print("Choix invalide. Veuillez réessayer.")
