from django.db import models

class Direccion(models.Model):
    direccionid = models.IntegerField(db_column='DireccionID', primary_key=True)
    calleprincipal = models.CharField(db_column='CallePrincipal', max_length=50)
    callesecundaria = models.CharField(db_column='CalleSecundaria', max_length=50)
    sector = models.CharField(db_column='Sector', max_length=50)

    class Meta:
        managed = False
        db_table = 'Persona.Direccion'

    def __str__(self):
        return f"{self.calleprincipal} y {self.callesecundaria}"

class Persona(models.Model):
    personaid = models.IntegerField(db_column='PersonaID', primary_key=True)
    cedula = models.CharField(db_column='Cedula', max_length=10, unique=True)
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50)
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=50, null=True, blank=True)
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50)
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50)
    fechanacimiento = models.DateField(db_column='FechaNacimiento')
    genero = models.CharField(db_column='Genero', max_length=1)
    telefono = models.CharField(db_column='Telefono', max_length=10, null=True, blank=True)
    correo = models.CharField(db_column='Correo', max_length=50, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.DO_NOTHING, db_column='DireccionID')

    class Meta:
        managed = False
        db_table = 'Persona.Persona'

    def __str__(self):
        return f"{self.primernombre} {self.primerapellido}"

class Parroquia(models.Model):
    parroquiaid = models.IntegerField(db_column='ParroquiaID', primary_key=True)
    direccionid = models.IntegerField(db_column='DireccionID')
    nombre = models.CharField(db_column='Nombre', max_length=50)
    telefono = models.CharField(db_column='Telefono', max_length=10)

    class Meta:
        managed = False
        db_table = 'Informacion.Parroquia'

    def __str__(self):
        return str(self.nombre)

class Parroco(models.Model):
    personaid = models.IntegerField(db_column='PersonaID', primary_key=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.DO_NOTHING, db_column='ParroquiaID')
    tipoparroco = models.CharField(db_column='TipoParroco', max_length=50)
    estado = models.CharField(db_column='Estado', max_length=10)

    class Meta:
        managed = False
        db_table = 'Informacion.Parroco'

    def __str__(self):
        return f"Parroco {self.personaid}"

