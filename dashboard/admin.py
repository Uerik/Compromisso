from django.contrib import admin
from .models import Compromisso
# Register your models here.

class CompromissoADM(admin.ModelAdmin):
    list_display = ('oque', 'onde', 'dia', 'comQuem', 'obs')

admin.site.register(Compromisso, CompromissoADM)