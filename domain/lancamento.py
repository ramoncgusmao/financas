from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Lancamento:

    id: int
    descricao: str
    tipo: str
    data_cadastro: datetime
    data_pagamento: datetime
    valor: float
    mes: int
    ano: int
    
    