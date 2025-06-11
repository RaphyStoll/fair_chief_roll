#!/bin/bash

echo "🎲 Lancement du tirage de chefs de coalition"
read -p "Souhaitez-vous charger un fichier JSON existant ? (o/n) : " choix

if [[ "$choix" =~ ^[Oo]$ ]]; then
    read -p "Entrez le nom du fichier JSON (ex: data.json) : " fichier
    if [ ! -f "$fichier" ]; then
        echo "❌ Le fichier '$fichier' n'existe pas. Abandon."
        exit 1
    fi
else
    python3 collect_input_generate_json.py
    fichier="data.json"
    if [ ! -f "$fichier" ]; then
        echo "❌ Fichier '$fichier' introuvable après création. Abandon."
        exit 1
    fi
fi

# Étape 2 : Tirage
python3 tirage.py "$fichier"
if [ ! -f "chefs.json" ]; then
    echo "❌ Tirage échoué. Fichier 'chefs.json' non généré."
    exit 1
fi

# Étape 3 : Affichage
python3 display_chefs.py chefs.json