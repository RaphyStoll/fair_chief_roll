import json
import sys


def display_chefs(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            chefs = json.load(f)
    except Exception as e:
        print(f"\n❌ Erreur lors de la lecture du fichier : {e}")
        return

    print("\n👑 Résultat du tirage des chefs de coalition :\n")
    for coalition, info in chefs.items():
        nom_complet = f"{info['prenom']} {info['nom']}"
        sexe = "♀️" if info["sexe"] == "F" else "♂️"
        print(f"  - {coalition} : {nom_complet} ({info['login']}) {sexe}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python display_chefs.py chefs.json")
        sys.exit(1)

    display_chefs(sys.argv[1])
