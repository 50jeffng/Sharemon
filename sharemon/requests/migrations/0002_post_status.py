# Generated by Django 2.2 on 2019-04-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'resolved'), (2, 'pending')], default=2),
        ),
    ]
