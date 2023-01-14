from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class LancamentoDto:
    descricao: str
    tipo: str
    valor: float
