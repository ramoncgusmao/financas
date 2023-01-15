
from datetime import datetime
from domain.lancamento import Lancamento
from domain.lancamento_dto import LancamentoDto
from repository.lancamento_repository import LancamentoRepository


class LancamentoService:

    lancamento_repository = LancamentoRepository()
    
    def salvar(self, lancamento_dto: LancamentoDto) -> Lancamento:

        lancamento = Lancamento(
            id = 1,
            descricao=lancamento_dto.descricao,
            tipo = lancamento_dto.tipo,
            valor = lancamento_dto.valor,
            data = datetime.now()
        )
        
        return self.lancamento_repository.save(lancamento)
    
    def buscar_todos(self) -> list:
        return self.lancamento_repository.find_all()

    def buscar_por_id(self, id) -> list:
        return self.lancamento_repository.find_by_id(id)