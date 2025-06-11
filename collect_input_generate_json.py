import json


def input_coalitions():
    coalitions = []
    print("\n👉 Entrez les noms des coalitions (tapez 'fin' pour terminer) :")
    while True:
        entry = input(f"- Coalition {len(coalitions) + 1} : ").strip()
        if entry.lower() == "fin":
            break
        if entry:
            coalitions.append(entry)
    return coalitions


def input_participants():
    participants = []
    print("\n👉 Entrez les participants (tapez 'fin' comme prénom pour terminer) :")
    i = 1
    while True:
        print(f"\nParticipant {i} :")
        prenom = input("  Prénom : ").strip()
        if prenom.lower() == "fin":
            break
        nom = input("  Nom : ").strip()
        login = input("  Login (sans @) : ").strip().lstrip("@")
        sexe = input("  Sexe (M/F) : ").strip().upper()
        coalition = input("  Coalition : ").strip()

        participants.append(
            {
                "nom": nom,
                "prenom": prenom,
                "login": login,
                "sexe": sexe,
                "coalition": coalition,
            }
        )
        i += 1

    return participants


def main():
    print("=== Création d'un fichier JSON pour le tirage des chefs ===")
    coalitions = input_coalitions()
    participants = input_participants()

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
