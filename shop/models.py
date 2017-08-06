from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.models import OrderingBaseModel, ContentBaseModel, CommentBaseModel
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
import uuid
from django.conf import settings
from properties.models import CategoryProperty, ProductProperty



def make_upload_path(instance, filename, prefix = False):
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    f = parts[-1]
    filename = new_name + '.' + f
    return u"%s/%s" % (settings.SHOP_IMAGE_DIR, filename)



class Category(MPTTModel, ContentBaseModel, CommentBaseModel):
    """
    Category of products
    """
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name=_('Parent'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))
    count_prod = models.IntegerField(blank=True, null=True)
    



    def __str__(self):
        return self.name

    def get_filters(self):
        return FilterCategory.objects.filter(category=self).order_by('ordering')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['name']



class Brand(ContentBaseModel, CommentBaseModel):
    """
    Brands of products
    """
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))
    count_prod = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')



class Product(ContentBaseModel,CommentBaseModel):

    sky = models.CharField(_("Sky"),
        blank=True,
        default="",
        db_index=True,
        max_length=250)

    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name =_('Image'))
    category = models.ForeignKey(Category,
        on_delete=models.CASCADE,
        related_name='categories',
        blank=True,
        null=True,
        verbose_name =_('Category'))
    brand = models.ForeignKey(Brand,
        on_delete=models.CASCADE,
        related_name='brands',
        blank=True,
        null=True,
        verbose_name =_('Category'))
    price = models.DecimalField(max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name =_('Price'))
    promo = models.BooleanField(
        _(u'Show in home page'),
        default=False,
        help_text=_('Show this product on Home page?'))
    short_text = models.TextField(blank=True,)
    full_text = models.TextField(blank=True,)
    recomend = models.IntegerField(blank=True, null=True)
    saleslider = models.IntegerField(blank=True, null=True)
    price_ue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    in_shop = models.IntegerField(blank=True, null=True)
    selling_out = models.IntegerField(blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    action_time = models.DateTimeField(blank=True, null=True)
    action_name = models.CharField(max_length=250, blank=True, null=True)

    @property
    def properties(self):
        items = ProductProperty.objects.filter(product=self)
        return items

    def save(self, *args, **kwargs):
        if self.category:
            super(Product, self).save(*args, **kwargs)
            # we create properties if not exist
            for cp in CategoryProperty.objects.filter(category=self.category):
                pp = ProductProperty.objects.filter(category_property=cp,
                    product=self)
                if not pp:
                    pp = ProductProperty(category_property=cp, product=self, value="--")
                    pp.save()
            # we create filters if not exist
            for fc in FilterCategory.objects.filter(category=self.category):
                pf = ProductFilter.objects.filter(filter_category=fc,
                    product=self)
                if not pf:
                    pf = ProductFilter(filter_category=fc, product=self)
                    pf.save()

    def pic(self):
        if self.image:
            return u'<img src="https://fabro.com.ua/media/%s" width="70"/>' % self.image
            #thumb_u#
            #return u'<img src="%s" width="70"/>' % thumb_url
        else:
            return '(none)'
    pic.short_description = 'Image'
    pic.allow_tags = True


    def get_filters(self):
        res = {}
        category = self.category
        for fp in ProductFilter.objects.filter(product=self):
            name = fp.filter_category.name
            if not fp.filter_category.slug:
                fp.filter_category.slug = slugify(name)
                fp.filter_category.save()
            slug = fp.filter_category.slug
            selects = []
            for s in fp.values.all():
                selects.append(s.name)
            res.update({slug:selects})
        return res


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')




class Offer(OrderingBaseModel):
    product = models.ForeignKey(Product,
        on_delete=models.CASCADE,
        related_name='offers',
        null=True,
        verbose_name =_('Product'))
    name = models.CharField(_("Name"),
        default="",
        max_length=250)
    price = models.DecimalField(max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,
        verbose_name =_('Price'))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class Images( OrderingBaseModel):
    product = models.ForeignKey(Product,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        verbose_name =_('Product'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))

    alt = models.CharField(_("Alt"),
        default="",
        max_length=250)
    title = models.CharField(_("Title"),
        default="",
        max_length=250)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
