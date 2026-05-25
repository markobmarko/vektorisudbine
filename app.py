from flask import Flask, render_template, request
import requests

app = Flask(__name__)
SHEETDB_URL = 'https://sheetdb.io/api/v1/kbqi7gj0xrc09'

def get_zodiac_sign(m, d):
    m, d = int(m), int(d)
    if (m == 3 and 21 <= d <= 31) or (m == 4 and 1 <= d <= 19): return "Ovan"
    if (m == 4 and 20 <= d <= 30) or (m == 5 and 1 <= d <= 20): return "Bik"
    if (m == 5 and 21 <= d <= 31) or (m == 6 and 1 <= d <= 20): return "Blizanac"
    if (m == 6 and 21 <= d <= 30) or (m == 7 and 1 <= d <= 22): return "Rak"
    if (m == 7 and 23 <= d <= 31) or (m == 8 and 1 <= d <= 22): return "Lav"
    if (m == 8 and 23 <= d <= 31) or (m == 9 and 1 <= d <= 22): return "Devica"
    if (m == 9 and 23 <= d <= 30) or (m == 10 and 1 <= d <= 22): return "Vaga"
    if (m == 10 and 23 <= d <= 31) or (m == 11 and 1 <= d <= 21): return "Škorpija"
    if (m == 11 and 22 <= d <= 30) or (m == 12 and 1 <= d <= 21): return "Strelac"
    if (m == 12 and 22 <= d <= 31) or (m == 1 and 1 <= d <= 19): return "Jarac"
    if (m == 1 and 20 <= d <= 31) or (m == 2 and 1 <= d <= 18): return "Vodolija"
    if (m == 2 and 19 <= d <= 29) or (m == 3 and 1 <= d <= 20): return "Riba"
    return "Nepoznat"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        m = request.form.get('m_rodj')
        d = request.form.get('d_rodj')
        y = request.form.get('g_rodj')
        ime = request.form.get('ime')
        znak = get_zodiac_sign(m, d)
        
        data = {
            'Ime': ime, 'Znak': znak, 'Datum': f"{m}.{d}.{y}",
            'Otac': f"{request.form.get('ime_otac')} ({request.form.get('m_otac')}.{request.form.get('d_otac')}.{request.form.get('g_otac')})",
            'Majka': f"{request.form.get('ime_majka')} ({request.form.get('m_majka')}.{request.form.get('d_majka')}.{request.form.get('g_majka')})"
        }
        try: requests.post(SHEETDB_URL, json=data)
        except: pass
        
        analiza = (f"Vaš primarni vektor, definisan kao {znak}, ukazuje na retku astralnu konjukciju "
                   "u trenutku rođenja. Korelacija sa podacima roditelja otkriva karmičke tragove "
                   "koji definišu 2026. godinu. Vaša energija je u fazi 'otključavanja', gde se "
                   "blokade iz prošlosti transformišu u prilike za uspeh.")
        
        return render_template('rezultat.html', ime=ime, znak=znak, analiza=analiza)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)