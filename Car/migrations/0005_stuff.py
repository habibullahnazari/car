# Generated by Django 5.0.2 on 2024-03-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_alter_gallery_photo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='media/stuff')),
                ('job_position', models.CharField(max_length=100)),
                ('facebook', models.URLField()),
                ('x', models.URLField()),
                ('gplus', models.URLField()),
                ('instagram', models.URLField()),
            ],
        ),
    ]
