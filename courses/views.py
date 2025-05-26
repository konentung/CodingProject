from django.shortcuts import render
from .models import Course, Category, CourseApply
from django.core.paginator import Paginator

# 課程清單
def course_list(request):
    courses = Course.objects.all()
    # paginator = Paginator(courses, 6)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'course/course_list.html', locals())

# 課程詳細資訊
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course/course.html', locals())