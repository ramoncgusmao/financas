from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Lancamento:

    id: int
    descricao: str
    entrada: str
    data: datetime
    valor: Optional[float] = 0.0
    



if __name__ == '__main__':
    x = Lancamento(1, "salario", "entrada", datetime.now())
    print(x)
    print(x.descricao)
    print(x.valor)
    x.valor = 3000
    print(x.valor)
    print(x)