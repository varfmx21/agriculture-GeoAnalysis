from flask import Flask, render_template, request, redirect, url_for # type: ignore

# use this command to activate virtual enviorment in git bash to run the app: source .venv/Scripts/activate
# to deactivate the virtual environment: deactivate
# for running the app use this command: python app.py

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/humedad')
def humedad():
    return render_template('humedad.html')

@app.route('/precipitacion')
def precipitacion():
    return render_template('precipitacion.html')

@app.route('/temperatura')
def temperatura():
    return render_template('temperatura.html')

@app.route('/vegetacion')
def vegetacion():
    return render_template('vegetacion.html')

@app.route('/fertilidad')
def fertilidad():
    return render_template('fertilidad.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

if __name__== '_main_':
    app.run(host='127.0.0.1', port=8000, debug=True)