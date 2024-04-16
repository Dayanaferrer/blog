from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import cadastro_user, fazer_login, paineldousuario, gerenciar_perfil, logout_user
from inicio.views import inicio, sobre, contato
from categorias.views import categoria

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio , name='inicio'), 
    path('cadastro/', cadastro_user, name='cadastro'),
    path('login/', fazer_login, name='login'),    
    path('sobre/', sobre, name='sobre'), 
    path('contato/', contato, name='contato'), 
    path('post/', include('post.urls')),
    path('usuario/', include('usuario.urls')),
    path('categoria/<str:cats>/', categoria, name='categoria'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
