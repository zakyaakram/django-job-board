# Generated by Django 5.1.2 on 2024-11-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]