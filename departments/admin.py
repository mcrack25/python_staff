from django.contrib import admin
from .models import Department, DepartmentNumbers


class DepartmentNumbersInline(admin.StackedInline):
    model = DepartmentNumbers
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [DepartmentNumbersInline]
