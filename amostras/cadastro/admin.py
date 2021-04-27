from django.contrib import admin
from .models import Inscricao

# Register your models here.
@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['model', 'number', 'hardware', 'supplier', 'location', 'created']