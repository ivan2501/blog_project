from django.urls import path
from . import views #relativen import (od istiot folder importiraj mi go views)

urlpatterns = [
    path("", views.home, name="Blog-Home"),
    path("about/", views.about, name="Blog - About")
]