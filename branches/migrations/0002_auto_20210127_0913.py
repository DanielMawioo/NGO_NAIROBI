# Generated by Django 3.0 on 2021-01-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_offices',
            name='issues_addressed',
            field=models.ManyToManyField(blank=True, to='branches.Issues_Addressed'),
        ),
        migrations.AlterField(
            model_name='regional_office',
            name='issues_addressed',
            field=models.ManyToManyField(blank=True, to='branches.Issues_Addressed'),
        ),
    ]
