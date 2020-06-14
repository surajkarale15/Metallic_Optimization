# Generated by Django 2.2.7 on 2020-06-14 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('inventory', models.FloatField()),
                ('price', models.FloatField()),
                ('active', models.CharField(default='Y', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('active', models.CharField(default='Y', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chemical_composition',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('percentage', models.IntegerField()),
                ('active', models.CharField(default='Y', max_length=10)),
                ('comodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Commodity')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Element')),
            ],
        ),
    ]
