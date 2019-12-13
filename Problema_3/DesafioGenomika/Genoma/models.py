from django.db import models


class Genoma(models.Model):

	name = models.CharField('Nome da Doença', max_length=50)
	gene = models.CharField('Genes da doença', max_length=100)
	

	class Meta:
		verbose_name = 'Doença'
		verbose_name_plural = 'Doenças'