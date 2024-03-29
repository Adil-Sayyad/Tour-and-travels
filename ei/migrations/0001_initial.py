# Generated by Django 5.0 on 2023-12-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('name', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('desc', models.TextField()),
                ('byair', models.TextField()),
                ('bytrain', models.TextField()),
                ('byroad', models.TextField()),
            ],
        ),
    ]
