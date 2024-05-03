from flask import Flask, request, jsonify
from particulier import Particulier

app = Flask(__name__)

@app.route('/python', methods=['POST'])
def votre_fonction_python():
    data = request.json
    adresse_de_depart = data.get('start')
    adresse_d_arrivee = data.get('end')
    moyen_de_locomotion = data.get('vehicle')
    Personne = Particulier(moyen_de_locomotion)
    results = Personne.eviter_zone_risquee(adresse_de_depart, adresse_d_arrivee)
    # Renvoyer les résultats au format JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
