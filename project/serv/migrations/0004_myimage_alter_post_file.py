# Generated by Django 4.2.5 on 2024-11-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0003_alter_post_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
