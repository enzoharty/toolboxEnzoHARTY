import subprocess
import os 

menu_options = {
    "1": "Rapport détaillé",
    "2": "Rapport résumé",
    "3": "Retour au menu"
}

while True:
    print("Menu:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    user_input = input("Entrez votre choix: ")

    if user_input in menu_options:
        print(f"Vous avez choisi {menu_options[user_input]}")
        if user_input == "1":
            subprocess.run(["python", "pdfresult.py"])
            pass
        elif user_input == "2":
            subprocess.run(["python", "menurapportresumer.py"])
        elif user_input == "3":
            os.system("python main.py") 
    else:
        print("Choix invalide. Veuillez réessayer.")
