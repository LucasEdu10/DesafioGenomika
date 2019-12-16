from django.contrib import admin
from DesafioGenomika.genoma.models import Genoma

class GenomaAdmin(admin.ModelAdmin):

	list_display = ['disease','gene']

admin.site.register(Genoma, GenomaAdmin)



# Register your models here.
