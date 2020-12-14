from fastapi import FastAPI, HTTPException
import db

app =FastAPI()

@app.get("/proyectos/listado/{NombreEmpresa}")
async def obtener_proyectos(NombreEmpresa: str):
    Lista = db.obtener_proyectos(NombreEmpresa)
    if len(Lista) == 0:
            raise HTTPException(status_code=400, detail="No existen proyectos de "+ NombreEmpresa.replace('_', ' ', 30))   
    else:
        return Lista

@app.get("/proyectos/consultar/{NombreEmpresa}")
async def obtener_proyectos_by_Id(NombreEmpresa: str, NombreProyecto: str):
    Proyecto = db.obtener_proyectos_by_Id(NombreEmpresa, NombreProyecto)
    if len(Proyecto) == 0:
        raise HTTPException(status_code=400, detail="La empresa " + NombreEmpresa.replace('_', ' ', 30) +
                                                     " no tiene un proyecto con nombre " + NombreProyecto.replace('_', ' ', 30))   
    else:
        return Proyecto

@app.post("/proyectos/crear/{NombreEmpresa}")
async def crear_proyecto(NombreEmpresa: str, NombreProyecto: str, proyecto: db.Proyecto):
    bandera = db.crear_proyecto(NombreEmpresa, NombreProyecto, proyecto)
    if bandera:
        return {"mensaje": "El proyecto "+NombreProyecto.replace('_', ' ', 30)+" fue creado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="Ya existe el proyecto "+NombreProyecto.replace('_', ' ', 30))

@app.delete("/proyectos/borrar/{NombreEmpresa}")
async def eliminar_proyecto(NombreEmpresa: str, NombreProyecto: str):
    bandera = db.eliminar_proyecto(NombreEmpresa, NombreProyecto)
    if bandera:
        return {"mensaje": "El proyecto "+NombreProyecto.replace('_', ' ', 30)+" fue eliminado correctamente."}
    else:
        raise HTTPException(status_code=400, detail="La empresa " + NombreEmpresa.replace('_', ' ', 30) +
                                                     " no tiene un proyecto con nombre " + NombreProyecto.replace('_', ' ', 30))
        
        
    