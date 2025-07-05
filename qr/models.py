from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    certificate_number = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    # Training certificate fields
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    card_number = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    
    # Equipment certificate fields
    sticker_no = models.CharField(max_length=50, blank=True, null=True)
    equipment_id = models.CharField(max_length=50, blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    next_inspection_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # Lifting gear certificate fields
    item_name = models.CharField(max_length=100, blank=True, null=True)
    lifting_inspection_date = models.DateField(blank=True, null=True)
    lifting_next_inspection = models.DateField(blank=True, null=True)
    serial_no = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)
    swl = models.CharField(max_length=50, blank=True, null=True)
    standard_ref = models.CharField(max_length=100, blank=True, null=True)
    lifting_remarks = models.TextField(blank=True, null=True)
    inspector = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        base_url = getattr(settings, 'SITE_DOMAIN', 'http://127.0.0.1:8000')
        qr_data = f"{base_url}/verify/{self.certificate_number}/"

        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f'qr_{self.certificate_number}.png'

        self.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)