from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
    path('update/<int:id>', views.update_compromisso, name='update_item'),
]
