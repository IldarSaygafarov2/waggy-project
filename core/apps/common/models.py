import uuid

from django.db import models


class BaseModel(models.Model):
    """
    An abstract base model that provides common fields for all models.
    """

    id = models.UUIDField(
        primary_key=True, editable=False, verbose_name="ID", default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        ordering = ["-created_at"]
