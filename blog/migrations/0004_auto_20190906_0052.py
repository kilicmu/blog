# Generated by Django 2.2.5 on 2019-09-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_headpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='Cdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Uimg',
            field=models.ImageField(upload_to='blog/user_img', verbose_name='头像'),
        ),
    ]
