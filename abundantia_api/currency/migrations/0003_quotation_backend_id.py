# Generated by Django 2.1.5 on 2019-02-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_currency_is_cryptocurrency'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='backend_id',
            field=models.CharField(db_index=True, default='hgbrasil', max_length=32),
            preserve_default=False,
        ),
    ]
