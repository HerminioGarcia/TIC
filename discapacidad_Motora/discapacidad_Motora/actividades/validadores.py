from django.core.validators import FileExtensionValidator, RegexValidator

documentos_validador = FileExtensionValidator(
    allowed_extensions=['pdf'],
    message="Sólo se permiten Documentos PDF"
)