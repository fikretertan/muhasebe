from flask import Flask, send_from_directory, request, jsonify
import os
import json

app = Flask(__name__, static_url_path='', static_folder='.')

DATA_FILE = os.path.join(os.path.dirname(__file__), 'veriler.json')

DEFAULT_DATA = {
    "kasa": 0,
    "cariler": [],
    "ortaklar": [
        {"ad": "Ertan", "bakiye": 0, "sifre": "1234"},
        {"ad": "Fikret", "bakiye": 0, "sifre": "1234"}
    ],
    "hareketler": []
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/veriler', methods=['GET'])
def get_veriler():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_DATA, f, ensure_ascii=False, indent=2)
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "JSON okuma hatası", "details": str(e)}), 500

@app.route('/api/veriler', methods=['POST'])
def save_veriler():
    try:
        req_data = request.get_json()
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(req_data, f, ensure_ascii=False, indent=2)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": "Dosyaya yazılamadı", "details": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)