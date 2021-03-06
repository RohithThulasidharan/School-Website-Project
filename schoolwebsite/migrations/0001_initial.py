# Generated by Django 3.2.8 on 2021-11-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exammarks',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('science', models.IntegerField(db_column='Science')),
                ('maths', models.IntegerField(db_column='Maths')),
                ('english', models.IntegerField(db_column='English')),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
            ],
            options={
                'db_table': 'ExamMarks',
                'managed': False,
            },
        ),
    ]
