from django.contrib import admin

# Register your models here.
from catalogapp.models import ProductCatalog, Section

admin.site.register(ProductCatalog)
admin.site.register(Section)