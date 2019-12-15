# Script baseado na documentação do psycopg2 
# Link da documentação base: https://www.devmedia.com.br/como-criar-uma-conexao-em-postgresql-com-python/34079

import psycopg2

try:
    print("Conectando ao banco da Genomika...")
    banco_genomika = psycopg2.connect(
    	database="d5mma0lt0jpjfj",
    	user="ekvytxmooqboqc",
    	password="638c124d07e29a9bdf595724d3293a39b2b84f9c2b3f8fe6878e7975fca6efeb",
    	host="ec2-107-21-122-38.compute-1.amazonaws.com",
    	port="5432")
    print("Sucesso ao conectar")
except:
    print("Conexão não realizada!")

try:
	print('conectando ao banco local')
	my_banco = psycopg2.connect(
		database="postgres",
		user="postgres",
		password="",
		host="localhost",
		port="5440")
	print("sucesso ao conectar")
except:
	print("Não conectou!")


pg_cursor = banco_genomika.cursor()
sqlite_cursor = my_banco.cursor()

print("Coletando informações...")
pg_cursor.execute("SELECT * FROM pheno_db")
rows = pg_cursor.fetchall()
print("Dados coletados!!")
#print(rows)

print("Atualizando o Banco Local...")
for row in rows:
	id = row[0]
	gene = row[1]
	disease = row[2]
	
	sqlite_cursor.execute("INSERT INTO genoma_genoma (id, gene, disease) VALUES (%s, %s, %s)", (id, gene, disease))
	
	my_banco.commit()
print("Local database updated!")

banco_genomika.close()
my_banco.close()
