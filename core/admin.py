from django.contrib import admin
from .models import (
    Persona,
    Direccion,
    Catequizando,
    Parroquia,
    Parroco,
    NivelCatequesis,
    CicloCatequesis,
    Grupo,
    Sacramento,
    Certificado,
    LogCertificadoEmision
)

# ----------------------------------------------------------
# PERSONA
# ----------------------------------------------------------
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'personaid', 'cedula', 'primernombre', 'primerapellido',
        'telefono', 'correo', 'genero', 'get_direccion'
    )
    search_fields = ('cedula', 'primernombre', 'primerapellido')
    list_filter = ('genero',)
    ordering = ('primerapellido', 'primernombre')

    def get_direccion(self, obj):
        return obj.direccion
    get_direccion.short_description = "Dirección"


# ----------------------------------------------------------
# DIRECCIÓN
# ----------------------------------------------------------
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('direccionid', 'calleprincipal', 'callesecundaria', 'sector')
    search_fields = ('calleprincipal', 'sector')


# ----------------------------------------------------------
# CATEQUIZANDO
# ----------------------------------------------------------
@admin.register(Catequizando)
class CatequizandoAdmin(admin.ModelAdmin):
    list_display = (
        'personaid', 'get_nombre', 'estado', 'anioencurso',
        'tiposangre', 'paisnacimiento', 'ciudadnacimiento'
    )
    search_fields = ('personaid__cedula', 'personaid__primernombre')
    list_filter = ('estado', 'tiposangre', 'anioencurso')

    def get_nombre(self, obj):
        return f"{obj.personaid.primernombre} {obj.personaid.primerapellido}"
    get_nombre.short_description = "Catequizando"


# ----------------------------------------------------------
# PARROQUIA
# ----------------------------------------------------------
@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('parroquiaid', 'nombre', 'telefono')
    search_fields = ('nombre',)


# ----------------------------------------------------------
# PARROCO
# ----------------------------------------------------------
@admin.register(Parroco)
class ParrocoAdmin(admin.ModelAdmin):
    list_display = (
        'personaid',
        'get_persona',
        'get_parroquia',
        'tipoparroco',
        'estado'
    )
    list_filter = ('estado', 'tipoparroco')
    search_fields = ('personaid',)

    def get_persona(self, obj):
        return Persona.objects.get(personaid=obj.personaid)
    get_persona.short_description = "Nombre"

    def get_parroquia(self, obj):
        return obj.parroquia.nombre
    get_parroquia.short_description = "Parroquia"


# ----------------------------------------------------------
# NIVEL CATEQUESIS
# ----------------------------------------------------------
@admin.register(NivelCatequesis)
class NivelCatequesisAdmin(admin.ModelAdmin):
    list_display = ('nivelcatequesisid', 'nombre', 'libroasignado', 'edadminima')
    search_fields = ('nombre', 'libroasignado')


# ----------------------------------------------------------
# CICLO CATEQUESIS
# ----------------------------------------------------------
@admin.register(CicloCatequesis)
class CicloCatequesisAdmin(admin.ModelAdmin):
    list_display = ('cicloid', 'nombreciclo', 'fechainicio', 'fechafin', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombreciclo',)


# ----------------------------------------------------------
# GRUPO
# ----------------------------------------------------------
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = (
        'grupoid', 'nombregrupo', 'estado',
        'get_nivelcatequesis', 'get_ciclo'
    )
    search_fields = ('nombregrupo',)
    list_filter = ('estado', 'nivelcatequesis')
    ordering = ('nivelcatequesis', 'nombregrupo')

    def get_nivelcatequesis(self, obj):
        return obj.nivelcatequesis.nombre
    get_nivelcatequesis.short_description = "Nivel"

    def get_ciclo(self, obj):
        return obj.ciclo.nombreciclo
    get_ciclo.short_description = "Ciclo"


# ----------------------------------------------------------
# SACRAMENTO
# ----------------------------------------------------------
@admin.register(Sacramento)
class SacramentoAdmin(admin.ModelAdmin):
    list_display = ('sacramentoid', 'nombre')
    search_fields = ('nombre',)


# ----------------------------------------------------------
# CERTIFICADO
# ----------------------------------------------------------
@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = (
        'certificadoid',
        'get_catequizando',
        'get_nivel',
        'get_parroco',
        'numerocertificado',
        'fechaemision'
    )
    search_fields = ('numerocertificado',)
    list_filter = ('nivelcatequesisid',)

    def get_catequizando(self, obj):
        try:
            p = Persona.objects.get(personaid=obj.catequizando_personaid)
            return f"{p.primernombre} {p.primerapellido}"
        except Persona.DoesNotExist:
            return obj.catequizando_personaid
    get_catequizando.short_description = "Catequizando"

    def get_nivel(self, obj):
        try:
            return NivelCatequesis.objects.get(nivelcatequesisid=obj.nivelcatequesisid).nombre
        except NivelCatequesis.DoesNotExist:
            return obj.nivelcatequesisid
    get_nivel.short_description = "Nivel Catequesis"

    def get_parroco(self, obj):
        try:
            par = Parroco.objects.get(personaid=obj.parroco_personaid)
            return Persona.objects.get(personaid=par.personaid)
        except:
            return obj.parroco_personaid
    get_parroco.short_description = "Parroco"


# ----------------------------------------------------------
# LOG EMISIÓN CERTIFICADO
# ----------------------------------------------------------
@admin.register(LogCertificadoEmision)
class LogCertificadoAdmin(admin.ModelAdmin):
    list_display = (
        'logid',
        'certificado',
        'get_catequizando',
        'usuarioemite',
        'fechaemision'
    )
    search_fields = ('certificado__certificadoid', 'usuarioemite')
    ordering = ('-fechaemision',)

    def get_catequizando(self, obj):
        try:
            p = Persona.objects.get(personaid=obj.catequizando_personaid)
            return f"{p.primernombre} {p.primerapellido}"
        except:
            return obj.catequizando_personaid
    get_catequizando.short_description = "Catequizando"
