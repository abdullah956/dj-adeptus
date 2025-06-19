from django.db import models

class Certificate(models.Model):
    CERTIFICATE_TYPES = [
        ('training', 'Training Certificate'),
        ('equipment', 'Equipment Certificate'),
    ]

    certificate_type = models.CharField(max_length=20, choices=CERTIFICATE_TYPES)
    name = models.CharField(max_length=100)
    certificate_number = models.CharField(max_length=50)

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