from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, ExpertTips, SubCategory, FaqHeaders, Faq, Legal, PremiumTitles, Premium


admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(SubCategory, ImportExportModelAdmin)
admin.site.register(ExpertTips, ImportExportModelAdmin)
admin.site.register(FaqHeaders, ImportExportModelAdmin)
admin.site.register(Faq, ImportExportModelAdmin)
admin.site.register(Legal, ImportExportModelAdmin)
admin.site.register(PremiumTitles, ImportExportModelAdmin)
admin.site.register(Premium, ImportExportModelAdmin)

class CategoryModel(admin.ModelAdmin):
    list_display = ('image', 'name', 'description')

class SubCategoryModel(admin.ModelAdmin):
    list_display = ('name', 'category')

# class MainsubsModel(admin.ModelAdmin):
#     list_display = ('image', 'name', 'description')

