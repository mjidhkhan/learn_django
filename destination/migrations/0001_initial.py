# Generated by Django 3.0.1 on 2019-12-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=120)),
                ('averagePrice', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('propertyCount', models.IntegerField()),
                ('imageUrl', models.TextField(blank=True, null=True)),
                ('imageAlt', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]