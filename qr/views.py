from django.shortcuts import render
from django.http import JsonResponse
from .models import Certificate

def verify_certificate(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        certificate_number = request.GET.get('certificate_number')
        cert_type = request.GET.get('certificate_type')

        if not certificate_number or not cert_type:
            return JsonResponse({'error': 'Please fill all fields'}, status=400)

        try:
            cert = Certificate.objects.get(certificate_number=certificate_number, certificate_type=cert_type)
            data = {
                'name': cert.name,
                'certificate_number': cert.certificate_number,
                'type': cert_type,
            }

            if cert_type == 'training':
                data.update({
                    'registration_number': cert.registration_number,
                    'card_number': cert.card_number,
                    'course': cert.course,
                    'issue_date': cert.issue_date,
                    'renewal_date': cert.renewal_date,
                })
            elif cert_type == 'equipment':
                data.update({
                    'sticker_no': cert.sticker_no,
                    'equipment_id': cert.equipment_id,
                    'inspection_date': cert.inspection_date,
                    'next_inspection_date': cert.next_inspection_date,
                    'location': cert.location,
                    'comments': cert.comments,
                })

            return JsonResponse({'certificate': data})

        except Certificate.DoesNotExist:
            return JsonResponse({'error': 'Invalid certificate number or type'}, status=404)

    # Fallback for initial load
    return render(request, 'home.html')
