from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Exam,StudentProfile
from .forms import CreateExamForm



class HomeView(TemplateView):
    template_name = "multichoice/home.html"


class ContactView(TemplateView):
    template_name = "multichoice/contact.html"

def examonline(request):
    results = Exam.objects.all()
    return render(request,'multichoice/test.html',{'exam':results})

@method_decorator(login_required, name="dispatch")
class StudentProfileUpdateView(UpdateView):
    model = StudentProfile
    fields =["Class","roll_No","name","gender","phone_no","address","pic"]
    

@method_decorator(login_required, name="dispatch")
class StudentProfileListView(ListView):
    model = StudentProfile
    


@method_decorator(login_required, name="dispatch")
class StudentProfileDetailView(DetailView):
    model = StudentProfile




def create(request):
    if request.method == 'POST':
        form = CreateExamForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/multichoice/examlist')
    else:
        form = CreateExamForm()

    context = {'form' : form}
    return render(request, 'multichoice/create.html', context)




class ExamListView(ListView):
    model = Exam


class ExamDetailView(DetailView):
    model = Exam

class ExamDeleteView(DeleteView):
    model = Exam

class ExamUpdateView(UpdateView):
    model = Exam
    fields =["marks","Q_No","Question","option1","option2", "option3","option4","corrans"]