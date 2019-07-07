# Generated by Django 3.0.dev20190224003410 on 2019-04-22 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.apps.main_app.models.dump
import web.apps.main_app.validation.ip_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.BigIntegerField()),
                ('asn', models.IntegerField(null=True)),
                ('network', web.apps.main_app.models.dump.IPField(max_length=60)),
                ('path', models.CharField(max_length=255, null=True)),
                ('community', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=60, validators=[web.apps.main_app.validation.ip_validation.validate_ipv46_network])),
                ('network', models.CharField(max_length=60, null=True, validators=[web.apps.main_app.validation.ip_validation.validate_ipv46_address])),
                ('broadcast', models.CharField(max_length=60, null=True, validators=[web.apps.main_app.validation.ip_validation.validate_ipv46_address])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RouteObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Asn')),
                ('prefix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Prefix')),
            ],
        ),
    ]
