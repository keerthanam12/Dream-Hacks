

# managementsystem/forms.py
from django import forms
from .models import QuizSubmission

class QuizSubmissionForm(forms.ModelForm):
    class Meta:
        model = QuizSubmission
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4']  # Update with your actual field names
