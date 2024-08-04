from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job, Applicants, Selected

# Register your models here.

admin.site.register(Job, ImportExportModelAdmin)
admin.site.register(Applicants, ImportExportModelAdmin)
admin.site.register(Selected, ImportExportModelAdmin)