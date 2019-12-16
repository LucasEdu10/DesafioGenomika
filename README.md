# Desafio Genomika
	- Repositório criado para o Desafio de conhecimentos do estagio de desenvolvimento

#Problema (1)

	- Todos os seres humanos compartilham aproximadamente 99,9% dos mesmos nucleotídeos
	em seu genoma e até a mesma ordem como são apresentados. Portanto, se apenas soubermos alguns
	genomas completos de uma espécie podemos ter os principais componentes para identificar o genoma
	de toda a espécie.
	Determinar o genoma completo de um organismo (chamado de sequenciamento de genoma) é uma ds
	principais tarefas em bioinformática. Infelizmente, nós não possuímos tecnologia microscópica que
	consiga realizar um zoom a nível de nucleotídeo e determinar a sequência de nucleotídeos de um
	genoma, um por vez. Entretanto, pesquisadores podem aplicar metódos bioquímicos para gerar e
	identificar pequenos fragmentos de DNA que chamamos de reads. Após obter uma grande coleção de
	reads de múltiplas cópias do mesmo genoma, o objetivo é reconstruir o genoma a partir destes pequenos
	fragmentos de DNA. Este processo é chamado de fragment assembly.

	- RESPOSTA:
		 Nesta questão me basei em um script com uma função recursiva já criado, fiz somente alguns ajustes para funcionar, aonde neste script ele faz a montagem do conteudo.

	1 - Para rodar o script `python assembly.py` ele vai gerar outro arquivo na mesma pasta com o conteudo.


#Problema (2)

	- Nosso problema 2 continua focando em algoritmos, especialmente trabalhamos com
	busca em vários sistemas para captura de dados e processamento para tomada de decisão. Queremos
	avaliar tecnicamente seu domínio de algoritmos e estrutura de dados. A Figura 1 a seuir, representa o
	grafo de dependência entre módulos de um sistema. A aresta indica a relação de dependência entre dois
	módulos indicada pelo sentido, por exemplo: 1 2, indica que o módulo 1 é uma dependência do modulo
	2 (ou o modulo 2 depende de 1), ou seja, para carregar o modulo 2 precisamos primeiro carregar o
	modulo 1. Implemente um algoritmo em Python ou Pseudocódigo (formato TXT) que retorne a ordem
	correta de carregamento de todos os módulos do sistema.

	- RESPOSTA:
		Nesta questão fiz um script aonde ele pega a relação de cada modulo e se organizar-se para fazer com que os modulos carregassem todos certos, a ideia era fazer com que a lista retornasse assim: ['0', '1', '2', '3', '4', '5', '6', '7']
	
	2 - Para rodar o script `python3 ordenar.py`

#Problema (3)

	-	O segundo problema envolve o desenvolvimento de uma aplicação web com
	HTML/CSS/JavaScript + backend usando python + banco de dados à sua escolha.
	O aplicativo é uma ferramenta on-line de sugestão de genes a serem analisados dado uma ou mais
	doenças/sintomas clínicos de um paciente. Graças ao advento das tecnologias de sequenciamento de
	nova geração, hoje é possível sequenciar múltiplos genes simultaneamente com boa qualidade para
	diversos fins como pesquisas de novas doenças genéticas e fins clínicos, como detecção de doenças
	raras e tumores a partir de variantes genéticas encontradas na regiões do DNA humanos.

	- RESPOSTA:
		Nesta questão foram usadas as seguintes ferramentas: 
			framework django
			docker

	3 - Para rodar o projeto:
		`docker-compose up` 
		3.1 - Para rodar o script de atualização do banco:
			`python3 update_banco.py`, neste caso precisamos instalar a biblioteca psycopg2, para baixar ela rode o comando: `pip3 install psycopg2`

