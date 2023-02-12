
from fastapi import APIRouter

from service.relatorio_service import RelatorioService


relatorio_route = APIRouter()
relatorio_service = RelatorioService()
@relatorio_route.get("/saldo")
def saldo(subtrair: str = 'saida'):
    return relatorio_service.saldo(subtrair)

@relatorio_route.get("/extrato")
def extrato(mes: int = 0, ano: int = 0): 
    return relatorio_service.extrato(mes, ano)

@relatorio_route.get("/consolidado/{tipo}/ano/{ano}")
def consolidado_por_tipo(tipo: str, ano: str): 
    ano = int(ano)
    return relatorio_service.consolidado_por_tipo(tipo, ano)