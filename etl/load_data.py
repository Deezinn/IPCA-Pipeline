import psycopg2
from config.database import database_info

class load:
    def __init__(self):
        pass

    conn = psycopg2.connect(host=database_info['host'],
                            port=database_info['port'],
                            user=database_info['user'],
                            password=database_info['password'],
                            dbname=database_info['dbname'],)
    print('conectou')

    cur = conn.cursor()

    # aqui ficará o insert dos dados tratados em csv

    cur.close()
    conn.close()
    print('desconectou do banco')

