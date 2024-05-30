from flask import Flask, jsonify, request, render_template
from logik import collect_data, delete_json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        # Rufe die Funktion collect_data aus der logik.py-Datei auf
        result = collect_data()

        # Hier kannst du die Rückgabe der collect_data-Funktion weiterverarbeiten
        # Zum Beispiel in der Antwort verwenden oder in einer Datenbank speichern

        return result

@app.route('/delete_json', methods=['POST'])
def delete():
    return delete_json()

if __name__ == '__main__':
    app.run(debug=True)
