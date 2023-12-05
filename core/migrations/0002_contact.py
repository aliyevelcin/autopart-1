# Generated by Django 4.2.7 on 2023-11-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, null=True, verbose_name='full_name')),
                ('email', models.CharField(max_length=300, null=True, verbose_name='email')),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('subject', models.CharField(max_length=300, null=True, verbose_name='subject')),
                ('message', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
