# Generated by Django 3.0.6 on 2020-05-18 19:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('Q_No', models.IntegerField()),
                ('Question', models.CharField(max_length=10000)),
                ('option1', models.CharField(max_length=5000)),
                ('option2', models.CharField(max_length=5000)),
                ('option3', models.CharField(blank=True, max_length=5000, null=True)),
                ('option4', models.CharField(blank=True, max_length=5000, null=True)),
                ('corrans', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ('-Question',),
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('roll_No', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('Class', models.CharField(choices=[('FE', 'FE'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], default='FE', max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('address', models.TextField(blank=True, null=True)),
                ('pic', models.ImageField(null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-roll_No',),
            },
        ),
    ]
