# Projet-professionnel-toolbox

Enzo HARTY DE PIERREBOURG Master-4-CS-b

## Name

Toolbox 

## Getting started

Pour importer le git il vous suffira de faire 

    git clone https://github.com/enzoharty/toolboxEnzoHARTY.git

puis de mettre vos identifiant git

## Installation

Tout se fera en ligne de commande.

Il faudra dans un premier temps importer le git sur votre VM kali-linux.
Dans un second temps, il faudra rendre le fichier prerequis.sh exécutable en faisant :

    chmod +x prerequis.sh

Il se peut que le fichier soit pas pris en compte donc il faudra le convertir

    dos2unix prerequis.sh

enfin vous pourrez le lancer, il installera python, ainsi que reportlab qui seront obligatoire pour l'application

    ./prerequis.sh

Maintenant vous pouvez l'application :

    python main.py



## Description / usage 

Ma toolbox aura plusieurs fonctionnalités :

1) Dans un premier temps vous pourrez scan, vous aurez le choix d'afficher des IP public grâce à un mot clé donné ( ssh, http) ou vous pourrez scanner un IP public ( SHODAN ) ou un IP privé ( NMAP ) l'ip privé peut-être l'ip de votre propre machine ( qui sera récupérée automatiquement ) ou un IP que vous fournirez.

2) Une fois le scan fait vous pourrez lister les ports ouverts pour ensuite faire la suite.

3) Si le port 80 ou 443 est ouvert vous pourrez utiliser la découverte de répertoire sur un serveur web ( Dirbuster )

4) Si le port 22 est ouvert vous pourrez faire un bruteforce en SSH sur l'ip où le port 22 est ouvert. 
Vous pourrez choisir d'utiliser une liste d'utilisateur et de mot de passe ou de renseigner par vous même les crédentials si vous les connaisser.

5) Si le bruteforce est réussi et que des crédentials sont récupérés, ils seront stockés. Vous pourrez ensuite utiliser l'option 5 pour extraire des données sur la machine cible. ( paramiko )

6) Sachant que chaque scan que vous faites est stocké dans des fichiers temporaire, vous pourrez supprimer le ou les fichiers que vous ne voulez plus et que vous ne voulez pas que les résultats apparaissent dans le rapport final.

7) Génération du rapport final grâce aux fichiers temporaires, vous pouvez choisir de voir le rapport en détail ou résumé il faudra juste notifié si vous avez fait un scan privé ou un scan public.


## Plan

1) SCAN 
    - LISTE  via mot clé
    - Scan public
    - Scan privé
        - ip locale
        - ip donnnée
2) LISTE DES PORTS ouverts

3) Découverte de dossiers sur un serveur web

4) Brute force sur le port 22
    - choisir ou pas un fichier avec des noms d'utilisateurs ( liste/user.txt )
    - choisir ou pas un fichier avec des mots de passe ( liste/mdp.txt )

5) Récupération de données sur la machine cible où le bruteforce a été fait.

6) Lister les fichiers temporaire 
    - supprimer 1 fichier
    - supprimer tous les fichiers.

7) Génération du rapport 
    - rapport complet
    - rapport résumé
        - Résumé pour le scan IP privé
        - Résumé pour le scan IP public
        
## Librairies

1 script bash pour installer les prérequis.
Le reste script python. ( Python 3.11.2 )

Module utilsés : Paramiko, nmap, shodan, reportlab, json, argparse, datetime

## A venir

Amélioration en cours : 
- Ajout d'un detecteur de wifi ( LYNIS )
- Bruteforce FTP
- Rapport plus clair avec des graphiques


## Project status

Version 1 finie.

