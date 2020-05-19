"""Online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('contact/', views.ContactView.as_view()),
    
    path('exam', views.examonline),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.ExamDetailView.as_view()),
    path('delete/<int:pk>', views.ExamDeleteView.as_view(success_url='/multichoice/examlist')),
    path('examlist/', views.ExamListView.as_view()),

    path('edit/<int:pk>', views.ExamUpdateView.as_view(success_url='/multichoice/examlist')),

    path('studentprofile/', views.StudentProfileListView.as_view()),
    path('studentprofile/<int:pk>', views.StudentProfileDetailView.as_view()),
    path('studentprofile/edit/<int:pk>', views.StudentProfileUpdateView.as_view(success_url='/multichoice/studentprofile')),





    path('', RedirectView.as_view(url='home/')),
    
]
