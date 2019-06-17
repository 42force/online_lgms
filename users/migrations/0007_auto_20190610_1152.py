# Generated by Django 2.1.7 on 2019-06-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190610_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='howdidyouhear',
            field=models.CharField(blank=True, choices=[('RADIO', 'RADIO'), ('NEWS', 'NEWS'), ('FRIENDS', 'FRIENDS'), ('FACEBOOK', 'FACEBOOK')], default='FACEBOOK', help_text='How did you hear about us?', max_length=20, verbose_name='How did you heard about us?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='progoption',
            field=models.CharField(blank=True, choices=[('GRADE SCHOOL', 'GRADE SCHOOL'), ('CASA', 'CASA'), ('SPED', 'SPED'), ('HOMESTUDY', 'HOMESTUDY'), ('HIGH SCHOOL', 'HIGH SCHOOL')], default='CASA', help_text='Please select Program', max_length=20, verbose_name='Program Option'),
        ),
    ]