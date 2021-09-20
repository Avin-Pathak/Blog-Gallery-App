# Generated by Django 3.2.6 on 2021-09-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='gall')),
                ('video', models.FileField(upload_to='gall')),
            ],
        ),
    ]
