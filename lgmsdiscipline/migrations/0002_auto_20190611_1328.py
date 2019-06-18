# Generated by Django 2.1.7 on 2019-06-11 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lgmsdiscipline', '0001_initial'),
        ('lgmssis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdiscipline',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'inactive': False}, to='lgmssis.Student'),
        ),
        migrations.AddField(
            model_name='studentdiscipline',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lgmssis.Faculty'),
        ),
        migrations.AddField(
            model_name='disciplineactioninstance',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgmsdiscipline.DisciplineAction'),
        ),
        migrations.AddField(
            model_name='disciplineactioninstance',
            name='student_discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgmsdiscipline.StudentDiscipline'),
        ),
    ]
