# logik.py
import json
from flask import request, redirect, url_for, jsonify
import json

JSON_FILE_PATH = 'data.json'

def collect_data():
    if request.method == 'POST':
        # Zugriff auf die Formulardaten
        contact_id = request.form['contact_id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []


        existing_data = next((item for item in data if item['name'] == name and item['email'] == email and item['address'] == address and item['contact_id'] == contact_id), None)
        if existing_data:
            return redirect(url_for('index'))

        # Füge neue Daten hinzu
        new_data = {
            'contact_id': contact_id,
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
    
def delete_json():
    try:
        # Leere Liste (oder leeres Dictionary) in die JSON-Datei schreiben
        with open(JSON_FILE_PATH, 'w') as json_file:
            json.dump([], json_file)
        
        return jsonify({'message': 'JSON Datei wurde erfolgreich geleert.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_contact(contact_id):
    with open('data.json', 'r') as f:
        contacts = json.load(f)

    updated_contacts = [contact for contact in contacts if contact['id'] != contact_id] 

    with open('data.json', 'w')as f:
        json.dump(updated_contacts, f, indent=4)

        return True, "contact deleted succesfully"
    


