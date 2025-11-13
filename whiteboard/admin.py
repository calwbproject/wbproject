from django.contrib import admin

from whiteboard.models import Company, Engineer

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    
admin.site.register(Company, CompanyAdmin)

class EngineerAdmin(admin.ModelAdmin):
    list_display=('id', 'engineer_name', 'engineer_type', 'engineer_no', 'start_date', 'company', 'sales', 'end_date', 'engineer_status')

admin.site.register(Engineer, EngineerAdmin)


