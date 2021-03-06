# Generated by Django 3.0.dev20190224003410 on 2019-06-17 09:07

from django.db import migrations, models
import web.apps.main_app.validation.ip_validation


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20190617_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefix',
            name='broadcast',
            field=models.CharField(max_length=60, null=True, validators=[web.apps.main_app.validation.ip_validation.validate_ipv46_address]),
        ),
        migrations.AlterField(
            model_name='prefix',
            name='network',
            field=models.CharField(max_length=60, null=True, validators=[web.apps.main_app.validation.ip_validation.validate_ipv46_address]),
        ),
    ]
