# Generated by Django 3.1.4 on 2020-12-26 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0014_auto_20201225_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='medical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.medical'),
        ),
    ]
