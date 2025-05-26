from django.contrib import admin
from .models import Report, ReportType

# Report Admin
class ReportAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'report_type', 'other_report_type', 'report_content', 'created_at', 'is_completed')
        }),
    )

# ReportType Admin
class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportType, ReportTypeAdmin)