from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
import traceback
from .models import User, UserInfo
from news.models import NewsUnit
from .form import LoginForm, UserForm, UserInfoForm, RegisterForm
import re

User = get_user_model()

# index view
def index(request):
    news = NewsUnit.objects.filter(is_show=True).order_by('-pub_date')[:5]
    return render(request, 'index.html', locals())

# login view
def login_view(request):
    # 使用者已經登入，重新導向首頁
    if request.user.is_authenticated:
        return redirect(reverse('Index'))

    if request.method == 'POST':
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                remember_me = form.cleaned_data.get('remember_me', False)

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(1209600)
                    return JsonResponse({'status': 'success', 'message': '登入成功!'})
                else:
                    return JsonResponse({'status': 'error', 'message': '帳號或密碼錯誤!'})
            else:
                return JsonResponse({'status': 'error', 'message': '輸入錯誤!'})
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'status': 'error', 'message': '系統錯誤，請連絡系統管理員!'})
    else:
        return render(request, 'account/login.html', {'form': LoginForm()})

# logout view
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('Index'))
    else:
        return redirect(reverse('Login'))

# register view
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('Index'))
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': '帳號已存在！'})
            form.save()
            return JsonResponse({'status': 'success', 'message': '註冊成功！'})
        else:
            message = ''
            for field, errors in form.errors.items():
                for err in errors:
                    message += f"{err}\n"
            return JsonResponse({'status': 'error', 'message': message})

    return render(request, 'account/register.html', locals())

# 網站地圖頁面
def sitemap_view(request):
    return render(request, 'sitemap.html')

# user info view
@login_required(redirect_field_name='UserInfo')
def user_info(request):
    user = request.user

    user_instance = User.objects.get(username=user.username)
    user_info_instance = UserInfo.objects.filter(user=user).first()
    
    user_form = UserForm(instance=user_instance)
    user_info_form = UserInfoForm(instance=user_info_instance) if user_info_instance else UserInfoForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        user_info_form = UserInfoForm(request.POST, instance=user_info_instance)

        if user_form.is_valid() and user_info_form.is_valid():
            user_form.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()
            return render(request, 'account/info.html', locals(), 200)
        else:
            errors = {**user_form.errors, **user_info_form.errors}
            return render(request, 'account/info.html', locals(), 400)

    return render(request, 'account/info.html', locals())