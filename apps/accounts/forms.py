from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from apps.core.i18n.service import t


from .models import User
from .utils import unique_username_from_email


_PASSWORD_ERROR_MAP = {
    "This password is too short. It must contain at least 6 characters.": (
        "Parol juda qisqa. Kamida 6 belgi bo‘lishi kerak."
    ),
    "This password is too short. It must contain at least 10 characters.": (
        "Parol juda qisqa. Kamida 6 belgi bo‘lishi kerak."
    ),
    "The two password fields didn’t match.": "Parollar mos kelmadi.",
    "The two password fields didn't match.": "Parollar mos kelmadi.",
}


def _localize_password_errors(exc: ValidationError) -> ValidationError:
    messages = []
    for msg in exc.messages:
        key = _PASSWORD_ERROR_MAP.get(str(msg))
        if key is None and str(msg).startswith("The password is too similar"):
            key = "Parol shaxsiy ma’lumotlarga juda o‘xshash."
        messages.append(t(key or str(msg)))
    return ValidationError(messages)


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Ism", max_length=150)
    last_name = forms.CharField(label="Familiya", max_length=150)
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = t("Ism")
        self.fields["last_name"].label = t("Familiya")
        self.fields["email"].label = t("Email")
        self.fields["password1"].label = t("Parol")
        self.fields["password2"].label = t("Parolni tasdiqlang")
        self.fields["password1"].help_text = t("Kamida 6 belgi.")
        self.fields["password2"].help_text = ""
        self.fields["password1"].strip = True
        self.fields["password2"].strip = True
        required_msg = t("Bu maydon majburiy.")
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"
            field.error_messages["required"] = required_msg
        self.fields["email"].error_messages["invalid"] = t("To‘g‘ri email manzilini kiriting.")

    def clean_email(self):
        email = self.cleaned_data["email"].lower().strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(t("Bu email allaqachon ro‘yxatdan o‘tgan."))
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if isinstance(password1, str):
            password1 = password1.strip()
        if not password1:
            raise ValidationError(t("Bu maydon majburiy."), code="required")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if isinstance(password2, str):
            password2 = password2.strip()
        if not password2:
            raise ValidationError(t("Bu maydon majburiy."), code="required")
        return password2

    def validate_passwords(
        self,
        password1_field_name="password1",
        password2_field_name="password2",
    ):
        password1 = self.cleaned_data.get(password1_field_name)
        password2 = self.cleaned_data.get(password2_field_name)
        if password1 and password2 and password1 != password2:
            self.add_error(
                password2_field_name,
                ValidationError(t("Parollar mos kelmadi."), code="password_mismatch"),
            )

    def validate_password_for_user(self, user, password_field_name="password2"):
        password = self.cleaned_data.get(password_field_name)
        if not password:
            return
        try:
            validate_password(password, user)
        except ValidationError as error:
            self.add_error(password_field_name, _localize_password_errors(error))

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
        self.fields["username"].label = t("Email")
        self.fields["password"].label = t("Parol")
        self.fields["password"].widget.attrs["class"] = "input"
        required_msg = t("Bu maydon majburiy.")
        for field in self.fields.values():
            field.error_messages["required"] = required_msg
        self.fields["username"].error_messages["invalid"] = t("To‘g‘ri email manzilini kiriting.")

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
                raise ValidationError(t(self.error_messages["invalid_login"]), code="invalid_login")
            if getattr(self.user_cache, "is_blocked", False):
                raise ValidationError(t("Hisobingiz bloklangan. Administrator bilan bog‘laning."))
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
        help_text="Kamida 6 belgi. Bo‘sh qoldirsangiz — parol o‘zgarmaydi.",
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
        self.fields["username"].label = t("Foydalanuvchi nomi")
        self.fields["email"].label = t("Email")
        self.fields["first_name"].label = t("Ism")
        self.fields["last_name"].label = t("Familiya")
        self.fields["current_password"].label = t("Joriy parol")
        self.fields["new_password1"].label = t("Yangi parol")
        self.fields["new_password2"].label = t("Yangi parolni tasdiqlang")
        self.fields["new_password1"].help_text = t("Kamida 6 belgi. Bo‘sh qoldirsangiz — parol o‘zgarmaydi.")
        required_msg = t("Bu maydon majburiy.")
        for field in self.fields.values():
            field.widget.attrs["class"] = "input"
            field.error_messages["required"] = required_msg
        self.fields["email"].error_messages["invalid"] = t("To‘g‘ri email manzilini kiriting.")

    def clean_username(self):
        username = (self.cleaned_data.get("username") or "").strip()
        if not username:
            raise ValidationError(t("Foydalanuvchi nomi majburiy."))
        qs = User.objects.filter(username__iexact=username)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError(t("Bu foydalanuvchi nomi band."))
        return username

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").lower().strip()
        if not email:
            raise ValidationError(t("Email majburiy."))
        qs = User.objects.filter(email__iexact=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError(t("Bu email allaqachon band."))
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("new_password1") or ""
        p2 = cleaned.get("new_password2") or ""
        current = cleaned.get("current_password") or ""
        if p1 or p2:
            if not p1 or not p2:
                raise ValidationError(t("Yangi parolni ikkala maydonga ham yozing."))
            p1 = p1.strip()
            p2 = p2.strip()
            cleaned["new_password1"] = p1
            cleaned["new_password2"] = p2
            if p1 != p2:
                raise ValidationError(t("Yangi parollar mos kelmadi."))
            if self.instance.has_usable_password():
                if not current:
                    raise ValidationError(t("Parolni o‘zgartirish uchun joriy parolni kiriting."))
                if not self.instance.check_password(current):
                    raise ValidationError(t("Joriy parol noto‘g‘ri."))
            try:
                validate_password(p1, self.instance)
            except ValidationError as exc:
                raise _localize_password_errors(exc) from exc
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password1")
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user
