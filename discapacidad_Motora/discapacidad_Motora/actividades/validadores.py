from django.core.validators import FileExtensionValidator, RegexValidator

documentos_validador = FileExtensionValidator(
    allowed_extensions=['pdf'],
    message="Sólo se permiten Documentos PDF"
)

imagen_validador = FileExtensionValidator(
    allowed_extensions=['png','jpg'],
    message="Sólo se permiten imágenes PNG"
)