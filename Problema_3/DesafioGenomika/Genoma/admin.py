from django.contrib import admin
from DesafioGenomika.Genoma.models import Genoma


admin.site.site_header = 'Genoma'

class GenomaAdmin(admin.ModelAdmin):

	list_display = ['name','gene']
	change_list_template = 'admin/Genoma/change_list.html'
	#change_list_template = 'admin/Genoma/imagen.html'

	def import_gene(self, request):
		if import_gene in request.POST:
			print('BOTAO FUNCIONANDO')
		else:
			print('FAAAAIL')



admin.site.register(Genoma, GenomaAdmin)	

# Register your models here.
