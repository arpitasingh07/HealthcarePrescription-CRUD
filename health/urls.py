from django.urls import path

from . import views

urlpatterns = [
    path('',views.showPatients, name="showPatients"),
    path('base',views.insertPatients, name="insertPatients"),
    path('edit/<int:id>',views.editPatients, name="editPatients"),
    path('update/<int:id>',views.updatePatients, name="updatePatients"),
    path('delete/<int:id>',views.deletePatients, name="deletePatients"),
]