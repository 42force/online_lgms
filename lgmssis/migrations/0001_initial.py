# Generated by Django 2.1.7 on 2019-06-11 05:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import lgmssis.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('lname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('streetname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name')),
                ('cityname', models.CharField(blank=True, max_length=255, null=True, verbose_name='City Name')),
                ('zip', models.IntegerField(blank=True, null=True, verbose_name='Zip Code')),
                ('mobilenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, region=None, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('progoption', models.CharField(blank=True, choices=[('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA'), ('HOMESTUDY', 'HOMESTUDY'), ('SPED', 'SPED'), ('HIGH SCHOOL', 'HIGH SCHOOL')], default='CASA', help_text='Please select Program', max_length=20)),
                ('howdidyouhear', models.CharField(blank=True, choices=[('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA'), ('HOMESTUDY', 'HOMESTUDY'), ('SPED', 'SPED'), ('HIGH SCHOOL', 'HIGH SCHOOL')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20)),
                ('graddate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', lgmssis.models.IntegerRangeField(help_text='Example 2014', unique=True)),
                ('full_name', models.CharField(blank=True, help_text='Example Class of 2014', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('primary', models.BooleanField(blank=True, help_text='If set true - all students in this cohort will have it set as primary!')),
            ],
        ),
        migrations.CreateModel(
            name='CountryOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Country Options List',
            },
        ),
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complete Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobilenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, null=True, region=None, verbose_name='Mobile Number')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Place or City')),
                ('programme', models.CharField(blank=True, max_length=255, null=True, verbose_name='Course or Programme')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altemail', models.EmailField(blank=True, max_length=254)),
                ('number', models.IntegerField(blank=True)),
                ('ext', models.CharField(blank=True, max_length=10, null=True)),
                ('teacher', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Grade')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ReasonLeft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('grad_date', models.DateField(blank=True, null=True)),
                ('active_year', models.BooleanField(help_text='DANGER!! This is the current school year. There can only be one and setting this will remove it from other years. If you want to change the active year you almost certainly want to click Admin, Change School Year.')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrn_no', models.CharField(blank=True, default='', max_length=64, verbose_name='Learners Number')),
                ('grad_date', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bday', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('date_dismissed', models.DateField(blank=True, null=True)),
                ('unique_id', models.IntegerField(blank=True, help_text='For integration with outside databases', null=True, unique=True)),
                ('parent_guardian', models.CharField(blank=True, editable=False, max_length=150)),
                ('streetname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Name')),
                ('zip', models.CharField(blank=True, editable=False, max_length=10)),
                ('parent_email', models.EmailField(blank=True, editable=False, max_length=254)),
                ('class_of_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.ClassYear')),
                ('reason_left', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.ReasonLeft')),
                ('siblings', models.ManyToManyField(blank=True, to='lgmssis.Student')),
            ],
            options={
                'permissions': (('view_ssn_student', 'View student lrn_no'), ('view_mentor_student', 'View mentoring information student'), ('reports', 'View reports')),
            },
        ),
        migrations.CreateModel(
            name='StudentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='student_files')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgmssis.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentHealthRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgmssis.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=64, verbose_name='Subject Name')),
                ('color', models.CharField(default='#00b35c', max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Subjects Lists Information',
            },
        ),
        migrations.CreateModel(
            name='FamilyAccessUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user_students',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lgmssis.GradeLevel'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='fuser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cohort',
            name='students',
            field=models.ManyToManyField(blank=True, db_table='sis_studentcohort_students', to='lgmssis.Student'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='country_of_birth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.CountryOption'),
        ),
        migrations.CreateModel(
            name='SubjectCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('lgmssis.student',),
        ),
    ]
