# Generated by Django 3.1.4 on 2021-02-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifyApp', '0009_auto_20210221_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='profile_picture',
            field=models.ImageField(default='profile_picture/def.jpg', upload_to='profile_picture'),
        ),
    ]
