
from domain.lancamento import Lancamento


class LancamentoRepository:

    db_lancamento: list = []
    indice: int = 0

    def save(self, lancamento: Lancamento) -> Lancamento:
        self.indice += 1
        lancamento.id = self.indice
        self.db_lancamento.append(lancamento)
        return lancamento
    
    def find_all(self) -> list:
        return self.db_lancamento

    def find_by_id(self, id) -> list:

        return next(filter(lambda lancamento: lancamento.id == id, self.db_lancamento),None)

    def delete(self, id):
        lancamento = self.find_by_id(id)
        self.db_lancamento.remove(lancamento)

    def update(self, lancamento_antigo: Lancamento, lancamento_novo: Lancamento) -> Lancamento:
        indice = self.db_lancamento.index(lancamento_antigo)
        self.db_lancamento[indice] = lancamento_novo
        return lancamento_novo

    
    