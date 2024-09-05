from django.urls import path
from .views import HomePageView, journal_detail, contact, email_sent,journal_create
# from .views import listeJournaux

# urlpatterns = [
#     path("", listeJournaux, name="home")
# ]

# app_name = "journaux"

urlpatterns = [
    path("", HomePageView.as_view(), name="journaux_list"),
    path("journaux/<int:id>/", journal_detail, name="journaux_detail"),
    path("contact-us/", contact, name="contact"),
    path("email-ok/", email_sent, name="email-sent"),
    path('journaux/add/', journal_create, name='journal-create'),
]