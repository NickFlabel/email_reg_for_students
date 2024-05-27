from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.signing import Signer


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        instance.is_active = False
        instance.save()
        signer = Signer()
        signed_username = signer.sign(instance.username)
        message = f'http://127.0.0.1:8000/activate/{signed_username}'
        email = EmailMessage('Активация', message, to=[instance.email], from_email='admin@admin.com')
        email.send()
