# Generated by Django 2.2.2 on 2019-07-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_marks_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='sub1',
            field=models.IntegerField(verbose_name='Subject1'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sub2',
            field=models.IntegerField(verbose_name='Subject2'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sub3',
            field=models.IntegerField(verbose_name='Subject3'),
        ),
    ]
