# Generated by Django 4.2.4 on 2023-08-27 12:03
# And updated by FalseR

from django.db import migrations


def create_currencies(apps, schema_editor):
    Currency = apps.get_model('core', 'Currency')
    Currency(code3="BYN").save()
    Currency(code3="USD").save()
    Currency(code3="EUR").save()
    Currency(code3="RUB").save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_currencies)
    ]
