# Generated by Django 4.1.7 on 2023-03-03 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='like_count',
        ),
    ]