# Generated by Django 3.1 on 2020-09-16 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200915_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='name',
        ),
    ]
