# Generated by Django 4.2.5 on 2024-11-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0004_myimage_alter_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('TN', 'Танки'), ('DD', 'ДД'), ('HL', 'Хиллеры'), ('ME', 'Торговцы'), ('GM', 'Гилдмастера'), ('QG', 'Квестгиверы'), ('BS', 'Кузнецы'), ('TS', 'Кожевники'), ('PM', 'Зельевары'), ('SM', 'Мастера заклинаний'), ('BU', 'Куплю'), ('SL', 'Продам')], default=None, max_length=15),
        ),
    ]