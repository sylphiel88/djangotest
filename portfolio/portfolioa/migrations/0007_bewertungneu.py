# Generated by Django 3.2.4 on 2021-07-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioa', '0006_delete_bewertungneu'),
    ]

    operations = [
        migrations.CreateModel(
            name='bewertungneu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bw1Formulierung', models.IntegerField()),
                ('bw1Css', models.IntegerField()),
                ('bw1Aufbau', models.IntegerField()),
                ('bw1Aenderung', models.TextField()),
                ('bw2Fancy', models.IntegerField()),
                ('bw2Projects', models.IntegerField()),
                ('bw2Aenderung', models.TextField()),
                ('bw3Dtl', models.IntegerField()),
                ('bw3Inhalt', models.IntegerField()),
                ('bw3Aenderung', models.TextField()),
                ('bw4Bewe', models.IntegerField()),
                ('bw4Aenderung', models.TextField()),
                ('bw5Start', models.IntegerField()),
                ('bw5Proj', models.IntegerField()),
                ('bw5Farbe', models.IntegerField()),
                ('bw5Aenderung', models.TextField()),
            ],
        ),
    ]