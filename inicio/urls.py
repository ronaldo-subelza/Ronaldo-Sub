from proyecto_3.urls import path
from .views import inicio, datos, template1, template2


urlpatterns = [
    path('', inicio),
    path('datos1/<nombre>/', datos),
    path('template1/', template1),
    path('template2/', template2),
]
