# Generated by Django 5.1.1 on 2024-10-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_studata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studata',
            name='roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studata',
            name='stu_class',
            field=models.TextField(choices=[('class 6', 'class 6'), ('class 7', 'class 7'), ('class 8', 'class 8'), ('class 9', 'class 9'), ('class 10', 'class 10'), ('class 11', 'class 11'), ('class 12', 'class 12')]),
        ),
    ]
