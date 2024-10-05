from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='stu form'),
    path('view-data/', views.viewData, name='View Data'),
    path('update/<int:id>', views.updateData, name='Update Student'),
    path('delete/<int:b>', views.deleteData, name='Delete Student'),
]