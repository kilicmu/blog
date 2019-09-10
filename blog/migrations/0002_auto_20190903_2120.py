# Generated by Django 2.2.5 on 2019-09-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_pic',
            field=models.ImageField(upload_to='blog/article_img', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='a_uploadTime',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
    ]