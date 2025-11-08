from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    # ...existing code...
    path('flashcards/', include('flashcards.urls')),
]