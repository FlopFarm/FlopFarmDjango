# Generated by Django 3.2 on 2021-05-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flopfarm_admin', '0002_alter_instance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Instance_using', to='flopfarm_admin.user'),
        ),
    ]
