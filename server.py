import flask
from logik import collect_data  # Importiere die Funktion collect_data aus logik.py

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

if __name__ == '__main__':
    app.run(debug=True)
