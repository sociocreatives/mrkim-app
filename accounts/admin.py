from django.contrib import admin
from .models import User, Profile, Tvets
from import_export.admin import ImportExportModelAdmin

class UserModel(admin.ModelAdmin):
    list_display = ('email', 'username', 'role', 'date_joined', 'last_login')

class TvetsModel(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(User, UserModel)
admin.site.register(Profile)
admin.site.register(Tvets, ImportExportModelAdmin)