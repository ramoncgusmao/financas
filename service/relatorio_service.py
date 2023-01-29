
from datetime import datetime
from typing import List
from service.lancamento_service import LancamentoService


class RelatorioService:
    lancamento_service = LancamentoService()
    
    def saldo(self, subtrair: str):
        lancamentos = self.lancamento_service.buscar_todos()
        naturezas = {}
        for lancamento in lancamentos:
            if naturezas.setdefault(lancamento.tipo):
                naturezas[lancamento.tipo] += lancamento.valor
            else:
                naturezas[lancamento.tipo] = lancamento.valor
            
        naturezas['saldo'] = 0.0
        for chave in naturezas:
            naturezas[chave] = round(naturezas[chave], 2)
            if chave == 'saldo':
                continue
            if(chave == subtrair):
                naturezas['saldo'] -= naturezas[chave]
            else:
                naturezas['saldo'] += naturezas[chave]
        return naturezas

    
    def extrato(self, mes: int, ano: int):
        data_atal = datetime.now()
        if(mes == 0):
            mes = data_atal.month
        if(ano == 0):
            ano = data_atal.year

        lancamentos = self.lancamento_service.buscar_todos()
        return list(filter(lambda lanc: lanc.mes == mes and lanc.ano == ano, lancamentos))
    
    def consolidado_por_tipo(self, tipo: str, ano: int):
        lancamentos = self.lancamento_service.buscar_todos()
        lancamentos_filter = list(filter(lambda lanc: lanc.tipo == tipo and lanc.ano == ano, lancamentos))
        meses_dict = {}

        for lancamento in lancamentos_filter:
            if meses_dict.setdefault(lancamento.mes):
                meses_dict[lancamento.mes] += lancamento.valor
            else:
                meses_dict[lancamento.mes] = lancamento.valor
        return [
            {"mes": mes, "valor": round(valor,2), "tipo": tipo}
            for mes, valor in meses_dict.items()
        ]
