from django.db import models


class Staff(models.Model):
    lname = models.CharField('Фамилия', max_length=100)
    fname = models.CharField('Имя', max_length=100)
    sname = models.CharField('Отчество', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
