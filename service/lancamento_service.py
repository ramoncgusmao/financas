
from datetime import datetime
from typing import List
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
            data_cadastro = datetime.now(),
            data_pagamento= lancamento_dto.data_pagamento,
        )
        
        return self.lancamento_repository.save(lancamento)
    
    def buscar_todos(self) -> list:
        return self.lancamento_repository.find_all()

    def buscar_por_id(self, id) -> list:
        return self.lancamento_repository.find_by_id(id)
    
    def deletar(self, id):
        self.lancamento_repository.delete(id)

    def atualizar(self, id, lancamento_dto: LancamentoDto) -> Lancamento:
        lancamento_antigo = self.buscar_por_id(id)

        lancamento_novo = Lancamento(
            id = lancamento_antigo.id,
            descricao=lancamento_dto.descricao,
            tipo = lancamento_dto.tipo,
            valor = lancamento_dto.valor,
            data = lancamento_antigo.data
        )

        return self.lancamento_repository.update(lancamento_antigo, lancamento_novo)
    
    def salvar_lote(self, list_json: list):
        list_lancamento: List[Lancamento] = []
        for json_lancamento in list_json:
            
            lancamento_dto = LancamentoDto(
                descricao=json_lancamento['descricao'],
                tipo=json_lancamento['tipo'],
                valor=json_lancamento['valor'],
                data_pagamento=json_lancamento['data_pagamento']
            )
            list_lancamento.append(self.salvar(lancamento_dto=lancamento_dto))
        return list_lancamento
