from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuario/", include("usuario.urls")),
    path("produto/", include("produto.urls")),
    path("ingrediente/", include("ingrediente.urls")),
]
