from django.contrib import admin
from .models import NewsUnit, Category, NewsComment

# NewsUnits Admin
class NewsUnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_show', 'click_count')

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# NewsComment Admin
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'author', 'pub_date')

admin.site.register(NewsUnit, NewsUnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsComment, NewsCommentAdmin)