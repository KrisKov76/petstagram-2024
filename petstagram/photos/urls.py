from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.photo_add_page, name='photo-add'),  # Photo Add Page
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),  # Photo Details Page
        path('edit/', views.photo_edit_page, name='photo-edit'),  # Photo Edit Page
    ])),
]
