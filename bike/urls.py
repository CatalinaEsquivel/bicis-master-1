from django.urls import path
from .views import index, iniciosesion, registro, bicicletas, home, form_bicicleta
urlpatterns = [
    path('', index, name='admin-index'),
    path('bicicletas/', bicicletas, name='bicicletas'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('registro/', registro, name='registro'),
]

urlpatterns = [
    path('',home,name='home'),
    path('form-bicicleta',form_bicicleta,name="form_bicicleta")
]