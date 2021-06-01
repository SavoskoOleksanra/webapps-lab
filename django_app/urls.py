from django.urls import path
from django_app import views
from django_app.models import ConnectedUsers

urlpatterns = [
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:poll_id>/', views.room, name='poll_id'),
]

ConnectedUsers.objects.all().delete()
