import psycopg2

def load():

    conn = psycopg2.connect(
        # aqui colocaremos as variaveis de ambiente
    )


    conn.close()


load()
