from django.contrib import admin
from .models import User, Category, UserInfo, Level, Job

# User Admin
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('name', 'gender', 'email', 'phone', 'category')
        }),
        ('Permissions', {
            'fields': ('is_active', 'permission')
        }),
        ('dates', {
            'fields': ('created_at', 'updated_at')
        })
    )

# UserInfo Admin
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'cname', 'ename', 'identification_number', 'job', 'company', 'school', 'birthday', 'address', 'level')

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Level Admin
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Job)