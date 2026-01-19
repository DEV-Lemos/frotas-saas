import uuid

from django.db import models


class BaseUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimestampedModel(BaseUUIDModel):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedModel(BaseUUIDModel):
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
