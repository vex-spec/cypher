
from django.contrib import admin
from django.urls import path
from cyberpunkapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name = 'login'),
    path('index/', views.index, name = 'index'),
    path('', views.register, name = 'register'),
]
