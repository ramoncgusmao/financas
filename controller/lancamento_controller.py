import codecs
import csv
from fastapi import APIRouter, File, UploadFile

from domain.lancamento_dto import LancamentoDto
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
