# Generated by Django 4.2.9 on 2024-01-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_in_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_moderated',
            field=models.BooleanField(default=False),
        ),
    ]
