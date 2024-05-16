import argparse
import subprocess

def scan():
    print("Lancement du scan Nmap.")
    subprocess.run(["python", "scan.py"])  # Appeler scan.py

def liste_port():
    print("Liste des ports ouverts après le scan:")
    subprocess.run(["python", "listeport.py"])

def dirbuster():
    print("Option 3 sélectionnée")
    subprocess.run(["python", "dirbuster.py"])

def bruteforce_ssh():
    print("Option 4 sélectionnée")
    subprocess.run(["python", "password.py"])  # Appeler password.py


def retrieve_data_via_ssh():
    print("Option 5 sélectionnée")
    subprocess.run(["python", "sshrecup.py"])

def list_temporary_files():
    print("Option 6 sélectionnée")
    subprocess.run(["python", "suppression.py"])

def generate_full_report():
    print("Option 7 sélectionnée")
    subprocess.run(["python", "rapportfinal.py"])



def main():
    parser = argparse.ArgumentParser(description="Menu d'options")
    parser.add_argument("-s", "--scan", action="store_true", help="Lancer un scan")
    parser.add_argument("-o", "--option", type=int, help="Option avec un argument entier")
    args = parser.parse_args()

    while True:
        if args.option:
            option = args.option
            if option == 1:
                scan()
                break
            elif option == 2:
                liste_port()
                break
            elif option == 3:
                dirbuster()
                break
            elif option == 4:
                bruteforce_ssh()
                break
            elif option == 5:
                retrieve_data_via_ssh()
                break
            elif option == 6:
                list_temporary_files() 
                break
            elif option == 7:
                generate_full_report()
            else:
                print("Option invalide")
        elif args.scan:
            scan()
            break
        else:
            print("""
 __                .__ ___.                 
_/  |_  ____   ____ |  |\_ |__   _______  ___
\   __\/  _ \ /  _ \|  | | __ \ /  _ \  \/  /
 |  | (  <_> |  <_> )  |_| \_\ (  <_> >    < 
 |__|  \____/ \____/|____/___  /\____/__/\_ \
                             \/            \/
 ==========================================
        Menu d'options :
 ==========================================
        """)
            print("1. Lancer un scan")
            print("2. Liste des ports ouvert")
            print("3. Découverte de répertoire sur un serveur web")
            print("4. Bruteforce SSH")
            print("5. Récupération de données via le SSH")
            print("6. Liste des fichiers temporaire")
            print("7. Génération du rapport complet")
            print("=" * 20)

            choix = input("Choisissez une option en tapant le numéro correspondant : ")
            if choix.isdigit():
                choix = int(choix)
                if 1 <= choix <= 7:
                    if choix == 1:
                        scan()
                        break
                    elif choix == 2:
                        liste_port()
                        break
                    elif choix == 3:
                        dirbuster()
                        break
                    elif choix == 4:
                        bruteforce_ssh()
                        break
                    elif choix == 5:
                        retrieve_data_via_ssh()
                    elif choix == 6:
                        list_temporary_files()
                        break
                    elif choix == 7:
                        generate_full_report()
                        break
                else:
                    print("Option invalide")
            else:
                print("Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()
