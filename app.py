from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fipe', methods=['GET'])
def obter_dados_fipe():
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    ano = request.args.get('ano')

    url = f"https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros?codigoTabelaReferencia=277&codigoMarca={marca}&codigoModelo={modelo}&anoModelo={ano}&codigoTipoCombustivel=1&tipoVeiculo=carro&tipoConsulta=tradicional"
    headers = {
        'Referer': 'https://veiculos.fipe.org.br/'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Suporte ao formato JSONP para uso no Power BI
    callback = request.args.get('callback')
    if callback:
        return f"{callback}({jsonify(data).data.decode('utf-8')})"
    else:
        return jsonify(data)

if __name__ == '__main__':
    from flask_cors import CORS

CORS(app)
    app.run()
