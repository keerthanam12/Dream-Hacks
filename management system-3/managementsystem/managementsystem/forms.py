from django import forms
from .models import TestSubmission

class TestSubmissionForm(forms.ModelForm):
    class Meta:
        model = TestSubmission
        fields = ['answers']