# Generated by Django 3.0.dev20190224003410 on 2019-05-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_origins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dump',
            name='path',
            field=models.TextField(null=True),
        ),
    ]
