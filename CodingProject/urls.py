"""
URL configuration for CodingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as accountsViews 
from courses import views as coursesViews
from reports import views as reportsViews
from news import views as newsViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # -------- Index --------
    path('', accountsViews.index, name='Index'),
    # -------- Accounts --------
    path('login/', accountsViews.login_view, name='Login'),
    path('logout/', accountsViews.logout_view, name='Logout'),
    path('register/', accountsViews.register, name='Register'),
    path('user_info/', accountsViews.user_info, name='UserInfo'),
    path('accounts/', include('allauth.urls')),

    # -------- 聯絡我們 --------
    path('contact/', reportsViews.report_view, name='ContactUs'),

    # -------- Courses --------
    path('courses/', coursesViews.course_list, name='CourseList'),
    path('courses/<int:course_id>/', coursesViews.course_detail, name='CourseDetail'),    # -------- News --------
    path('news/<int:news_id>/', newsViews.news_item, name='NewsItem'),
    
    # -------- 網站地圖 --------
    path('sitemap/', accountsViews.sitemap_view, name='Sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    from django.views.static import serve
    urlpatterns += [
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
        path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
    ]
