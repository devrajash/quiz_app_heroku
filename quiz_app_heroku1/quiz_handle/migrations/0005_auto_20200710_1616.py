# Generated by Django 3.0 on 2020-07-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_handle', '0004_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
