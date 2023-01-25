
from fastapi import APIRouter

from service.relatorio_service import RelatorioService


relatorio_route = APIRouter()
relatorio_service = RelatorioService()
@relatorio_route.get("/saldo")
def saldo(subtrair: str = 'saida'):
    return relatorio_service.saldo(subtrair)