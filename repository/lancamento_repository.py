
from domain.lancamento import Lancamento


class LancamentoRepository:

    db_lancamento: list = []

    def save(self, lancamento: Lancamento) -> Lancamento:
        lancamento.id = len(self.db_lancamento) + 1
        self.db_lancamento.append(lancamento)
        return lancamento