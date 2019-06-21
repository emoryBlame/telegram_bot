# Generated by Django 2.2.2 on 2019-06-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]