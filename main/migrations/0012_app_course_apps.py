# Generated by Django 4.1.3 on 2023-07-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_course_programm'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', verbose_name='Приложение')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='apps',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='main.app'),
        ),
    ]
