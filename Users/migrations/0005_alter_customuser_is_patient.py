# Generated by Django 3.2.9 on 2021-12-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_customuser_is_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='is_patient'),
        ),
    ]
