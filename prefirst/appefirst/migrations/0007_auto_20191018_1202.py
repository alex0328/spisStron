# Generated by Django 2.2.6 on 2019-10-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appefirst', '0006_auto_20191018_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumbers',
            name='number_1',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='lottonumbers',
            name='number_2',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='lottonumbers',
            name='number_3',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='lottonumbers',
            name='number_4',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='lottonumbers',
            name='number_5',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='lottonumbers',
            name='number_6',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
