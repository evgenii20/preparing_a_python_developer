from django.contrib import admin

# Register your models here.
from hitcount.models import HitCount

admin.site.register(HitCount)
