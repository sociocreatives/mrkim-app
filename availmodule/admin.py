from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Availability

# Register your models here.
admin.site.register(Availability, ImportExportModelAdmin)