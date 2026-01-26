import uuid

from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TenantAwareModel(UUIDModel):
    """
    Use em qualquer model que pertence a uma Empresa (tenant).
    """

    empresa = models.ForeignKey(
        "tenants.Empresa",
        on_delete=models.PROTECT,
        related_name="%(class)ss",
        db_index=True,
    )

    class Meta:
        abstract = True
