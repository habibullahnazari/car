# Generated by Django 5.0.2 on 2024-03-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0008_rename_logo_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alt',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
