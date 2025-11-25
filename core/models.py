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
