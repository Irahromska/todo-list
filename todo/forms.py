from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < timezone.now():
            raise ValidationError("Deadline must be in the future")
        return deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
