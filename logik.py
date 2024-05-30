# logik.py
import json
from flask import request, redirect, url_for

def collect_data():
    if request.method == 'POST':
        # Zugriff auf die Formulardaten
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []


        existing_data = next((item for item in data if item['name'] == name and item['email'] == email and item['address'] == address), None)
        if existing_data:
            return redirect(url_for('index'))

        # Füge neue Daten hinzu
        new_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address
        }
        data.append(new_data)

        # Speichere die Daten in die JSON-Datei
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('index'))

