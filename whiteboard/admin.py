from django.contrib import admin

from whiteboard.models import Company, Engineer

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    search_fields = ['company_name']
    
admin.site.register(Company, CompanyAdmin)

class EngineerAdmin(admin.ModelAdmin):
    list_display=('id', 'engineer_name', 'engineer_type', 'engineer_no', 'start_date', 'company', 'sales_name', 'end_date', 'engineer_status')
    search_fields=['engineer_name', 'company__company_name', 'sales__first_name']
    
    def sales_name(self, obj):
        return obj.sales.first_name

admin.site.register(Engineer, EngineerAdmin)


