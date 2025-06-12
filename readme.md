# 🧠 Tirage de Chefs de Coalition

Ce programme permet de tirer aléatoirement un chef par coalition à partir d'une liste de
participants, avec une règle de parité (au moins une femme doit être chef).

---

## ✅ Fonctionnalités principales

- 🎲 Tirage aléatoire d'un chef par coalition
- 🔄 Gestion des coalitions vides (membres extérieurs peuvent être assignés)
- 👩‍🦰 Garantie d'avoir au moins une femme parmi les chefs
- 📤 Sortie des résultats dans un fichier `JSON`
- 🪵 Journalisation (`.log`) des étapes pour transparence
- 🛠️ Script bash pour enchaîner toutes les étapes facilement

---

## ⚙️ Installation rapide

```bash
git clone https://github.com/tonrepo/fair-chef-roll.git
cd fair-chef-roll
chmod +x run_tirage.sh
```

---

## ✅ Prérequis

- Python 3.7 ou plus
- Aucun package externe requis (standard library uniquement)

---

## 📝 Format attendu du fichier JSON d'entrée

Le fichier doit avoir deux clés principales : `coalitions` et `participants`.

```json
{
  "coalitions": ["Pinguin", "Grenouille", "Requin"],
  "participants": [
    {
      "nom": "Durand",
      "prenom": "Alice",
      "login": "adurand",
      "sexe": "F",
      "coalition": "Pinguin"
    },
    {
      "nom": "Martin",
      "prenom": "Bob",
      "login": "bmartin",
      "sexe": "M",
      "coalition": "Pinguin"
    }
    // etc.
  ]
}
```

✅ **Contraintes :**

- `login` ne doit **pas contenir de @** (il est ajouté automatiquement)
- `sexe` doit être **"M" ou "F"** (insensible à la casse)
- `coalition` doit être un nom présent dans la liste `coalitions`

---

## 🚀 Utilisation via script Bash

Utiliser le script `run_tirage.sh` pour exécuter toutes les étapes :

```bash
bash run_tirage.sh
```

Ce script permet de :

- Choisir entre **créer un nouveau fichier** ou **charger un fichier existant**
- Lancer automatiquement le **tirage**
- Afficher les **résultats dans le terminal**

---

## 🧪 Exemple d'exécution manuelle (test rapide)

```bash
python collect_input_generate_json.py  # Crée un fichier data.json interactif
python tirage.py data.json             # Lance le tirage
python display_chefs.py chefs.json     # Affiche le résultat dans le terminal
```

---

## 🧪 Tests

Un fichier de test prêt à l'emploi est fourni : `test_data.json`

Deux options pour le lancer :

### 1. En ligne de commande directe :

```bash
python tirage.py test_data.json
python display_chefs.py chefs.json
```

### 2. Depuis le script bash interactif :

Lorsque `run_tirage.sh` demande si vous souhaitez charger un fichier JSON existant, répondez **o**,
puis indiquez :

```bash
bash run_tirage.sh
🎲 Lancement du tirage de chefs de coalition
Souhaitez-vous charger un fichier JSON existant ? (o/n) : o
Entrez le nom du fichier JSON (ex: data.json) : test_data.json
```

Cela permet de valider le bon fonctionnement du tirage sans saisir de données manuellement.

---

## 📂 Fichiers générés

- `chefs.json` : résultat final du tirage (1 chef par coalition)
- `tirage.log` : journal détaillé du processus

---

## 👤 Exemple de sortie (terminal)

```

👑 Résultat du tirage des chefs de coalition :

- Pinguin : Alice Durand (@adurand) ♀️
- Gronouille : Bob Martin (@bmartin) ♂️
- Requin : Claire Doe (@cdoe) ♀️

```

---

## 💬 Intégration future (Discord Bot)

Le format `chefs.json` est conçu pour être facilement utilisable par un bot Discord. Il contient
uniquement les données minimales : `nom`, `prenom`, `login` (@tag), `sexe`.

---

## 📜 Licence

MIT – libre à utiliser, modifier, partager

```

```
