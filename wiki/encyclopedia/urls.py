from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_entry, name="title"),
    path("search/", views.search, name="search"),
    path("random/", views.random_page, name="random_page"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("save_page/", views.save_page, name="save_page"),
]
