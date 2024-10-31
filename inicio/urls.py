from proyecto_3.urls import path
from .views import inicio, datos, template1, template2, crear_indumentaria, buscar_indumentaria, crear_indumentarias

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name="inicio"),
    path('datos1/<nombre>/', datos),
    path('template1/', template1),
    path('template2/', template2),
    path('crear-indumentaria/<prenda>/<marca>/<talla>', crear_indumentaria),
    path('buscar_indumentaria/', buscar_indumentaria, name="buscar_indumentaria"),
    path('crear_indumentarias/', crear_indumentarias, name="crear_indumentarias"),
]

