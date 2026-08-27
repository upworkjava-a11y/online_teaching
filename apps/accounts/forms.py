from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
)
from django.core.exceptions import ValidationError

from .models import User
from .utils import unique_username_from_email


class StyledPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["email"].widget.attrs.update({"class": "input", "autofocus": True})


class StyledSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].label = "Yangi parol"
        self.fields["new_password2"].label = "Yangi parolni tasdiqlang"
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Ism", max_length=150)
    last_name = forms.CharField(label="Familiya", max_length=150)
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Parol"
        self.fields["password2"].label = "Parolni tasdiqlang"
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Bu email allaqachon ro‘yxatdan o‘tgan.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        user.username = unique_username_from_email(user.email)
        user.role = User.Role.STUDENT
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "input", "autofocus": True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].label = "Parol"
        self.fields["password"].widget.attrs["class"] = "input"

    error_messages = {
        "invalid_login": "Email yoki parol noto‘g‘ri.",
        "inactive": "Bu hisob faol emas.",
    }

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise ValidationError(self.error_messages["invalid_login"], code="invalid_login")
            if getattr(self.user_cache, "is_blocked", False):
                raise ValidationError("Hisobingiz bloklangan. Administrator bilan bog‘laning.")
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="Foydalanuvchi nomi", max_length=150)
    email = forms.EmailField(label="Email")
    current_password = forms.CharField(
        label="Joriy parol",
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    new_password1 = forms.CharField(
        label="Yangi parol",
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Kamida 10 belgi. Bo‘sh qoldirsangiz — parol o‘zgarmaydi.",
    )
    new_password2 = forms.CharField(
        label="Yangi parolni tasdiqlang",
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        labels = {
            "first_name": "Ism",
            "last_name": "Familiya",
            "username": "Foydalanuvchi nomi",
            "email": "Email",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"

    def clean_username(self):
        username = (self.cleaned_data.get("username") or "").strip()
        if not username:
            raise ValidationError("Foydalanuvchi nomi majburiy.")
        qs = User.objects.filter(username__iexact=username)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Bu foydalanuvchi nomi band.")
        return username

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").lower().strip()
        if not email:
            raise ValidationError("Email majburiy.")
        qs = User.objects.filter(email__iexact=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Bu email allaqachon band.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("new_password1") or ""
        p2 = cleaned.get("new_password2") or ""
        current = cleaned.get("current_password") or ""
        if p1 or p2:
            if not p1 or not p2:
                raise ValidationError("Yangi parolni ikkala maydonga ham yozing.")
            if p1 != p2:
                raise ValidationError("Yangi parollar mos kelmadi.")
            if self.instance.has_usable_password():
                if not current:
                    raise ValidationError("Parolni o‘zgartirish uchun joriy parolni kiriting.")
                if not self.instance.check_password(current):
                    raise ValidationError("Joriy parol noto‘g‘ri.")
            from django.contrib.auth.password_validation import validate_password

            validate_password(p1, self.instance)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password1")
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user
