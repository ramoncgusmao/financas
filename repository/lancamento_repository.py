
from domain.lancamento import Lancamento


class LancamentoRepository:

    db_lancamento: list = []

    def save(self, lancamento: Lancamento) -> Lancamento:
        lancamento.id = len(self.db_lancamento) + 1
        self.db_lancamento.append(lancamento)
        return lancamento
    
    def find_all(self) -> list:
        return self.db_lancamento

    def find_by_id(self, id) -> list:

        return next(filter(lambda lancamento: lancamento.id == id, self.db_lancamento),None)