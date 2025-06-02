from config.database import connect_db
from schemas.clientes_sch import clientes_schema


async def insertar_cliente(nombre, apellido, email, descripcion, curso, ano, direccion, postal, contrasena) -> dict:
    with connect_db() as conn:
        cur = conn.cursor()
        sql = """
        INSERT INTO clientes (nombre, apellido, email, descripcion, curso, ano, direccion, postal, contrasena)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (nombre, apellido, email, descripcion, curso, ano, direccion, postal, contrasena))
        conn.commit()
        return {"msg": "insertado correctamente"}


async def obtener_clientes() -> list[dict]:
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes")
        datos = cur.fetchall()
        return clientes_schema(datos)


async def actualizar_cliente(cliente_id: int, apellido: str, direccion: str) -> dict:
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE clientes SET apellido = %s, direccion = %s WHERE id = %s", (apellido, direccion, cliente_id))
        conn.commit()
        return {"msg": "actualizado correctamente"}


async def eliminar_cliente(cliente_id: int) -> dict:
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conn.commit()
        return {"msg": "eliminado correctamente"}
