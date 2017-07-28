from django.core.management.base import BaseCommand, CommandError
from old.models import ShopBrand
from shop.models import Brand



class Command(BaseCommand):

    def handle(self, *args, **options):
        for c in ShopBrand.objects.using('old').all():
            brand = Brand.objects.filter(slug=c.pk).first()
            if not brand:
                brand = Brand(pk=c.pk)

            brand.name = c.name
            brand.slug = c.slug
            brand.title = c.title
            brand.description = c.metadesc
            brand.keywords = c.metakey

            brand.image = c.image
            brand.save()
            print(brand.id)
