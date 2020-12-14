from pydantic import BaseModel
 
class EmpresaIn(BaseModel):
    nombre_empresa: str

class EmpresaOut(BaseModel):
    nombre_empresa: str

    

