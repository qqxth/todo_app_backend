# Generated by Django 4.1.2 on 2022-11-13 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_is_did'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-created', 'is_did')},
        ),
    ]
