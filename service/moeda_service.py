
import json
import requests


class MoedaService():

    moedas = {
        'dollar': 'USD-BRL',
        'euro': 'EUR-BRL',
        'Libra': 'GBP-BRL'
    }

    def chamar_api(self, moeda: str):
       url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
       valores = requests.get(url=url)
       return json.loads(valores.text)

    def buscar_moedas(self):
        valores_em_reais = []
        for chave in self.moedas:
            valores = self.chamar_api(self.moedas[chave])
            chave_valores = valores.popitem()
            
            valor = chave_valores[1]
            valores_em_reais.append({'moeda': chave, 'maxima': valor['high'], 'minima': valor['low'], 'data': valor['create_date']})
        return valores_em_reais