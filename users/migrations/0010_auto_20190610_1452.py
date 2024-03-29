# Generated by Django 2.1.7 on 2019-06-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190610_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='howdidyouhear',
            field=models.CharField(blank=True, choices=[('FRIENDS', 'FRIENDS'), ('FACEBOOK', 'FACEBOOK'), ('RADIO', 'RADIO'), ('NEWS', 'NEWS')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20, verbose_name='How did you heard about us?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='progoption',
            field=models.CharField(blank=True, choices=[('HIGH SCHOOL', 'HIGH SCHOOL'), ('HOMESTUDY', 'HOMESTUDY'), ('SPED', 'SPED'), ('CASA', 'CASA'), ('GRADE SCHOOL', 'GRADE SCHOOL')], default='CASA', help_text='Please select Program', max_length=20, verbose_name='Program Option'),
        ),
    ]
