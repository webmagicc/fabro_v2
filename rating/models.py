from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import  ugettext_lazy as _
from core.models import BaseModel


class Rating(BaseModel):
	vote = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')