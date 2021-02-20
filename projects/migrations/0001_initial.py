# Generated by Django 3.1.7 on 2021-02-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id_projects', models.IntegerField(db_column='id_Projects', primary_key=True, serialize=False)),
                ('name_projects', models.CharField(blank=True, max_length=45, null=True)),
                ('filled_projects', models.CharField(blank=True, max_length=45, null=True)),
                ('descriotion_projects', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
    ]
