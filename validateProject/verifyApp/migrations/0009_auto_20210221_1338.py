# Generated by Django 3.1.4 on 2021-02-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifyApp', '0008_auto_20210221_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_picture/def.jpg', null=True, upload_to='profile_picture'),
        ),
    ]
