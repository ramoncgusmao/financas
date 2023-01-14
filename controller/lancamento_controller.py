
from fastapi import APIRouter

from domain.lancamento_dto import LancamentoDto
from service.lancamento_service import LancamentoService

lancamento_service = LancamentoService()

lancamento_route = APIRouter()

@lancamento_route.post("/")
async def salvar(lancamento_dto: LancamentoDto):
    return lancamento_service.salvar(lancamento_dto)
    