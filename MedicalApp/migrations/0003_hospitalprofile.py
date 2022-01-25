# Generated by Django 3.2.9 on 2022-01-25 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='hospital_pics')),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MedicalApp.hospital')),
            ],
        ),
    ]