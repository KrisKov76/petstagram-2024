from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.pet_add_page, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet-details'),  # Pet Details Page
        path('edit/', views.pet_edit_page, name='pet-edit'),  # Pet Edit Page
        path('delete/', views.pet_delete_page, name='pet-delete'),  # Pet Delete Page
    ])),
]