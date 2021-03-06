# Generated by Django 3.2 on 2021-05-01 15:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdgeProvider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular user', primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='Enter the user name', max_length=200)),
                ('password', models.CharField(help_text='Enter the password', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular user', primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='Enter the user name', max_length=200)),
                ('password', models.CharField(help_text='Enter the password', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular instance', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the instance name', max_length=200)),
                ('type', models.CharField(blank=True, choices=[('c', 'General Computing Instance'), ('d', 'Deep Learning API')], default='c', help_text='Instance type', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('u', 'Serving')], default='o', help_text='Instance status', max_length=1)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Instance_provided', to='flopfarm_admin.edgeprovider')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Instance_using', to='flopfarm_admin.user')),
            ],
        ),
    ]
