import json
import paramiko

def convert_txt_to_json(txt_file_path, json_file_path):
    try:
        # Ouvre le fichier texte en lecture
        with open(txt_file_path, "r") as txt_file:
            # Lit le contenu du fichier texte
            txt_content = txt_file.read()
        
        # Convertit le contenu en format JSON
        json_content = {"txt_content": txt_content}

        # Écrit le contenu JSON dans un fichier
        with open(json_file_path, "w") as json_file:
            json.dump(json_content, json_file, indent=4)

        print(f"Fichier JSON créé avec succès : {json_file_path}")
    
    except FileNotFoundError:
        print(f"Le fichier {txt_file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def connect_ssh_with_credentials(credentials_file):
    try:
        # Lecture des informations de connexion depuis le fichier credentials.json
        with open(credentials_file, "r") as file:
            credentials = json.load(file)

        # Connexion SSH à la machine virtuelle
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(credentials['hostname'], username=credentials['username'], password=credentials['password'])

        # Liste des commandes à exécuter sur la machine virtuelle
        commands_to_execute = [
            "rm /tmp/extraction.txt",
            "nano /tmp/extraction.txt",
            "echo '-------------------------- information du systeme --------------------------' >> /tmp/extraction.txt",
            "cat /etc/*release >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- IP A --------------------------' >> /tmp/extraction.txt",
            "ip a >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- networks --------------------------' >> /tmp/extraction.txt",
            "cat /etc/networks >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- Connexions réseau actives --------------------------' >> /tmp/extraction.txt",
            "netstat -tulnp >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- password --------------------------' >> /tmp/extraction.txt",
            "cat /etc/passwd >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- group --------------------------' >> /tmp/extraction.txt",
            "cat /etc/group >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- Fichier conf sensible  --------------------------' >> /tmp/extraction.txt",
            "cat /etc/ssh/sshd_config >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- authorized_keys --------------------------' >> /tmp/extraction.txt",
            "cat ~/.ssh/authorized_keys >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '-------------------------- resolv.conf  --------------------------' >> /tmp/extraction.txt",
            "cat /etc/resolv.conf >> /tmp/extraction.txt",
            "sleep 2",  # Pause de 2 secondes
            "echo '------------------------------------------' >> /tmp/extraction.txt"
       ]   
    

        # Exécution des commandes sur la machine virtuelle
        for command in commands_to_execute:
            stdin, stdout, stderr = ssh.exec_command(command)
            # Ajoutez ici la gestion de la sortie si nécessaire

        # Transfert du fichier extraction.txt depuis la machine virtuelle vers la machine locale
        sftp = ssh.open_sftp()
        sftp.get('/tmp/extraction.txt', 'tmp-result/extraction.txt')
        sftp.close()

        # Fermeture de la connexion SSH
        ssh.close()


    except FileNotFoundError:
        print("Le fichier de credentials n'a pas été trouvé.")
    except paramiko.AuthenticationException:
        print("Échec de l'authentification SSH.")
    except paramiko.SSHException as e:
        print(f"Erreur SSH : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    credentials_file = "tmp-result/credentialsSSH.json"  # Chemin vers le fichier credentials.json
    connect_ssh_with_credentials(credentials_file)
