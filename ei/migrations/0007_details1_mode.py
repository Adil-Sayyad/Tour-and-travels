# Generated by Django 4.2.7 on 2023-12-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ei', '0006_alter_payment_from_alter_payment_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='details1',
            name='mode',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
