from django.http import JsonResponse
from django.shortcuts import render
from .models import Certificate

def verify_certificate(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        certificate_number = request.GET.get('certificate_number')
        if not certificate_number:
            return JsonResponse({'error': 'Please enter the certificate number'}, status=400)

        try:
            cert = Certificate.objects.get(certificate_number=certificate_number)
            data = {
                'name': cert.name,
                'certificate_number': cert.certificate_number,

                # Training fields
                'registration_number': cert.registration_number,
                'card_number': cert.card_number,
                'course': cert.course,
                'issue_date': cert.issue_date,
                'renewal_date': cert.renewal_date,

                # Equipment fields
                'sticker_no': cert.sticker_no,
                'equipment_id': cert.equipment_id,
                'inspection_date': cert.inspection_date,
                'next_inspection_date': cert.next_inspection_date,
                'location': cert.location,
                'comments': cert.comments,
            }
            return JsonResponse({'certificate': data})

        except Certificate.DoesNotExist:
            return JsonResponse({'error': 'Certificate not found'}, status=404)

    return render(request, 'home.html')
