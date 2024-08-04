from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, ExpertTips, SubCategory, FaqHeaders, Faq, Legal


admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(SubCategory, ImportExportModelAdmin)
admin.site.register(ExpertTips, ImportExportModelAdmin)
admin.site.register(FaqHeaders, ImportExportModelAdmin)
admin.site.register(Faq, ImportExportModelAdmin)
admin.site.register(Legal, ImportExportModelAdmin)

class CategoryModel(admin.ModelAdmin):
    list_display = ('image', 'name', 'description')

class SubCategoryModel(admin.ModelAdmin):
    list_display = ('name', 'category')

# class MainsubsModel(admin.ModelAdmin):
#     list_display = ('image', 'name', 'description')

