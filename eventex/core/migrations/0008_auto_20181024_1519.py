# Generated by Django 2.1.2 on 2018-10-24 18:19

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]