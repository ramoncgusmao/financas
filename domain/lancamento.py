from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Lancamento:

    id: int
    descricao: str
    tipo: str
    data: datetime
    valor: Optional[float] = 0.0
    