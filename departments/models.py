from django.db import models


class Department(models.Model):
    name = models.CharField('подразделение', max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='childs', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class DepartmentNumbers(models.Model):
    number = models.CharField('номер', max_length=30)
    department = models.ForeignKey(Department, models.PROTECT, null=True, blank=True, verbose_name='подразделение')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Номер подразделения'
        verbose_name_plural = 'Номера подразделения'
