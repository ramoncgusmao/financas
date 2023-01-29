
from fastapi import APIRouter

from service.moeda_service import MoedaService


moeda_route = APIRouter()
moeda_service = MoedaService()
@moeda_route.get("/hoje")
def moedas_hoje():
    return moeda_service.buscar_moedas()