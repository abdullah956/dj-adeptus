# urls.py

from django.urls import path
from .views import verify_certificate

urlpatterns = [
    path('', verify_certificate, name='verify_certificate'),  # Home page shows form + result
]
