# Generated by Django 3.0 on 2020-07-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_handle', '0003_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='SOME STRING', max_length=100),
        ),
    ]
