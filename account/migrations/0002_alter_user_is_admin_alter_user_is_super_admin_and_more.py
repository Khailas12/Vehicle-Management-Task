# Generated by Django 4.0.8 on 2022-11-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_super_admin',
            field=models.BooleanField(default=False, verbose_name='Super Admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='User'),
        ),
    ]