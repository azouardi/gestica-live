# Generated by Django 3.2.4 on 2021-08-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_office_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankacount',
            name='bic',
            field=models.CharField(blank=True, max_length=8, verbose_name='Code BIC/SWIFT'),
        ),
    ]
