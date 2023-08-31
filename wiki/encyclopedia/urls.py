from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_Entry, name="title"),
    path("search/", views.search, name="search"),
    path("random/", views.randomPage, name="randomPage")
]
