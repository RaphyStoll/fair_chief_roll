# 🧠 Tirage de Chefs de Coalition

Ce programme permet de tirer aléatoirement un chef par coalition à partir d'une liste de
participants, avec une règle de parité (au moins une femme doit être chef).

## ✅ Fonctionnalités principales

- Tirage aléatoire d'un chef par coalition
- Gestion des coalitions vides (membres extérieurs peuvent être assignés)
- Garantie d'avoir au moins une femme parmi les chefs
- Sortie des résultats dans un fichier JSON
- Journalisation (.log) des étapes pour transparence
- Script bash pour enchaîner toutes les étapes facilement

---

## 📝 Format attendu du fichier JSON d'entrée

Le fichier doit avoir deux clés principales : `coalitions` et `participants`.

```json
{
  "coalitions": ["Pinguin", "Gronouille", "Requin"],
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

- `login` **ne doit pas contenir de `@`** (il est ajouté automatiquement)
- `sexe` doit être `"M"` ou `"F"`
- `coalition` doit être un nom présent dans la liste `coalitions`

---

## 🚀 Utilisation via script Bash

Utiliser le script `run_tirage.sh` pour exécuter toutes les étapes :

```bash
bash run_tirage.sh
```

Ce script permet de :

1. Choisir entre créer un nouveau fichier ou charger un fichier existant
2. Lancer automatiquement le tirage
3. Afficher les résultats dans le terminal

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
uniquement les données minimales : nom, prénom, login (@tag), sexe.
