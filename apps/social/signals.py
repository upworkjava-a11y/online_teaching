from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_social_profile(sender, instance, created, **kwargs):
    if created:
        from apps.social.models import SocialProfile

        SocialProfile.objects.get_or_create(user=instance)
