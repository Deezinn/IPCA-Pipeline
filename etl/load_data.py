import psycopg2
from config.database import database_info
from etl.transforms.ipca_transform import transform

class load(transform):
    def __init__(self, dataframes=None):
        super().__init__()
        self.dataframes = dataframes

    def insert_data(self):
     conn = psycopg2.connect(host=database_info['host'],
                             port=database_info['port'],
                             user=database_info['user'],
                             password=database_info['password'],
                             dbname=database_info['dbname'],)
     for datasets in self.dataframes:
        print(datasets)

    #  print('conectou')

    #  cur = conn.cursor()


    #  cur.close()
    #  conn.close()
    #  print('desconectou do banco')

