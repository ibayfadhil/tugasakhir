# Generated by Django 2.2.12 on 2020-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0008_buku'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jumlah',
            field=models.IntegerField(null=True),
        ),
    ]
