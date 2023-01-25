import codecs
import csv
from datetime import datetime 
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from domain.lancamento_dto import LancamentoDto
from domain.parametros_lote_dto import ParametrosLoteDto
from service.lancamento_service import LancamentoService

lancamento_service = LancamentoService()

lancamento_route = APIRouter()

@lancamento_route.post("/", status_code=201)
async def salvar(lancamento_dto: LancamentoDto):
    return lancamento_service.salvar(lancamento_dto)
    

@lancamento_route.get("/")
async def buscar_todos():
    return lancamento_service.buscar_todos()

@lancamento_route.get("/{id}")
async def buscar_todos(id: int):
    return lancamento_service.buscar_por_id(id)


@lancamento_route.delete("/{id}", status_code=204)
async def deletar(id: int):
    lancamento_service.deletar(id)

@lancamento_route.put("/{id}")
async def atualizar(id: int, lancamento_dto: LancamentoDto):
    return lancamento_service.atualizar(id, lancamento_dto)

@lancamento_route.post("/em-lote")
async def salvar_lote(arquivo: UploadFile = File()):
    csv_reader = csv.DictReader(codecs.iterdecode(arquivo.file, 'utf-8'))
    csv_list = list(csv_reader)
    arquivo.file.close()
    return lancamento_service.salvar_lote(csv_list)


@lancamento_route.post("/popular")
def popular_lancamento(parametros_de_lote: ParametrosLoteDto):
    lancamentos_dto = lancamento_service.popular_lancamentos(parametros_de_lote)
    file_path = 'arquivo_lancamento.csv'
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['descricao', 'tipo','valor', 'data_pagamento'])
        for lacamento in lancamentos_dto:
            data_pagamento = lacamento.data_pagamento.strftime('%m/%d/%Y')
            writer.writerow([lacamento.descricao, lacamento.tipo, lacamento.valor, data_pagamento])


    return FileResponse(file_path)    