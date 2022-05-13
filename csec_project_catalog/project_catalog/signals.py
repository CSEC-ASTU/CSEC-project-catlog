from django.db.models.signals import post_save
from django.dispatch import receiver
from project_catalog.bot import send_to_channel
from project_catalog.models import Project


@receiver(post_save, sender=Project)
def project_post_save(sender, instance, created, *args, **kwargs):
    if created and not instance.posted_on_tg:
        if instance.is_approved == True:
            try:

                send_to_channel(instance)
                instance.posted_on_tg = True
                instance.save()
            except Exception as e:
                print(e)
                pass
    else:
        if not instance.posted_on_tg and instance.is_approved == True:
            try:

                send_to_channel(instance)
                instance.posted_on_tg = True
                instance.save()
            except Exception as e:
                print(e)
                pass
