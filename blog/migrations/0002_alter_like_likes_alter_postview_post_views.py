# Generated by Django 4.2.9 on 2024-01-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postview',
            name='post_views',
            field=models.BooleanField(default=False),
        ),
    ]
