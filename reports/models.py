from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('phishing', 'Phishing'),
        ('malware', 'Malware'),
        ('data_breach', 'Data Breach'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
