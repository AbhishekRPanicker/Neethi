# Generated by Django 4.2.5 on 2023-09-28 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='occupation',
            field=models.CharField(choices=[('1', 'Criminal lawyer'), ('2', 'Environmental lawyer'), ('3', 'Family lawyer'), ('4', 'Corporate lawyer'), ('5', 'Civil lawyer'), ('6', 'Tax lawyer'), ('7', 'Cyber lawyer'), ('8', 'Government lawyer'), ('9', 'Military lawyer'), ('10', 'Others')], max_length=4),
        ),
        migrations.AlterField(
            model_name='info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]
