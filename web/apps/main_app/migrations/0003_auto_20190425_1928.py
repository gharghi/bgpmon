# Generated by Django 3.0.dev20190224003410 on 2019-04-25 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_neighbors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asn',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
