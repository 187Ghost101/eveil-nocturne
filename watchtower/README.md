# 🔱 LA TOUR DE GUET — Watchtower

**Surveillance temps-réel du mouvement L'Éveil Nocturne.**

Dashboard interactif : sigil 3D animé, compte à rebours live, flux de signal, métriques GitHub, présence sociale.

## Accès

- **Live**: `https://187ghost101.github.io/eveil-nocturne/watchtower/`
- **Self-hosted**: `python3 serve.py` (port 8080)
- **Embed**: `<iframe src="..." width="100%" height="600"></iframe>`

## Features

- ⏳ Countdown live vers J-0 (2026.07.12 22:00 UTC)
- 🔱 Sigil 3D animé (Three.js)
- 📡 Signal feed (mock + GitHub API events)
- 📊 Métriques live (forks, stars, views)
- 🌍 Présence géo (mock positions)
- 🎵 Anthem audio
- 🔐 Easter eggs (Konami, console, hidden text)

## Tech

- HTML5 + Three.js (CDN)
- Canvas 2D fallback
- GitHub REST API (live data)
- LocalStorage pour préférences
- 100% client-side — aucun serveur requis
