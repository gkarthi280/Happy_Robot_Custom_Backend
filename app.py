from flask import Flask, jsonify, abort
import csv

app = Flask(__name__)

@app.route('/loads/<reference_number>', methods=['GET'])
def get_load(reference_number):
    with open('loads.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['reference_number'].lower() == reference_number.lower():
                return jsonify(row)
    abort(404, description="Load not found")

if __name__ == '__main__':
    app.run(debug=True)
