# Generated by Django 4.1.2 on 2022-11-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': [models.OrderBy(models.F('is_did'), nulls_last=True), '-created']},
        ),
    ]
