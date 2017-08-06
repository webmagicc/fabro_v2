from django.contrib import admin
from .models import FilterCategory, FilterSelect, ProductFilter



class FilterSelectInline(admin.TabularInline):
    model = FilterSelect
    extra = 1
    prepopulated_fields = {"slug": ("name",)}




@admin.register(FilterCategory)
class FilterCategoryAdmin(admin.ModelAdmin):
    inlines = [FilterSelectInline, ]
    list_display = ('name','slug', 'published')
    list_editable = ('published',)
    prepopulated_fields = {"slug": ("name",)}




@admin.register(FilterSelect)
class FilterSelectAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductFilter)
class ProductFilterAdmin(admin.ModelAdmin):
    pass
