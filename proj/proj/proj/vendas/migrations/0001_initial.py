# Generated by Django 2.0.5 on 2018-06-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('mesa', models.IntegerField()),
                ('descricao', models.CharField(max_length=40)),
                ('qtd', models.IntegerField()),
                ('valor_unit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
