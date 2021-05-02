# Generated by Django 3.2 on 2021-05-02 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flopfarm_admin', '0004_auto_20210502_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Instance_provided', to='flopfarm_admin.user'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Instance_using', to='flopfarm_admin.user'),
        ),
    ]