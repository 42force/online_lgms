# Generated by Django 2.1.7 on 2019-06-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190610_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='howdidyouhear',
            field=models.CharField(blank=True, choices=[('FACEBOOK', 'FACEBOOK'), ('RADIO', 'RADIO'), ('NEWS', 'NEWS'), ('FRIENDS', 'FRIENDS')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20, verbose_name='How did you heard about us?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='progoption',
            field=models.CharField(blank=True, choices=[('CASA', 'CASA'), ('HIGH SCHOOL', 'HIGH SCHOOL'), ('SPED', 'SPED'), ('GRADE SCHOOL', 'GRADE SCHOOL'), ('HOMESTUDY', 'HOMESTUDY')], default='CASA', help_text='Please select Program', max_length=20, verbose_name='Program Option'),
        ),
    ]