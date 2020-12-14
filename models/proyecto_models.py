from pydantic import BaseModel
 
class ProyectoIn(BaseModel):
    nombre_empresa: str
    nombre_proyecto: str

class ProyectoOut(BaseModel):
    descripcion_proyecto: str
    fases_proyecto: int
    presupuesto_plan: int
    fecha_inicio_plan: str
    fecha_final_plan: str
    no_personal_requerido: int
    
