# Generated by Django 3.1.4 on 2020-12-24 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_medical_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors_Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=100, null=True)),
                ('prescription', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.appointment')),
            ],
        ),
    ]
