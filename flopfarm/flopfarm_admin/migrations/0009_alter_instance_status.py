# Generated by Django 3.2 on 2021-05-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flopfarm_admin', '0008_auto_20210502_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(blank=True, choices=[('i', 'Idle'), ('r', 'Running')], default='i', help_text='Instance status', max_length=1),
        ),
    ]
