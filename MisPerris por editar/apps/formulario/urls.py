from django.conf.urls import url,include
from apps.formulario.views import lista_Contacto,formulario_view
urlpatterns = [
    url(r'^ver$', lista_Contacto, name='verC'),
    url(r'^crea$', formulario_view, name='creaC'),
]