import psycopg2

def conect_db():
    conn = psycopg2.connect(
        database = "examen",
        user = "luis",
        password = "luis",
        host = "localhost",
        port = "5432",
    )
    return conn
