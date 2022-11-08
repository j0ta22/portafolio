from django.urls import path
from .views import contacto
from django.conf.urls.static import static
app_name = 'contacto'

urlpatterns = [
    path('', contacto, name='contacto'),    
]