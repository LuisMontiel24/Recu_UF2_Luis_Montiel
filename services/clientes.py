from config.database import connect_db


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



