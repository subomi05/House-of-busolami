from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery_page, name="gallery"),
    path(
     "appointment-success/",
      views.appointment_success,
     name="appointment_success",
    ),
]