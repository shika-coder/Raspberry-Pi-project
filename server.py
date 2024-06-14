from flask import Flask, jsonify, request, render_template
from logik import collect_data, delete_json, delete_contact
import json

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

@app.route('/contacts')
def contacts():
    with open('data.json') as f:
        contacts = json.load(f)
    return jsonify(contacts)


@app.route('/delete_contact', methods=['POST'])
def delete_conatcs():
    return delete_contact()

@app.route('/view_contatcs')
def view_contacts():
    return render_template('contacts.html', methods=['POST'])

@app.route('/enter_contact', methods=['POST'])
def return_contact():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
