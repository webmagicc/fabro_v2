from django.db import models
from django.conf import settings
from shop.models import Product
from core.models import OrderingBaseModel
from django.utils.translation import to_locale, get_language, ugettext_lazy as _

class Cart(OrderingBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             verbose_name=_('User'))
    coockie = models.CharField(_('Cookie'),
                               max_length=100,
                               db_index=True,
                               default="")
    total_sum = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=0.00,
                                null=True,
                                blank=True,
                                verbose_name=_('Total sum'))
    total_qt = models.IntegerField(_('Total quantity'),
                                   null=True,
                                   default=0,
                                   blank=True)
    def __str__(self):
        return self.coockie

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')



class CartItem(OrderingBaseModel):
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE,
                             null=True,
                             verbose_name=_('Cart'))
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name=_('Product'))
    total = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=0.00,
                                null=True,
                                blank=True,
                                verbose_name=_('Total sum'))
    qt = models.IntegerField(_('Total quantity'),
                                   null=True,
                                   default=0,
                                   blank=True)
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')
