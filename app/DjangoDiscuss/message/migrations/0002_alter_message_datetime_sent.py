# Generated by Django 4.2.9 on 2024-01-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datetime_sent',
            field=models.DateTimeField(auto_now_add=True, help_text='Format: YYYY-MM-DD HH:MM:SS'),
        ),
    ]