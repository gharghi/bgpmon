# Generated by Django 3.0.dev20190224003410 on 2019-05-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='wrong_asn',
            field=models.IntegerField(null=True),
        ),
    ]
