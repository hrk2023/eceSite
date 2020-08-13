from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('subject/',views.subjectAdd, name="subject"),
    path('dberror/',views.dberror, name="dberror"),
    path('deletesub/<id>/',views.subjectDelete, name="delete"),
    path('videoadd/', views.videoadd, name="videoadd"),
    path('videopage/<course>', views.videopage, name="videopage")
]