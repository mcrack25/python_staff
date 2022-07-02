from django.contrib import admin
from .models import Staff, Post, PostType
from .forms import PhotoForm


admin.site.register(Post)
admin.site.register(PostType)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    form = PhotoForm
