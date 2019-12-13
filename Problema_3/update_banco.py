# Script baseado na documentação do psycopg2 
# Link da documentação base: https://www.devmedia.com.br/como-criar-uma-conexao-em-postgresql-com-python/34079

import psycopg2

try:
    print("Conectando ao banco...")
    pg_conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            host="localhost",
            port="5440")
    print("Sucesso ao conectar")
except:
    sys.exit("Conexão não realizada!")


pg_cursor = pg_conn.cursor()

print("Coletando informações...")
pg_cursor.execute("SELECT * FROM auth_user")
rows = pg_cursor.fetchall()
print("Dados coletados!!")

print(rows)