# Generated by Django 5.0.3 on 2024-05-24 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]