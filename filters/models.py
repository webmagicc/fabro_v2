from django.db import models
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
import uuid

from fabro_v2.models import (
    BaseModel,
    OrderingBaseModel,
    SlugBaseModel
    )
from django.utils.encoding import python_2_unicode_compatible, force_text
from slugify import slugify



class FilterCategory(SlugBaseModel):
    category = models.ForeignKey('shop.Category',
        on_delete=models.CASCADE,
        related_name='filtercategories',
        verbose_name =_('Category'))

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)

        super(FilterCategory, self).save()

    class Meta:
        verbose_name = _('Filter Category')
        verbose_name_plural = _('Filters Category')



class FilterSelect(SlugBaseModel):
    filter_category = models.ForeignKey(FilterCategory,
        on_delete=models.CASCADE,
        related_name='filterselect',
        verbose_name =_('Filter Category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Filter Select')
        verbose_name_plural = _('Filters Select')



class ProductFilter(OrderingBaseModel):
    product = models.ForeignKey('shop.Product',
        on_delete=models.CASCADE,
        related_name='filterproducts',
        null=True,
        verbose_name =_('Product'))
    filter_category = models.ForeignKey(FilterCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='filter_select_product',
        verbose_name =_('Filter Category'))
    values = models.ManyToManyField(FilterSelect,
        related_name='filtervalues',
        blank=True,
        verbose_name =_('Values'))
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Product Filter')
        verbose_name_plural = _('Product Filters')
