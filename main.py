from db.proyecto_db import Proyecto
from db.proyecto_db import obtener_proyectos, obtener_proyectos_by_Id, crear_proyecto, eliminar_proyecto

from models.proyecto_models import ProyectoIn, ProyectoOut
from models.empresa_models import EmpresaIn, EmpresaOut

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api =FastAPI()

origins = ["http://localhost.tiangolo.com",
           "https://localhost.tiangolo.com",
           "http://localhost", "http://localhost:8080",]
api.add_middleware(CORSMiddleware, allow_origins=origins,
                    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

@api.get("/")
async def root():
    return{"mensaje" : "Bienvenido a Proyectia"}

@api.get("/proyectos/listado")
async def main_obtener_proyectos(empresain: EmpresaIn):
    NombreEmpresa = empresain.nombre_empresa
    Lista = obtener_proyectos(NombreEmpresa)
    if len(Lista) == 0: 
            raise HTTPException(status_code=404, detail="No existen proyectos de "+ NombreEmpresa.replace('_', ' ', 30))   
    else:
        return Lista

@api.get("/proyectos/consultar/{NombreEmpresa}")
async def main_obtener_proyectos_by_Id(NombreEmpresa, proyectoin: ProyectoIn):
    NombreProyecto = proyectoin.nombre_proyecto
    Proyecto = obtener_proyectos_by_Id(NombreEmpresa, NombreProyecto)
    if Proyecto == False:
        raise HTTPException(status_code=404, detail="La empresa " + NombreEmpresa.replace('_', ' ', 30) +
                                                     " no tiene un proyecto con nombre " + NombreProyecto.replace('_', ' ', 30))   
    else:
        return Proyecto

@api.post("/proyectos/crear/{NombreEmpresa}")
async def main_crear_proyecto(NombreEmpresa: str, NombreProyecto: str, proyecto: Proyecto):
    bandera = crear_proyecto(NombreEmpresa, NombreProyecto, proyecto)
    if bandera:
        return {"mensaje": "El proyecto "+NombreProyecto.replace('_', ' ', 30)+" fue creado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Ya existe el proyecto "+NombreProyecto.replace('_', ' ', 30))

@api.delete("/proyectos/borrar")
async def main_eliminar_proyecto(proyectoin: ProyectoIn):
    NombreEmpresa = proyectoin.nombre_empresa
    NombreProyecto = proyectoin.nombre_proyecto
    bandera = eliminar_proyecto(NombreEmpresa, NombreProyecto)
    if bandera:
        return {"mensaje": "El proyecto "+NombreProyecto.replace('_', ' ', 30)+" fue eliminado correctamente."}
    else:
        raise HTTPException(status_code=404, detail="La empresa " + NombreEmpresa.replace('_', ' ', 30) +
                                                     " no tiene un proyecto con nombre " + NombreProyecto.replace('_', ' ', 30))
        
        
    