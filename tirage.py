import json
import random
import sys
from datetime import datetime


def log(msg, file):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    file.write(f"{timestamp} {msg}\n")


def load_data(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_result(output_path, result):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def run_tirage(data, log_file):
    coalitions = data["coalitions"]
    participants = data["participants"]

    coalition_members = {c: [] for c in coalitions}
    for p in participants:
        p["login"] = "@" + p["login"].lstrip("@")  # Force @
        if p["coalition"] in coalition_members:
            coalition_members[p["coalition"]].append(p)

    chefs = {}
    non_chefs = participants.copy()

    log("Roll 1 - Tirage initial :", log_file)
    for c in coalitions:
        membres = coalition_members[c]
        if membres:
            chef = random.choice(membres)
            chefs[c] = chef
            non_chefs.remove(chef)
            log(f"  - {c} → {chef['login']}", log_file)
        else:
            log(f"  - {c} → Aucun membre", log_file)

    # Étape 2 : gérer les coalitions vides
    empty = [c for c in coalitions if c not in chefs]
    if empty:
        log("Coalition(s) sans chef après Roll 1 : " + ", ".join(empty), log_file)
        for c in empty:
            if non_chefs:
                rep = random.choice(non_chefs)
                chefs[c] = rep
                non_chefs.remove(rep)
                log(f"  -> @ Migration : {rep['login']} devient chef de {c}", log_file)

    # Étape 3 : vérifier si au moins une femme est chef
    femmes = [c for c in chefs.values() if c["sexe"] == "F"]
    if not femmes:
        log("Vérification parité : aucune femme n'est chef.", log_file)
        femme_candidates = [p for p in participants if p["sexe"] == "F"]
        if femme_candidates:
            cible = random.choice(coalitions)
            nouvelle = random.choice(femme_candidates)
            log(f"Roll 2 - Forçage parité :", log_file)
            log(f"  -> Coalition choisie : {cible}", log_file)
            log(f"  -> Nouvelle cheffe : {nouvelle['login']}", log_file)
            chefs[cible] = nouvelle
        else:
            log("  -> Aucun profil féminin disponible pour correction.", log_file)
    else:
        log(f"Vérification parité : OK ({len(femmes)} femme(s) chef(s))", log_file)

    log("Tirage terminé avec succès.", log_file)
    return {
        c: {
            "nom": chefs[c]["nom"],
            "prenom": chefs[c]["prenom"],
            "login": chefs[c]["login"],
            "sexe": chefs[c]["sexe"],
        }
        for c in coalitions
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tirage.py data.json")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = "chefs.json"
    log_path = "tirage.log"

    data = load_data(input_path)

    with open(log_path, "w", encoding="utf-8") as log_file:
        result = run_tirage(data, log_file)

    save_result(output_path, result)
    print(f"\n✅ Tirage terminé. Résultat : {output_path}, Log : {log_path}")
