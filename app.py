from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Vercel üçün lazım olan əsas obyekt yönləndirilməsi
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/etimologiya')
def etimalogiyası():
    return render_template('etimalogiyası.html')

@app.route('/tarix')
def tarixi():
    return render_template('tarixi.html')

@app.route('/teklif-ve-iradlar')
def təklif_və_iradlar():
    return render_template('təklif və iradlar.html')

@app.route('/melumat')
def məlumat():
    return render_template('məlumat.html')

@app.route('/netice', methods=['POST'])
def netice():
    teklif = request.form.get('teklif')
    email = request.form.get('email')
    return render_template('nəticə.html', təklif=teklif, email=email)

@app.route('/eko-toksikologiya')
def eko_toksikologiya_və_qanlı_minerallar():
    return render_template('eko-toksikologiya və qanlı minerallar (kritik araşdırma).html')

@app.route('/struktur-analiz')
def telefonun_təkamülündə_struktur_və_material_analizi():
    return render_template('telefonun təkamülündə struktur və material analizi.html')

@app.route('/muqayiseli-analiz')
def müqayisəli_analiz_klasik_telefonlar_və_smartfonlar():
    return render_template('müqayisəli analiz klassik telefonlar və smartfonlar.html')

@app.route('/sosial-iqtisadi-tesirler')
def qlobal_sosial_iqtisadi_təsirlər():
    return render_template('qlobal sosial-iqtisadi təsirlər (statistik araşdırma).html')

@app.route('/gizli-elm-sensorlar')
def smartfonların_arxasındakı_gizli_elm():
    return render_template('smartfonların arxasındakı gizli elm sensorlar ordusu.html')

# Vercel-in layihəni oxuması üçün bu sətir mütləq qalmalıdır
# app.run hissəsini Vercel özü idarə edir.
