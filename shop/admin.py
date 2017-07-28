from django.contrib import admin
from shop.models import Category, Product, Offer, Images
from mptt.admin import MPTTModelAdmin
from properties.models import CategoryProperty, ProductProperty
from filters.models import FilterCategory, ProductFilter, FilterSelect
from django.forms import TextInput, ModelForm, Textarea, Select


class CategoryPropertyInline(admin.TabularInline):
    model = CategoryProperty
    extra = 1
    verbose_name_plural = 'Params'
    suit_classes = 'suit-tab suit-tab-params'


class FilterCategoryInline(admin.TabularInline):
    model = FilterCategory
    extra = 1
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    inlines = [CategoryPropertyInline,FilterCategoryInline,]
    prepopulated_fields = {"slug": ("name",)}
    suit_form_tabs = (('general', 'General'),
        ('params', 'Params'),
        ('filters','Filters'))
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
             'name',
             'slug',
             'title',
             'description',
             'keywords',
             'image',
             'parent',
             'count_prod',
             'reit',
             'count_votes',
             'comments_count',
             ]
        }),
    ]



class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    extra = 1
    verbose_name_plural = 'Params'
    suit_classes = 'suit-tab suit-tab-params'


class ProductFilterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        if self.instance:
            i = self.instance
            if i.filter_category:
                self.fields["values"].queryset =\
                 FilterSelect.objects.filter(filter_category=i.filter_category)
            else:
                self.fields["values"].queryset =\
                 FilterSelect.objects.all()[:1]

    class Meta:
        model = ProductFilter
        fields = '__all__'

class ProductFilterInline(admin.TabularInline):
    form = ProductFilterForm
    model = ProductFilter
    extra = 1
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 1
    verbose_name_plural = 'Offers'
    suit_classes = 'suit-tab suit-tab-offers'


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1
    verbose_name_plural = 'Images'
    suit_classes = 'suit-tab suit-tab-images'

@admin.register(Product)
class ProductAdmin( admin.ModelAdmin):
    inlines = [ProductPropertyInline,
                OfferInline,
                ProductFilterInline,
                ImagesInline]

    list_display = ('name', 'pic', 'brand', 'category', 'published')
    list_filter = ('category','brand')
    serch_fields = ['id','name', 'sky']

    suit_form_tabs = (('general', 'General'),
        ('offers', 'Offers'),
        ('params', 'Params'),
        ('filters','Filters'),
        ('images','Images'),)
    fieldsets = [
        ('General', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name',
             'slug',
             'title',
             'description',
             'keywords',
             'image',
             'category',
             'price',]
        }),
    ]
