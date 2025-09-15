from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("academics/", views.academics, name="academics"),
    path("event/", views.event, name="event"),
    path("admissions/", views.admissions, name="admissions"),
    path("service/", views.service, name="service"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
]
