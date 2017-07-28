from django.db import models
from django.utils.translation import to_locale, get_language, ugettext_lazy as _


class BaseModel(models.Model):
    """
    Absrtact model
    Add to standart models date of
    crete and update
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name=_(u'Creation date'))
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name=_(u'Modification date'))

    objects = models.Manager()

    class Meta:
        abstract = True

class OrderingBaseModel(BaseModel):
    """
    Absrtact model
    Add to BaseModel  published,
    ordering
    """
    published = models.BooleanField(
        _(u'Published'),
        default=True,
        help_text=_('Decides whether entity should be treated as active.'))
    ordering = models.IntegerField(_(u'Ordering'),
        default=0,
        blank=True,
        null=True)

    class Meta:
        abstract = True


class ContentBaseModel(OrderingBaseModel):
    """
    Absrtact model
    Add to BaseModel  title, description, keywords
    """
    name = models.CharField(_('Name'),
                            max_length=250,
                            default="")
    title = models.CharField(_("Title"),
                            blank=True,
                            default="",
                            max_length=250)
    description = models.CharField(_('Meta description'),
                            max_length=250,
                            blank=True,
                            default="")
    keywords = models.CharField(_('Meta keywords'),
                            max_length=250,
                            blank=True,
                            default="")
    slug = models.CharField(_('Slug'),
                            max_length=250,
                            blank=True,
                            db_index=True,
                            default="")

    class Meta:
        abstract = True


class SlugBaseModel(OrderingBaseModel):
    """
    Absrtact model
    Add to BaseModel  slug
    """
    name = models.CharField(_('Name'),
                            max_length=250,
                            default="")
    slug = models.CharField(_('Slug'),
                            max_length=250,
                            blank=True,
                            db_index=True,
                            default="")

    class Meta:
        abstract = True
