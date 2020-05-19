from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.core.validators import MinValueValidator, RegexValidator

# Create your models here.


class Exam(models.Model):
    marks = models.IntegerField(null=True, blank= True)
    Q_No = models.IntegerField()
    Question = models.CharField(max_length=10000)
    option1 = models.CharField(max_length=5000)
    option2 = models.CharField(max_length=5000)
    option3 = models.CharField(max_length=5000, null=True, blank= True)
    option4 = models.CharField(max_length=5000, null=True, blank= True)
    corrans =  models.CharField(max_length=5000)

    class Meta:
        ordering = ('Q_No',)

    def __str__(self):
        return "%s" % self.Question


class StudentProfile(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    roll_No = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    Class = models.CharField(max_length=20, default="FE", choices= (("FE","FE"), ("SE","SE"),("TE","TE"),("BE","BE")))
    
    gender = models.CharField(max_length=10, default="male", choices= (("male","male"), ("female","female")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank= True)
    address =models.TextField(null=True, blank= True)
    pic = models.ImageField(upload_to="images", null=True)

    class Meta:
        ordering = ('-roll_No',)

    def __str__(self):
        return "%s" % self.user