class Catequizando(models.Model):
    personaid = models.OneToOneField(Persona, on_delete=models.DO_NOTHING, db_column='PersonaID', primary_key=True)
    parroquiaid = models.IntegerField(db_column='ParroquiaID')
    paisnacimiento = models.CharField(db_column='PaisNacimiento', max_length=25)
    ciudadnacimiento = models.CharField(db_column='CiudadNacimiento', max_length=50)
    numerohijo = models.IntegerField(db_column='NumeroHijo')
    numerohermanos = models.IntegerField(db_column='NumeroHermanos')
    estado = models.CharField(db_column='Estado', max_length=10)
    anioencurso = models.CharField(db_column='AnioEnCurso', max_length=20, null=True, blank=True)
    tiposangre = models.CharField(db_column='TipoSangre', max_length=3)
    alergia = models.CharField(db_column='Alergia', max_length=50, null=True, blank=True)
    comentario = models.CharField(db_column='Comentario', max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Participante.Catequizando'

    def __str__(self):
        return str(self.personaid)

class NivelCatequesis(models.Model):
    nivelcatequesisid = models.IntegerField(db_column='NivelCatequesisID', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50)
    descripcion = models.CharField(db_column='Descripcion', max_length=200, null=True, blank=True)
    libroasignado = models.CharField(db_column='LibroAsignado', max_length=50)
    edadminima = models.IntegerField(db_column='EdadMinima')
    sacramentoid = models.IntegerField(db_column='SacramentoID', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Catequesis.NivelCatequesis'

    def __str__(self):
        return str(self.nombre)

class CicloCatequesis(models.Model):
    cicloid = models.IntegerField(db_column='CicloID', primary_key=True)
    nombreciclo = models.CharField(db_column='NombreCiclo', max_length=100)
    fechainicio = models.DateField(db_column='FechaInicio')
    fechafin = models.DateField(db_column='FechaFin')
    estado = models.CharField(db_column='Estado', max_length=10)

    class Meta:
        managed = False
        db_table = 'Catequesis.CicloCatequesis'

    def __str__(self):
        return str(self.nombreciclo)

class Grupo(models.Model):
    grupoid = models.IntegerField(db_column='GrupoID', primary_key=True)
    nivelcatequesis = models.ForeignKey(NivelCatequesis, on_delete=models.DO_NOTHING, db_column='NivelCatequesisID')
    ciclo = models.ForeignKey(CicloCatequesis, on_delete=models.DO_NOTHING, db_column='CicloID')
    nombregrupo = models.CharField(db_column='NombreGrupo', max_length=50)
    estado = models.CharField(db_column='Estado', max_length=10)

    class Meta:
        managed = False
        db_table = 'Catequesis.Grupo'

    def __str__(self):
        return str(self.nombregrupo)

class Sacramento(models.Model):
    sacramentoid = models.IntegerField(db_column='SacramentoID', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=25)

    class Meta:
        managed = False
        db_table = 'Sacramento.Sacramento'

    def __str__(self):
        return str(self.nombre)

class Certificado(models.Model):
    certificadoid = models.IntegerField(db_column='CertificadoID', primary_key=True)
    catequizando_personaid = models.IntegerField(db_column='Catequizando_PersonaID')
    nivelcatequesisid = models.IntegerField(db_column='NivelCatequesisID')
    parroco_personaid = models.IntegerField(db_column='Parroco_PersonaID')
    numerocertificado = models.CharField(db_column='NumeroCertificado', unique=True, max_length=12)
    fechaemision = models.DateField(db_column='FechaEmision')

    class Meta:
        managed = False
        db_table = 'Sacramento.Certificado'

    def __str__(self):
        return f"Certificado {self.certificadoid}"

class LogCertificadoEmision(models.Model):
    logid = models.IntegerField(db_column='LogID', primary_key=True)
    certificado = models.ForeignKey(
        Certificado,
        on_delete=models.DO_NOTHING,
        db_column='CertificadoID'
    )
    catequizando_personaid = models.IntegerField(db_column='Catequizando_PersonaID')
    fechaemision = models.DateTimeField(db_column='FechaEmision')
    usuarioemite = models.CharField(db_column='UsuarioEmite', max_length=128, null=True, blank=True)
    observacion = models.CharField(db_column='Observacion', max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Sacramento.LogCertificadoEmision'

    def __str__(self):
        return f"Log {self.logid}"



class Representante(models.Model):
    personaid = models.OneToOneField(Persona, on_delete=models.DO_NOTHING, db_column='PersonaID', primary_key=True)
    relacion = models.CharField(db_column='Relacion', max_length=25)
    ocupacion = models.CharField(db_column='Ocupacion', max_length=50)

    class Meta:
        managed = False
        db_table = 'Participante.Representante'

    def __str__(self):
        return str(self.personaid)


class Padrino(models.Model):
    personaid = models.OneToOneField(Persona, on_delete=models.DO_NOTHING, db_column='PersonaID', primary_key=True)
    sacramentoid = models.ForeignKey(Sacramento, on_delete=models.DO_NOTHING, db_column='SacramentoID')

    class Meta:
        managed = False
        db_table = 'Participante.Padrino'

    def __str__(self):
        return str(self.personaid)


class CatequizandoRepresentante(models.Model):
    # Composite PK (Representante_PersonaID, Catequizando_PersonaID)
    representante_personaid = models.OneToOneField(Representante, on_delete=models.DO_NOTHING, db_column='Representante_PersonaID', primary_key=True)
    catequizando_personaid = models.ForeignKey(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID')

    class Meta:
        managed = False
        db_table = 'Participante.CatequizandoRepresentante'
        unique_together = (('representante_personaid', 'catequizando_personaid'),)


class CatequizandoPadrino(models.Model):
    # Composite PK (Padrino_PersonaID, Catequizando_PersonaID)
    padrino_personaid = models.OneToOneField(Padrino, on_delete=models.DO_NOTHING, db_column='Padrino_PersonaID', primary_key=True)
    catequizando_personaid = models.ForeignKey(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID')

    class Meta:
        managed = False
        db_table = 'Participante.CatequizandoPadrino'
        unique_together = (('padrino_personaid', 'catequizando_personaid'),)


class FeBautismo(models.Model):
    febautismoid = models.IntegerField(db_column='FeBautismoID', primary_key=True)
    catequizando_personaid = models.ForeignKey(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID')
    parroquia_parroquiaid = models.ForeignKey(Parroquia, on_delete=models.DO_NOTHING, db_column='Parroquia_ParroquiaID')
    fechabautismo = models.DateField(db_column='FechaBautismo')
    numerotomo = models.IntegerField(db_column='NumeroTomo', null=True, blank=True)
    paginatomo = models.IntegerField(db_column='PaginaTomo', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Participante.FeBautismo'
    
    def __str__(self):
        return f"Fe Bautismo {self.febautismoid}"


class Sesion(models.Model):
    sesionid = models.IntegerField(db_column='SesionID', primary_key=True)
    fecha = models.DateTimeField(db_column='Fecha')
    grupoid = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING, db_column='GrupoID')

    class Meta:
        managed = False
        db_table = 'Catequesis.Sesion'

    def __str__(self):
        return f"Sesion {self.sesionid}"


class Catequista(models.Model):
    personaid = models.OneToOneField(Persona, on_delete=models.DO_NOTHING, db_column='PersonaID', primary_key=True)
    tipocatequista = models.CharField(db_column='TipoCatequista', max_length=20)
    estado = models.CharField(db_column='Estado', max_length=10)

    class Meta:
        managed = False
        db_table = 'Catequesis.Catequista'
    
    def __str__(self):
        return str(self.personaid)


class CatequistaGrupo(models.Model):
    # Composite PK (GrupoID, Catequista_PersonaID)
    grupoid = models.OneToOneField(Grupo, on_delete=models.DO_NOTHING, db_column='GrupoID', primary_key=True)
    catequista_personaid = models.ForeignKey(Catequista, on_delete=models.DO_NOTHING, db_column='Catequista_PersonaID')

    class Meta:
        managed = False
        db_table = 'Catequesis.CatequistaGrupo'
        unique_together = (('grupoid', 'catequista_personaid'),)


class Asistencia(models.Model):
    # Composite PK (Catequizando_PersonaID, SesionID)
    catequizando_personaid = models.OneToOneField(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID', primary_key=True)
    sesionid = models.ForeignKey(Sesion, on_delete=models.DO_NOTHING, db_column='SesionID')
    estapresente = models.BooleanField(db_column='EstaPresente')

    class Meta:
        managed = False
        db_table = 'Catequesis.Asistencia'
        unique_together = (('catequizando_personaid', 'sesionid'),)


class Calificacion(models.Model):
    calificacionid = models.IntegerField(db_column='CalificacionID', primary_key=True)
    catequizando_personaid = models.ForeignKey(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID')
    tipocalificacion = models.CharField(db_column='TipoCalificacion', max_length=10)
    grupoid = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING, db_column='GrupoID')
    valor = models.DecimalField(db_column='Valor', max_digits=4, decimal_places=2)
    fecha = models.DateTimeField(db_column='Fecha')

    class Meta:
        managed = False
        db_table = 'Catequesis.Calificacion'

    def __str__(self):
        return f"Calificacion {self.calificacionid}"


class Inscripcion(models.Model):
    # Clave compuesta logicamente (Catequizando + Grupo).
    # Usamos CatequizandoID como PK para Django, pero cambiamos a ForeignKey para evitar restriccion unique de OneToOne.
    # Atencion: No usar save()/delete() ORM, solo lectura o SPs.
    
    catequizando_personaid = models.ForeignKey(Catequizando, on_delete=models.DO_NOTHING, db_column='Catequizando_PersonaID', primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING, db_column='GrupoID')
    fechainscripcion = models.DateTimeField(db_column='FechaInscripcion')
    estadoinscripcion = models.CharField(db_column='EstadoInscripcion', max_length=10)
    estadopago = models.CharField(db_column='EstadoPago', max_length=10)
    esexcepcion = models.BooleanField(db_column='EsExcepcion')

    class Meta:
        managed = False
        db_table = 'Participante.Inscripcion'
        unique_together = (('catequizando_personaid', 'grupo'),)

    def __str__(self):
        return f"{self.catequizando_personaid} - {self.grupo}"
