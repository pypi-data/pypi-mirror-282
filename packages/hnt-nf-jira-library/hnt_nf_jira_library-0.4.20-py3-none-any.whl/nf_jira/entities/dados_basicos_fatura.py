from pydantic import BaseModel
from typing import List, Optional

from .itens_fatura import ItensFatura

class DadosBasicosFatura(BaseModel):
    cod_fornecedor: str
    data_fatura: str
    referencia: Optional[str] = None
    montante: float
    valor_bruto: Optional[float]=0.0
    valor_liquido: Optional[float]
    juros: float=0    
    bus_pl_sec_cd: str
    texto: str
    centro_custo_destinatario: str
    centro_destinatario: str
    itens: Optional[List[ItensFatura]] = None

    def handle_montante(self):
        self.valor_bruto = self.montante
