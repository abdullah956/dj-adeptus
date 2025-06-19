# views.py

from django.shortcuts import render
from .models import Certificate

def verify_certificate(request):
    context = {}
    if request.method == 'GET' and 'certificate_number' in request.GET:
        certificate_number = request.GET.get('certificate_number')
        cert_type = request.GET.get('certificate_type')

        print("DEBUG: certificate_number =", certificate_number)
        print("DEBUG: certificate_type =", cert_type)

        if certificate_number and cert_type:
            try:
                cert = Certificate.objects.get(certificate_number=certificate_number, certificate_type=cert_type)
                context['certificate'] = cert
                context['type'] = cert_type
            except Certificate.DoesNotExist:
                context['error'] = 'Invalid certificate number or type'
        else:
            context['error'] = 'Please fill all fields'
    
    return render(request, 'home.html', context)
