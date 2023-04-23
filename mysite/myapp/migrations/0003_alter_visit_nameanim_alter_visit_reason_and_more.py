# Generated by Django 4.1.7 on 2023-04-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='nameAnim',
            field=models.CharField(max_length=255, verbose_name='Кличка вихованця'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='reason',
            field=models.CharField(choices=[('', 'Причина візиту:'), ('Вакцинація', 'Вакцинація'), ('Огляд', 'Огляд'), ('Косметичні процедури', 'Косметичні процедури'), ('Лікування', 'Лікування')], max_length=255, verbose_name='Причина візиту'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='specAn',
            field=models.CharField(choices=[('', 'Вид тварини'), ('Собака', 'Собака'), ('Кіт', 'Кіт'), ('Інше', 'Інше')], max_length=255, verbose_name='Вид тварини'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='textArea',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]