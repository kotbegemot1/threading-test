# Generated by Django 3.2.6 on 2021-08-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20200401_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='delay',
            field=models.SmallIntegerField(verbose_name='Задержка'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mail',
            name='mail_adress',
            field=models.EmailField(max_length=254, verbose_name='Введите Email получателя'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='subject',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='text',
            field=models.TextField(verbose_name='Текст сообщения'),
        ),
    ]
