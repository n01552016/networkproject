from django.db import models

class Email(models.Model):
    smtp_sender = models.EmailField()
    smtp_password = models.CharField(max_length=255)
    receivers = models.EmailField()
    cc = models.EmailField(blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    class Meta:
        app_label = 'emailsender'