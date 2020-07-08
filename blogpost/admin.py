from django.contrib import admin
from .models import SampleModel,BlogModel

# Register your models here.

admin.site.register(SampleModel)
admin.site.register(BlogModel)