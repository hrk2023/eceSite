from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('subject/',views.subjectAdd, name="subject"),
    path('dberror/',views.dberror, name="dberror"),
    path('deletesub/<id>/',views.subjectDelete, name="delete"),
    path('videoadd/', views.videoadd, name="videoadd"),
    path('pdfadd/', views.pdfadd, name="pdfadd"),
    path('liveadd/', views.livevidadd, name="liveadd"),
    path('videopage/<course>', views.videopage, name="videopage"),
    path('pdfpage/<course>', views.pdfpage, name="pdfpage"),
    path('livevidpage/<course>', views.livevidpage, name="livevidpage"),
    path('classification/<course>', views.classification, name="classification")
]