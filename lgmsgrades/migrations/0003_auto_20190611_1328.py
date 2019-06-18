# Generated by Django 2.1.7 on 2019-06-11 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lgmsgrades', '0002_auto_20190611_1328'),
        ('lgmssis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgmssis.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('student', 'course', 'marking_period')},
        ),
    ]
