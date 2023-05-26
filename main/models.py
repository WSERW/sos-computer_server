from django.db import models

# Create your models here.


class Course(models.Model):

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = "Курсы"

    TAGS = [
        ('child', 'Детский'),
        ('dev', 'Программирование'),
        ('design', 'Дизайн'),
        ('office', 'Офисный'),
    ]

    name = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    tag = models.CharField(choices=TAGS, max_length=50,
                           default='', blank=True, verbose_name='Тег')
    image = models.ImageField(default=None, null=True,
                              blank=True, verbose_name='Оболожка')
    demo = models.BooleanField(default=False, verbose_name='Демонстрационный')

    def __str__(self):
        return f'{self.name}'


class Theme(models.Model):

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = "Темы"

    LEVELS = [
        ('base', 'Базовый'),
        ('advanced', 'Продвинутый'),
        ('expert', 'Экспертный'),
    ]
    order = models.IntegerField(
        verbose_name='Порядковый номер темы', default=0)
    name = models.CharField(max_length=200, verbose_name='Название темы')
    level = models.CharField(
        choices=LEVELS, max_length=50, default='base', verbose_name='Уровень темы')
    course = models.ForeignKey(
        Course, related_name='themes', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.name}'


class Paragraph(models.Model):

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = "Пункты"

    name = models.CharField(max_length=200, verbose_name='Название пункта')
    theme = models.ForeignKey(
        Theme, related_name='paragraphs', on_delete=models.CASCADE, verbose_name='Тема')

    def __str__(self):
        return f'{self.name}'


class Spec(models.Model):

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"

    text = models.TextField(default='', verbose_name='Спецификация')
    course = models.ForeignKey(
        Course, related_name='specs', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.text


class CourseLevel(models.Model):

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

    LEVELS = [
        ('base', 'Базовый'),
        ('advanced', 'Продвинутый'),
        ('expert', 'Экспертный'),
    ]
    level = models.CharField(
        choices=LEVELS, max_length=50, default='base', verbose_name='Уровень')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Стоимость')
    course = models.ForeignKey(
        Course, related_name='levels', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.level
