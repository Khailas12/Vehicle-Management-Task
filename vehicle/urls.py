from django.urls import path
from . import views
from django.contrib.auth import views as auth


app_name = 'vehicle'


urlpatterns = [

    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
