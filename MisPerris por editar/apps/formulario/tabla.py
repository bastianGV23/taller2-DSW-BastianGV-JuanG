import django_tables2 as tables
from .models import Contacto

class tablaContacto(tables.Table):
    class Meta:
     model = Contacto
     template_name = 'django_tables2/bootstrap-responsive.html'