# Generated by Django 4.2.9 on 2024-02-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0003_reminder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
    ]
