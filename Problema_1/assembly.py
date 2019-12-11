
#arquivo = open('/home/lucas/Projetos/DesafioGenomika/SelecaoEstagio2019/SelecaoEstagio2019/Problema1/output.txt', 'r')
#print(arquivo.readlines())

def long(reads, genoma=''):
	if len(reads) == 0:
		return genoma
	if len(genoma) == 0:
		genoma = reads.pop(0)
		return long(reads, genoma)

	for i in range(len(reads)):
		a = reads[i]
		l = len(a)
		for p in range(l / 2):
			q = l - p
			if genoma.startswith(a[p:]):
				reads.pop(i)
				return long(reads, a[:p] + genoma)
			if genoma.endswith(a[:q]):
				reads.pop(i)
				return long(reads, genoma + a[q:])

if __name__ == "__main__":
 
	#arquivo = open("/home/augusto/Downloads/rosalind_long.txt")
	arquivo = open('/home/lucas/Projetos/DesafioGenomika/SelecaoEstagio2019/SelecaoEstagio2019/Problema1/output.txt', 'r')
	sequencia=[]
	i=-1
	for linha in arquivo:
		if linha.find('>') != -1:		
			i+=1
			sequencia.append('')
		else:		
			sequencia[i]=sequencia[i]+linha.rstrip()
	print long(sequencia)
