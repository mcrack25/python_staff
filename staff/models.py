from django.db import models
from departments.models import Department


class PostType(models.Model):
    name = models.CharField('название', max_length=100)
    priority = models.IntegerField('приоритет', default=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип должности'
        verbose_name_plural = 'Типы должностей'


class Post(models.Model):
    name = models.CharField('название', max_length=100)
    post_type = models.ForeignKey(PostType, models.PROTECT, verbose_name='тип должности')
    priority = models.IntegerField('приоритет', default=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Staff(models.Model):
    lname = models.CharField('фамилия', max_length=100)
    fname = models.CharField('имя', max_length=100)
    sname = models.CharField('отчество', max_length=100, null=True, blank=True)
    number = models.IntegerField('внутренний номер', null=True, blank=True)
    post = models.ForeignKey(Post, models.PROTECT, verbose_name='должность')
    department = models.ForeignKey(Department, models.PROTECT, verbose_name='подразделение')

    def __str__(self):
        return ' '.join(filter(None, [self.lname, self.fname, self.sname]))

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
