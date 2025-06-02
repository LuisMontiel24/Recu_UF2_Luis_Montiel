def cliente_schema(cliente):
    return {
        "id": cliente[0],
        "nombre": cliente[1],
        "apellido": cliente[2],
        "email": cliente[3],
        "curso": cliente[5],
        "ano": cliente[6],
        "direccion": cliente[7]
    }

def clientes_schema(lista_clientes):
    return [cliente_schema(client) for client in lista_clientes]
