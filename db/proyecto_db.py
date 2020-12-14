from pydantic import BaseModel

class Proyecto(BaseModel):
    descripcion_proyecto: str
    fases_proyecto: int
    presupuesto_plan: int
    fecha_inicio_plan: str
    fecha_final_plan: str
    no_personal_requerido: int

proyectos = {
    ("Empresa 1","Proyecto 1.1"): Proyecto( 
                                            descripcion_proyecto = "Proyecto 1 de la empresa 1",
                                            fases_proyecto = 1,
                                            presupuesto_plan = "1000",
                                            fecha_inicio_plan = "01/01/2001",
                                            fecha_final_plan = "10/01/2000",
                                            no_personal_requerido = 1),
    ("Empresa 2","Proyecto 2.1"): Proyecto(
                                            descripcion_proyecto = "Proyecto 1 de la empresa 2",
                                            fases_proyecto = 2,
                                            presupuesto_plan = "2000",
                                            fecha_inicio_plan = "02/01/2000",
                                            fecha_final_plan = "01/02/2000",
                                            no_personal_requerido = 2),
    ("Empresa 1","Proyecto 1.2"): Proyecto(
                                            descripcion_proyecto = "Proyecto 2 de la empresa 1",
                                            fases_proyecto = 3,
                                            presupuesto_plan = "1000",
                                            fecha_inicio_plan = "01/01/2000",
                                            fecha_final_plan = "01/02/2000",
                                            no_personal_requerido = 2),
    ("Empresa 2","Proyecto 2.2"): Proyecto(   
                                            descripcion_proyecto = "Proyecto 2 de la empresa 2",
                                            fases_proyecto = 3,
                                            presupuesto_plan = "1000",
                                            fecha_inicio_plan = "01/01/2000",
                                            fecha_final_plan = "01/02/2000",
                                            no_personal_requerido = 2),
    ("Empresa 1","Proyecto 1.3"): Proyecto(
                                            descripcion_proyecto = "Proyecto 3 de la empresa 1",
                                            fases_proyecto = 3,
                                            presupuesto_plan = "1000",
                                            fecha_inicio_plan = "01/01/2000",
                                            fecha_final_plan = "01/02/2000",
                                            no_personal_requerido = 2),
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

        
