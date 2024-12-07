# Generated by Django 5.1.3 on 2024-12-06 08:55

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="content",
            field=tinymce.models.HTMLField(default=1),
        ),
    ]
