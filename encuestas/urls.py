"""
URL configuration for encuestas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from encuesta.views import home
from django.conf import settings
from django.conf.urls.static import static
from encuesta.views import cargar_documento, ejecuta_tarea
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('encuesta/', include('encuesta.urls'), name='encuesta'),
    path('cuenta/', include('cuenta.urls'), name='cuenta'),
    path('cargar_documento/', cargar_documento, name='cargar_documento'),
    path('ejecuta_tarea/', ejecuta_tarea, name='ejecuta_tarea'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_usuario'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refrescar_token'),

]




urlpatterns += i18n_patterns(
    path("cms/", include("cms.urls")),
)


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)