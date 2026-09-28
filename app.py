import json
import os
from flask import Flask, render_template, request

# template_folder='.' diyerek index.html dosyasını aynı klasörden okumasını sağlıyoruz
app = Flask(__name__, template_folder='.')


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/kaydet', methods=['POST'])
def kaydet():
  ad = request.form.get('ad')
  soyad = request.form.get('soyad')
  telefon = request.form.get('telefon')
  mesaj = request.form.get('mesaj')

  yeni_veri = {'ad': ad, 'soyad': soyad, 'telefon': telefon, 'mesaj': mesaj}

  veri_listesi = []
  if os.path.exists('veriler.json'):
    try:
      with open('veriler.json', 'r', encoding='utf-8') as f:
        veri_listesi = json.load(f)
    except:
      veri_listesi = []

  veri_listesi.append(yeni_veri)

  with open('veriler.json', 'w', encoding='utf-8') as f:
    json.dump(veri_listesi, f, ensure_ascii=False, indent=4)

  return '<h1>Mesajınız Başarıyla Kaydedildi!</h1><a href="/">Geri Dön</a>'


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 10000))
  app.run(host='0.0.0.0', port=port)
