# Generated by Django 3.2.12 on 2022-05-25 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_auto_20220525_2100'),
        ('staff', '0003_alter_staff_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='departments.department', verbose_name='подразделение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='внутренний номер'),
        ),
    ]
