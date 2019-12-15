from django.db import models

class Genoma(models.Model):

	disease = models.CharField('Nome da Doença', max_length=200, null=True)
	gene = models.CharField('Genes da doença', max_length=200, null=True)
	

	class Meta:
		verbose_name = 'Doença'
		verbose_name_plural = 'Doenças'


# Create your models here.
