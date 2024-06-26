# Generated by Django 4.2.13 on 2024-05-19 04:17

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasaInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, help_text='CASA programme', max_length=255, null=True, verbose_name='Casa Inquiry')),
                ('inquiryname', models.TextField(blank=True, max_length=350, verbose_name='How can we help?')),
            ],
            options={
                'verbose_name_plural': 'CASA Inquiry Lists',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=64, verbose_name='Last Name')),
                ('inquryname', models.TextField(blank=True, max_length=5000, verbose_name='How can we help?')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
            ],
            options={
                'verbose_name_plural': 'Contact Us Lists',
            },
        ),
        migrations.CreateModel(
            name='GradeSchoolInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, help_text='Grade School programme', max_length=255, null=True, verbose_name='Grade School  programme')),
                ('inquiryname', models.TextField(blank=True, max_length=350, verbose_name='How can we help?')),
            ],
            options={
                'verbose_name_plural': 'GS Inquiry Lists',
            },
        ),
        migrations.CreateModel(
            name='HighSchoolInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, help_text='High School programme', max_length=255, null=True, verbose_name='High School  programme')),
                ('inquiryname', models.TextField(blank=True, max_length=350, verbose_name='How can we help?')),
            ],
            options={
                'verbose_name_plural': 'HS Inquiry Lists',
            },
        ),
        migrations.CreateModel(
            name='HomeStudyInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, help_text='Home Study programme', max_length=255, null=True, verbose_name='Home Study programme')),
                ('inquiryname', models.TextField(blank=True, max_length=350, verbose_name='How can we help?')),
            ],
            options={
                'verbose_name_plural': 'Home Study Programme Inquiry Lists',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, max_length=255, null=True, verbose_name='Course or Programme')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Inquiry Lists',
            },
        ),
        migrations.CreateModel(
            name='SpedInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64, verbose_name='Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('programme', models.CharField(blank=True, help_text='SPED programme', max_length=255, null=True, verbose_name='SPED programme')),
                ('inquiryname', models.TextField(blank=True, max_length=350, verbose_name='How can we help?')),
            ],
            options={
                'verbose_name_plural': 'SPED Inquiry Lists',
            },
        ),
    ]
