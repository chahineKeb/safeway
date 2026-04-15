# 🛡️ SafeWay Toulouse

Application web de sécurité citoyenne pour la ville de Toulouse. Permet d'envoyer des alertes géolocalisées en temps réel, visibles par un réseau de Veilleurs citoyens.

**Projet réalisé dans le cadre d'un cours — 2025**

---

## Aperçu

![SafeWay](https://img.shields.io/badge/SafeWay-Toulouse-3b82f6?style=for-the-badge&logo=shield&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)

> 🌐 **Application en ligne** : [safeway.ananas-frais.fr](http://safeway.ananas-frais.fr)

---

## Fonctionnalités

- 🗺️ **Carte temps réel** — alertes géolocalisées sur OpenStreetMap (Leaflet.js)
- ⚠️ **3 niveaux d'alerte** — Inquiétude (orange) · Agression (orange foncé) · Urgence Police (rouge)
- 👥 **Réseau de Veilleurs** — citoyens actifs dans un rayon de 1 km
- 🆘 **Bouton SOS** — accès direct à l'alerte d'urgence
- 🌙 **Mode sombre** — avec carte dark (CartoDB Dark Matter)
- 📱 **Design mobile-first** — mockup téléphone sur desktop pour la présentation
- 🎬 **Splash screen** — page d'entrée animée avec effet radar

---

## Stack technique

| Couche | Technologie |
|--------|-------------|
| Backend | Python 3.11 + Flask |
| Frontend | HTML5 · CSS3 · JavaScript vanilla |
| Carte | Leaflet.js + OpenStreetMap / CartoDB |
| Hébergement | o2switch (Phusion Passenger) |
| Police | Inter — Google Fonts |

---

## Structure du projet

```
safeway-toulouse/
├── app.py                  # Serveur Flask (routes + données en mémoire)
├── passenger_wsgi.py       # Point d'entrée Phusion Passenger (o2switch)
├── requirements.txt        # Dépendances Python
├── run.bat                 # Lanceur Windows (double-clic)
├── templates/
│   └── index.html          # Interface complète (splash + app)
└── static/
    ├── css/
    │   └── style.css       # Design system complet (light + dark mode)
    └── js/
        └── app.js          # Logique carte, alertes, navigation, dark mode
```

---

## Lancer en local

### Prérequis
- Python 3.10+
- pip

### Installation

```bash
# Cloner le repo
git clone https://github.com/TON_USER/safeway-toulouse.git
cd safeway-toulouse

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py
```

Ouvrir **[http://localhost:5000](http://localhost:5000)** dans le navigateur.

**Ou sur Windows** : double-clic sur `run.bat`

---

## API

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET` | `/` | Page principale |
| `GET` | `/api/alerts` | Liste des alertes (JSON) |
| `POST` | `/api/alerts` | Ajouter une alerte |

### Exemple de réponse `/api/alerts`

```json
[
  {
    "id": "1",
    "lat": 43.6047,
    "lon": 1.4442,
    "level": "inquietude",
    "description": "Individu suspect suivant des passants.",
    "heure": "10:15",
    "lieu": "Place du Capitole"
  }
]
```

---

## Déploiement sur o2switch

1. Uploader les fichiers dans `/home/user/safeway.ananas-frais.fr/`
2. cPanel → **Setup Python App** → créer l'app :
   - Startup file : `passenger_wsgi.py`
   - Entry point : `application`
3. Terminal cPanel :
```bash
source /home/user/virtualenv/safeway.ananas-frais.fr/3.11/bin/activate
pip install flask
```
4. **Restart** l'app dans Setup Python App

---

## Contexte du projet

En France, l'espace public n'est pas le même pour tout le monde :

- **200 000** femmes victimes de violences physiques hors ménage chaque année *(INSEE)*
- **8 femmes sur 10** ont subi du harcèlement dans l'espace public

SafeWay répond à ce constat en créant un réseau de solidarité citoyenne instantané.

---
