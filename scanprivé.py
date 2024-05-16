import socket
import subprocess
import re
import os

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except OSError as e:
        print(f"Erreur lors de la récupération de l'adresse IP locale : {e}")
        return None

def run_nmap_scan(target_ip):
    try:
        command = f"nmap -sV -Pn --script vulners {target_ip}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("Commande Nmap exécutée avec succès.")
        save_scan_result(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du scan Nmap : {e}")
    except OSError as e:
        print(f"Erreur lors de l'accès aux ressources système : {e}")

def save_scan_result(output):
    output_file = "tmp-result/resultatscanPRIVE.txt"
    if not os.path.exists("tmp-result"):
        os.makedirs("tmp-result")
    with open(output_file, 'w') as outfile:
        outfile.write(output)
    print(f"Résultat du scan enregistré dans : {output_file}")

def main():
    print("Choisissez une option :")
    print("1. Scanner l'IP locale")
    print("2. Scanner une IP donnée")

    try:
        choice = int(input("Entrez votre choix (1 ou 2) : "))
        if choice == 1:
            target_ip = get_local_ip()
            if target_ip:
                run_nmap_scan(target_ip)
            else:
                print("Impossible de récupérer l'adresse IP locale.")
        elif choice == 2:
            target_ip = input("Entrez l'IP à scanner : ")
            run_nmap_scan(target_ip)
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

if __name__ == '__main__':
    main()
