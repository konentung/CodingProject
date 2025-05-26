from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Category, UserInfo, Level, Job
from django.core.exceptions import ValidationError
import re

class LoginForm(forms.Form):

    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入帳號'}),
    )

    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入密碼'}),
    )

    remember_me = forms.BooleanField(
        label="記住我",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input txt'}),
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入帳號'}),
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入密碼'}),
    )

    password2 = forms.CharField(
        label="確認密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control txt', 'placeholder': '請再次輸入密碼'}),
    )

class UserForm(forms.ModelForm):

    name = forms.CharField(
        label="暱稱",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入暱稱', 'required': 'required'}),
    )

    # 設定預設顯示的選項為空白
    gender = forms.ChoiceField(
        label="性別",
        required=True,
        choices=(
            ('M', '男'),
            ('F', '女'),
        ),
        widget=forms.Select(attrs={'class': 'form-control txt', 'placeholder': '請選擇性別'}),
    )

    email = forms.EmailField(
        label="電子郵件",
        required=True,
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入電子郵件'}),
    )

    phone = forms.CharField(
        label="手機號碼",
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入手機號碼'}),
    )

    category = forms.ModelChoiceField(
        label="類別",
        required=False,
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control txt'}),
    )

    class Meta:
        model = User
        fields = ['name', 'gender', 'email', 'phone', 'category']

class UserInfoForm(forms.ModelForm):

    cname = forms.CharField(
        label="中文姓名",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入中文姓名'}),
    )

    ename = forms.CharField(
        label="英文姓名",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入英文姓名'}),
    )

    identification_number = forms.CharField(
        label="身份證字號",
        required=False,
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入身份證字號'}),
    )

    job = forms.ModelChoiceField(
        label="職業",
        required=False,
        queryset=Job.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control txt'}),
    )

    company = forms.CharField(
        label="公司名稱",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入公司名稱'}),
    )

    school = forms.CharField(
        label="學校名稱",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入學校名稱'}),
    )

    birthday = forms.DateField(
        label="生日",
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入生日', 'type': 'date'}),
    )

    address = forms.CharField(
        label="地址",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control txt', 'placeholder': '請輸入地址'}),
    )

    level = forms.ModelChoiceField(
        label="等級",
        required=False,
        queryset=Level.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control txt'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 在初始化時強制禁用 level 欄位
        self.fields['level'].widget.attrs['disabled'] = 'disabled'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^09\d{8}$', phone):
            raise ValidationError("手機號碼格式不正確，請輸入09開頭的10位數字")
        return phone

    def clean_identification_number(self):
        identification_number = self.cleaned_data.get('identification_number')
        if not identification_number:
            return identification_number
        # 驗證格式是否為大寫英文字母 + 1 或 2 + 8 位數字
        if not re.match(r'^[A-Z][12]\d{8}$', identification_number):
            raise ValidationError("身份證字號格式不正確，請輸入正確的身份證字號")
        return identification_number


    class Meta:
        model = UserInfo
        fields = ['cname', 'ename', 'identification_number', 'job', 'company', 'school', 'birthday', 'address', 'level']