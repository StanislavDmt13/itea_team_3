# Generated by Django 4.1 on 2022-08-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_task_content_alter_task_closed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='opened_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
