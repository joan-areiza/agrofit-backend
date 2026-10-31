from django.contrib import admin
from .models import EstadosContacto, MensajesContacto


class EstadosContactoAdmin(admin.ModelAdmin):
    list_display = ("id_estado_contacto_pk", "nombre_estado")
    search_fields = ("nombre_estado",)
class MensajesContactoAdmin(admin.ModelAdmin):
    list_display = (
        "id_mensaje_pk",
        "nombres_remitente",
        "correo_remitente",
        "titulo_mensaje",
        "fecha_envio",
        "id_estado_contacto_fk",
    )
    list_filter = ("id_estado_contacto_fk", "fecha_envio")
    search_fields = ("nombres_remitente", "correo_remitente", "titulo_mensaje", "contenido_mensaje")
    date_hierarchy = "fecha_envio"
    readonly_fields = ("fecha_envio",)

admin.site.register(EstadosContacto,EstadosContactoAdmin)
admin.site.register(MensajesContacto,MensajesContactoAdmin)

