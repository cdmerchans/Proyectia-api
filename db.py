from pydantic import BaseModel

class Proyecto(BaseModel):
    presupuesto_plan: str
    tiempo_plan_horas: int 

proyectos = {
    ("Empresa 1","Proyecto 1.1"): Proyecto(
                                            presupuesto_plan="1000",
                                            tiempo_plan_horas="11"),
    ("Empresa 2","Proyecto 2.1"): Proyecto(
                                            presupuesto_plan="2000",
                                             tiempo_plan_horas="22"),
    ("Empresa 1","Proyecto 1.2"): Proyecto(
                                            presupuesto_plan="3000",
                                             tiempo_plan_horas="33"),
    ("Empresa 2","Proyecto 2.2"): Proyecto(
                                            presupuesto_plan="4000",
                                             tiempo_plan_horas="44"),
    ("Empresa 1","Proyecto 1.3"): Proyecto(
                                            presupuesto_plan="5000",
                                             tiempo_plan_horas="55")
}

def obtener_proyectos(NombreEmpresa: str):
    NombreEmpresa = NombreEmpresa.replace('_', ' ', 30)
    lista_proyectos = []
    for key in proyectos:
        if key[0] == NombreEmpresa:
            lista_proyectos.append({key[1]:proyectos[key]})
    return lista_proyectos

def obtener_proyectos_by_Id(NombreEmpresa: str, NombreProyecto: str):
    NombreEmpresa = NombreEmpresa.replace('_', ' ', 30)
    NombreProyectoKey = NombreProyecto.replace('_', ' ', 30)
    key = (NombreEmpresa, NombreProyectoKey)
    if key in proyectos:
        proyecto = {key[1]:proyectos[key]}
    else:
        proyecto = []
    return proyecto

def crear_proyecto(NombreEmpresa: str, NombreProyecto: str, proyecto: Proyecto):
    NombreEmpresa = NombreEmpresa.replace('_', ' ', 30)
    NombreProyecto = NombreProyecto.replace('_', ' ', 30)
    key = (NombreEmpresa, NombreProyecto)
    if key in proyectos:
        return False
    else:
        proyectos[NombreEmpresa, NombreProyecto] = proyecto
        return True

def eliminar_proyecto(NombreEmpresa: str, NombreProyecto: str):
    NombreEmpresa = NombreEmpresa.replace('_', ' ', 30)
    NombreProyecto = NombreProyecto.replace('_', ' ', 30)
    key = (NombreEmpresa, NombreProyecto)
    if key in proyectos:
        del proyectos[key]
        return True
    else:
        return False
