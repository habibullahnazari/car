# Generated by Django 5.0.2 on 2024-03-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0005_stuff'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
    ]
