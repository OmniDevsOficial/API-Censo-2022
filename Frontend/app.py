from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/mapa')
# def mapa():
#     return render_template('mapa.html')

@app.route('/sobre')
def sobre():
     return render_template('sobre.html')

@app.route('/graficos')
def graficos():
    return render_template('graficos_sjc.html')

@app.route('/grafico/<regiao>/<tipo>')
def get_grafico(regiao, tipo):
    """
    Retorna o HTML de um gráfico específico
    regiao: sjc, Norte, Sul, Leste, Oeste, Centro
    tipo: piramide_2010, piramide_2022, populacao, taxa_crescimento
    """
    # Mapeamento dos tipos de gráficos para os nomes de arquivos
    graficos_map = {
        'sjc': {
            'piramide_2010': 'graficos/piramide_etaria_sjc_2010.html',
            'piramide_2022': 'graficos/piramide_etaria_sjc_2022.html',
            'populacao': 'graficos/populacao_regiao_sjc.html',
            'taxa_crescimento': 'graficos/taxa_crescimento_sjc.html',
            'nivel_escolaridade': 'graficos/nivel_escolaridade_sjc.html',
            'internet_domicilio': 'graficos/internet_domicilio_sjc.html',
            'oeste_sul': 'graficos/populacao_regiao_oeste_x_sul.html'
        },
        'Norte': {
            'populacao': 'graficos/populacao_regiao_Norte.html',
            'populacao_bairro': 'graficos/populacao_bairro_Norte.html'
        },
        'Sul': {
            'populacao': 'graficos/populacao_regiao_Sul.html',
            'populacao_bairro': 'graficos/populacao_bairro_Sul.html'
        },
        'Leste': {
            'populacao': 'graficos/populacao_regiao_Leste.html',
            'populacao_bairro': 'graficos/populacao_bairro_Leste.html'
        },
        'Oeste': {
            'populacao': 'graficos/populacao_regiao_Oeste.html',
            'populacao_bairro': 'graficos/populacao_bairro_Oeste.html'
        },
        'Centro': {
            'populacao': 'graficos/populacao_regiao_Centro.html',
            'populacao_bairro': 'graficos/populacao_bairro_Centro.html'
        },
        'Sudeste': {
            'populacao': 'graficos/populacao_regiao_Sudeste.html',
            'populacao_bairro': 'graficos/populacao_bairro_Sudeste.html'
        },
        'São Francisco Xavier': {
            'populacao_bairro': 'graficos/populacao_bairro_São Francisco Xavier.html'
        }
    }
    
    # Buscar o template do gráfico
    if regiao in graficos_map and tipo in graficos_map[regiao]:
        template_path = graficos_map[regiao][tipo]
        return render_template(template_path)
    else:
        return "<p>Gráfico não disponível</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
