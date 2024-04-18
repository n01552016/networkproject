# Generated by Django 4.2.7 on 2024-04-17 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_sender', models.EmailField(max_length=254)),
                ('smtp_password', models.CharField(max_length=255)),
                ('receivers', models.EmailField(max_length=254)),
                ('cc', models.EmailField(blank=True, max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]
