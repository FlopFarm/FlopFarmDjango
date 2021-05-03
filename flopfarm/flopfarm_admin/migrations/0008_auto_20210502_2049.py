# Generated by Django 3.2 on 2021-05-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flopfarm_admin', '0007_auto_20210502_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='IP',
            field=models.CharField(blank=True, help_text='Enter IP', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='instance',
            name='password',
            field=models.CharField(blank=True, help_text='Enter SSH password', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='instance',
            name='username',
            field=models.CharField(blank=True, help_text='Enter SSH user name', max_length=200, null=True),
        ),
    ]