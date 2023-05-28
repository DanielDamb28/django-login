from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_screen, name='login'),
    path("cadastro/", views.cadastro_screen, name='cadastro'),
    path("logout/", views.logout_view, name='logout')
]
