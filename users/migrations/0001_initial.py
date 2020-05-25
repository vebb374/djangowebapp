# Generated by Django 3.0.6 on 2020-05-25 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profilepic', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('Fullname', models.CharField(default=None, max_length=40)),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default=None, max_length=10)),
                ('Date of Birth', models.DateField(default='2000-01-01')),
                ('Mothername', models.CharField(default=None, max_length=40)),
                ('Fathername', models.CharField(default=None, max_length=40)),
                ('nationality', models.CharField(choices=[('India', 'India'), ('Other country', 'Other country')], default=None, max_length=30)),
                ('address', models.TextField(default='your address with pincode', max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('pwd', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default=None, max_length=10)),
                ('branch', models.CharField(choices=[('Cse', 'Cse'), ('Ece', 'Ece'), ('Eee', 'Eee'), ('Civil', 'Civil'), ('Mech', 'Mech'), ('Chemical', 'Chemical'), ('Bio-tech', 'Bio-tech'), ('metallurgy', 'Metallurgy')], default=None, max_length=20)),
                ('category', models.CharField(choices=[('OC', 'Other Caste'), ('BC', 'Backward Caste'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe')], default=None, max_length=10)),
                ('tenthcertificate', models.FileField(default='default.pdf', upload_to='tenth')),
                ('intercertificate', models.FileField(default='default.pdf', upload_to='inter')),
                ('jeerankcertificate', models.FileField(default='default.pdf', upload_to='jee')),
                ('aadhar_card', models.FileField(default='default.pdf', upload_to='aadhar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
