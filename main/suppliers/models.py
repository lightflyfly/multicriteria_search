import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


@receiver(post_save, sender=Supplier)
def update_supplier_index(sender, instance, **kwargs):
    instance.supplierdocument.update(using='default')
