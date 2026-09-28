from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'veriler.json'

@app.route('/')
def ana_sayfa():
    # Flask otomatik olarak templates/index.html dosyasını okur
    return render_template('index.html')

# (Geri kalan /api/kaydet ve /api/kayitlar kodları aynı kalacak)