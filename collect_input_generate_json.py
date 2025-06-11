import json


def input_coalitions():
    coalitions = []
    print("\n👉 Entrez les noms des coalitions (tapez 'fin' pour terminer) :")
    while True:
        entry = input(f"- Coalition {len(coalitions) + 1} : ").strip()
        if entry.lower() == "fin":
            break
        if not entry:
            print("  ⚠️  Nom de coalition vide, réessayez.")
            continue
        if entry in coalitions:
            print("  ⚠️  Cette coalition existe déjà, réessayez.")
            continue
        coalitions.append(entry)
    return coalitions


def input_participant(index, coalitions):
    print(f"\nParticipant {index} :")

    while True:
        prenom = input("  Prénom : ").strip()
        if prenom.lower() == "fin":
            return None
        if prenom:
            break
        print("  ⚠️  Prénom vide, réessayez.")

    while True:
        nom = input("  Nom : ").strip()
        if nom:
            break
        print("  ⚠️  Nom vide, réessayez.")

    while True:
        login = input("  Login (sans @) : ").strip().lstrip("@")
        if login:
            break
        print("  ⚠️  Login vide, réessayez.")

    while True:
        sexe = input("  Sexe (M/F) : ").strip().upper()
        if sexe in ["M", "F"]:
            break
        print("  ⚠️  Sexe invalide. Entrez M ou F.")

    while True:
        coalition = input("  Coalition : ").strip()
        if coalition in coalitions:
            break
        print("  ⚠️  Coalition inconnue. Réessayez parmi : " + ", ".join(coalitions))

    return {
        "nom": nom,
        "prenom": prenom,
        "login": login,
        "sexe": sexe,
        "coalition": coalition,
    }


def input_participants(coalitions):
    participants = []
    print("\n👉 Entrez les participants (tapez 'fin' comme prénom pour terminer) :")
    i = 1
    while True:
        participant = input_participant(i, coalitions)
        if participant is None:
            break
        participants.append(participant)
        i += 1
    return participants


def main():
    print("=== Création d'un fichier JSON pour le tirage des chefs ===")
    coalitions = input_coalitions()
    participants = input_participants(coalitions)

    data = {"coalitions": coalitions, "participants": participants}

    filename = input(
        "\n💾 Nom du fichier à enregistrer (par défaut: data.json) : "
    ).strip()
    if not filename:
        filename = "data.json"
    if not filename.endswith(".json"):
        filename += ".json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Données enregistrées dans {filename}")


if __name__ == "__main__":
    main()
