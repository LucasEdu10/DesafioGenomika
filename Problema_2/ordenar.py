
# Primeiro, vamos transferir o dado na imagem da Figura 1 (Grafo de dependência entre módulos)
# em, de fato, um grafo de dependência entre módulos. Nesse grafo, cada nó representará
# um módulo, e cada relação representará as dependências do módulo correspondente.

modulos = {
    '0': [],
    '1': [],
    '2': ['1'],
    '3': ['0'],
    '4': [],
    '5': ['3'],
    '6': ['2', '4', '5'],
    '7': ['5', '6'],
}

# Para fazer o carregamento dos módulos na ordem correta, devemos carregar primeiro
# os módulos sem dependências e, uma vez que esses sejam carregados, carregar os
# módulos dependentes desses primeiros, e assim seguir recursivamente até que todos
# os módulos sejam carregados.

# Como esse relacionamento de dependência está descrito como um grafo, podemos implementar
# esse requisito percorrendo esse grafo como se estivéssemos fazendo uma busca em profundidade
# no mesmo.

def carregar(modulos):

    def carregar_recursivo(modulos, modulo):
        modulos_carregados.append(modulo)
        for modulo_dependente in modulos[modulo]:
            if modulo_dependente not in modulos_carregados:
                carregar_recursivo(modulos, modulo_dependente)

    modulos_carregados = []
    for modulo in modulos:
        if modulo not in modulos_carregados:
            carregar_recursivo(modulos, modulo)
    return modulos_carregados


modulos_carregados = carregar(modulos)
print(modulos_carregados)