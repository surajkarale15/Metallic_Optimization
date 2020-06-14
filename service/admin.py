from django.contrib import admin

# Register your models here.

from service.models import *

admin.site.register(Element)
admin.site.register(Commodity)
admin.site.register(Chemical_composition)
