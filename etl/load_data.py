# import psycopg2
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


from config.database import database_info


# def load():

#     conn = psycopg2.connect(
#         # aqui colocaremos as variaveis de ambiente
#     )


#     conn.close()


# load()

if __name__ == "__main__":
    # Seu código principal
    print(database_info)
