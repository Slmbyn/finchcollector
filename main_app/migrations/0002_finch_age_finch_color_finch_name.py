# Generated by Django 5.0 on 2023-12-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='age',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finch',
            name='color',
            field=models.CharField(default='Red', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finch',
            name='name',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]
