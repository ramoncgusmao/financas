
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

    


