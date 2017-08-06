from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import  ugettext_lazy as _
from core.models import OrderingBaseModel


class Comment(MPTTModel, OrderingBaseModel):
    author = models.CharField(_('Author name'),
        max_length=250,
        default="")
    author_id = models.PositiveIntegerField(_('Author id'),
        null=True,
        db_index=True,
        default=0)
    author_email = models.EmailField(_('Author Email'),
        blank=True,
        db_index=True,
        default="")
    text = models.TextField(_("Comment"),
        blank=True,
        default="")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    likes = models.PositiveIntegerField(_('Likes'),
        null=True,
        db_index=True,
        default=0)
    dislikes = models.PositiveIntegerField(_('Dislikes'),
        null=True,
        db_index=True,
        default=0)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name=_('Parent'))
    advantages = models.TextField(_("Advantages"),
        blank=True,
        default="")
    limitations = models.TextField(_("Limitations"),
        blank=True,
        default="")

    class Meta:
        verbose_name='Comment'
        verbose_name_plural = 'Comments'


    class MPTTMeta:
        order_insertion_by = ['id']
