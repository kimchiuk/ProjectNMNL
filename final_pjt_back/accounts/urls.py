from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.user_update)
]
