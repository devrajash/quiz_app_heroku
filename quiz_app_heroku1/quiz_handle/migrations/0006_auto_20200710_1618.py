# Generated by Django 3.0 on 2020-07-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_handle', '0005_auto_20200710_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='question_a',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='question_b',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='question_c',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='question_d',
            field=models.CharField(default='', max_length=100),
        ),
    ]
