# OKOKOK mais propre les resultat
import shodan
import csv
import json
import subprocess
import os

API_KEY = "gh8Ixz0zc2YxQXARZqay75sR7vxeTz6H"
API_KEY_SHODAN = shodan.Shodan(API_KEY)

def scan_host_by_ip(ip):
    try:
        results = API_KEY_SHODAN.host(ip)
        # Liste pour stocker les résultats des scans
        scan_results = []

        # Votre logique de scan par adresse IP ici
        print(f"Résultats du scan pour l'adresse IP {ip}:")
        print(f"Adresse IP : {results['ip_str']}")
        print(f"Organisation : {results.get('org', 'N/A')}")
        print(f"Système d'exploitation : {results.get('os', 'N/A')}")
        print(f"Ports : {', '.join(str(port) for port in results['ports'])}")

        for service in results['data']:
            port = service['port']
            product = service.get('product', 'N/A')
            version = service.get('version', 'N/A')
            cve_details = []

            if 'vulns' in service:
                vulns_info = service['vulns']
                for cve in vulns_info.keys():
                    if cve.startswith('CVE-'):
                        cve_details.append({'CVE': cve, 'Summary': vulns_info[cve]['summary']})
           
            # Ajouter les résultats du scan à la liste
            scan_results.append({'IP': ip, 'Port': port, 'Product': product, 'Version': version, 'CVEs': cve_details})

        # Écrire les résultats des scans dans un fichier JSON
        with open('tmp-result/resultatscanPUBLIC.json', 'w') as json_file:
            json.dump(scan_results, json_file, indent=4)

    except shodan.APIError as e:
        print(f"Erreur : {e}")

def shearch_by_keyword(keyword):
    try:
        info_by_keyword = API_KEY_SHODAN.search(keyword)
        # Votre logique de recherche par mot-clé ici
        print(f"Résultats de la recherche pour le mot-clé '{keyword}':")
        print("[+] Le total d'adresse IP trouvé est de : ", info_by_keyword["total"], "\n")
        for info in info_by_keyword["matches"]:
            print("[+]" + info["ip_str"])

    except shodan.APIError as e:
        print(f"Erreur : {e}")

def main():
    print("Menu de scan :")
    print("1. Liste d'IP publique avec un mot-clé")
    print("2. Scanner  IP publique")
    print("3. Scanner  IP privée")
    choix = int(input("Choisissez une option en tapant le numéro correspondant : "))

    if choix == 1:
        keyword = input("Entrez le mot-clé à rechercher : ")
        shearch_by_keyword(keyword)
    elif choix == 2:
        ip = input("Entrez l'adresse IP publique à scanner : ")
        scan_host_by_ip(ip)
    elif choix == 3:
        subprocess.run(["python", "scanprivé.py"])
    else:
        print("Option invalide")
    os.system("python main.py")

if __name__ == "__main__":
    main()
