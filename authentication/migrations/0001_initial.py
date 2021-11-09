# Generated by Django 3.2.8 on 2021-10-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('classroom_id', models.IntegerField(db_column='Classroom_ID', primary_key=True, serialize=False)),
                ('standard', models.IntegerField(db_column='Standard')),
                ('section', models.TextField(db_column='Section')),
                ('no_of_students', models.IntegerField(blank=True, db_column='No_of_students', null=True)),
            ],
            options={
                'db_table': 'Classrooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalExamMarks',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('roll_no_field', models.IntegerField(db_column='Roll No.')),
                ('subject_name', models.CharField(db_column='Subject Name', max_length=30)),
                ('subject_marks', models.IntegerField(db_column='Subject Marks')),
            ],
            options={
                'db_table': 'Final Exam Marks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('parent_id', models.IntegerField(db_column='Parent_ID', primary_key=True, serialize=False)),
                ('parent_name', models.CharField(db_column='Parent Name', max_length=30)),
            ],
            options={
                'db_table': 'Parents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.IntegerField(db_column='Student_ID', primary_key=True, serialize=False)),
                ('student_name', models.CharField(db_column='Student Name', max_length=30)),
                ('phone_no_field', models.BigIntegerField(blank=True, db_column='Phone No.', null=True)),
                ('date_of_birth', models.DateField(db_column='Date of Birth')),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Students',
                'managed': False,
            },
        ),
    ]