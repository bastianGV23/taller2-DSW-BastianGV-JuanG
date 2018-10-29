from apps.rescate.views import lista_rescate,crea_rescate
from django.conf.urls import url,include
urlpatterns = [
    url(r'^ver$', lista_rescate, name='ver'),
    url(r'^crea$', crea_rescate, name='crea'),
]