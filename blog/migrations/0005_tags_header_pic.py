# Generated by Django 2.2.5 on 2019-09-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190906_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='header_pic',
            field=models.ImageField(default='', upload_to='blog/tags_pic', verbose_name='图片'),
        ),
    ]