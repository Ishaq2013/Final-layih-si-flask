from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/etimalogiyası')
def etimalogiyası():
    return render_template('etimalogiyası.html')

@app.route('/tarixi')
def tarixi():
    return render_template('tarixi.html')

@app.route('/təklif və iradlar')
def təklif_və_iradlar():
    return render_template('təklif və iradlar.html')

@app.route('/məlumat')
def məlumat():
    return render_template('məlumat.html')

@app.route('/nəticə' , methods=['POST'])
def netice():
    teklif = request.form.get('teklif')
    email = request.form.get('email')
    return render_template('nəticə.html', təklif=teklif, email=email)

@app.route('/eko-toksikologiya və qanlı minerallar')
def eko_toksikologiya_və_qanlı_minerallar():
    return render_template('eko-toksikologiya və qanlı minerallar (kritik araşdırma).html')

@app.route('/telefonun təkamülündə sturuktur və material analizi')
def telefonun_təkamülündə_struktur_və_material_analizi():
    return render_template('telefonun təkamülündə struktur və material analizi.html')

@app.route('/müqayisəli analiz klasik telefonlar və smartfonlar')
def müqayisəli_analiz_klasik_telefonlar_və_smartfonlar():
    return render_template('müqayisəli analiz klassik telefonlar və smartfonlar.html')

@app.route('/qlobal sosial iqtisadi təsirlər')
def qlobal_sosial_iqtisadi_təsirlər():
    return render_template('qlobal sosial-iqtisadi təsirlər (statistik araşdırma).html')

@app.route('/smartfonların arxasındakı gizli elm sensorlar ordusu')
def smartfonların_arxasındakı_gizli_elm():
    return render_template('smartfonların arxasındakı gizli elm sensorlar ordusu.html')

if __name__ == '__main__':
    app.run(debug=True) 