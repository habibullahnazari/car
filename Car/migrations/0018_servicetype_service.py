# Generated by Django 5.0.2 on 2024-03-31 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0017_alter_about_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(max_length=50)),
                ('photo', models.ImageField(help_text='Image size should be width= 800px height=480px', upload_to='media/about')),
                ('description', models.CharField(max_length=50)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_type', to='Car.servicetype')),
            ],
        ),
    ]
