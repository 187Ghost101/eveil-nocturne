# 🔱 L'ÉVEIL NOCTURNE — Discord Bot

Bot Discord officiel du mouvement L'Éveil Nocturne.

## Installation

```bash
pip install discord.py
export DISCORD_TOKEN="your_token_here"
python3 bot.py
```

## Get a token

1. Go to https://discord.com/developers/applications
2. New Application → "L'Éveil Nocturne"
3. Bot tab → Reset Token → copy
4. Enable MESSAGE CONTENT INTENT
5. Invite to your server via OAuth2 URL generator

## Features

- `/serment` — Affiche les 4 engagements du mouvement
- `/arsenal` — Liste les 6 outils open-source
- `/countdown` — Temps avant le drop J-0
- `/sigil` — Affiche le sigil et la trinité
- `/manifesto` — Lien vers le manifeste
- `/aide` — Liste des commandes
- Welcome message branded (auto) à chaque nouveau membre
- Auto-reaction avec 🖤 sur les 🔱 / ☾ / ◉

## Customize

Edit `BRAND` dict in `bot.py`:
- name, tagline, trinity
- principles, serment, arsenal
- colors (hex)
- drop_date

## License

CC BY-SA 4.0 — L'Éveil Nocturne 2026
