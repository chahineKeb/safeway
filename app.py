from flask import Flask, render_template, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# Alertes simulées en mémoire (remises à zéro au redémarrage)
alerts = [
    {
        "id": "1",
        "lat": 43.6047,
        "lon": 1.4442,
        "level": "inquietude",
        "description": "Individu suspect suivant des passants depuis plusieurs minutes.",
        "heure": "10:15",
        "lieu": "Place du Capitole"
    },
    {
        "id": "2",
        "lat": 43.6008,
        "lon": 1.4458,
        "level": "agression",
        "description": "Vol à l'arraché signalé près de la sortie du métro.",
        "heure": "09:45",
        "lieu": "Métro Jean-Jaurès"
    },
    {
        "id": "3",
        "lat": 43.6112,
        "lon": 1.4285,
        "level": "urgence",
        "description": "Besoin d'aide immédiate — patrouille demandée d'urgence.",
        "heure": "10:30",
        "lieu": "Parc Compans-Caffarelli"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)


@app.route('/api/alerts', methods=['POST'])
def add_alert():
    data = request.get_json(force=True)
    new_alert = {
        "id": str(uuid.uuid4()),
        "lat": float(data.get('lat', 43.6045)),
        "lon": float(data.get('lon', 1.4440)),
        "level": data.get('level', 'inquietude'),
        "description": data.get('description', 'Alerte signalée par un utilisateur.'),
        "heure": datetime.now().strftime('%H:%M'),
        "lieu": data.get('lieu', 'Toulouse')
    }
    alerts.append(new_alert)
    return jsonify(new_alert), 201


if __name__ == '__main__':
    print("=" * 50)
    print("  SafeWay Toulouse — Démarrage du serveur")
    print("  Ouvrez : http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
