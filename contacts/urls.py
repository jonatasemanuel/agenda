from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('find/', views.find, name='find'),
        path('<int:contact_id>', views.show_contact, name='show_contact'),
        ]
