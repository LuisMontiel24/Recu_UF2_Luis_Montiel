from fastapi import FastAPI, Request
from services.clientes import insertar_cliente, obtener_clientes, actualizar_cliente, eliminar_cliente

app = FastAPI()

@app.post("/crear_cliente")
async def crear(request: Request) -> dict:
    datos = await request.json()
    return await insertar_cliente(
        datos["nombre"],
        datos["apellido"],
        datos["email"],
        datos["descripcion"],
        datos["curso"],
        datos["ano"],
        datos["direccion"],
        datos["postal"],
        datos["contrasena"]
    )

@app.get("/clientes")
async def listar() -> list[dict]:
    return await obtener_clientes()

@app.put("/actualizar_cliente/{cliente_id}")
async def actualizar(cliente_id: int, request: Request) -> dict:
    datos = await request.json()
    return await actualizar_cliente(cliente_id, datos["apellido"], datos["direccion"])

@app.delete("/eliminar_cliente/{cliente_id}")
async def eliminar(cliente_id: int) -> dict:
    return await eliminar_cliente(cliente_id)
