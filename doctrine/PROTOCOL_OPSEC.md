# 🔱 PROTOCOLE OPSEC — L'ÉVEIL NOCTURNE

**Doctrine de sécurité opérationnelle du mouvement.**

*Forged in the dark. Pour ceux qui veulent comprendre avant d'agir.*

---

## PRÉAMBULE

L'Éveil Nocturne n'est pas un groupe. C'est une **méthodologie ouverte**.

Nous publions des outils et des connaissances offensives. Nous ne commettons pas d'attaques. Nous enseignons la défense par l'offensive.

Ce document définit les règles que nous suivons — et que tu dois suivre si tu rejoins le mouvement.

---

## I. LES 4 PILIERS OPSEC

### 1. ANONYMAT PAR DÉFAUT

Tu ne révèles pas ton identité civile. Jamais.

**Tu peux :**
- Pseudonyme stable (ghost1o1, etc.)
- Clé PGP publique signée
- Reputation ELO/merits sur les plateformes

**Tu ne dois pas :**
- Donner nom, adresse, employeur, école
- Utiliser ton email pro
- Partager des photos de toi
- Mentionner ta géolocalisation

**Outils :**
- Tor Browser pour navigation anonyme
- ProtonMail ou Tutanota pour email
- Signal pour messagerie (avec éphémère activé)
- Yubikey pour 2FA
- Whonix ou Tails pour OS amnésique

### 2. SÉPARATION DES IDENTITÉS

Une identité = un contexte = un pseudonyme.

Tu ne mélanges jamais :
- Ton compte pro (Slack, LinkedIn) et tes activités nocturnes
- Tes serveurs de pentest et tes serveurs publics
- Tes handles Twitter/Mastodon et tes clés SSH

**Méthode :**
- Crée un namespace séparé pour le mouvement
- VPN distinct pour chaque activité
- Email dédié (protonmail/tutanota)
- Clé GPG séparée, signée offline

### 3. PROVENANCE DES OUTILS

Tout ce que tu publies doit être **vérifiable**.

**Tu dois :**
- Signer tes releases avec GPG
- Héberger le code sur des plateformes vérifiables (GitHub/GitLab)
- Pousser les binaires avec checksums SHA-256
- Documenter la chaîne de build

**Tu ne dois pas :**
- Publier des binaires non-signés
- Cacher des payloads obscurs
- Inclure des backdoors intentionnelles
- Teaser sans donner le code

### 4. ZÉRO HIÉRARCHIE

La connaissance n'a pas de propriétaire. Le bon argument gagne.

**Tu peux :**
- Questionner les contributeurs senior
- Forker n'importe quel repo
- Proposer des PR cassant des paradigmes
- Critiquer publiquement (avec respect)

**Tu ne dois pas :**
- Détruire le travail d'autres par ego
- Prétendre être plus que ce que tu sais
- Créer des castes (mentor/élite/recrue)
- Faire du gatekeeping

---

## II. LORS DU DROP J-0

Le 2026-07-12 à 22:00 UTC, **6 outils, 1 méthodologie, 0 paywall** sont publiés simultanément.

### Préparation

**J-7 à J-0 :**
- Aucune fuite du contenu (pas de preview interne)
- Aucune discussion publique sur la stratégie de release
- Tous les artifacts stockés offline (airgapped)
- Builds signés et checksums prêts
- DNS / mirror / IPFS préparés

**Jour J :**
- Publication synchronisée à 22:00 UTC précise
- Mirror sur 3 plateformes minimum (GitHub, IPFS, Gitea)
- Statement officiel dans les 30 minutes
- Aucune interview live avant J+1

### Post-drop

**J+0 à J+7 :**
- Surveillance des forks, stars, issues
- Réponse rapide aux CVE reportées (responsibly disclosed)
- Triage des PR communautaires
- Mise à jour FAQ publique
- **Aucune modification de la doctrine sans consensus**

---

