# Generated by Django 4.1.3 on 2023-04-24 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_courselevel_rename_child_course_demo_course_tag_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courselevel',
            options={'verbose_name': 'Уровень', 'verbose_name_plural': 'Уровни'},
        ),
        migrations.AlterField(
            model_name='course',
            name='demo',
            field=models.BooleanField(default=False, verbose_name='Демонстрационный'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Оболожка'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(blank=True, choices=[('child', 'Детский'), ('dev', 'Программирование'), ('design', 'Дизайн'), ('office', 'Офисный')], default=None, max_length=50, null=True, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='main.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='level',
            field=models.CharField(choices=[('base', 'Базовый'), ('advanced', 'Продвинутый'), ('expert', 'Экспертный')], default='base', max_length=50, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название пункта'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='main.theme', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='main.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='level',
            field=models.CharField(choices=[('base', 'Базовый'), ('advanced', 'Продвинутый'), ('expert', 'Экспертный')], default='base', max_length=50, verbose_name='Уровень темы'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название темы'),
        ),
    ]
