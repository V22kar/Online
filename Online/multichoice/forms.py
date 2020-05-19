from django.forms import ModelForm
from .models import Exam

class CreateExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['marks','Q_No','Question', 'option1', 'option2', 'option3','option4','corrans']