# urls.py

from django.urls import path
from .views import verify_certificate,verify_certificate_qr,show_all_certificates

urlpatterns = [
    path('', verify_certificate, name='verify_certificate'),  # Home page shows form + result
    path('verify/<str:certificate_number>/', verify_certificate_qr, name='verify_certificate_qr'),  # QR code verification
    path('certificates/', show_all_certificates, name='show_all_certificates'),

    
]
