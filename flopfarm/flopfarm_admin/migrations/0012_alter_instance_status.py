# Generated by Django 3.2 on 2021-05-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flopfarm_admin', '0011_rename_os_ethaddress_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'offline'), ('i', 'Idle'), ('r', 'Running')], default='i', help_text='Instance status', max_length=1),
        ),
    ]