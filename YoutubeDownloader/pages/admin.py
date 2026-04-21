from django.contrib import admin
from .models import Historico


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
	list_display = ('title', 'format', 'created_at')
	search_fields = ('title', 'url')
	list_filter = ('format',)
