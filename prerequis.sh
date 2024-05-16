#!/bin/bash

# Installation de Python si ce n'est pas déjà installé
if ! command -v python3 &> /dev/null; then
    echo "Installation de Python..."
    sudo apt update
    sudo apt install -y python3
    echo "Python installé avec succès."
else
    echo "Python est déjà installé."
fi

# Installation de pip si ce n'est pas déjà installé
if ! command -v pip3 &> /dev/null; then
    echo "Installation de pip..."
    sudo apt install -y python3-pip
    echo "pip installé avec succès."
else
    echo "pip est déjà installé."
fi

# Installation de ReportLab
echo "Installation de ReportLab..."
pip3 install reportlab
echo "ReportLab installé avec succès."

# Créer le répertoire "tmp-result" s'il n'existe pas
if [ ! -d "tmp-result" ]; then
    mkdir tmp-result
    echo "Répertoire 'tmp-result' créé avec succès."
else
    echo "Le répertoire 'tmp-result' existe déjà."
fi

# Message final
echo "Vous pouvez maintenant lancer l'application de pentest."

