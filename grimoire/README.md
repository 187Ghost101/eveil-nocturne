# 📜 LE GRIMOIRE — L'Éveil Nocturne

Artefact visuel interactif du mouvement L'Éveil Nocturne.

Un manifeste chiffré qui se révèle quand tu le touches. Trois phases :
- **LA LUNE** — silence et lune montante
- **L'ŒIL** — la vérité s'ouvre
- **LE SIGNAL** — le feu s'allume

## Usage

```bash
# Ouverture
open grimoire.html

# Ou via Python
python3 -m http.server 8080
# → http://localhost:8080/grimoire.html
```

## Le cipher

Le grimoire contient un cipher à 3 couches :
1. **ROT13** sur les phrases du manifeste
2. **Substitution simple** (clé = "L'EVEIL NOCTURNE 2026")
3. **Hash SHA-256** de l'engagement ("There is no lock.")

Quand tu cliques, le cipher se déchiffre en temps réel. Le grimoire "sait" que tu es prêt quand tu dépasses 7 secondes d'attention.

## Fichiers

- `grimoire.html` — artefact principal (auto-suffisant)
- `README.md` — ce fichier
