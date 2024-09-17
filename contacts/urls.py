from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('view/<int:id>/', views.view_contact, name='view_contact'),
    path('update/<int:id>/', views.update_contact, name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]