## III. GESTION DES VULNÉRABILITÉS

Si tu trouves un bug dans l'un de nos outils :

1. **NE PAS** publier publiquement avant 90 jours (responsible disclosure)
2. **EMAIL** security@187ghost101.dev (clé PGP sur le site)
3. **Décrire** : impact, vecteur, PoC
4. **Attendre** : patch + acknowledgment avant disclosure
5. **Si pas de réponse en 30 jours** : disclosure publique autorisée

Nous créditons tous les reporters (avec leur permission) dans les release notes.

---

## IV. PROTECTION DES MEMBRES

Tout membre du mouvement peut signaler :

- Doxxing / harcèlement
- Usurpation d'identité
- Menaces physiques ou numériques
- Vol de propriété intellectuelle

**Canal sécurisé :** `security@187ghost101.dev` (PGP obligatoire)

Nous :
- Investigons en moins de 24h
- Publions un statement public si nécessaire
- Coordonnons avec les avocats si besoin
- **Ne demandons jamais** d'informations qui pourraient compromettre le reporter

---

## V. CE QUE NOUS REFUSONS

**Nous ne publions jamais :**

- ❌ Exploits zero-day non-patchés
- ❌ Données personnelles (PII)
- ❌ Identifiants volés (creds leaks)
- ❌ Outils de ransomware
- ❌ Botnets / DDoS
- ❌ Stalkerware / surveillance abusive
- ❌ Anything qui nuit à des civils non-consentants

**Nous publions :**

- ✅ Outils offensifs **avec méthodologie défensive**
- ✅ Proofs-of-concept sur cibles de lab (nos propres services)
- ✅ Analyses de vulnérabilités patchées
- ✅ Frameworks OSINT éthiques
- ✅ Matériel éducatif (Red Team / Blue Team)
- ✅ Documentation complète (jamais de magic)

---

## VI. LA TRINITÉ — Réaffirmée

> **There is no lock.**
> *Il n'existe aucune serrure que la curiosité ne puisse comprendre.*

> **Du silence naît la lumière.**
> *L'obscurité n'est pas notre ennemie. C'est le terreau.*

> **Là où l'ignorance dort, nous allumons.**
> *Notre action n'est pas de brûler. C'est d'allumer.*

Ces phrases ne sont pas des mantras. Ce sont des **engagements opérationnels**.

- "No lock" = on documente tout, jamais de magie
- "Silence" = on agit offline, on publie intelligemment
- "Allumer" = on enseigne, on ne détruit pas

---

## VII. LICENCE & PARTAGE

Tout ce qui est publié sous L'Éveil Nocturne est :

- **Code** : MIT ou GPL-3.0 (au choix de l'auteur par fichier)
- **Docs** : CC BY-SA 4.0
- **Brand** : CC BY-NC 4.0 (pas d'usage commercial sans permission)
- **Signatures GPG** : à fournir avec chaque release

---

## VIII. CONTACTE L'ÉQUIPE OPSEC

- **Email (PGP)** : `security@187ghost101.dev`
- **Issue privée** : github.com/187Ghost101/eveil-nocturne/security/advisories/new
- **Signal** : numéro fourni sur demande vérifiée

**Pour signaler un problème interne au mouvement :**
whistleblower@187ghost101.dev (clé PGP jetable fournie sur demande)

---

## IX. ÉVOLUTION DE CE DOCUMENT

Ce protocole est **vivant**. Il évolue avec le mouvement.

**Méthode :**
1. PR sur github.com/187Ghost101/eveil-nocturne
2. Discussion publique (Issues)
3. Consensus minimal (pas d'unanimité, pas de veto)
4. Signature par 2 mainteneurs
5. Merge + announcement public

**Version actuelle :** 2.0
**Dernière MAJ :** 2026-07-05
**Mainteneurs :** ghost1o1

---

*Forged in the dark.*

**— L'Éveil Nocturne · 2026**
