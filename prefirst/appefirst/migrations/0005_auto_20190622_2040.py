# Generated by Django 2.2.1 on 2019-06-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appefirst', '0004_pages_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domains',
            name='domain_token',
            field=models.CharField(blank=True, default=None, max_length=64),
        ),
    ]
