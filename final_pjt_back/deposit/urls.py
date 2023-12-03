from django.urls import path
from . import views

urlpatterns = [
    path("", views.save_deposit_products),
    path("deposit/", views.deposit_list),
    path("deposit_option/", views.deposit_option),
    path("savings/", views.savings_list),
    path("savings_option/", views.savings_option),
]
