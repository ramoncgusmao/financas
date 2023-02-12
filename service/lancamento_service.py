
from datetime import datetime
import random
from typing import List
from domain.lancamento import Lancamento
from domain.lancamento_dto import LancamentoDto
from domain.parametros_lote_dto import ParametrosLoteDto
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
            mes= lancamento_dto.data_pagamento.month,
            ano= lancamento_dto.data_pagamento.year
        )
        
        return self.lancamento_repository.save(lancamento)
    
    def buscar_todos(self) -> List[Lancamento]:
        return self.lancamento_repository.find_all()

    def buscar_por_id(self, id) -> Lancamento:
        return self.lancamento_repository.find_by_id(id)
    
    def deletar(self, id):
        self.lancamento_repository.delete(id)

    def atualizar(self, id, lancamento_dto: LancamentoDto) -> Lancamento:
        lancamento_antigo = self.buscar_por_id(id)

        lancamento_novo = Lancamento(
            id = lancamento_antigo.id,
            descricao=lancamento_dto.descricao,
            tipo = lancamento_dto.tipo,
            valor = float(lancamento_dto.valor),
            data = lancamento_antigo.data
        )

        return self.lancamento_repository.update(lancamento_antigo, lancamento_novo)
    
    def salvar_lote(self, list_json: list):
        list_lancamento: List[Lancamento] = []
        for json_lancamento in list_json:
            data_pagamento = datetime.strptime(json_lancamento['data_pagamento'],'%m/%d/%Y')
            lancamento_dto = LancamentoDto(
                descricao=json_lancamento['descricao'],
                tipo=json_lancamento['tipo'],
                valor=float(json_lancamento['valor']),
                data_pagamento=data_pagamento
            )
            list_lancamento.append(self.salvar(lancamento_dto=lancamento_dto))
        return list_lancamento

    def popular_lancamentos(self,paramentos_lote: ParametrosLoteDto) -> List[LancamentoDto]:
        lancamentos_dto: List[LancamentoDto] = []
        entradas = ['salario', 'freelance', 'dinheiro emprestado', 'extra']
        saidas = ['luz', 'agua', 'supermercado', 'lanche', 'cinema', 'cartao de credito', 'internet']
        for i in range(paramentos_lote.quantidade):
            indice = random.randint(0, (len(saidas) - 1))
            descricao = saidas[indice]
            tipo = 'pago'
            valor = random.uniform(10.0, 500.00)
            dia = random.randint(1,28)
            mes = random.randint(1,12)
            if(i % 4 == 0):
                tipo = 'recebido'
                valor = random.uniform(500.0, 3000.00)
                indice = random.randint(0, (len(entradas) - 1))
                descricao = entradas[indice]
            
            valor = round(valor, 2)
            data_pagamento = datetime(year=paramentos_lote.ano, month=mes, day=dia)
            lancamento_dto = LancamentoDto(descricao=descricao, tipo=tipo, valor=valor, data_pagamento=data_pagamento)
            lancamentos_dto.append(lancamento_dto)
        return lancamentos_dto
