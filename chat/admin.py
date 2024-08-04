from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Message

# Register your models here.

admin.site.register(Message, ImportExportModelAdmin)


