# Generated by Django 5.0.2 on 2024-03-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0012_about_footer_delete_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_footer',
            name='desciption',
            field=models.TextField(help_text='maximum size is 280 character', max_length=280),
        ),
    ]
