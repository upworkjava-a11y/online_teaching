from __future__ import annotations

from django import forms
from django.conf import settings

from apps.accounts.avatars import avatar_choices


class MessageForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "maxlength": 1000, "placeholder": "Xabar yozing…"}),
        max_length=getattr(settings, "SOCIAL_MESSAGE_MAX_LENGTH", 1000),
    )


class AvatarPresetForm(forms.Form):
    avatar_preset = forms.ChoiceField(choices=avatar_choices())


class AvatarUploadForm(forms.Form):
    avatar = forms.ImageField()


class ProfileBioForm(forms.Form):
    bio = forms.CharField(
        required=False,
        max_length=280,
        widget=forms.Textarea(attrs={"rows": 3, "maxlength": 280}),
    )
