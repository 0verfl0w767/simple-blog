# Generated by Django 5.0.1 on 2024-02-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='포스트 내용'),
        ),
    ]