from django.db.models.signals import (
    m2m_changed,
    post_delete,
    post_save,
    pre_delete,
    pre_save,
)

# signals imports
from django.dispatch import receiver

from .bot import send_to_channel
from .models import Project


@receiver(pre_save, sender=Project)
def project_pre_save(sender, instance, *args, **kwargs):
    global Flag
    if instance.id == None:
        print(instance, "my instance >>>>>>>>>>>>>")

    else:

        if instance.approved_status == True:
            if not instance.posted_on_tg == True:
                send_to_channel(instance)
                instance.posted_on_tg = True


@receiver(post_save, sender=Project)
def project_post_save(sender, instance, created, *args, **kwargs):
    if created and instance.posted_on_tg:
        send_to_channel(instance)
