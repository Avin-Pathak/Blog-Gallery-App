# Generated by Django 3.2.6 on 2021-09-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_alter_photomodel_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomodel',
            name='video',
            field=models.FileField(blank=True, upload_to='gall'),
        ),
    ]
