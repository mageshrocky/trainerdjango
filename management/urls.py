from django.urls import path
from . import views
from .views import homepage, login_management, create_account, created, trainer, dashboard, search

urlpatterns =[
    path('homepage/', homepage),
    path('login_management/', views.login_management, name='account'),
    path('management/', views.management, name = 'manager'),
    path('trainer/', views.trainer, name='trainer'),
    path('create_account/', create_account),
    path('created/', created),
    path('dashboard/', dashboard),
    path('search/', search),
    path('logout/', views.logout, name='log out'),
]