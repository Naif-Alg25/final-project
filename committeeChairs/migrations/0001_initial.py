# Generated by Django 3.1.7 on 2021-03-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteesCharis',
            fields=[
                ('id_committees_charis', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_committees_charis', models.CharField(blank=True, default='nothing', max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'committees_charis',
                'managed': False,
            },
        ),
    ]
