# devs_proyect/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls import handler404
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


# app_name = 'core'  # Esta línea no es necesaria aquí, ya que el archivo 'urls.py' de 'core' maneja las rutas específicas de la app core

urlpatterns = [
    # Ruta para la página de inicio (esta ruta ya es parte de 'core.urls', no necesitas incluir devs_proyect.urls aquí)
    path('', views.index, name='index'),
    
    # Rutas de administración
    path('admin/', admin.site.urls),
    path('acercade/', views.acercade_view, name='about'),  # Ruta para la página "Acerca de"
    path('contacto/', views.contacto_view, name='contacto'),  # Ruta para la página "Contacto"
    path('article/<int:id>/', views.articulo_view, name='articulo'),  # Ruta para la página "Artículo"
    path('categorias/', views.categorias_view, name='categories'),

    # Rutas de autenticación
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Rutas para resetear contraseña
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<uuid:token>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<uuid:token>/', views.ResetPassword, name='reset-password'),
    path('password-reset-sent-generic/', views.PasswordResetSentGeneric, name='password-reset-sent-generic'),

    #perfiles
    path('my-profile/', views.profile_view, name='my-profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    #Buscador
    path("buscar/", views.search_products, name="search_products"),
    
    #dashboard
    path('dashboard/', include('dashboard.urls')),
    
    # Incluyendo las rutas de la app 'sale'
    path('sale/', include('sale.urls')),
    
    # Pagos
    path("payment/", include('payment.urls')),

    # Categorias
    path('categories/', views.categories, name='categories'),
]

# Asigna la función personalizada a handler404
handler404 = 'core.views.custom_404_view'

# Si estás en modo DEBUG, servir los archivos estáticos y de medios
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)