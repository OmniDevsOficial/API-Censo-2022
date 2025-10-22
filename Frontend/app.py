from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/grafico')
def grafico():
    return render_template('grafico.html')


if __name__ == '__main__':
    app.run(debug=True)
