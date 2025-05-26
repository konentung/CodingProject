from django.contrib import admin
from .models import Course, Category, CourseApply

# Courses Admin
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category')
        }),
        ('YotubeCourse', {
            'fields': ('youtube_url', 'image')
        }),
        ('ClassInPerson', {
            'fields': ('apply_url', 'max_people', 'tuition_fee', 'course_start_datetime', 'course_end_date')
        }),
        ('dates', {
            'fields': ('created_at', 'updated_at')
        })
    )

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# CourseApply Admin
class CourseApplyAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'apply_datetime')
    fieldsets = (
        (None, {
            'fields': ('user', 'course', 'apply_datetime')
        }),
        ('Status', {
            'fields': ('status', 'is_completed', 'is_paid', 'is_cancelled')
        })
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseApply, CourseApplyAdmin)