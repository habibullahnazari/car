# Generated by Django 5.0.2 on 2024-03-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0015_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aboutus',
            field=models.TextField(help_text='maximum character is 600', max_length=600),
        ),
        migrations.AlterField(
            model_name='about',
            name='slogan',
            field=models.CharField(help_text='max length is 150 character', max_length=150),
        ),
    ]
