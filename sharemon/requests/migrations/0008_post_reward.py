# Generated by Django 2.1.7 on 2019-04-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0007_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reward',
            field=models.CharField(default='NONE', max_length=100),
        ),
    ]