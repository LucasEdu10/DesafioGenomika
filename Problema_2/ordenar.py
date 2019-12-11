from collections import defaultdict

#def ordenar():

V = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']

#D = [('v0','v03'), ('v1','v2'), ('v3','v5'), ('v5','v6'), ('v5','v7'), ('v6', 'v7'), ('v4','v6'), ('v2', 'v6')]


grafo = {'v0' : ['v3'],
		 'v1' : ['v2'],
		 'v2' : ['v6'],
		 'v3' : ['v0'],
		 'v4' : ['v6'],
		 'v5' : ['v6', 'v7'],
		 'v6' : ['v7'],
		 'v7' : [],
		 }

modulo_1 = ('v0','v3')
modulo_2 = ('v1','v2')
modulo_3 = ('v3','v5')
modulo_4 = ('v5','v6')
modulo_5 = ('v5','v7')
modulo_6 = ('v6','v7')
modulo_7 = ('v4','v6')
modulo_8 = ('v2','v6')

'''print(min(V))
print(max(V))
print(V)'''

'''def pega_todos_da_lista():

	V = pega_todos_da_lista()

	for conteudo in V:
		print(conteudo)

iguais = modulo_1 in modulo_3

print(iguais)'''
def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

print(grafo.get_arestas())

def caminho_certo():

	for i in grafo:
		#print(V)
		if grafo and modulo_1:
			#print("Há coisas iguais")
			print(grafo)

print(caminho_certo())

'''if modulo_1 and modulo_3:
	print("Tem objetos iguais")

else:
	print("Não tem objetos iguais")'''


#return ordenar
