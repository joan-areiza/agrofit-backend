from django.contrib import admin

# Register your models here.
# Configurar el título del panel
title = "Administración de AgroFit"
subtitle = "AgroFit Admin"
description = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = subtitle
admin.site.index_title = description

#list_display Columnas visibles
#search_fields Campos con buscador
#list_filter Filtros laterales
#readonly_fields Solo lectura